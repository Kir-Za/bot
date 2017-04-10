from django.db.models import Q
from django.views.generic import FormView, ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.core.urlresolvers import reverse_lazy
from interface.models import OrdinaryUser
from .models import MyNote
from .forms import SearchForm


class SearchAPI(LoginRequiredMixin, FormView):
    form_class = SearchForm

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_key = form.cleaned_data['search_field']
            return redirect(reverse('note_list', kwargs={'keys': search_key}))
        else:
            return redirect('note_list', kwargs={'keys': 'last'})


class CommonNoteView(LoginRequiredMixin, ListView):
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


class AddNoteView(LoginRequiredMixin, CreateView):
    template_name = 'remider.html'
    model = MyNote
    fields = ['title', 'keys', 'text_body']
    success_url = reverse_lazy('note_list', kwargs={'keys': 'last'})

    def form_valid(self, form):
        form.instance.customer = OrdinaryUser.objects.get(username=self.request.user)
        form.instance.title = self.request.POST['title']
        form.instance.keys = self.request.POST['keys']
        form.instance.text_body = self.request.POST['text_body']
        return super(AddNoteView, self).form_valid(form)


class DeatilNoteView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = MyNote


class RemoveNoteView(LoginRequiredMixin, DeleteView):
    model = MyNote
    success_url = reverse_lazy('note_list', kwargs={'keys': 'last'})
