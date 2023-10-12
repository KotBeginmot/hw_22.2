from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from catalog.apps import CatalogConfig
from catalog.forms import ProductCreateForm, CategoryCreateForm
from catalog.models import Product, ContactData, Category
from version.models import Version

app_name = CatalogConfig.name


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


class ContactsCreateView(CreateView):
    model = ContactData
    template_name = 'catalog/contacts.html'
    fields = ('name', 'phone', 'text')
    success_url = reverse_lazy('catalog:contacts')


class ProductsListView(ListView):
    model = Category
    template_name = 'catalog/products.html'


class CategoryProductsListView(ListView):
    model = Product
    template_name = 'catalog/category_product.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(category=self.kwargs.get('pk'))

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category = Category.objects.get(id=self.kwargs.get('pk'))

        context_data['title'] = f" Категория {category.name}"

        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'catalog/product_create.html'

    def get_success_url(self):
        return reverse('catalog:category_product', args=[self.object.category_id])


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'

    # success_url = reverse_lazy('catalog:products')
    def get_success_url(self):
        return reverse('catalog:category_product', args=[self.object.category_id])


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'catalog/catalog_form.html'
    success_url = reverse_lazy('catalog:products')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'catalog/catalog_form.html'
    success_url = reverse_lazy('catalog:products')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/category_delete.html'
    success_url = reverse_lazy('catalog:products')
