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
    def __init__(self, name=None, breed=None):
        # Name validation
        name_valid = isinstance(name, str) and 1 <= len(name) <= 25 if name is not None else True
        breed_valid = breed in APPROVED_BREEDS

        # If the name is provided, validate it
        if name is not None and not name_valid:
            print("Name must be string between 1 and 25 characters.")

        # Validate breed
        if not breed_valid and breed is not None:
            print("Breed must be in list of approved breeds.")

        # Only assign valid attributes
        if name_valid:
            self.name = name.title() if name else None

        if breed_valid:
            self.breed = breed
