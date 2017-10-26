from django.conf.urls import url
from . import views


# The pattern r'^$' looks for an empty string because ^ means beginning
# and $ means end.

# This first entry in the url patterns means that if there is no extra string
# after the root of the web server, it should show the user the post list.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

