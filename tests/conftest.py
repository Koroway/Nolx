import pytest
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username='testuser', password='password', first_name='Test')

@pytest.fixture
def user_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

@pytest.fixture
def category():
    from ads.models import Category
    return Category.objects.create(name='Test Category', slug='test-slug')

@pytest.fixture
def ad(user, category):
    from ads.models import Ad
    return Ad.objects.create(
        name='Test Ad',
        author=user,
        price=100,
        description='Test description',
        is_published=True,
        category=category
    )