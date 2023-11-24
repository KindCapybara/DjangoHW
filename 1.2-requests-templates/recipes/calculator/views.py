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
}


def recipe(requests, recipe=''):
    persons = int(requests.GET.get("servings", 1))
    dish_dict = DATA.get(recipe, {})
    context = {
        'recipe': {
            ingredient: amount * persons
            for ingredient, amount in dish_dict.items()
        }
    }
    return render(requests, 'calculator/index.html', context)
