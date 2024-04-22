from django.contrib import admin

from company.models import Employee, Company, Position


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'company')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company)
admin.site.register(Position)
