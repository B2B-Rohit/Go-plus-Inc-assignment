from django.shortcuts import render, redirect
from .models import Count

def home(request):
    count = Count.objects.first()
    return render(request, 'index.html', {'count': count})

def like(request):
    count = Count.objects.first()
    count.like_count += 1
    count.save()
    return render(request, 'index.html',{'count': count})

def dislike(request):
    count = Count.objects.first()
    count.dislike_count += 1
    count.save()
    return render(request, 'index.html',{'count':count})
