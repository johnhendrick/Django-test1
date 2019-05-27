from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

# #shelved for generic views
# def index(request):
#     latest_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_list': latest_list}
#     return render(request, 'polls/index.html', context)

"""
Quicker way to define render without loader and HttpResponse()
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):

#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_list'

    def get_queryset(self):

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # no explicit context is provided, generic view is provided with the Django model
    model = Question

    template_name = 'polls/detail.html'
    # attribute to tell Django to use a specific template name
    # because the default template for the generic view is <app name>/<model name>_detail.html

    def get_queryset(self):
        # Exclude any questions that are not published
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# note that the vote function below has race condition - multiple computations can be done outside the server independently prior to saving into database
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
