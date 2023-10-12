from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView


from version.forms import VersionForm
from version.models import Version


# Create your views here.
class VersionListView(ListView):
    model = Version

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(versions_activity=True)
        return queryset


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.object.product_id])

class VersionDetailView(DetailView):
    model = Version

class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('version:list')


class VersionUpdateView(UpdateView):
    form_class = VersionForm
    model = Version
    success_url = reverse_lazy('version:list')