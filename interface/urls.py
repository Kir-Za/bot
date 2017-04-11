from django.conf.urls import url
from .views import MainView, LogoutView

urlpatterns = [
    url(r'^$', LogoutView.as_view(), name='log_out_api'),
    url(r'^login/$', MainView.as_view(), name='login_page'),
    url(r'^logout/$', LogoutView.as_view(), name='log_out_api'),
]
