from django.shortcuts import render
import json
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import CustomUser
# Create your views here.

@csrf_exempt
def login(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return JsonResponse({'message': 'OK'}, status=200)

    else:
        return JsonResponse({'message': 'User not found!'}, status=200)

@csrf_exempt
def logout(request):
    user = auth.logout(request)

    return JsonResponse({'message': 'logged out'}, status=200)

@csrf_exempt
def register(request):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')

    user = CustomUser.objects.create_user(username=username)
    user.set_password(password)
    user.save()

    return JsonResponse({'message': f'user with username {user.username} created'}, status=200)