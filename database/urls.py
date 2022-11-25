
from django.urls import path
from . import views
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
        path('' , views.getroutes),
        path('collect/' , views.getsupply),
        path('add/' , views.additem),
        path('get/<str:pk>/' , views.getitem),
        path('update/<str:pk>' , views.updateitem ),
        path('delete/<str:pk>' , views.deleteitem ),
        path('collectworker/' , views.getsupplyworker ),
        path('api/register/', RegisterAPI.as_view(), name='register'),
        path('api/login/', LoginAPI.as_view(), name='login'),
        path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
        path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
        ]
