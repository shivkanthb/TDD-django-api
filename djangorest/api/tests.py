from django.test import TestCase

# Create your tests here.
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
	"""Test suite for Bucketlist model"""

	def setUp(self):
		self.bucketlist_name = "Write world class code"
		self.bucketlist = Bucketlist(name=self.bucketlist_name)

	def test_model_can_create_a_bucketlist(self):
		old_count = Bucketlist.objects.count()
		self.bucketlist.save()
		new_count = Bucketlist.objects.count()
		self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
	""" Test suite for api views"""

	def setUp(self):
		self.client = APIClient()
		self.bucketlist_data = {'name' : 'Go to Ibiza'}
		self.response = self.client.post(
			reverse('create'),
			self.bucketlist_data,
			format="json")

	def test_api_can_create_a_bucketlist(self):
		""" Test the creation capability"""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_a_bucketlist(self):
		bucketlist = Bucketlist.objects.get()
		response = self.client.get(
			reverse('details'),
			kwargs={'pk': bucketlist.id},
			format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, bucketlist)

	def test_api_can_update_bucketlist(self):
		change_bucketlist = {'name':'Updated bucketlist'}
		response = self.client.put(
			reverse('details', kwargs={'pk':bucketlist.id}),
			change_bucketlist,
			format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_api_can_delete_bucketlist(self):
		bucketlist = Bucketlist.objects.get()
		response = self.client.delete(
			reverse('details', kwargs={'pk': bucketlist.id}),
			format="json",
			follow=True)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
