from django.shortcuts import render

# Create your views here.
def coditions(request):
    d={'a':10,'b':5}
    return render(request,'coditions.html',context=d)