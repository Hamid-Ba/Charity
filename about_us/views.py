from django.shortcuts import render
from accounts.models import User


def about_us(request):
    if request.method == 'GET':
        users = User.objects.all()
        result = []

        for user in users: result.append(user.get_full_name())

        return render(request,'about_us.html',{'users':result})