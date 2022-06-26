from django.urls import path
from .views import una_vista, un_template
urlpatterns = [
    path('', un_template),
   # path('mi-template', un_template),
]