#!/usr/bin/env python3

class Dog:
    def __init__(self,name,breed="Mutt"):
        self.breed= breed
        self.name = name 
    


fido = Dog("fido")
print(fido.name)
fido.breed="shutt"
print(fido.breed)