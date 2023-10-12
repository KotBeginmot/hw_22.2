from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from pytils.templatetags.pytils_translit import slugify

import blogrecord
from blogrecord.models import BlogRecord


# Create your views here.
class BlogListView(ListView):
    model = BlogRecord

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(feature=True)

        return queryset


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'content', 'preview', 'feature')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'content', 'preview', 'feature')

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('blog:list')
