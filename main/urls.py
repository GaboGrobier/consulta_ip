from django.urls import path
from . import views
urlpatterns = [
    path('', views.home ),
    path('consulta/', views.consultar),
    path('json/', views.informacion_json),
    path('api/<str:numip>', views.ip_api)

]
