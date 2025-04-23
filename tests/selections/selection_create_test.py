import pytest


@pytest.mark.django_db
def test_selection_create(client, user_token, user, ad):
    response = client.post(
        "/selection/create/",
        {
            "name": "new test selection",
            "owner": user.id,
            "items": [ad.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}")

    assert response.status_code == 201
    assert response.data == {'id': 1, 'name': 'new test selection', 'owner': user.id, 'items': [ad.id]}