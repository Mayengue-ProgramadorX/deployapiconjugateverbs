import random
from .verbs import VERBS
from .services import STATES

def get_random_verb_and_state():
    verb = random.choice(VERBS)
    state = random.choice(STATES)
    return verb, state
