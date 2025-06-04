from django.contrib import admin
from django.urls import include, path

from .views import CustomLoginView, HomeView, TestView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('test/', TestView.as_view(), name='test'),

    path('source-m/', include('source_m.urls')),
]
