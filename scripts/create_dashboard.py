import os
import subprocess
import sys

# Auto-install pip packages
required_packages = ['openpyxl', 'xlrd']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installiere {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
wb.remove(wb.active)

# -------------------------------------------------------------
# Blatt 1: Ist-Daten (MIT HISTORIE)
# -------------------------------------------------------------
ws1 = wb.create_sheet('1_Ist_Daten')

# Wir legen Periode 0 und Periode 1 an. 
# Neue Perioden werden einfach als Spalte D, E, F usw. durch auto_import angefügt.
data1 = [
    ['Feld (Excel-Referenz)', 'Periode 0', 'Periode 1'],
    ['Kassenbestand (Start)', 0.85, 28.05],
    ['Eigenkapital', 31.27, 35.25],
    ['Gewinnvortrag', 2.00, 5.27],
    ['Pensionsrückstellungen', 13.87, 15.95],
    ['Geplante E-Steuer (%)', 0.30, 0.30],
    ['Zinssatz Langfristig (%)', 0.06, 0.06],
    ['Zinssatz Kurzfristig (%)', 0.08, 0.08]
]
for row in data1: ws1.append(row)

# -------------------------------------------------------------
# Blatt 2: Team-Inputs (Gilt für die Planung der nächsten Periode)
# -------------------------------------------------------------
ws2 = wb.create_sheet('2_Team_Inputs')
data2 = [
    ['Feld', 'Plan-Wert', 'Einheit', 'Kommilitonen fragen!'],
    ['Geplante Absatzmenge', 45000, 'Stück', 'Vertrieb'],
    ['Geplanter Preis', 3000, 'EUR', 'Vertrieb'],
    ['--- KOSTEN ---', '', '', ''],
    ['Total Herstellkosten', 90.0, 'MEUR', 'Fertigung (inkl. Personal)'],
    ['Total Verwaltungskosten', 10.0, 'MEUR', 'Verwaltung'],
    ['Total Marketing/Vertrieb', 15.0, 'MEUR', 'Marketing/Vertrieb'],
    ['--- INVESTITIONEN ---', '', '', ''],
    ['Abschreibungen Alt-Anlagen', 6.0, 'MEUR', 'Aus Anlagevermögen fortschreiben'],
    ['Geplante Neuinvestition (Kaufpreis)', 15.0, 'MEUR', 'Voller Preis = Cash-Abfluss!'],
    ['Geplante Neu-Abschreibung', 1.5, 'MEUR', 'Z.B. 10% des Kaufpreises'],
    ['Veränderung Pensionsrückstellungen', 2.0, 'MEUR', '+ Erhöhung schont Liquidität']
]
for row in data2: ws2.append(row)

# -------------------------------------------------------------
# Blatt 3: Szenarien (Dynamische Formeln)
# -------------------------------------------------------------
# Die Formel =INDEX('1_Ist_Daten'!2:2, COUNTA('1_Ist_Daten'!2:2))
# holt sich IN DIESER ZEILE immer den absolut rechesten (neuesten) Wert!
# Wir lagern das in "Hilfszellen" (Spalte E) aus, damit die Formeln lesbar bleiben.

ws3 = wb.create_sheet('3_Szenario_Rechner')

ws3['E1'] = "--- DYNAMISCHER IMPORTER (NICHT LÖSCHEN) ---"
ws3['E2'] = "Aktuelle Kasse:"
ws3['F2'] = "=INDEX('1_Ist_Daten'!2:2, COUNTA('1_Ist_Daten'!2:2))"

ws3['E3'] = "Aktuelles Eigenkapital:"
ws3['F3'] = "=INDEX('1_Ist_Daten'!3:3, COUNTA('1_Ist_Daten'!3:3))"

ws3['E4'] = "Gewinnvortrag:"
ws3['F4'] = "=INDEX('1_Ist_Daten'!4:4, COUNTA('1_Ist_Daten'!4:4))"

ws3['E5'] = "Pensionsrückstellungen:"
ws3['F5'] = "=INDEX('1_Ist_Daten'!5:5, COUNTA('1_Ist_Daten'!5:5))"

ws3['E6'] = "Steuersatz:"
ws3['F6'] = "=INDEX('1_Ist_Daten'!6:6, COUNTA('1_Ist_Daten'!6:6))"

ws3['E7'] = "Zinssatz Langfristig:"
ws3['F7'] = "=INDEX('1_Ist_Daten'!7:7, COUNTA('1_Ist_Daten'!7:7))"

ws3['E8'] = "Zinssatz Kurzfristig:"
ws3['F8'] = "=INDEX('1_Ist_Daten'!8:8, COUNTA('1_Ist_Daten'!8:8))"

for i in range(1, 9):
    ws3.cell(row=i, column=5).font = Font(color="808080", italic=True)
    ws3.cell(row=i, column=6).font = Font(color="808080", italic=True)


data3 = [
    ['Feld', 'Szenario A (Defensiv)', 'Szenario B (Aggressiv)', 'Szenario C'],
    ['--- 1: EINGABEN (CFO) ---', '', '', ''],
    ['Kurzfristiger Kredit (MEUR)', 10.0, 15.0, 5.0],
    ['Langfristiger Kredit (MEUR)', 15.0, 20.0, 10.0],
    ['Dividende (MEUR)', 1.0, 0.0, 2.0],
    ['--- 2: BERECHNUNG GEWINN ---', '', '', ''],
    ['Plan-Umsatz', "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000", "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000", "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000"],
    ['Plan-EBIT', "=B7-'2_Team_Inputs'!B5-'2_Team_Inputs'!B6-'2_Team_Inputs'!B7-'2_Team_Inputs'!B9-'2_Team_Inputs'!B11", "=C7-'2_Team_Inputs'!B5-'2_Team_Inputs'!B6-'2_Team_Inputs'!B7-'2_Team_Inputs'!B9-'2_Team_Inputs'!B11", "=D7-'2_Team_Inputs'!B5-'2_Team_Inputs'!B6-'2_Team_Inputs'!B7-'2_Team_Inputs'!B9-'2_Team_Inputs'!B11"],
    ['Plan-Zinsaufwand', "=(B3*F8)+(B4*F7)", "=(C3*F8)+(C4*F7)", "=(D3*F8)+(D4*F7)"],
    ['Plan-EBT (Ergebnis vor Steuern)', "=B8-B9", "=C8-C9", "=D8-D9"],
    ['Plan-Steuern', "=IF(B10>0, B10*F6, 0)", "=IF(C10>0, C10*F6, 0)", "=IF(D10>0, D10*F6, 0)"],
    ['Plan-Jahresüberschuss', "=B10-B11", "=C10-C11", "=D10-D11"],
    ['--- 3: TOPSIM ZIELEINGABEN ---', '', '', ''],
    ['Plan-Eigenkapital', "=F3+B12-B5", "=F3+C12-C5", "=F3+D12-D5"],
    ['Plan-EKR (%)', "=(B12/B14)*100", "=(C12/C14)*100", "=(D12/D14)*100"],
    ['Plan-Operativer Cashflow (MEUR)', "=B12+'2_Team_Inputs'!B9+'2_Team_Inputs'!B11+'2_Team_Inputs'!B12", "=C12+'2_Team_Inputs'!B9+'2_Team_Inputs'!B11+'2_Team_Inputs'!B12", "=D12+'2_Team_Inputs'!B9+'2_Team_Inputs'!B11+'2_Team_Inputs'!B12"],
    ['--- 4: TOPSIM FATAL CHECK ---', '', '', ''],
    ['Kassenbestand ENDE (>0!)', "=F2+B16+B3+B4-B5-'2_Team_Inputs'!B10", "=F2+C16+C3+C4-C5-'2_Team_Inputs'!B10", "=F2+D16+D3+D4-D5-'2_Team_Inputs'!B10"],
]

for idx, row in enumerate(data3, 1):
    for col_idx, value in enumerate(row, 1):
        ws3.cell(row=idx, column=col_idx, value=value)
    if '---' in str(row[0]):
        ws3.cell(row=idx, column=1).font = Font(bold=True)

# Styling
for ws in [ws1, ws2, ws3]:
    for col in range(1, 5):
        try:
            ws.cell(row=1, column=col).font = Font(bold=True)
            ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = 25
        except:
            pass
    ws.column_dimensions['A'].width = 45

# Datei speichern
file_path = os.path.join(os.getcwd(), 'TOPSIM_CFO_Dashboard.xlsx')
wb.save(file_path)
print(f"Dynamisches Excel-Dashboard erstellt: {file_path}")
