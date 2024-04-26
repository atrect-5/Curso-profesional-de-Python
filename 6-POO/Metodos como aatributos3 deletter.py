
class Usuario:
    def __init__(self, password):
        self._passwords = [] # Aqui se almacenara un registrp de todas las contraseñas que ha tenido
        self.password = password
 
    @property
    def password(self):
        # Este Getter regresa el ultimo elemento de la cadena de contraseñas (contraseña actual), None si no hay contraseñas
        return None if not len(self._passwords) else self._passwords[-1]
 
    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError("El password debe tener 8 dígitos como mínimo") # Solo acepta contraseñas con longitud mayor de 8
        self._passwords.append(password) # Agrega la contraseña a la lista de contraseñas
 
    @password.deleter
    def password(self):
        self._passwords = [] # Define la cadena de contraseñas como vacia (Elimina el registro de contraseñas)
 
 
# Creamos un usuario y asignamos la primer contraseña
user = Usuario("ClaveNumero1")
print("Clave actual:", user.password) # El Getter nos devuelve el ultimo elemento del registro (contraseña acutual)
# Clave actual: ClaveNumero1

# Agregamos otro registro
user.password = "SegundaClaveAsignada"
print("Clave actual:", user.password)
# Clave actual: SegundaClaveAsignada
 
# Aqui observamos el registro de todas las contraseñas que se han tenido (directamente en el atributo, ya que este no cuenta con Getter)
print("Historial de claves:", user._passwords)
# Historial de claves: ['ClaveNumero1', 'SegundaClaveAsignada']
 
del user.password # La palabra reservada 'del' llama al destructor del atributo (deletter)
print("Clave actual:", user.password)
# Clave actual: None
print("Historial de claves:", user._passwords)
# Historial de claves: []