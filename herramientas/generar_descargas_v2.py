# -*- coding: utf-8 -*-
"""Genera los archivos de descarga del catálogo Pirobioma a partir de data/cepas.js
(y data/cepas_en.js para la versión en inglés):
  descargas/pirobioma_catalogo.xlsx    (español)
  descargas/pirobioma_catalogue.xlsx   (inglés)
  descargas/pirobioma_sequences.fasta  (todas las secuencias, encabezados en inglés)
Uso: desde la raíz del repo ->  python herramientas/generar_descargas.py
Requiere: python3 + openpyxl, y node (para aplicar la traducción de cepas_en.js).
Volver a correr cada vez que se editen los datos."""
import json, os, re, subprocess, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://pirobioma.github.io/"
HOY = datetime.date.today().isoformat()
DOI = "https://doi.org/10.5281/zenodo.24043372"  # <- cambiar por el DOI real
AUT = "Acuña-Rodríguez IS, Ascencio Astudillo C, Barrera Valenzuela A & Miño R"
CITA_ES = "Cita sugerida: " + AUT + " (2026) El Pirobioma de la Región del Maule: cepario de hongos y bacterias pirófilos (FONDECYT 11240628). Versión 1.0 [Conjunto de datos]. Centro de Ecología Integrativa, Universidad de Talca. Zenodo. " + DOI + " — Catálogo en línea: https://pirobioma.github.io/"
CITA_EN = "Suggested citation: " + AUT + " (2026) The Pyrobiome of the Maule Region: a culture collection of pyrophilous fungi and bacteria (FONDECYT 11240628). Version 1.0 [Data set]. Centro de Ecología Integrativa, Universidad de Talca. Zenodo. " + DOI + " — Online catalogue: https://pirobioma.github.io/"

def cargar(js_files):
    code = "var window={};\n" + "\n".join(open(os.path.join(RAIZ, f), encoding="utf-8").read() for f in js_files)
    code = code.replace("const strains", "var strains") + "\nprocess.stdout.write(JSON.stringify(strains));"
    return json.loads(subprocess.run(["node"], input=code, capture_output=True, text=True, check=True, encoding="utf-8").stdout)

def partir_seq(t):
    # "16S rRNA · consenso 27F+1492R · 1331 pb" -> marcador, método
    partes = [p.strip() for p in (t or "").split("·")]
    return partes[0], (partes[1] if len(partes) > 1 else "")

T = {
 "es": dict(hoja="Cepas", hoja2="Léeme", url="catalogo.html#",
   cols=["Código","Tipo","Identificación","Phylum","Clase","Orden","Familia","Género","Especie",
         "Origen del suelo","Horizonte","Condición de quemado","Crecimiento en medio con carbón (1–5)",
         "Descripción morfológica","Marcador","Método de secuenciación","Largo (pb)","Secuencia","Ficha en línea"],
   tipo={"Bacteria":"Bacteria","Hongo":"Hongo"},
   crec=["","Crece muy poco","Crecimiento bajo","Crecimiento moderado","Crecimiento alto","Crece abundantemente"],
   leeme=[("Catálogo de cepas del Pirobioma del Maule",None),
     ("Proyecto ANID FONDECYT de Iniciación N° 11240628 · Universidad de Talca · Centro de Ecología Integrativa",None),
     ("Bacterias y hongos aislados en medio selectivo con carbón de madera quemada como única fuente de carbono, desde suelos de bosque nativo y plantaciones de Pinus radiata quemados en la Región del Maule, Chile.",None),
     ("",None),
     ("Columnas",True),
     ("Identificación: nombre asignado a partir de la secuencia (puede ser a nivel de género o 'sp').",None),
     ("Origen del suelo: Nativo (bosque nativo), Plantación (Pinus radiata) o Seta (cuerpo fructífero).",None),
     ("Condición de quemado: Quemado joven (incendio reciente) o Quemado viejo (incendio antiguo).",None),
     ("Crecimiento en medio con carbón: escala 1 (crece muy poco) a 5 (crece abundantemente).",None),
     ("Marcador: 16S rRNA para bacterias, ITS para hongos. Método: consenso de lecturas forward+reverse o lectura única.",None),
     ("Las secuencias también están disponibles en formato FASTA en el sitio (pirobioma_sequences.fasta).",None),
     ("Celdas vacías: dato aún no disponible para esa cepa.",None),
     ("",None),
     ("Licencia y cita",True),
     ("Datos bajo licencia CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.es): libres para uso no comercial citando al Proyecto Pirobioma del Maule (FONDECYT 11240628). Para uso comercial, solicitar autorización a ian.acuna@utalca.cl.",None),
     (CITA_ES,None),
     ("",None),
     ("Contacto: Ian S. Acuña-Rodríguez · ian.acuna@utalca.cl",None),
     ("Versión de los datos: {fecha} · {n} cepas",None)]),
 "en": dict(hoja="Strains", hoja2="Read me", url="en/catalog.html#",
   cols=["Code","Type","Identification","Phylum","Class","Order","Family","Genus","Species",
         "Soil origin","Horizon","Burn condition","Growth on charcoal medium (1–5)",
         "Morphological description","Marker","Sequencing method","Length (bp)","Sequence","Online record"],
   tipo={"Bacteria":"Bacterium","Hongo":"Fungus"},
   crec=["","Very little growth","Low growth","Moderate growth","High growth","Abundant growth"],
   leeme=[("Pyrobiome of the Maule Region — strain catalogue",None),
     ("ANID FONDECYT Initiation Project No. 11240628 · Universidad de Talca · Centro de Ecología Integrativa",None),
     ("Bacteria and fungi isolated on selective media with burned-wood charcoal as the sole carbon source, from soils of native forest and Pinus radiata plantations burned in the Maule Region, Chile.",None),
     ("",None),
     ("Columns",True),
     ("Identification: name assigned from the sequence (may be at genus level or 'sp').",None),
     ("Soil origin: Native forest, Pine plantation (Pinus radiata) or Mushroom (fruiting body).",None),
     ("Burn condition: Recently burned or Burned long ago.",None),
     ("Growth on charcoal medium: scale from 1 (very little growth) to 5 (abundant growth).",None),
     ("Marker: 16S rRNA for bacteria, ITS for fungi. Method: forward+reverse consensus or single read.",None),
     ("Sequences are also available in FASTA format on the website (pirobioma_sequences.fasta).",None),
     ("Empty cells: data not yet available for that strain.",None),
     ("",None),
     ("Licence and citation",True),
     ("Data licensed under CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.en): free for non-commercial use with attribution to the Pirobioma del Maule Project (FONDECYT 11240628). For commercial use, please request permission from ian.acuna@utalca.cl.",None),
     (CITA_EN,None),
     ("",None),
     ("Contact: Ian S. Acuña-Rodríguez · ian.acuna@utalca.cl",None),
     ("Data version: {fecha} · {n} strains",None)]),
}

