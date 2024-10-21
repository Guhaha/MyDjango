from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<year>/<int:month>/<slug:day>/', views.myvariable, name='myvariable'),
    path('turnTo', RedirectView.as_view(url='/'), name='turnTo')
]