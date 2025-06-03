from django.contrib import admin
from django.urls import include, path

from .views import CustomLoginView, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('source-m/', include('source_m.urls')),
]
