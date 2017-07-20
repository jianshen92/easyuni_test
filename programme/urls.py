from django.conf.urls import url
from programme import views

# urls for main page
urlpatterns = [
    url(r'^$', views.display_view, name="display_page"),
    url(r'^edit/$', views.all_edit, name="all_edit"),
]

# urls for program category
urlpatterns += [
    url(r'^programcat/add/$', views.add_program_category, name="program_cat_add"),
    url(r'^programcat/edit/(?P<id>[0-9]+)/?$', views.edit_program_category, name="program_cat_edit"),
]

# urls for program
urlpatterns += [
    url(r'^program/add/$', views.program_add, name="program_add"),
    url(r'^program/edit/(?P<id>[0-9]+)/?$', views.program_edit, name="program_edit"),
]

# urls for training
urlpatterns += [
    url(r'^training/add/$', views.training_add, name="training_add"),
    url(r'^training/edit/(?P<id>[0-9]+)/?$', views.training_edit, name="training_edit"),
]

# url for training date
urlpatterns += [
    url(r'^trainingdate/add/$', views.training_date_add, name="training_date_add"),
    url(r'^trainingdate/edit/(?P<id>[0-9]+)/?$', views.training_date_edit, name="training_date_edit"),
]