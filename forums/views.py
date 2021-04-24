from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Forum

class ForumListView(ListView):
    model = Forum
    template_name = 'forum_list.html'

class ForumDetailView(LoginRequiredMixin, DetailView):
    model = Forum
    template_name = 'forum_detail.html'

class ForumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Forum
    fields = ('title', 'body')
    template_name = 'forum_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ForumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Forum
    template_name = 'forum_delete.html'
    success_url = reverse_lazy('forum_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    fields = ('title', 'body')
    template_name = 'forum_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
