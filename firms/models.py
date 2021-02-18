from django.db import models


class List_of_firm(models.Model):
    list = models.TextField()


class Add_employee(models.Model):
    employee = models.TextField()


class Register_a_company(models.Model):
    company = models.TextField()

# STARTAPP
