from django.urls import path
from profles_api import views

urlpatterns = [
    path('helloworld/', views.HelloApiView.as_view())
]
