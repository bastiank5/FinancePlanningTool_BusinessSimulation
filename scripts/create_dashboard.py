import os
import subprocess
import sys
import shutil
from datetime import datetime

# Auto-install openpyxl falls nicht vorhanden
try:
    import openpyxl
except ImportError:
    print("Installiere openpyxl...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl

from openpyxl.styles import Font, PatternFill
from openpyxl.formatting.rule import CellIsRule

wb = openpyxl.Workbook()
# Standard-Blatt entfernen
wb.remove(wb.active)

# Blatt 1: Ist-Daten
ws1 = wb.create_sheet('1_Ist_Daten')
data1 = [
    ['Feld', 'Wert', 'Einheit', 'Hinweis (Aus letzter Excel/Berichten)'],
    ['Kassenbestand (Start Periode)', 28.05, 'MEUR', 'Aus Bilanz Aktiva'],
    ['Eigenkapital', 35.25, 'MEUR', 'Aus Bilanz Passiva'],
    ['Gewinnvortrag', 5.27, 'MEUR', 'Maximal mögliche Dividende'],
    ['Steuerlicher Verlustvortrag', 0.00, 'MEUR', 'Vorjahresverlust (vermindert Steuern)'],
    ['Pensionsrückstellungen', 15.95, 'MEUR', 'Passiva'],
    ['Bestehende Kurzfristkredite (Alt)', 12.0, 'MEUR', 'Werden auto-getilgt (fließen zwingend ab!)'],
    ['Bestehende Langfristkredite (Alt)', 20.0, 'MEUR', 'Nur für Plan-Zinsen wichtig'],
    ['Geplante E-Steuer (%)', 0.45, '%', 'Im Handbuch S.33 klar auf 45% festgelegt'],
    ['Zinssatz Langfristig (%)', 0.07, '%', 'Bsp: 7% aus Handbuch S.31 / Per.0'],
    ['Zinssatz Kurzfristig (%)', 0.08, '%', 'Bsp: 8% aus Berichten / Per.0'],
    ['Zinssatz Überziehen (%)', 0.13, '%', '13% Strafzins (Handbuch)']
]
for row in data1: ws1.append(row)

# Blatt 2: Team-Inputs
ws2 = wb.create_sheet('2_Team_Inputs')
data2 = [
    ['Feld', 'Wert', 'Einheit', 'Hinweis (Vom Team erfragen)'],
    ['Geplante Absatzmenge', 45000, 'Stück', 'Planzahl Vertrieb'],
    ['Geplanter Preis', 3000, 'EUR', 'Planzahl Vertrieb'],
    ['--- KERNAUSGABEN ---', '', '', ''],
    ['Total Herstellkosten', 90.0, 'MEUR', 'inkl. Personal in Fertigung'],
    ['Total Verwaltungskosten', 10.0, 'MEUR', ''],
    ['Total Marketing/Vertrieb', 15.0, 'MEUR', ''],
    ['Forschung & Entwicklung (F&E)', 2.50, 'MEUR', 'Ökologie, Technologie, etc.'],
    ['Marktforschung', 0.15, 'MEUR', 'Kosten für Berichte / Analysen'],
    ['--- INVESTITIONEN ---', '', '', ''],
    ['Freiwillige Tilgung Langfristkr.', 0.0, 'MEUR', 'Cash-Out! Kurzfrist wird automatisch getilgt.'],
    ['Abschreibungen Alt-Anlagen', 6.0, 'MEUR', 'inklusive 0.25 MEUR fixe Gebäude-AfA'],
    ['Geplante Neuinvestition', 15.0, 'MEUR', 'Totaler Kaufpreis Anlage - Cash Out!'],
    ['Geplante Neu-Abschreibung', 1.5, 'MEUR', 'Z.B. 10% Lineare Abschreibung'],
    ['Veränderung Pensionsrückstellungen', 2.0, 'MEUR', 'Positiv = Cash-plus']
]
for row in data2: ws2.append(row)

# Blatt 3: Szenarien
ws3 = wb.create_sheet('3_Szenario_Rechner')
data3 = [
    ['Feld', 'Szenario A (Defensiv)', 'Szenario B (Aggressiv)', 'Szenario C'],
    ['--- 1: EINGABEN (DEINE CFO ENTSCHEIDUNG) ---', '', '', ''],
    ['NEUER Kurzfristiger Kredit (MEUR)', 15.0, 20.0, 10.0],
    ['NEUER Langfristiger Kredit (MEUR)', 0.0, 10.0, 0.0],
    ['Dividende (MEUR)', 1.0, 0.0, 2.0],
    ['Geplanter Wertpapierkauf', 0.0, 0.0, 0.0],
    ['--- 2: BERECHNUNG EBIT & GEWINN ---', '', '', ''],
    ['Plan-Umsatz', "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000", "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000", "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000"],
    ['Plan-EBIT', "=B8-SUM('2_Team_Inputs'!B5:B9)-'2_Team_Inputs'!B12-'2_Team_Inputs'!B14", "=C8-SUM('2_Team_Inputs'!B5:B9)-'2_Team_Inputs'!B12-'2_Team_Inputs'!B14", "=D8-SUM('2_Team_Inputs'!B5:B9)-'2_Team_Inputs'!B12-'2_Team_Inputs'!B14"],
    ['Plan-Zinsaufwand', "=((B3+'1_Ist_Daten'!B7)*'1_Ist_Daten'!B11)+((B4+'1_Ist_Daten'!B8-'2_Team_Inputs'!B11)*'1_Ist_Daten'!B10)", "=((C3+'1_Ist_Daten'!B7)*'1_Ist_Daten'!B11)+((C4+'1_Ist_Daten'!B8-'2_Team_Inputs'!B11)*'1_Ist_Daten'!B10)", "=((D3+'1_Ist_Daten'!B7)*'1_Ist_Daten'!B11)+((D4+'1_Ist_Daten'!B8-'2_Team_Inputs'!B11)*'1_Ist_Daten'!B10)"],
    ['Plan-EBT (Ergebnis vor Steuern)', "=B9-B10", "=C9-C10", "=D9-D10"],
    ['Bemessungsgrundlage Steuer', "=MAX(0, B11-'1_Ist_Daten'!B5)", "=MAX(0, C11-'1_Ist_Daten'!B5)", "=MAX(0, D11-'1_Ist_Daten'!B5)"],
    ['Plan-Steuern', "=B12*'1_Ist_Daten'!B9", "=C12*'1_Ist_Daten'!B9", "=D12*'1_Ist_Daten'!B9"],
    ['Plan-Jahresüberschuss', "=B11-B13", "=C11-C13", "=D11-D13"],
    ['--- 3: TOPSIM ZIELEINGABEN ---', '', '', ''],
    ['Plan-Eigenkapital', "='1_Ist_Daten'!B3+B14-B5", "='1_Ist_Daten'!B3+C14-C5", "='1_Ist_Daten'!B3+D14-D5"],
    ['Plan-EKR (%)', "=(B14/B16)*100", "=(C14/C16)*100", "=(D14/D16)*100"],
    ['Plan-Operativer Cashflow (MEUR)', "=B14+'2_Team_Inputs'!B12+'2_Team_Inputs'!B14+'2_Team_Inputs'!B15", "=C14+'2_Team_Inputs'!B12+'2_Team_Inputs'!B14+'2_Team_Inputs'!B15", "=D14+'2_Team_Inputs'!B12+'2_Team_Inputs'!B14+'2_Team_Inputs'!B15"],
    ['--- 4: TOPSIM FATAL CHECK ---', '', '', ''],
    ['Kassenbestand ENDE (Alarm < 0)', "='1_Ist_Daten'!B2+B18+B3+B4-B5-'2_Team_Inputs'!B13-'1_Ist_Daten'!B7-'2_Team_Inputs'!B11-B6", "='1_Ist_Daten'!B2+C18+C3+C4-C5-'2_Team_Inputs'!B13-'1_Ist_Daten'!B7-'2_Team_Inputs'!B11-C6", "='1_Ist_Daten'!B2+D18+D3+D4-D5-'2_Team_Inputs'!B13-'1_Ist_Daten'!B7-'2_Team_Inputs'!B11-D6"],
]

for idx, row in enumerate(data3, 1):
    ws3.append(row)
    if '---' in str(row[0]):
        ws3.cell(row=idx, column=1).font = Font(bold=True)

# Styling und Ampel
from openpyxl.formatting.rule import CellIsRule

for ws in [ws1, ws2, ws3]:
    for col in range(1, 4):
        try:
            ws.cell(row=1, column=col).font = Font(bold=True)
            ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = 25
        except:
            pass
    ws.column_dimensions['A'].width = 45

# Rote Ampel wenn Kasse unter 0 fällt (Zeile 20)
red_fill = PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')
white_font = Font(color='FFFFFF', bold=True)
ws3.conditional_formatting.add('B20:D20', CellIsRule(operator='lessThan', formula=['0'], stopIfTrue=True, fill=red_fill, font=white_font))

# Backup & Speichern
file_path = os.path.join(os.getcwd(), 'TOPSIM_CFO_Dashboard.xlsx')
if os.path.exists(file_path):
    backup_path = os.path.join(os.getcwd(), f"TOPSIM_CFO_Dashboard_Backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
    shutil.copy(file_path, backup_path)
    print(f"Alte Version gesichert unter: {backup_path}")

wb.save(file_path)
print(f"Neues professionelles Excel-Dashboard erstellt: {file_path}")
