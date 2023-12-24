from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)
def home_view(request):
    # HTML-вёрстка и данные о вашем первом Django-сайте
    html = "<h1>Добро пожаловать!</h1><p>Здесь вы найдете много интересного.</p>"

    # Сохранение данных о посещении страницы в логи
    logger.info("Данные о посещении страницы")

    return HttpResponse(html)


def about_view(request):
    # HTML-вёрстка и данные о вас
    html = "<h1>Обо мне</h1><p>Я - начинающий веб-разработчик, изучаю Django и другие технологии.</p>"

    # Сохранение данных о посещении страницы в логи"
    logger.error("Посещение страницы 'О себе'")


    return HttpResponse(html)