from django.conf.urls import url
from .views import CommonNoteView, SearchAPI, AddNoteView, DeatilNoteView, RemoveNoteView

urlpatterns = [
    url(r'^note_add/$', AddNoteView.as_view(), name='note_add'),
    url(r'^note_list/(?P<keys>.*)/$', CommonNoteView.as_view(), name='note_list'),
    url(r'^search_api/$', SearchAPI.as_view(), name='serach_api'),
    url(r'^note_detail/(?P<pk>.*)/$', DeatilNoteView.as_view(), name='note_detail'),
    url(r'^note_del/(?P<pk>.*)/$', RemoveNoteView.as_view(), name='note_del'),
]
