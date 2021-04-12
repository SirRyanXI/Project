from django.urls import path
from .views import (
    ForumListView,
    ForumUpdateView,
    ForumDetailView,
    ForumDeleteView,
    ForumCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        ForumUpdateView.as_view(), name='forum_edit'),
    path('<int:pk>/',
        ForumDetailView.as_view(), name='forum_detail'),
    path('<int:pk>/delete/',
        ForumDeleteView.as_view(), name='forum_delete'),
    path('new/', ForumCreateView.as_view(), name='forum_new'),
    path('', ForumListView.as_view(), name='forum_list'),
]