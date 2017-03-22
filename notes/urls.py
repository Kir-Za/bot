from django.conf.urls import url
from .views import CommonNoteView, SearchAPI

urlpatterns = [
    url(r'^note_list/$', CommonNoteView.as_view(), name='note_page'),
    url(r'^search_api/$', SearchAPI.as_view(), name='serach_api'),
]
