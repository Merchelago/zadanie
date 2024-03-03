from django.shortcuts import render, redirect
from .models import Product, Lesson, Group
from .forms import ProductForm, LessonForm, GroupForm


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Перенаправляем на список продуктов после успешного добавления
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')  # Перенаправляем на список уроков после успешного добавления
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form})


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')  # Перенаправляем на список групп после успешного добавления
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})


def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'group_detail.html', {'group': group})
