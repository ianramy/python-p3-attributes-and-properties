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
    def __init__(self, name=None, job=None):
        name_valid = isinstance(name, str) and 1 <= len(name) <= 25 if name is not None else True
        job_valid = job in APPROVED_JOBS

        # Only print the first validation error encountered
        if not name_valid:
            print("Name must be string between 1 and 25 characters.")
        if not job_valid:
            print("Job must be in list of approved jobs.")

        if name_valid:
            self.name = name.title()if name else None

        if job_valid:
            self.job = job
