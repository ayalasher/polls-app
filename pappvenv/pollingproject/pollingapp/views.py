from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.

def greeting(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    output = ",".join([q.text_question for q in latest_questions_list ])
    template = loader.get_template("pollingapp/index.html")
    context = {
        "latest_question_list":latest_questions_list
    }
    return HttpResponse(template.render(context,request))

    return HttpResponse(output)

def details(request,question_id):
    return HttpResponse("you are looking at question %s ." % question_id )

def results(request,question_id):
    response = "you are looking at the reults of the question %s . "
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("You are looking at the votes of the question %s ."  %question_id )
