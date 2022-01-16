from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
import sys
sys.path.append("..")
from chat.models import TmpUser

# Create your views here.
def start(request):
    user = TmpUser.objects.all()[0]
    context = {
        'user' : user,
    }
    return render(request, 'set_user/start.html', context)

def loading(request):
    return render(request, 'set_user/loading.html')

def select_nuser(request):
    user = TmpUser.objects.all()
    context = {
        'user' : user,
    }
    return render(request, 'set_user/select_nuser.html', context)

def nickname(request):
    TmpUser.objects.all().delete()
    if request.method == 'POST':
        new_user = TmpUser.objects.create(
            name = request.POST['contents'],
        )
        return redirect('/start/')
    return render(request, 'set_user/nickname.html')

def recommend(request):

    return render(request, 'set_user/recommend.html')