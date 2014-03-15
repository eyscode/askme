from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from web.models import Pregunta


def home(request):
    q = request.GET.get('q')
    if q:
        ps = Pregunta.objects.filter(title__icontains=q)
    else:
        ps = Pregunta.objects.all()
    context = {'preguntas': ps, 'q': q}
    return render(request, 'lista_preguntas.html', context)


def form_ask(request):
    if request.method == "GET":
        return render(request, 'crea_pregunta.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        Pregunta.objects.create(title=title, content=content)
        return redirect(reverse('index'))


#CBVs


class ListAsk(ListView):
    model = Pregunta
    template_name = 'lista_preguntas.html'
    context_object_name = 'preguntas'


class FormAsk(CreateView):
    model = Pregunta
    template_name = 'crea_pregunta2.html'
    success_url = reverse_lazy('index')
    fields = ('title', 'content')