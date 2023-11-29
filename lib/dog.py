#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="", breed="Mutt"):
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name
            if breed not in Dog.APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
                breed = "Mutt"  # Assign default breed if not in the list
            self.breed = breed
            print(f"{self.name} is born! Breed: {self.breed}")


    pass