def fila(s, t):
    tx = s.get("taxonomia") or {}
    marcador, metodo = partir_seq(s.get("seq_tipo"))
    sq = (s.get("secuencia") or "").strip()
    nombre = s.get("nombre_display") or ""
    if nombre in ("Sin identificar", "Unidentified"): nombre = ""
    c = s.get("crecimiento")
    return [s["id"], t["tipo"].get(s["tipo"], s["tipo"]), nombre,
            tx.get("phylum") or "", tx.get("clase") or "", tx.get("orden") or "", tx.get("familia") or "",
            tx.get("genero") or "", tx.get("especie") or "",
            s.get("origen") or "", s.get("horizonte") or "", s.get("condicion_quemado") or "",
            c if c else None, s.get("descripcion") or "",
            marcador, metodo if sq else "", len(sq) if sq else None, sq,
            BASE_URL + t["url"] + s["id"]]

def excel(strains, lang, salida):
    t = T[lang]; wb = Workbook(); ws = wb.active; ws.title = t["hoja"]
    ws.append(t["cols"])
    verde = PatternFill("solid", fgColor="2F4A2B")
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF"); cell.fill = verde
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for s in strains:
        ws.append(fila(s, t))
        link = ws.cell(row=ws.max_row, column=len(t["cols"])); link.hyperlink = link.value; link.style = "Hyperlink"
    anchos = [8,10,30,16,18,18,18,16,28,18,12,18,14,60,10,26,10,40,40]
    for i, w in enumerate(anchos, 1): ws.column_dimensions[get_column_letter(i)].width = w
    for row in ws.iter_rows(min_row=2):
        row[13].alignment = Alignment(wrap_text=True, vertical="top")
        for c in row: 
            if c.column != 14: c.alignment = Alignment(vertical="top")
    ws.row_dimensions[1].height = 32
    ws.freeze_panes = "B2"; ws.auto_filter.ref = ws.dimensions
    ws2 = wb.create_sheet(t["hoja2"]); ws2.column_dimensions["A"].width = 120
    for txt, bold in t["leeme"]:
        ws2.append([txt.format(fecha=HOY, n=len(strains))])
        c = ws2.cell(row=ws2.max_row, column=1); c.alignment = Alignment(wrap_text=True)
        if bold or ws2.max_row == 1: c.font = Font(bold=True, size=13 if ws2.max_row == 1 else 11)
    wb.save(salida)

def fasta(strains, salida):
    with open(salida, "w", encoding="utf-8", newline="\n") as f:
        n = 0
        for s in strains:
            sq = re.sub(r"\s+", "", s.get("secuencia") or "")
            if not sq: continue
            marcador, metodo = partir_seq(s.get("seq_tipo"))
            nombre = s.get("nombre_display") or "Unidentified"
            f.write(f">{s['id']} {nombre} | {marcador} | {metodo} | {s.get('origen')} | {s.get('condicion_quemado')} | {s.get('horizonte')} | Pirobioma del Maule FONDECYT 11240628\n")
            for i in range(0, len(sq), 70): f.write(sq[i:i+70] + "\n")
            n += 1
    return n

if __name__ == "__main__":
    os.makedirs(os.path.join(RAIZ, "descargas"), exist_ok=True)
    es = cargar(["data/cepas.js"]); en = cargar(["data/cepas.js", "data/cepas_en.js"])
    excel(es, "es", os.path.join(RAIZ, "descargas", "pirobioma_catalogo.xlsx"))
    excel(en, "en", os.path.join(RAIZ, "descargas", "pirobioma_catalogue.xlsx"))
    n = fasta(en, os.path.join(RAIZ, "descargas", "pirobioma_sequences.fasta"))
    print(f"OK: {len(es)} cepas · {n} secuencias en FASTA")
