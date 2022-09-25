from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist


from Conf_App.models import Room


class Main(View):
    def get(self, request):
        return render(request, template_name='main.html')

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, template_name='home.html')


class AddRoom(View):
    def get(self, request):
        return render(request, template_name='new_room.html')

    def post(self, request):

        roomName = request.POST.get("roomName")
        capacity = int(request.POST.get("capacity"))
        projector = "projector" in request.POST

        try:
            Room.objects.get(name=roomName)
        except ObjectDoesNotExist:
            if capacity >= 0 and len(roomName) > 0:
                Room.objects.create(name=roomName, capacity=capacity, projector=projector)
                return render(request, template_name='home.html')
            else:
                return HttpResponse("Oopsi Woopsi! Something went wrong :(")
        else:
            return HttpResponse("room already exist")


class RoomList(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, template_name='room_list.html', context={'rooms': rooms})


class RemoveRoom(View):
    def get(self, request, room_id):
        Room.objects.get(pk=room_id).delete()
        return redirect("Room-List")











