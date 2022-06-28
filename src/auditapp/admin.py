from django.contrib import admin

# Register your models here.
from .models import Emp, AuditStandard, AuditRequirements, Checklist, CRA

admin.site.register(Emp)
# class EmpAdmin(admin.ModelAdmin):
#     list_display = ('id','emp_type_of_audit', 'emp_date_of_audit')
# admin.site.register(Emp,EmpAdmin)    

# admin.site.register(ISO)
# admin.site.register(ISAGO)
admin.site.register(AuditStandard)
admin.site.register(AuditRequirements)
admin.site.register(Checklist)
admin.site.register(CRA)



# Register your models here.

