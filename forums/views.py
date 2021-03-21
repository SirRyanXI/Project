from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Forum

class ForumListView(ListView):
    model = Forum
    template_name = 'forum_list.html'

class ForumDetailView(DetailView):
    model = Forum
    template_name = 'forum_detail.html'

class ForumUpdateView(UpdateView):
    model = Forum
    fields = ('title', 'body',)
    template_name = 'forum_edit.html'

class ForumDeleteView(DeleteView):
    model = Forum
    template_name = 'forum_delete.html'
    success_url = reverse_lazy('forum_list')

class ForumCreateView(CreateView):
    model = Forum
    fields = ('title', 'body', 'author')
    template_name = 'forum_new.html'