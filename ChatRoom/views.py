from django.shortcuts import render,redirect
from .models import Room,Message
from datetime import datetime
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(requests):
    return render(requests,'home.html')

def room(requests,room):
    username=requests.GET.get('username')
    room_details=Room.objects.get(name=room)
    time=datetime.now
    return render(requests,'room.html',{

        'username':username,
        'room':room,
        'room_details':room_details,
        'time':time,
    })

def checkview(requests):
    room=requests.POST['room_name']
    username=requests.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(requests):
    message = requests.POST['message']
    username = requests.POST['username']
    room_id = requests.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Message Sent!!")

def getMessages(requests,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})