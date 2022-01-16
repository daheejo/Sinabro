from django.shortcuts import render, redirect
from .activity_lists import activity_lists
from chat.models import TmpUser
from .models import Post

# Create your views here.

def menu(request):
    exist = 0
    user = TmpUser.objects.all()[0]
    natures = user.nature_activities
    cities =  user.city_activities
    persons = user.person_activities

    context = {
            'natures' :  natures,
            'cities' : cities,
            'persons' : persons,
            'exist' : exist,
        }
    return  render(request, 'activities/menu.html', context)

def select(request):
    if request.method == 'POST':
        user = TmpUser.objects.all()[0]
        user.nature_activities = request.POST.getlist('natures')
        user.city_activities = request.POST.getlist('cities')
        user.person_activities = request.POST.getlist('persons')

        return redirect('/activities/')
        
        
    activity_natures = activity_lists('nature')
    activity_cities = activity_lists('city')
    activity_persons = activity_lists('person')
    context = {
        'natures' : activity_natures,
        'cities' : activity_cities,
        'persons' : activity_persons,
    }
    return render(request, 'activities/select.html', context) 

def do(request):    
    action_list = ['달리기', '영화보기']
    context = {
        'action_list' : action_list
    }
    return render(request, 'activities/do.html', context) 


def write_action(request):    
    if request.method == 'POST':
        return redirect('/activities/post_list/')
    action = 'movie'
    context = {
        'action' : action
    }
    return render(request, 'activities/write_action.html', context) 

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'activities/post_list.html', context)
