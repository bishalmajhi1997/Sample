from django.shortcuts import render
from django.http import HttpResponse,Http404
from api.models import Question,Choice
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
def index(request):

    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=','.join([q.question_text for q in latest_question_list])
    #template=loader.get_template("api/index.html")
    context={'latest_question_list':latest_question_list}
#    return HttpResponse(template.render(context,request))
    return render(request,'api/index.html',context)

    #return HttpResponse(output)
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request,'api/details.html',{'question':question})
def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'api/results.html',{'question':question})
    #response="you are looking at the results of question %s "
    #return HttpResponse(response % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name='api/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name='api/details.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
