from django.shortcuts import render
from models import UserManager

# def index(request):
#     return render(request, 'autentifikasi/index.html')

def addUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        UserManager.objects.create_user(email, username, password)
        users = UserManager.objects.all()
        context = {
        'users': users,
        }
        return render(request, 'autentifikasi/listUsers.html', context)