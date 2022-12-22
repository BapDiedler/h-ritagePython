from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def nourrir(self):
        pass


class Panda(Animal):
    def nourrir(self):
        print("nourrir avec du bambou")


po = Panda()
po.nourrir()
