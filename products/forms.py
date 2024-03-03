from django import forms
from .models import Product
from .models import Lesson
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['product', 'name', 'min_users', 'max_users']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['product', 'title', 'video_link']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'start_date']