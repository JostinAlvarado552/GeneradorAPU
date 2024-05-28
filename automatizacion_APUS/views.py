import xlwings as xw
from django.contrib import messages
from .models import Rubros, Definicion, Especificacion, Medicion_Pago, Apu, Categoria
from django.shortcuts import render

def buscar_rubros(request):
    if request.method == 'POST':
        ids = request.POST.get('ids', '').split(',')
        rubros_data = {}
        contador = 1
        for id in ids:
            try:
                rubro = Rubros.objects.get(id=int(id))
                definiciones = list(Definicion.objects.filter(rubro=rubro).values('contenido'))
                especificaciones = list(Especificacion.objects.filter(rubro=rubro).values('contenido'))
                mediciones_pagos = list(Medicion_Pago.objects.filter(rubro=rubro).values('contenido'))

                # Obtener los detalles de los APUs desde la base de datos
                detalles = {}
                apus = Apu.objects.filter(rubro=rubro)
                for apu in apus:
                    categoria_nombre = apu.categoria.contenido
                    if categoria_nombre not in detalles:
                        detalles[categoria_nombre] = []
                    detalles[categoria_nombre].append({'nombre': apu.contenido})

                rubros_data[id] = {
                    'contador': f'{contador:03d}',
                    'rubro': rubro.concepto,
                    'unidad': rubro.unidad,
                    'definiciones': definiciones,
                    'especificaciones': especificaciones,
                    'mediciones_pagos': mediciones_pagos,
                    'detalles': detalles,
                }
                contador += 1
            except Rubros.DoesNotExist:
                messages.error(request, f"No se encontró el rubro con ID {id}")
            except Exception as e:
                messages.error(request, f"Error al procesar el rubro con ID {id}: {str(e)}")

        context = {
            'rubros_data': rubros_data,
        }
        print(context)
        return render(request, 'resultado_rubros.html', context)
    else:
        return render(request, 'buscar_rubros.html')



def process_id(id_value):
    Detalles = {}
    try:
        wb = xw.Book('automatizacion_APUS/documento/apu.xlsm')
        sheet = wb.sheets['ANALISIS']
        sheet.range('C5').value = id_value
        wb.app.calculate()

        # Inicialización del diccionario Detalles con listas para cada categoría
        Detalles = {
            sheet.range('D16').value: [],
            sheet.range('D39').value: [],
            sheet.range('D62').value: [],
            sheet.range('D85').value: []
        }

        # Proceso para el rango 18-38
        for i in range(18, 38):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'F{i}').value
            if nombre and nombre != 0.0:
                Detalles[sheet.range('D16').value].append({'nombre': nombre, 'cantidad': cantidad})

        # Proceso para el rango 41-61
        for i in range(41, 61):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'F{i}').value
            if nombre and nombre != 0.0:
                Detalles[sheet.range('D39').value].append({'nombre': nombre, 'cantidad': cantidad})

        # Proceso para el rango 64-84
        for i in range(64, 84):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'H{i}').value
            if nombre and nombre != 0.0:
                Detalles[sheet.range('D62').value].append({'nombre': nombre, 'cantidad': cantidad})

        # Proceso para el rango 87-92
        for i in range(87, 92):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'H{i}').value
            if nombre and nombre != 0.0:
                Detalles[sheet.range('D85').value].append({'nombre': nombre, 'cantidad': cantidad})

        # Eliminar las claves que tienen listas vacías
        Detalles = {key: value for key, value in Detalles.items() if value}

        wb.save()
        wb.close()

    except Exception as e:
        return {'error': str(e)}

    return Detalles




