from django.contrib import admin
from Interface import models as InterfaceModels
from RestApi import models as RestApiModels


admin.site.register(InterfaceModels.Task)


class WorkerStatus_Admin(admin.ModelAdmin):
    list_display = ['workerName', 'status', 'created_at', 'updated_at']
admin.site.register(InterfaceModels.WorkerStatus, WorkerStatus_Admin)
