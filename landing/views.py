from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from app.forms import TemplateForm


# Create your views here.
class TemplView(View):
    def get(self, request):
        form = TemplateForm()
        return render(request, 'landing/index.html', context={"form": form})

    def post(self, request):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            text = form.cleaned_data.get("name")  # Имя
            email = form.cleaned_data.get("email")  # E-mail
            textarea = form.cleaned_data.get("message")  # Сообщение

            return JsonResponse(form.cleaned_data,
                                json_dumps_params={'ensure_ascii': False,
                                                   'indent': 4})

        return render(request, 'landing/index.html', context={"form": form})
