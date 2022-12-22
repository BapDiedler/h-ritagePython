from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def nom(self):
        pass

    def onDoitFaire(self,action):
        print(f"{action} {self.nom()} avec {self.nourrir()}")

    @abstractmethod
    def nourrir(self):
        pass

    @abstractmethod
    def heure(self):
        pass


class Panda(Animal):

    def nom(self):
        return "le panda"

    def nourrir(self):
        return "du bambou"

    def heure(self):
        return "12h/14h"


class Lion(Animal):

    def nom(self):
        return "le lion"

    def nourrir(self):
        return "de la viande"

    def heure(self):
        return "12h/14h et 19h/20h"
