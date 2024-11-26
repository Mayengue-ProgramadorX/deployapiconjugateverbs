import random
from .verbs import VERBS

PRONOUNS = ["I", "You", "He", "She", "It", "We", "You (plural)", "They"]

STATES = ["present", "past", "future"]


def  handle_present_conjugation(verb, pronoun):
    forms = verb["present"].split("/")
    if len(forms) == 1:
        # Regular verb in the present tense (only one form)
        return forms[0]
    
    else:
        # Irregular verb in the present tense (two different forms)
        if pronoun in ["I", "We", "You", "You (plural)", "They"]:
            return forms[0]
        
        elif pronoun in ["He", "She", "It"]:
            return forms[1]


def conjugate_random_verb_with_all_pronouns():
    verb = random.choice(VERBS)
    state = random.choice(STATES)    

    conjugations = {}
    for pronoun in PRONOUNS:
        if state == "present":
           conjugated = handle_present_conjugation(verb, pronoun)
        
        elif state == "past":
            conjugated = verb["past"]
        
        elif state == "future":
            conjugated = verb["future"]
            
        conjugations[pronoun] = conjugated
        
    return {
        "verb": verb["base"],
        "state": state,
        "conjugations": conjugations
    }
    