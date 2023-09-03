from dhango.shortcuts import render
def home(request):
    return render(request,'index.html')
