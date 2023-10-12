from django.urls import path

from blogrecord.apps import BlogrecordConfig
from blogrecord.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogrecordConfig.name

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),

]
