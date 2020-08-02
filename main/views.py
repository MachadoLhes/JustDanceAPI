# Django Imports
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

# App Imports
import json
from main.functions import get_random_song, mount_response_json


# Views
@require_http_methods(["GET", "POST"])
def main(request):
    if request.method == "GET":
        return render(request, 'main.html')
    elif request.method == "POST":
        try:
            isUnlimited = request.POST['isUnlimited']
        except:
            isUnlimited = False

        song = get_random_song(isUnlimited)

        response = mount_response_json(song)

        context = {
            'post': True,
            'isUnlimited': isUnlimited,
            'response': response,
        }

        return render(request, 'main.html', context)
    else:
        return HttpResponse("405 Method Not Allowed", status=405)

@require_http_methods(["GET"])
def getSong(request):
    if request.method == "GET":
        song = get_random_song(True)

        return JsonResponse(mount_response_json(song))