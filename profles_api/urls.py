from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profles_api import views

router = DefaultRouter()
router.register("helloviewset", views.HelloViewSet, base_name="helloviewset")
router.register("profiles", views.UserProfileViewSet)
router.register("profilefeed", views.UserProfileFeedViewSet)


urlpatterns = [
    path('helloworld/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
