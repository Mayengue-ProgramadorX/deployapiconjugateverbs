PRONOUNS = ["I", "You", "He", "She", "It", "We", "You (plural)", "They"]

STATES = ["present", "past", "future"]

def handle_present_conjugation(verb, pronoun):
    forms = verb["present"].split("/")
    if len(forms) == 1:
        return forms[0]
    else:
        if pronoun in ["I", "We", "You", "You (plural)", "They"]:
            return forms[0]
        elif pronoun in ["He", "She", "It"]:
            return forms[1]

def conjugate_with_all_pronouns(verb, state):
    conjugations = {}
    for pronoun in PRONOUNS:
        if state == "present":
            conjugated = handle_present_conjugation(verb, pronoun)
        elif state == "past":
            conjugated = verb["past"]
        elif state == "future":
            conjugated = verb["future"]
        conjugations[pronoun] = conjugated
    return conjugations
