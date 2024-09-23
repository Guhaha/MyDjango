from django.shortcuts import render

# Create your views here.
def index(request):
    # val = 'TTTT!'
    # print(f'this is index html show... {val}')
    return render(request, 'index.html')