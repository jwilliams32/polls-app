from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.template import loader, RequestContext, Template, Context
from django.template.loader import render_to_string
# Use the loader to render a template
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    template = 'polls/index.html'
    context = {

        'latest_questions': latest_questions
    }
    # creates a dict where the key latest_questions have the values of latest_question
    return render(request, template, context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # pk is the id
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
        # request.Post returns a dict like object that lets you access submitted data by a key name (choice) will return id
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Please select a choice'})
    else:
        # adds the vote by one
        selected_choice.votes += 1
        # save the users vote
        selected_choice.save()
        # Allows us not to have a hard coded URL
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

