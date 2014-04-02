from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from web.forms import QuestionForm
from web.mixins import SearchMixin
from web.models import Question


class ListQuestionView(SearchMixin, ListView):
    model = Question
    template_name = 'list_question.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        ctx = super(ListQuestionView, self).get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q')
        return ctx

    def get_queryset(self):
        return self.model.objects.all()[:5]


class CreateQuestionView(CreateView):
    model = Question
    template_name = 'create_question'
    success_url = reverse_lazy('index')
    form_class = QuestionForm

    def form_valid(self, form):
        form.instance.user = User.objects.first()  # cambiar por self.request.user
        return super(CreateQuestionView, self).form_valid(form)


class DetailQuestionView(DetailView):
    model = Question
    template_name = 'detail_question.html'
    context_object_name = 'question'