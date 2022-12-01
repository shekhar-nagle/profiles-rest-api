from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello_viewset')
"""Note: base_name is use to retrive the URL in our router """

urlpatterns = [
path('hello-view/', views.HelloApiVIew.as_view()),
path('', include(router.urls))
]
