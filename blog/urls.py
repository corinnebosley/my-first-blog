from django.conf.urls import url
from . import views


# The pattern r'^$' looks for an empty string because ^ means beginning
# and $ means end.

# This first entry in the url patterns means that if there is no extra string
# after the root of the web server, it should show the user the post list.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]
