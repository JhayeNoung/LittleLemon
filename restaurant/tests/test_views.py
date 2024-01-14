from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuItemViewTest(TestCase):
    # create data for the test database
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        MenuItem.objects.create(title='Dish 1', price=10.99)
        MenuItem.objects.create(title='Dish 2', price=15.99)

    #logic for the tests
    def test_getall(self):
        # URL for the view you want to test
        url = reverse('menu')

        # Create an instance of the Django REST framework test client
        client = APIClient()

        # Create a token for the user
        token = Token.objects.create(user=self.user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # Send a GET request to the view
        response = client.get(url, format='json')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve all MenuItem objects from the test database
        MenuItem_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(MenuItem_items, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual("response.data", serializer.data)
