from django.shortcuts import render, redirect
from todo_list.models import List
from todo_list.forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or none)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item added to the list"))

    all_items = List.objects.all
    return render(request, "home.html", {"all_items": all_items})


def about(request):
    return render(request, "about.html", {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item deleted"))
    return redirect("home")


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect("home")


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect("home")


def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or none, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item has been edited"))
            return redirect('home')

    item = List.objects.get(pk=list_id)
    return render(request, "edit.html", {"item": item})

