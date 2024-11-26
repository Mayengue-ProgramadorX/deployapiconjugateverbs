from django.http import JsonResponse
from .services import conjugate_random_verb_with_all_pronouns


def get_conjugations(request):
    data = conjugate_random_verb_with_all_pronouns()
    return JsonResponse(data)


