from django import forms

from catalog.models import Product, Category
from version.models import Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form control'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_versions_activity(self):
        clean_data = self.cleaned_data['versions_activity']
        for i in Version.objects.filter(product_id=self.cleaned_data['product']):
            if i.versions_activity:
                raise forms.ValidationError('Уже есть минимум 1 активная версия , удалите ее')
        return clean_data