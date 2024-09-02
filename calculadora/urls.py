from django.urls import path
from .views import ProductoListView, CalculoInversionView, RedirectToSwaggerView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='productos-list'),
    path('calcular-inversion/', CalculoInversionView.as_view(), name='calcular-inversion'),
    path('', RedirectToSwaggerView.as_view())
]
