import pytest

from ads.serializers import AdDetailSerializer


@pytest.mark.django_db
def test_ads_detail(client, ad, user_token):
    response = client.get(
        f"/ad/{ad.id}/",
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}")

    print(f"Response status code for /ad/{ad.id}/: {response.status_code}")
    print(f"Response data for /ad/{ad.id}/: {response.data}")

    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data