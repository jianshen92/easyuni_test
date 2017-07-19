from django.contrib import admin
from programme.models import ProgramCategory, Program, Training, TrainingDate
# Register your models here.

class ProgramCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProgramCategory, ProgramCategoryAdmin)

class ProgramAdmin(admin.ModelAdmin):
    pass
admin.site.register(Program, ProgramAdmin)

class TrainingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Training, TrainingAdmin)

class TrainingDateAdmin(admin.ModelAdmin):
    pass
admin.site.register(TrainingDate, TrainingDateAdmin)