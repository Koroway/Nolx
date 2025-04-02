from django.shortcuts import render

import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def home(request):
    return JsonResponse({"status": "ok"}, status=200)
@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Ad.objects.all()

        search_text = request.GET.get("name", None)
        if search_text:
            ads = ads.filter(text=search_text)

        response = []
        for ad in ads:
            response.append(
                {
                    "Id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published,
                }
            )

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.load(request.body)

        ad = Ad.objects.create(
            name=(ad_data["name"]),
            author=(ad_data["author"]),
            price=(ad_data["price"]),
            descriptions=(ad_data["description"]),
            address=(ad_data["address"]),
            is_published=(ad_data["is_published"])
        )

        return JsonResponse({
            "Id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


class AdsDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "Id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()

        search_text = request.GET.get("name", None)
        if search_text:
            categories = categories.filter(text=search_text)

        response = []
        for category in categories:
            response.append(
                {
                    "Id": category.id,
                    "name": category.name,
                }
            )

        return JsonResponse(response, safe=False)

    def post(self, request):
       cat_data = json.load(request.body)

       cat = Ad.objects.create(
            name=(cat_data["name"]),
        )

       return JsonResponse({
            "Id": cat.id,
            "name": cat.name,
        })



class CategoriesDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
                "Id": category.id,
                "name": category.name,
        })