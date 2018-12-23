from django.shortcuts import render

# Create your views here.

def index(request):
    """main page of cinema web"""
    return render(request, 'learning_logs/index.html')