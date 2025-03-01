from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter() #creating wifi router
router.register('', views.AppointmentViewSet) # creating antenna of the router

urlpatterns = [
    path('', include(router.urls)),
]

