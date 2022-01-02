from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from calc.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('calc.urls')),
    #path('', include(router.urls)),
#    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#    path('admin/', admin.site.urls),
]
