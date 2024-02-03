from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    # Возьмём нужное. А ненужное не возьмём:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )
    
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context) 

"""
def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
            'id', 'title', 'description'
        # Исключи те объекты, у которых is_published=False:
        ).exclude(is_published=False)
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context) 
"""