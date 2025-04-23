import pytest

from ads.serializers import AdDetailSerializer


@pytest.mark.django_db
def test_ads_create(client, ad, user_token):
    response = client.get(
        f"/ad/{ad.id}/",
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}")

    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data