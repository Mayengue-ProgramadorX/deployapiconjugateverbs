from django.http import JsonResponse
from .randomizer import get_random_verb_and_state
from .services import conjugate_with_all_pronouns


def get_conjugations(request):
    verb, state = get_random_verb_and_state()
    conjugations = conjugate_with_all_pronouns(verb, state)
    data = {
        "verb": verb["base"],
        "state": state,
        "conjugations": conjugations,
    }
    return JsonResponse(data)


#controla o time 
