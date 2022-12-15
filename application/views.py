from django.http.response import JsonResponse
from .models import Service


# Create your views here.

def show_services(request):
    services = Service.objects.values()
    services = [
        {'name': item.get('name'), 'price': item.get('price')} for item in services
    ]
    return JsonResponse(services, safe=False)
