from django.shortcuts import render
from .models import FoodLog
from .serializers import FoodLogSerializer, FoodLogMiniSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

class FoodLogview(viewsets.ModelViewSet):
    queryset = FoodLog.objects.all()
    serializer_class = FoodLogSerializer

    def list(self, request, *args, **kwargs):
        foodItems = FoodLog.objects.all()
        serializer = FoodLogSerializer(foodItems, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def foodlogList(request):
	foodLoglists = FoodLog.objects.all().order_by('-id')
	serializer = FoodLogSerializer(foodLoglists, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def foodlogDetail(request, pk):
	foodLog = FoodLog.objects.get(id=pk)
	serializer = FoodLogSerializer(foodLog, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def foodItemCreate(request):
	serializer = FoodLogSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def foodItemUpdate(request, pk):
	foodItem = FoodLog.objects.get(id=pk)
	serializer = FoodLogSerializer(instance=foodItem, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def foodItemDelete(request, pk):
	fooditem = FoodLog.objects.get(id=pk)
	fooditem.delete()
	return Response('Requested Item has been succsesfully deleted!')


# trial --ignore
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/foodlog-list/',
		'Detail View':'/foodlog-detail/<str:pk>/',
		'Create':'/foodlog-create/',
		'Update':'/foodlog-update/<str:pk>/',
		'Delete':'/foodlog-delete/<str:pk>/',
		}
	return Response(api_urls)