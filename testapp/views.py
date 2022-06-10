

# Create your views here.
import json
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.core import serializers
 
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tutorial_list_published(request):
    
    tutorials = Tutorial.objects.filter(is_status=1)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    # try:
    #     thing = serializers.serialize('json', [Tutorial.objects.get(published=True),])
    #     thing = json.loads(thing)[0]['fields']
    #     thing_serialized_single = TutorialSerializer(data=thing)

    #     if thing_serialized_single.is_valid():
    #         return JsonResponse({'status':'success', 'data': thing_serialized_single.data}, safe = False, status = status.HTTP_200_OK)
    #     return JsonResponse({'status':'fail', 'data': thing_serialized_single.errors}, safe = False, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    # except Tutorial.DoesNotExist: 
    #     return JsonResponse({'status':'fail' ,'message': 'The thing does not exist'}, status=status.HTTP_404_NOT_FOUND) 