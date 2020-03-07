from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'Interactions', views.InteractionViewSet)


urlpatterns = [
    path('',views.index, name = "index"),
    path('searching/', views.searching, name="searching"),
    path('api',include(router.urls)),
    path('test',views.test, name="test"),
    path('look/', views.InteractionAPIView.as_view())

]