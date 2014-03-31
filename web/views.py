from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from web.mixins import SearchMixin
from web.models import Pregunta


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
    template_name = 'crea_pregunta.html'
    success_url = reverse_lazy('index')
    fields = ('title', 'content')