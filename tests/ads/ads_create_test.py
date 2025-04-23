import json
import pytest

@pytest.mark.django_db
def test_ads_create(client, user, category):
    response = client.post(
        "/ad/create/",
        {
            "name": "new test ad",
            "price": 10,
            "description": "test description",
            "is_published": False,
            "author": user.id,
            "category": category.id
        },
        content_type="application/json")

    assert response.status_code == 201
    response_data = json.loads(response.content)
    assert 'id' in response_data
    assert response_data['author'] == user.id
    assert response_data['category'] == category.id
    assert response_data['description'] == 'test description'
    assert response_data['image'] is None
    assert response_data['is_published'] is False
    assert response_data['name'] == 'new test ad'
    assert response_data['price'] == 10