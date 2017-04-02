from django.conf.urls import url

from .views import ApiListView , ApiDetailView, ApiDestroyView, ApiUpdateView, ApiCreateView
urlpatterns = [
    url(r'^$', ApiListView.as_view(),name='list' ),
    url(r'^(?P<pk>\d+)/$', ApiDetailView.as_view(),name='detail' ),
    url(r'^(?P<pk>\d+)/delete/$', ApiDestroyView.as_view(),name='delete' ),
    url(r'^(?P<pk>\d+)/edit$', ApiUpdateView.as_view(),name='update' ),
    url(r'^create/$', ApiCreateView.as_view(),name='create' ),

]