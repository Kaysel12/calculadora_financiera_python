# calculadora/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Producto, DiaFeriado
from .serializers import ProductoSerializer, CalculoInversionSerializer
from .services import InversionService
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse

class ProductoListView(APIView):
    permission_classes = [IsAuthenticated]

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(name='search', type=str, location=OpenApiParameter.QUERY, description='Filtro de búsqueda para productos'),
    #         OpenApiParameter(name='sort', type=str, location=OpenApiParameter.QUERY, description='Campo por el cual ordenar los productos')
    #     ]
    # )

    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CalculoInversionView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=CalculoInversionSerializer,
        responses={
            200: OpenApiResponse(description='Resultado del cálculo'),
            400: OpenApiResponse(description='Error en la solicitud'),
            500: OpenApiResponse(description='Error en el envío de datos')
        },
    )

    def post(self, request):
        serializer = CalculoInversionSerializer(data=request.data)
        if serializer.is_valid():
            resultado = InversionService.calcular_fechas(serializer.validated_data)
            return Response(resultado, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
