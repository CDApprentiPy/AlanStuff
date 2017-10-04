from django.conf.urls import url
from views import landing, create

urlpatterns = [
    url(r'^', landing , name='landing'),
    url(r'^user/create', create , name='create'),
]