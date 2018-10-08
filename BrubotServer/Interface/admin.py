from django.contrib import admin
from Interface import models as InterfaceModels


class Task_Admin(admin.ModelAdmin):
    list_display = ['taskName', 'status', 'type']
    list_editable = ['taskName', 'status', 'type']
admin.site.register(InterfaceModels.Task, Task_Admin)


class WorkerStatus_Admin(admin.ModelAdmin):
    list_display = ['workerName', 'status', 'created_at', 'updated_at']
admin.site.register(InterfaceModels.WorkerStatus, WorkerStatus_Admin)
