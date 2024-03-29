from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  template = loader.get_template("poll/index.html")
  context = {
    "latest_question_list": latest_question_list,
  }

  return HttpResponse(template.render(context, request))



def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, "polls/detail.html", {"question": question})



def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "poll/results.html", {"question": question})



def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    return render(
      request,
      "poll/detail.html",
      {
        "question": question,
        "error_message": "You didn't select a choice.",
      },
    )
  selected_choice.votes = F("votes") + 1
  selected_choice.save()
  return HttpResponse(reverse("poll:results", args=(question_id,)))