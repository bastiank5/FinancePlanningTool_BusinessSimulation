import os
import subprocess
import sys

# Auto-install openpyxl falls nicht vorhanden
try:
    import openpyxl
except ImportError:
    print("Installiere openpyxl...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl

from openpyxl.styles import Font

wb = openpyxl.Workbook()
# Standard-Blatt entfernen
wb.remove(wb.active)

# Blatt 1: Ist-Daten
ws1 = wb.create_sheet('1_Ist_Daten')
data1 = [
    ['Feld', 'Wert', 'Einheit', 'Hinweis (Aus letzter Excel)'],
    ['Kassenbestand (Start Periode)', 28.05, 'MEUR', 'Aus Bilanz Aktiva'],
    ['Eigenkapital', 35.25, 'MEUR', 'Aus Bilanz Passiva'],
    ['Gewinnvortrag', 5.27, 'MEUR', 'Maximal mögliche Dividende'],
    ['Pensionsrückstellungen', 15.95, 'MEUR', 'Passiva'],
    ['Geplante E-Steuer (%)', 0.30, '%', 'Im Handbuch prüfen. 0.30 = 30%'],
    ['Zinssatz Langfristig (%)', 0.06, '%', 'Bsp: 6% aus Berichten'],
    ['Zinssatz Kurzfristig (%)', 0.08, '%', 'Bsp: 8% aus Berichten']
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
    ['--- INVESTITIONEN ---', '', '', ''],
    ['Abschreibungen Alt-Anlagen', 6.0, 'MEUR', 'GuV / Anlagenblatt'],
    ['Geplante Neuinvestition (Maschine)', 15.0, 'MEUR', 'Totaler Kaufpreis - Cash Out!'],
    ['Geplante Neu-Abschreibung', 1.5, 'MEUR', 'Z.B. 10% von Maschine'],
    ['Veränderung Pensionsrückstellungen', 2.0, 'MEUR', 'Positiv = Cash-plus']
]
for row in data2: ws2.append(row)

# Blatt 3: Szenarien
ws3 = wb.create_sheet('3_Szenario_Rechner')
data3 = [
    ['Feld', 'Szenario A (Defensiv)', 'Szenario B (Aggressiv)', 'Szenario C'],
    ['--- 1: EINGABEN (DEINE CFO ENTSCHEIDUNG) ---', '', '', ''],
    ['Kurzfristiger Kredit (MEUR)', 10.0, 15.0, 5.0],
    ['Langfristiger Kredit (MEUR)', 15.0, 20.0, 10.0],
    ['Dividende (MEUR)', 1.0, 0.0, 2.0],
    ['Geplanter Wertpapierkauf', 0.0, 0.0, 0.0],
    ['--- 2: BERECHNUNG EBIT & GEWINN ---', '', '', ''],
    ['Plan-Umsatz', "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000", "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000", "='2_Team_Inputs'!B2*'2_Team_Inputs'!B3/1000000"],
    ['Plan-EBIT', "=B8-'2_Team_Inputs'!B5-'2_Team_Inputs'!B6-'2_Team_Inputs'!B7-'2_Team_Inputs'!B9-'2_Team_Inputs'!B11", "=C8-'2_Team_Inputs'!B5-'2_Team_Inputs'!B6-'2_Team_Inputs'!B7-'2_Team_Inputs'!B9-'2_Team_Inputs'!B11", "=D8-'2_Team_Inputs'!B5-'2_Team_Inputs'!B6-'2_Team_Inputs'!B7-'2_Team_Inputs'!B9-'2_Team_Inputs'!B11"],
    ['Plan-Zinsaufwand', "=(B3*'1_Ist_Daten'!B8)+(B4*'1_Ist_Daten'!B7)", "=(C3*'1_Ist_Daten'!B8)+(C4*'1_Ist_Daten'!B7)", "=(D3*'1_Ist_Daten'!B8)+(D4*'1_Ist_Daten'!B7)"],
    ['Plan-EBT (Ergebnis vor Steuern)', "=B9-B10", "=C9-C10", "=D9-D10"],
    ['Plan-Steuern', "=IF(B11>0, B11*'1_Ist_Daten'!B6, 0)", "=IF(C11>0, C11*'1_Ist_Daten'!B6, 0)", "=IF(D11>0, D11*'1_Ist_Daten'!B6, 0)"],
    ['Plan-Jahresüberschuss', "=B11-B12", "=C11-C12", "=D11-D12"],
    ['--- 3: TOPSIM ZIELEINGABEN ---', '', '', ''],
    ['Plan-Eigenkapital', "='1_Ist_Daten'!B3+B13-B5", "='1_Ist_Daten'!B3+C13-C5", "='1_Ist_Daten'!B3+D13-D5"],
    ['Plan-EKR (%)', "=(B13/B15)*100", "=(C13/C15)*100", "=(D13/D15)*100"],
    ['Plan-Operativer Cashflow (MEUR)', "=B13+'2_Team_Inputs'!B9+'2_Team_Inputs'!B11+'2_Team_Inputs'!B12", "=C13+'2_Team_Inputs'!B9+'2_Team_Inputs'!B11+'2_Team_Inputs'!B12", "=D13+'2_Team_Inputs'!B9+'2_Team_Inputs'!B11+'2_Team_Inputs'!B12"],
    ['--- 4: TOPSIM FATAL CHECK ---', '', '', ''],
    ['Kassenbestand ENDE (Darf NIEMALS < 0 sein!)', "='1_Ist_Daten'!B2+B17+B3+B4-B5-'2_Team_Inputs'!B10-B6", "='1_Ist_Daten'!B2+C17+C3+C4-C5-'2_Team_Inputs'!B10-C6", "='1_Ist_Daten'!B2+D17+D3+D4-D5-'2_Team_Inputs'!B10-D6"],
]

for idx, row in enumerate(data3, 1):
    ws3.append(row)
    if '---' in str(row[0]):
        ws3.cell(row=idx, column=1).font = Font(bold=True)

# Styling
for ws in [ws1, ws2, ws3]:
    for col in range(1, 4):
        try:
            ws.cell(row=1, column=col).font = Font(bold=True)
            ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = 25
        except:
            pass
    ws.column_dimensions['A'].width = 45

# Datei speichern
file_path = os.path.join(os.getcwd(), 'TOPSIM_CFO_Dashboard.xlsx')
wb.save(file_path)
print(f"Excel-Dashboard erfolgreich auf einfache V1 zurückgesetzt: {file_path}")
