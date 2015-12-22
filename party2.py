class Person:
    def __init__(self, name, age, like_music):
        self.name=name
        self.age=age
        self.like_music = like_music

    def party_priority(age,like_music):
        if age > 25:
            priority = 3
        elif age >= 18:
            if like_music:
                priority = 1
            else:
                priority = 2
        else:
            priority = 4

        return priority

def party_message(p):
    if p.age > 25:
        message = 'Sorry, ' +p.name + ", you're too old gramps."
    elif p.age >=18:
        if  p.like_music:
            message = 'Hi, ' +p.name + ", you're coming. Bring JD."
        else:
            message = 'No, ' +p.name + ", you're not coming."
    else:
        message = 'No, ' +p.name + ", you're not coming. Too young."
    return message
