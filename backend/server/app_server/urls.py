from django.urls import path, include
from .api import (
        UserAPI, AccountAPI, LoginAPI
    )
from .views import home
from knox import views as knox_views
urlpatterns = [
    path('', home, name='home'),
    path('users/register/', UserAPI.as_view({'post': 'create'})),
    path('users/list/', UserAPI.as_view({'get': 'list'})),
    path('users/login/', LoginAPI.as_view({'post': 'login'})),
    path('users/logout/', knox_views.LogoutView.as_view()),
    path('users/<int:pk>/', UserAPI.as_view({'get': 'details'})),
    path('users/<int:pk>/delete/', UserAPI.as_view({'get': 'delete'})),
    path('create-account/', AccountAPI.as_view({'post': 'create_account'}), name='account'),
    path('list-accounts/', AccountAPI.as_view({'get': 'list_accounts'}), name='list_accounts')
]