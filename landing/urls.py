from django.urls import path
from landing.views import TemplView

landing_name = 'landing'

urlpatterns = [
    # TODO добавьте здесь маршрут для вашего обработчика отображения страницы приложения landing
    path('', TemplView.as_view(), name='landing_page'),

]
