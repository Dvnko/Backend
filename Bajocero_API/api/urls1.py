from django.urls import path
from .views import RegistroView

urlpatterns = [
    path('registros/', RegistroView.as_view(), name='registros_lista'),
    path('registros/<int:id>', RegistroView.as_view(), name='registros_proceso')
]
