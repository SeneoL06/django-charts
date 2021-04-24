from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # shortcut for http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Consumers", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        default_items = [qs_count, 60, 44, 76, 45, 21]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

