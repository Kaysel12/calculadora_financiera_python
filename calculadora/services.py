# calculadora/services.py

from datetime import timedelta, datetime
from .models import Producto, DiaFeriado
from django.utils.timezone import make_aware

class InversionService:

    @staticmethod
    def calcular_fechas(data):
        producto_id = data['producto']
        en_reinversion = data['en_reinversion']
        plazo = data['plazo']
        fecha_creacion = data['fecha_creacion']
        
        producto = Producto.objects.get(id=producto_id)
        hora_operativa = producto.hora_operativa
        es_dentro_horario = fecha_creacion.time() <= hora_operativa

        fecha_inicio = InversionService.calcular_fecha_inicio(fecha_creacion)

        if en_reinversion:
            if es_dentro_horario:
                dias_a_sumar = producto.dias_reinversion_in
            else:
                dias_a_sumar = producto.dias_reinversion_out
        else:
            if es_dentro_horario:
                dias_a_sumar = producto.dias_operativos_in
            else:
                dias_a_sumar = producto.dias_operativos_out

        fecha_inicio = fecha_inicio + timedelta(days=dias_a_sumar)

        fechas = InversionService.calcular_fecha_fin(fecha_inicio, plazo)

        return {
            "producto": producto_id,
            "plazo": plazo,
            "fecha_funcional": fecha_creacion,
            "fecha_inicio": fechas['fecha_inicio'],
            "fecha_fin": fechas['fecha_final'],
            "plazo_real": (fechas['fecha_final'] - fechas['fecha_inicio']).days
        }

    @staticmethod
    def calcular_fecha_fin(fecha_inicio, plazo):
        fecha_inicio = InversionService.calcular_fecha_inicio(fecha_inicio)
        fecha_fin = fecha_inicio + timedelta(days=plazo)

        while fecha_fin.weekday() >= 5 or DiaFeriado.objects.filter(fecha=fecha_fin.date()).exists():
            fecha_fin += timedelta(days=1)

        return {
            "fecha_inicio": fecha_inicio,
            "fecha_final": fecha_fin
        }


    @staticmethod
    def calcular_fecha_inicio(fecha_inicio):
        fecha_inicio = fecha_inicio

        while fecha_inicio.weekday() >= 5 or DiaFeriado.objects.filter(fecha=fecha_inicio.date()).exists():
            fecha_inicio += timedelta(days=1)

        return fecha_inicio