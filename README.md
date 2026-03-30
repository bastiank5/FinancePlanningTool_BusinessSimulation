# TOPSIM Finance Tool – Strategie-Tutor & Auto-Dashboard

Willkommen bei deinem **Virtuellen CFO-Büro**. 
Dieses Setup trennt strikt zwischen **Kalkulation** (passiert im zu 100% sicheren Excel-Dashboard) und **Strategischer Beratung & Lehre** (passiert durch die KI-Agenten anhand eurer Handbücher).

---

## 📂 Die Architektur

```text
Finance Tool/
├── GEMINI.md                                ← Die übergeordneten Regeln (Entscheidungsverbot!)
├── TOPSIM_CFO_Dashboard.xlsx                ← Hier rechnest du Szenarien in Sekundenschnelle
├── scripts/
│   └── auto_import.py                       ← Skript zum Auto-Transfer aus .xls in die Excel
├── .gemini/
│   └── agents/
│       ├── data-importer.md                 ← Der Agent, der das Skript startet
│       ├── finance-advisor.md               ← Der Tutor (Handbuch-Leser, Erklärer)
│       └── strategy-challenger.md             ← Der Risikoscanner (Advocatus Diaboli)
└── Sources/
    ├── Kennzahlen-Lexikon.md                ← 📚 Definitionen & Soll/Ist Marker
    ├── Planspiel Handbuch und Expertengruppen/ ← PDFs mit den offiziellen Regeln
    └── Periode X/                           ← zz.B. Periode 1, Periode 2 (Ablageort der .xls)
```

---

## 🚀 Der High-Speed Workflow für jede Runde

1. **Die neue Datei ablegen:** Die Runde ist zu Ende, du bekommst die `reports-X.xls`. Lege sie einfach in den Ordner `Sources/Periode X/`.
2. **Den Importer rufen:** Tippe hier in das Chatfenster:
   > *"Sende den `@data-importer` los, um die neue Periode in mein Dashboard zu laden."*
   Das Tool extrahiert die Basisdaten und fügt im `TOPSIM_CFO_Dashboard.xlsx` auf *Blatt 1* eine neue "Periode X" Spalte ein.
3. **Im Dashboard spielen:** Du öffnest dein `TOPSIM_CFO_Dashboard.xlsx`, fragst deine Teamkollegen, was sie ausgeben wollen (trägst das in *Blatt 2* ein) und probierst dann in *Blatt 3* verschiedene Kreditszenarien durch (Echtzeit-Berechnung).
4. **Beratung beim Mentor abholen:** Du bist dir unschlüssig? Sprich mit der KI:
   > *"Mentor, mein Excel spuckt für Kredit-Option A einen Cashflow von 4 aus, aber bei Option B eine höhere Rendite mit 2 Mio Cashflow. Bevor ich mich entscheide: Was sagt das Handbuch zu den Gefahren eines so geringen Cashflows?"*

Viel Spaß bei deiner CEO/CFO-Ausbildung!
