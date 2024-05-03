
# Creamos nuestra clase con la que trabajaremos con pickcle
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.skills = []
 
    # Hacemos una lista de las habilidades que tiene nuestra persona
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)