from django.conf.urls import url
from programme import views

urlpatterns = [
    url(r'^$', views.display_view, name="display_page"),
]
