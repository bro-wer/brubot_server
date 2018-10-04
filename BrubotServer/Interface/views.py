from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import models
from django.http import JsonResponse
from django.http import HttpResponse
from .utils.torrentSearcher import TorrentSearcher

# Create your views here.
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
    torrentName = request.GET.get('torrentName')

    print("torrentName")
    print(torrentName)

    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    response_data = TorrentSearcher(torrentName).getHtmlResponse()

    return HttpResponse(response_data)
