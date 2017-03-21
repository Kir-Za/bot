from django.conf.urls import url
from .views import MainView, MenuView, LogoutView

urlpatterns = [
    url(r'^login/$', MainView.as_view(), name='login_page'),
    url(r'^menu/$', MenuView.as_view(), name='menu_page'),
    url(r'^logout/$', LogoutView.as_view(), name='log_out_api'),
]
