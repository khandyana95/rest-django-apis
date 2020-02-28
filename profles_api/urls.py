from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profles_api import views

router = DefaultRouter()
router.register("helloviewset", views.HelloViewSet, base_name="helloviewset")

urlpatterns = [
    path('helloworld/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
