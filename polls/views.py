from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CalSerializer
from polls.models import Cal
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
def calc(request,pk):
    if request.method == 'POST':
        print("request.data")
        print(request.data)
        var1=int(request.data['var1'])
        var2=int(request.data['var2'])
        result=int(var1)+int(var2)
        data={'var1':var1,'var2':var2,'result':result}
        serializer = CalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"var2":var2,"var1":var1,"result": result})
    if request.method == 'GET':
        try:
            snippet = Cal.objects.get(id=pk)
        except Cal.DoesNotExist:
            return HttpResponse(status=404)
        serializer = CalSerializer(snippet)
        return JsonResponse(serializer.data)
    