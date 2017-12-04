from django.conf.urls import url
from posts import views

urlpatterns = [
    url(
        r'^posts/$',
        views.PostList.as_view(),
        name=views.PostList.name
    ),
    url(
        r'^posts/(?P<pk>[0-9]+)/$',
        views.PostDetail.as_view(),
        name=views.PostDetail.name
    ),
    url(
        r'^photos/$',
        views.PhotoList.as_view(),
        name=views.PhotoList.name
    ),
    url(
        r'^photos/(?P<pk>[0-9]+)/$',
        views.PhotoDetail.as_view(),
        name=views.PhotoDetail.name
    ),
    url(
        r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name
    )
]