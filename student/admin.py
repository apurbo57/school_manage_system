from django.contrib import admin
from .models import *

#class DetailInfoAdmin(admin.ModelAdmin):
    #list_display = ('std_class',)
admin.site.register(StudentInfo)
admin.site.register(StudentDetailInfo)
admin.site.register(StudentClassInfo)
admin.site.register(StudentShiftInfo)
admin.site.register(Attendance)
admin.site.register(Result)