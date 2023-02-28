from django import forms
from .models import ReviewRating
from .models import Product, ProductGallery
from category.models import Category


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
