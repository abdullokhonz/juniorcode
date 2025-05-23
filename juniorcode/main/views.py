from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Courses
from students.models import Students
from teachers.models import Teachers


# Create your views here.


def main(request):
    title: str = "JuniorCode — обучение программированию"

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

    noindex: bool = False

    return render(request, 'main/index.html', {
        'title': title,
        'data_class_format': data_class_format,
        'data_direction': data_direction,
        'noindex': noindex
    })


def robots_txt(request):
    robots_content = settings.ROBOTS_DEFAULT_RULES

    return HttpResponse(robots_content, content_type="text/plain")


# @require_GET
# def sitemap():
#     content = '''<?xml version="1.0" encoding="UTF-8"?>
#     <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
#        <url>
#           <loc>https://juniorcode.up.railway.app/</loc>
#           <lastmod>2025-04-12</lastmod>
#           <changefreq>weekly</changefreq>
#           <priority>1.0</priority>
#        </url>
#     </urlset>'''
#
#     return HttpResponse(content, content_type="application/xml")
