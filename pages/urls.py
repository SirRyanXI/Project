from django.urls import path
from .views import HomePageView, ShopPageView, ForumPageView

urlpatterns = [
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('forum/', ForumPageView.as_view(), name='forum'),
    path('', HomePageView.as_view(), name='home'),
]