from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    
    def some_operation(self):
        product = self.factory_method()
        result = product.presentacion()
        return result

class ConcreteDoctor(Creator):

    def factory_method(self):
        return Doctor()



class ConcretePatient(Creator):

    def factory_method(self):
        return Patient()


class User(ABC):

    @abstractmethod
    def presentacion(self):
        pass


class Doctor(User):

    def presentacion(self):
        return "Soy un Doctor"


class Patient(User):

    def presentacion(self):
        return "Soy un Paciente"


def client_code(user):
    print("Hola." f"{user.some_operation()}")

client_code(ConcreteDoctor())
client_code(ConcretePatient())