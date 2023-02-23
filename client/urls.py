
from .views import UsersAPIViewsSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UsersAPIViewsSet, basename='user')


from django.urls import path, include
urlpatterns = [
    path('users/', include(router.urls)),
]