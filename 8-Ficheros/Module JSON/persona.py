
# Definimos nuestra clase persona
class Persona:
    def __init__(self, nombre, skills=[]):
        self.nombre = nombre
        self.skills = skills # Guarda una lista de habilidades
 
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
 
    # Definimos el metodo __repr__ que nos regresa la informacion de nuestro objeto
    def __repr__(self):
        return f'{type(self).__name__}(nombre={self.nombre}, skills={self.skills})'
