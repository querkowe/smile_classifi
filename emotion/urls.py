from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'emotion'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('main/', views.main, name='main'),
    path('stream/', views.stream, name='stream'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
