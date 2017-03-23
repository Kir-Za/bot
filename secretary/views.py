from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView, View, CreateView
from .models import Reminder, ToDoList, TimeManage
from interface.models import OrdinaryUser
from .forms import ReminderForm


class RemiderView(LoginRequiredMixin, CreateView):
    template_name = 'remider.html'
    model = Reminder
    fields = ['time', 'note']

    def form_valid(self, form):
        form.instance.customer = OrdinaryUser.objects.get(username=self.request.user)
        form.instance.time = self.request.POST['time']
        form.instance.note = self.request.POST['note']
        return super(RemiderView, self).form_valid(form)


class ToDoListView(LoginRequiredMixin, CreateView):
    template_name = 'add_task.html'
    model = ToDoList
    fields = ['note']

    def form_valid(self, form):
        form.instance.customer = OrdinaryUser.objects.get(username=self.request.user)
        form.instance.note = self.request.POST['note']
        return super(ToDoListView, self).form_valid(form)
