from django.contrib import admin
from firms import models

class ListAdmin(admin.ModelAdmin):
    pass

class AddEmployeeAdmin(admin.ModelAdmin):
    pass


class RegisterACompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.List_of_firm, ListAdmin)
admin.site.register(models.Add_employee, AddEmployeeAdmin)
admin.site.register(models.Register_a_company, RegisterACompanyAdmin)
