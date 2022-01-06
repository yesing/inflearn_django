from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubSerializer, AddSerializer


def home(request):
    return render(request, 'home.html', {'name': 'name'})


@api_view(['GET', 'POST'])
def add(request):
    if request.method == 'POST':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        res = val1 + val2
        serializer = AddSerializer(res)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def sub(request):
    if request.method == 'POST':
        val1 = int(request.POST['num3'])
        val2 = int(request.POST['num4'])
        res = val1 - val2
        serializer = SubSerializer(res)
        return Response(serializer.data)
