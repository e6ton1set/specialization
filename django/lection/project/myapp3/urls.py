from django.urls import path
from myapp3.views import hello, HelloView, year_post, MonthPost, post_detail


urlpatterns = [
    path("hello/", hello, name="hello"),
    path("HelloView/", HelloView.as_view(), name="hello_view"),
    path("posts/<int:year>", year_post, name="year_post"),
    path("posts/<int:year>/<int:month>", MonthPost.as_view(), name="month_post"),
    path("posts/<int:year>/<int:month>/<slug:slug>", post_detail, name="post_detail"),
]