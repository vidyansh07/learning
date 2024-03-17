from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('<int:id>/', views.post_detail, name = 'post_details'),
]

# urlpatterns = [
#     path('', views.job_list, name = 'job_list'),
#     path('<slug:slug>/', views.job_detail, name = 'job_detail'),
# ]
