from django.shortcuts import render
from rest_framework.parsers import JSONParser  # parsing data from the client
from django.views.decorators.csrf import csrf_exempt  # To bypass having a CSRF token
from django.http import HttpResponse, JsonResponse  # for sending response to the client
from .serializers import TaskSerializer  # API definition for task
from .models import Task  # Task model


@csrf_exempt
def tasks(request):
    ''' List all task snippets '''
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)   # serialize the task data
        return JsonResponse(serializer.data,safe=False)  # return a Json response
    elif request.method == 'POST':
        data = JSONParser().parse(request)   # parse the incoming information
        serializer = TaskSerializer(data=data)   # instanciate with the serializer
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):
    try:
        # obtain the task with the passed id.
        task = Task.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)

        if serializer.is_valid():  # check whether the sent information is okay
            serializer.save()  # if okay, save it on the database
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        task.delete()
        # return a no content response.
        return HttpResponse(status=204)
