from django.shortcuts import render

def mss(request):
    return render(request, 'jobs/mss.html')
