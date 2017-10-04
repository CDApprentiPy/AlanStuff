from django.conf.urls import url 
from .views import CreateView, DetailsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^bucketlist/$', CreateView.as_view(), name='create'),
    url(r'^bucketlist/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name='details'),
]


# this line allows us to specify the datas format
urlpatterns = format_suffix_patterns(urlpatterns)