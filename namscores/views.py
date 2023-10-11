from django.http import JsonResponse
from .models import Scores
from .serializers import ScoresSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def scores_list(request, format=None):

    if request.method == 'GET':
        scores = Scores.objects.all()
        serializer = ScoresSerializer(scores, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ScoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    #The code below is used to return raw json instad of a object
    #return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def scores_details(request, id, format=None):

    try:
        scores = Scores.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoresSerializer(scores)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ScoresSerializer(scores, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        scores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)