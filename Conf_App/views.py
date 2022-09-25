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
            if capacity > 0 and len(roomName) > 0:
                Room.objects.create(name=roomName, capacity=capacity, projector=projector)
                return redirect('Home')
            else:
                return render(request, template_name='new_room.html', context={'error': 'Oopsi Woopsi! Something went wrong :('})
        else:
            return render(request, template_name='new_room.html',
                          context={'error': 'Room already exist!'})


class RoomList(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, template_name='room_list.html', context={'rooms': rooms})


class RemoveRoom(View):
    def get(self, request, room_id):
        Room.objects.get(pk=room_id).delete()
        return redirect("Room-List")


class EditRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(pk=room_id)
        return render(request, template_name='edit_room.html', context={'room': room})

    def post(self, request, room_id):
        roomName = request.POST.get("roomName") if len(request.POST.get("roomName")) > 0 else False
        capacity = int(request.POST.get("capacity")) if request.POST.get('capacity') else False
        projector = "projector" in request.POST
        room = Room.objects.get(pk=room_id)

        try:
            Room.objects.get(name=roomName)
        except ObjectDoesNotExist:
            if roomName:
                room.name = roomName
            if capacity:
                room.capacity = capacity
            room.projector = projector
            room.save()
            return redirect('Room-List')
        else:
            return render(request, template_name='edit_room.html',
                          context={'error': 'Room already exist!', 'room': room})







