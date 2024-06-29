from django.urls import path
from . import views # This imports views from the current app (videos)
from .views import update_qos


urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('update_qos/<int:video_id>/', update_qos, name='update_qos'),
]