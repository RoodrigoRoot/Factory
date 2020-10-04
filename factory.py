from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):

    @abstractmethod
    def create(self):
        pass

class Doctor(Person):

    def create(self, name):
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