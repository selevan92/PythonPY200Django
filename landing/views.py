from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from landing.forms import TemplateForm


# Create your views here.
class TemplView(View):
    def get(self, request):
        form = TemplateForm()
        return render(request, 'landing/index.html', context={"form": form})

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            name = form.cleaned_data.get("name")  # Имя
            email = form.cleaned_data.get("email")  # E-mail
            message = form.cleaned_data.get("message")  # Сообщение

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')

            data = {
                'name': name,
                'email': email,
                'message': message,
                'ip_address': ip,
                'user_agent': user_agent
            }

            return JsonResponse(data,
                                json_dumps_params={'ensure_ascii': False,
                                                   'indent': 4})

        return render(request, 'landing/index.html', context={"form": form})
