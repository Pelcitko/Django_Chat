from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from Chat_app.models import Room


def login(request):
    return render(request, "Chat_app/login.html", {})


class RoomList(ListView):
    model = Room

@login_required(login_url='/login/')
def room_list(request):
    queryset_list = Room.objects.all()
    paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list': queryset,
        'title': "Otevřené místnosti",
        'page_request_var': page_request_var,
    }

    return render(request, 'Chat_app/home2.html', context)

@login_required(login_url='/login/')
def home(request):
    # return HttpResponse("templates")
    return render(request, "Chat_app/home.html", {})  # response
