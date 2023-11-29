#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name="", job=""):
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()
            print(f"Person {self.name} is created.")

        if job != "":
            if job not in self.APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                self.job = None  
            else:
                self.job = job
                if hasattr(self, 'name') and hasattr(self, 'job'):
                    print(f"{self.name} works as a {self.job}.")

pass
