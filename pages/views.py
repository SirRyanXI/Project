from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ForumPageView(TemplateView):
    template_name = 'forum.html'

class ShopPageView(TemplateView):
    template_name = 'shop.html'