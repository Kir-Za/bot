from django.shortcuts import render
from django.views.generic import FormView, TemplateView, View, ListView
from django.shortcuts import render, redirect
from .models import MyNote
from .forms import SearchForm


class SearchAPI(FormView):
    form_class = SearchForm

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_key = form.cleaned_data['search_field']
            # return render(request, self.template_name)
            return redirect('note_page')
        else:
            return redirect('note_page')


class CommonNoteView(ListView):
    template_name = 'work_space.html'
    context_object_name = 'note_list'
    queryset = MyNote.objects.order_by('-time_add')

    def get_queryset(self):
        return MyNote.objects.all()

