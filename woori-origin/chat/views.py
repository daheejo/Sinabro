from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from .models import Message


# Create your views here.
def index(request):
    if request.method == 'POST':
        new_message = Message.objects.create(
            send_text=request.POST['contents']
        )
        return redirect('/chat/')

    latest_message_list = Message.objects.order_by('pub_date')[:20]
    context = {
        'latest_message_list':latest_message_list
    }

    return render(request, 'chat/index.html', context)

def detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'chat/detail.html', {'message':message})
