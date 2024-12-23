from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home(request):
    #можно сделать redirect(reverse('get_recipe'))
    #но так приятнее
    context = {
        'dishes': DATA.keys(),
        'person': [i for i in range(300)]
    }
    return render(request, 'home.html', context)


def get_recipe(request, dish=''):
    servings =  request.GET.get('servings', 1)
    recipe = {}
    if dish in DATA:
        for ingr, amount in DATA[dish].items():
            recipe[ingr] = amount * int(servings)
    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
