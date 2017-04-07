from django.conf.urls import url
from .views import CommonNoteView, SearchAPI, AddNoteView, DeatilNoteView

urlpatterns = [
    url(r'^add_note/$', AddNoteView.as_view(), name='add_note'),
    url(r'^note_list/(?P<keys>.*)/$', CommonNoteView.as_view(), name='note_page'),
    url(r'^search_api/$', SearchAPI.as_view(), name='serach_api'),
    url(r'^note_detail/(?P<pk>.*)/$', DeatilNoteView.as_view(), name='note_detail'),
]
