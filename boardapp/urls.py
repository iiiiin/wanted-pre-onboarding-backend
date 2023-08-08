from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    # path('signup/',views.UserCreate.as_view()),
    # path('api-auth/',include('rest_framework.urls')),
    path('post/',views.Postlist.as_view()),
    path('post/<int:pk>/',views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
