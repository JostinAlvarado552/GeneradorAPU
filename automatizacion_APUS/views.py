import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from docx.opc.oxml import qn
from openpyxl.reader.excel import load_workbook

from .forms import IDForm
from .models import Rubros, Definicion, Medicion_Pago
from docx import Document
import xlwings as xw
from django.shortcuts import render
from .forms import IDForm


def buscar_rubros(request):
    if request.method == 'POST':
        ids = request.POST.get('ids', '').split(',')
        rubros_encontrados = []
        definiciones = {}
        medicion_pagos = {}
        detalles_dict = {}
        for id in ids:
            try:
                rubro = Rubros.objects.get(id=int(id))
                rubros_encontrados.append(rubro)
                definiciones[rubro.id] = Definicion.objects.filter(rubro=rubro)
                medicion_pagos[rubro.id] = Medicion_Pago.objects.filter(rubro=rubro)
                detalles_dict[rubro.id] = process_id(id)
            except Rubros.DoesNotExist:
                messages.error(request, f"No se encontró el rubro con ID {id}")

        # Create a new Document
        doc = Document()
        doc.add_heading('Resultados de Búsqueda de Rubros', 0)

        for i, rubro in enumerate(rubros_encontrados):
            if i > 0:
                doc.add_page_break()  # Add a page break before each new rubro

            doc.add_heading(f'Rubro ID: {rubro.id}', level=1)
            doc.add_paragraph(f'Concepto: {rubro.concepto}')
            doc.add_paragraph(f'Unidad: {rubro.especificaciones}')
            doc.add_paragraph(f'Detalles: {detalles_dict}')
            doc.add_heading('Definiciones', level=2)
            if definiciones[rubro.id]:
                for definicion in definiciones[rubro.id]:
                    doc.add_paragraph(definicion.contenido)
            else:
                doc.add_paragraph('No hay definiciones disponibles.')

            doc.add_heading('Mediciones y Métodos de Pago', level=2)
            if medicion_pagos[rubro.id]:
                for mp in medicion_pagos[rubro.id]:
                    doc.add_paragraph(f'Medición: {mp.medicion}')
                    doc.add_paragraph(f'Método de Pago: {mp.metodoPago}')
            else:
                doc.add_paragraph('No hay mediciones y métodos de pago disponibles.')

        # Create a response with the document
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=resultados_rubros.docx'
        doc.save(response)
        return response

    else:
        return render(request, 'buscar_rubros.html')

def process_id(id_value):
    Detalles = {}
    try:
        wb = xw.Book('automatizacion_APUS/documento/APU.xlsm')
        sheet = wb.sheets['ANALISIS']
        sheet.range('C5').value = id_value
        wb.app.calculate()

        for i in range(18, 38):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'F{i}').value
            if nombre != 0.0:
                Detalles[sheet.range('D16').value] = {'nombre': nombre, 'cantidad': cantidad}

        for i in range(41, 61):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'F{i}').value
            if nombre != 0.0:
                Detalles[sheet.range('D39').value] = {'nombre': nombre, 'cantidad': cantidad}

        for i in range(64, 84):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'H{i}').value
            if nombre != 0.0:
                Detalles[sheet.range('D62').value] = {'nombre': nombre, 'cantidad': cantidad}

        for i in range(87, 92):
            nombre = sheet.range(f'D{i}').value
            cantidad = sheet.range(f'H{i}').value
            if nombre != 0.0:
                Detalles[sheet.range('D85').value] = {'nombre': nombre, 'cantidad': cantidad}

        wb.save()
        wb.close()

    except Exception as e:
        return {'error': str(e)}

    return Detalles


