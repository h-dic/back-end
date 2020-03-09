from django.urls import path,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'Interactions', views.InteractionViewSet)
router.register(r'Drugs', views.DrugsViewSet)
router.register(r'Herbs', views.HerbsViewSet)


urlpatterns = [
    path('',views.index, name = "index"),
    path('searching/', views.searching, name="searching"),
    path('api',include(router.urls)),
    path('saveinteractions/',views.save_interactions, name="test"),
    path('look/', views.InteractionAPIView.as_view()),
    path('savedrugsherbs/', views.save_herbs_and_drugs)

]