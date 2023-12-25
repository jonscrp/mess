from django.shortcuts import render

def index(request):
    return render(request, "sillyme/index.html")

def room(request, room_name):
    return render(request, "sillyme/room.html", {"room_name":room_name})