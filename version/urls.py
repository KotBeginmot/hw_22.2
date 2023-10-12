from django.urls import path

from version.apps import VersionConfig
from version.views import VersionListView, VersionCreateView, VersionDeleteView, VersionDetailView, VersionUpdateView

app_name = VersionConfig.name

urlpatterns = [
    path('versions/', VersionListView.as_view(), name='list'),
    path('create/<int:pk>/', VersionCreateView.as_view(), name='form'),
    path('delete/<int:pk>/', VersionDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', VersionDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', VersionUpdateView.as_view(), name='update'),
]
