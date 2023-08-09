from django.urls import path
from .views import PostViewSet
from rest_framework.urlpatterns import format_suffix_patterns

post_list = PostViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

post_detail = PostViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('post/', post_list),
    path('post/<int:pk>/', post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
