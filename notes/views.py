from django.shortcuts import render
from django.db.models import Q
from django.views.generic import FormView, TemplateView, View, ListView
from django.shortcuts import render, redirect, reverse
from .models import MyNote
from .forms import SearchForm


class SearchAPI(FormView):
    form_class = SearchForm

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_key = form.cleaned_data['search_field']
            return redirect(reverse('note_page', kwargs={'keys': search_key}))
        else:
            return redirect('note_page')


class CommonNoteView(ListView):
    template_name = 'work_space.html'
    context_object_name = 'note_list'
    queryset = MyNote.objects.order_by('-time_add')

    def get_queryset(self):
        if self.kwargs['keys'] == 'last':
            return MyNote.objects.order_by('-time_add')
        else:
            keys_list = self.kwargs['keys'].split(' ')
            search = []
            for element in keys_list:
                search.append('Q(keys__contains="'+element+'")|')
            search[-1] = search[-1].strip('|')
            search_str = ''.join(search)
            search_str = 'MyNote.objects.filter('+search_str+')'
            return eval(search_str)

