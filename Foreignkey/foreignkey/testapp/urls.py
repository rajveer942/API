from django.urls import path,include
from testapp import views
from rest_framework.routers import DefaultRouter

#Creating router object
router=DefaultRouter()
#Register Router
router.register('singer',views.SingerModelViewSet,basename='singer')
router.register('song', views.SongModelViewSet,basename='song')

urlpatterns = [
    path('singer',include(router.urls)),
    
]
