from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def main(request):
    data_class_format: list = [
        {
            'color': '#ff69b4',
            'icon': 'fa-solid fa-users-rays',
            'title': 'Групповые занятия',
            'text': 'Очные и онлайн занятия в мини-группах по расписанию.',
        },
        {
            'color': '#ffa500',
            'icon': 'fa-solid fa-street-view',
            'title': 'Индивидуальные занятия',
            'text': 'Программа обучения и расписание подстраиваются пот темп и знания ученика.',
        },
        {
            'color': '#87ceeb',
            'icon': 'fa-solid fa-computer',
            'title': 'Видеокурс',
            'text': 'Самостоятельное обучение в своём темпе по видеокурокам и интерактивным заданиям.',
        },
    ]

    data_direction: list = [
        {
            'color': '#ffff00',
            'icon': 'fa-solid fa-code',
            'title': 'Программирование',
            'text': 'Знакомство детей разных возростов с языками и визуальными средами программирования',
        },
        {
            'color': '#ff0000',
            'icon': 'fa-solid fa-gamepad',
            'title': 'Создание игр',
            'text': 'На этих курсах дети смогут взглянуть на игры глазами инженера-разработчика',
        },
        {
            'color': '#008000',
            'icon': 'fa-solid fa-desktop',
            'title': 'Создание сайтов',
            'text': 'Знакомство с веб-дизайном и веб-разработкой, развитие навыков по созданию сайтов',
        },
        {
            'color': '#a52a2a',
            'icon': 'fa-solid fa-cubes',
            'title': 'Цифровое творчество',
            'text': 'Цель курсов - развитие навыков моделирования и создания игровых миров',
        },
        {
            'color': '#000',
            'icon': 'fa-solid fa-keyboard',
            'title': 'Компьютерная грамотность',
            'text': 'Ученики познакомятся с устройством компьютера и интернета',
        },
        {
            'color': '#800080',
            'icon': 'fa-solid fa-pen-nib',
            'title': 'Графический дизайн',
            'text': 'Школьники изучат инструменты для работы с векторной графикой',
        },
    ]

    return render(request, 'main/index.html', {
        'data_class_format': data_class_format,
        'data_direction': data_direction,
    })


def robots_txt(request):
    robots_content = settings.ROBOTS_DEFAULT_RULES

    # Отправляем ответ с правильным типом контента
    return HttpResponse(robots_content, content_type="text/plain")
