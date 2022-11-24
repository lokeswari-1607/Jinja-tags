from django.shortcuts import render

# Create your views here.
def yeshu(request):
    return render(request,'yeshu.html',context={'name':'loki'})
