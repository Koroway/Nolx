import pytest
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.test import APIClient

@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "username"
    password = "password"

    django_user_model.objects.create_user(username=username, password=password, role="hr")
    response = client.post("/user/token/", {"username": username, "password": password}, format='json')

    print(f"Response status code from /user/token/: {response.status_code}")
    print(f"Response data from /user/token/: {response.data}")

    return response.data.get("access")