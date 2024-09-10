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
        # fecha_creacion = make_aware(datetime.strptime(data['fecha_creacion'], '%Y-%m-%d %H:%M:%S'))
        fecha_creacion = data['fecha_creacion']
        
        print("Fecha de creacion" ,fecha_creacion)
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


        fecha_fin = InversionService.calcular_fecha_fin(fecha_inicio, plazo)

        return {
            "producto": producto_id,
            "plazo": plazo,
            "fecha funcional": fecha_creacion,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "plazo_real": (fecha_fin - fecha_inicio).days
        }

    @staticmethod
    def calcular_fecha_fin(fecha_inicio, plazo):
        fecha_fin = fecha_inicio + timedelta(days=plazo)

        while fecha_fin.weekday() >= 5 or DiaFeriado.objects.filter(fecha=fecha_fin.date()).exists():
            print(f"Ajustando fecha: {fecha_fin} cae en fin de semana o feriado")
            fecha_fin += timedelta(days=1)

        return fecha_fin


    @staticmethod
    def calcular_fecha_inicio(fecha_inicio):
        fecha_inicio = fecha_inicio

        while fecha_inicio.weekday() >= 5 or DiaFeriado.objects.filter(fecha=fecha_inicio.date()).exists():
            fecha_inicio += timedelta(days=1)

        return fecha_inicio