from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):
	""" create behavior of our rest api"""
	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating new bucketlist"""
		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	""" Class to handle http GET, PUT and DELETE requests"""

	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer