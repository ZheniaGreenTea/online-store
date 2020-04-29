
from django.views.generic import ListView
#from django.shortcuts import get_object_or_404, render
from django.views import View
#from django.shortcuts import redirect
from .models import Category


class ProductListView(ListView):

    model = Category
    template_name = 'products/base.html'


    def get_context_data(self, *args, **kwargs):
                context = super(ProductListView,
                                self).get_context_data(**kwargs)

                category_slug = self.kwargs.get('slug')
                print('category_slug:', category_slug)
                if category_slug:
                    category = Category.objects.get(slug=category_slug)
                    print('category:', category)
                    context['products'] = category.product_set.all()
                    print('context:2', context)
                    return context

                return context

                

