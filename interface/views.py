from logging import getLogger
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, TemplateView, View
from django.core.exceptions import ObjectDoesNotExist
from .froms import FaceForm
from .models import OrdinaryUser

file_logger = getLogger('gal_logger')


class MainView(FormView):
    template_name = 'interface.html'
    form_class = FaceForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'ex_user_name' not in request.POST.keys():
                main_field = form.cleaned_data['main_field']
                try:
                    OrdinaryUser.objects.get(username=main_field)
                    return render(request, self.template_name, context={"user_name": main_field})
                except ObjectDoesNotExist:
                    return redirect(reverse('login_page'))
                except Exception as err:
                    file_logger.error(err)
            else:
                name = request.POST['ex_user_name']
                pswd = form.cleaned_data['main_field']
                user = authenticate(username=name, password=pswd)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect(reverse('menu_page'))
                else:
                    return redirect(reverse('login_page'))
        return redirect(reverse('login_page'))


class MenuView(LoginRequiredMixin, TemplateView):
    template_name = "menu.html"
    login_url = 'login_page'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['points'] = {'message': 'OK!'}
        # заметки
        # секретарь
        # список задач
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
