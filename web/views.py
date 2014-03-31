from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from web.mixins import SearchMixin
from web.models import Pregunta


def home(request):
    q = request.GET.get('q')
    if q:
        ps = Pregunta.objects.filter(title__icontains=q)
    else:
        ps = Pregunta.objects.all()
    context = {'preguntas': ps, 'q': q}
    return render(request, 'lista_preguntas.html', context)


class ListAsk(SearchMixin, ListView):
    model = Pregunta
    template_name = 'lista_preguntas.html'
    context_object_name = 'preguntas'

    def get_context_data(self, **kwargs):
        ctx = super(ListAsk, self).get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q')
        return ctx


class FormAsk(CreateView):
    model = Pregunta
    template_name = 'crea_pregunta2.html'
    success_url = reverse_lazy('index')
    fields = ('title', 'content')