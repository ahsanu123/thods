from typing import Callable, List, TypeVar
from dataclasses import dataclass

import numpy as np
from numpy import arccos, dot
from numpy._typing import NDArray

T = TypeVar("T")

v = np.array([[10, 9, 3]])
w = np.array([[2, 5, 12]])


class Mapping:
    def __init__(self):
        self.listNumber: list[int] = []
        self.add: Callable[[int, str], str]


@dataclass
class Employee:
    name: str
    dept: str
    salary: float


employee = Employee(name="hello", dept="world", salary=100)


class Stack[T]:
    passengers: list[T]
    pass


class Star:
    pass


class Animal:
    def __init__(self) -> None:
        self.name: str
        self.animalType: str


class Dog(Animal):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.animalType = "dog"


class Cat(Animal):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.animalType = "cat"


class MyPet[T: Animal]:
    def __init__(self, animal: T) -> None:
        self.animal: T = animal


bony = MyPet(Cat(name="bony"))
