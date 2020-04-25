from django.http import HttpResponse, Http404
# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Category


def first_function(request):
    return HttpResponse("app Products works good")

class CategoryListView(ListView):

        model = Category
        context_object_name = 'menu_category_list'  # ваше собственное имя переменной контекста в шаблоне
        template_name = 'products/base.html'  # Определение имени вашего шаблона


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView,
                        self).get_context_data(**kwargs)
        category = context['object']
        context["products"] = category.product_set.all()
        return context