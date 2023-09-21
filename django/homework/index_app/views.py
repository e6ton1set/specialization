from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    index_html = """
    <!doctype html>
    <html lang="ru">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Главная страница</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet"
                        integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9"
                        crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"
                        integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm"
                        crossorigin="anonymous"></script>
        </head>
        <body>
            <div class="container text-center my-5 ">
                <h1>Главная страницa</h1>
            </div>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container">
                    <a class="navbar-brand" href="/">
                    <img src="https://clck.ru/35oYhP" alt="Ruslan K." width="100">
                    </a>
                    <button class="navbar-toggler" 
                    type="button" 
                    data-bs-toggle="collapse" 
                    data-bs-target="#navbarNav"
                    aria-controls="navbarNav" 
                    aria-expanded="false" 
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                         <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="http://127.0.0.1:8000/about">Обо мне</a>
                            </li>
                        </ul>
                     </div>
                </div>
            </nav>
            <div class="card text-center cohabitation">
                <div class="card-body">
                    <h5 class="card-title">Привет!</h5>
                    <p class="card-text">Это мой первый проект на фреймворке Django.</p>
                </div>
            </div>
            <style>
                .cohabitation { 
                    margin-top: 50px; 
                    }
            </style>
        </body>
    </html>
    """
    return HttpResponse(index_html)
