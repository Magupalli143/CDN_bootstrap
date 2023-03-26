from django.shortcuts import render

# Create your views here.
def boost(request):
    return render(request,'boost.html')