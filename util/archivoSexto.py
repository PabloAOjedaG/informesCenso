from persistence.informeSexto import InformeSexto
import os
from openpyxl import load_workbook
import os

class ArchivoSexto:
    def crearArchivoSexto(self):
                
        archivoInicial = InformeSexto().lecturaArchivoSexto()
        rutaArchivoFormato = os.getcwd() + "\\censos\\FORMATO 6 MANUFACTURA - Aprobado.xlsx"
        direc_guardado = os.getcwd() + "\\Formatos Finales"
        if not os.path.exists(direc_guardado):
            os.makedirs(direc_guardado)
        for index, row in archivoInicial.iterrows():
            wb = load_workbook(rutaArchivoFormato)
            ws = wb.active
        
            InformeSexto().crearArchivoSexto(ws, row)
        

            output_path = f"{direc_guardado}" + "\\" + f"formularioSextoLleno_{index + 1}.xlsx"
            wb.save(output_path)