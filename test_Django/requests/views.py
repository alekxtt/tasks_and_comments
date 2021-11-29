from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import RequestMessageForm, RequestForm
from .models import RequestMessage, Request

@login_required(login_url='login/')
def create_requestapp(request):
    template = 'requests/create_request.html'
    form = RequestForm(request.POST or None)
    if not form.is_valid():
        requestapps = Request.objects.filter(user=request.user)
        paginator = Paginator(requestapps, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'form': form,
            'page_obj': page_obj,
        }
        return render(request, template, context)
    requestapp = form.save(False)
    requestapp.user = request.user
    requestapp.save()
    return redirect('requests:index')


@login_required(login_url='login/')
def create_request_message(request, request_id):
    form = RequestMessageForm(request.POST or None)
    requestapp = get_object_or_404(Request, id=request_id)
    if form.is_valid():
        requestmessage = form.save(commit=False)
        requestmessage.requestapp = requestapp
        requestmessage.save()
    return redirect('requests:find_request_id', requestapp.id)


@login_required(login_url='login/')
def find_request_id(request, request_id):
    template = 'requests/request_detail.html'
    requestapp = get_object_or_404(Request, id=request_id)
    messages = requestapp.requests.all()
    form = RequestMessageForm(request.POST or None)
    context = {
        'requestapp': requestapp,
        'form': form,
        'messages': messages,
    }
    return render(request, template, context)


@login_required(login_url='login/')
def find_request_id_sub(request):
    if request.method == "POST":
        id = request.POST['search_id']
    return redirect('requests:find_request_id', id)


@login_required(login_url='login/')
def find_messages_request_id(request, request_id):
    template = 'requests/list_of_messages.html'
    messages = Request.objects.get(id=request_id).requests.all()
    paginator = Paginator(messages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required(login_url='login/')
def list_of_requests(request):
    template = 'requests/list_of_requests.html'
    requestapps = Request.objects.filter(user=request.user)
    context = {
        'requestapps': requestapps,
    }
    return render(request, template, context)
