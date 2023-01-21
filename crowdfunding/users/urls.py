from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    path('<int:pk>', views.CustomUserDetail.as_view(), name='customuser-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)