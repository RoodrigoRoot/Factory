from abc import ABCMeta, abstractmethod
"""
Ejemplo del Patrón de Fabrica nivel básico.
"""
class Person(metaclass=ABCMeta):
    
    @abstractmethod
    def create(self):
        """Este método lo van a heredar todas clases por defecto"""
        pass

class Doctor(Person):

    def create(self, name):
        """Aquí creamos el Doctor"""
        print("Doctor: {}".format(name))

class Patient(Person):

    def create(self, name):
        print("Paciente: {}".format(name))
    
class Factory:

    @classmethod
    def createPerson(cls, designation, name):
        eval(designation)().create(name)

designation = input("Please enter the designation - ")
name = input("Please enter the person's name - ")
PersonFactory.createPerson(designation, name)

""" 
def factory_method(user):
    return eval(user)()

factory_method("Patient")
"""
