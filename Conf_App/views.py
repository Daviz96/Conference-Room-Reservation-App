from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, template_name='base_template.html')


class AddRoom(View):
    def get(self, request):
        return render(request, template_name='new_room.html')

    def post(self, request):
        # <other view logic>
        roomName = request.POST.get("roomName")
        capacity = request.POST.get("capacity")
        projector = request.POST.get("projector")

        return HttpResponse('result')


