from django.shortcuts import render


def all_blogs(request):
    return render(request,'blogpost/all_blogs.html')
