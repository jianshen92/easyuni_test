from django.conf.urls import url
from programme import views

urlpatterns = [
    url(r'^$', views.display_view, name="display_page"),
    url(r'^edit/$', views.all_edit, name="all_edit"),
]

urlpatterns += [
    url(r'^programcat/$', views.program_category, name="program_cat"),
    url(r'^programcat/add/$', views.add_program_category, name="program_cat_add"),
    url(r'^programcat/edit/(?P<id>[0-9]+)/?$', views.edit_program_category, name="program_cat_edit"),
]

urlpatterns += [
    url(r'^program/$', views.program, name="program"),
    url(r'^program/add/$', views.program_add, name="program_add"),
    url(r'^program/edit/(?P<id>[0-9]+)/?$', views.program_edit, name="program_edit"),
]

urlpatterns += [
    url(r'^training/$', views.training, name="training"),
    url(r'^training/add/$', views.training_add, name="training_add"),
    url(r'^training/edit/(?P<id>[0-9]+)/?$', views.training_edit, name="training_edit"),
]

urlpatterns += [
    url(r'^trainingdate/$', views.training_date, name="training_date"),
    url(r'^trainingdate/add/$', views.training_date_add, name="training_date_add"),
    url(r'^trainingdate/edit/(?P<id>[0-9]+)/?$', views.training_date_edit, name="training_date_edit"),
]