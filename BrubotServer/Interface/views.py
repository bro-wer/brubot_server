from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import models
from django.http import JsonResponse
from django.http import HttpResponse
from .utils.torrentSearcher.extratorrentSearcher import ExtratorrentSearcher
from django.http import JsonResponse



app_name='Interface'


class HomePage(TemplateView):
    template_name = "Interface/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allTasks = models.Task.objects.all()
        allWorkers = models.WorkerStatus.objects.all()
        print(str(len(allWorkers)))

        context.update({"allTasks" : allTasks})
        context.update({"allWorkers" : allWorkers})
        return context


class NewTask(TemplateView):
    template_name = "Interface/newtask.html"


def findTorrents(request):
    print("\nfindTorrents\n")

    extratorrentSearcher = ExtratorrentSearcher(request.GET.get('torrentName'))
    extratorrentSearcher.searchForTorrents()
    response_data = extratorrentSearcher.getHtmlResponse()

    return HttpResponse(response_data)


def getAllTasks(request):
    response_data = {}
    allTasks = models.Task.objects.all()
    for task in allTasks:
        response_data[str(task.id)] = task.getDict()
    return JsonResponse(response_data)

def getWaitingTasks(request):
    response_data = {}
    waitingTasks = models.Task.objects.all().filter(status = "NS")
    for task in waitingTasks:
        response_data[str(task.id)] = task.getDict()
    return JsonResponse(response_data)
