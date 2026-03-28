# TOPSIM Finance Tool

Dieses CLI-basierte Multi-Agenten-System automatisiert die Rolle des Finanzvorstands (CFO) im Planspiel **TOPSIM – Mastering Business Operations**. 

Das Tool extrahiert harte Finanzkennzahlen aus den komplexen Excel-Berichten, berechnet den Status Quo (Liquidität, Verschuldung, Cashflow) und kalkuliert auf Basis der Eingaben deiner Mitspieler verschiedene Finanzierungs-Szenarien für die nächste Periode.

---

## 📂 Ordnerstruktur

Um fehlerfrei zu funktionieren, erwartet das System diese feste Struktur:

```text
Finance Tool/
├── GEMINI.md                                ← Orchestrator-Prompt (Herzstück)
├── README.md                                ← Diese Anleitung
├── .gemini/
│   └── agents/
│       ├── finance-worker.md                ← Extraktions- & Rechenlogik
│       └── risk-reviewer.md                 ← Mathematische Qualitätsprüfung
└── Sources/
    ├── Kennzahlen-Lexikon.md                ← 📚 Nachschlagewerk für alle Formeln & Werte
    ├── Planspiel Handbuch und Expertengruppen/ ← PDFs mit Regeln (z.B. Steuersätze)
    ├── Weitere Informationen/               ← Skripte, Vorlesungen
    ├── Periode 0/                           ← Historie: reports-0.xls
    ├── Periode 1/                           ← Historie: reports-1.xls
    └── Periode X/                           ← Deine AKTUELLE Arbeitsperiode
        ├── reports-X.xls                    ← Der aktuelle Excel-Bericht
        └── planung.md                       ← DEINE EINGABEMASKE für die nächste Runde
```

---

## 🛠️ Workflow: So spielst du eine neue Periode

Die Arbeit mit dem Tool folgt in jeder Runde exakt denselben 4 Schritten:

### Schritt 1: Ordner vorbereiten
Sobald eine neue Runden-Auswertung da ist:
1. Erstelle einen neuen Ordner in `Sources/` (z.B. `Periode 2`).
2. Lege den neuen Excel-Bericht (`reports-2.xls`) dort ab.
3. Kopiere die Datei `planung.md` aus der letzten Periode in den neuen Ordner.

### Schritt 2: Team-Inputs einholen (`planung.md` ausfüllen)
Öffne die `planung.md` im Ordner der aktuellen Periode. 
Frag deine Kommilitonen aus den anderen Abteilungen nach ihren Plänen und ersetze die `???`-Platzhalter:
- **Vertrieb:** Geplanter Absatz, Preis, Werbung
- **Produktion:** Kauf neuer Maschinen, Fertigungsmenge
- **Personal:** Geplante Einstellungen

### Schritt 3: Eigene Finanz-Szenarien definieren
Scrolle in der `planung.md` nach unten zu den Finanz-Szenarien. 
Trage hier 1 bis 3 Optionen ein, wie du die Pläne deines Teams finanzieren willst (z.B. Szenario A: 10 Mio kurzfristiger Kredit, Szenario B: 15 Mio). 
*Hinweis: Steuersätze und Zinsen zieht sich das Tool automatisch aus dem Handbuch/Bericht, diese musst du nicht eintragen.*

### Schritt 4: Das System starten
Öffne das Projekt in deiner Gemini CLI und starte das Tool mit diesem Prompt:

> **"Analysiere die TOPSIM-Finanzberichte der aktuellsten Periode und die dazugehörige `planung.md`. Extrahiere den Status Quo und berechne meine Kreditszenarien (Plan-EBIT, Plan-EKR, Plan-Cashflow). Liefere das fertige TOPSIM-Eingabeblatt."**

---

## 📊 Was du als Ergebnis bekommst

Das Tool durchläuft nun autonom mehrere Analyse- und Prüfschleifen. Sobald der `@risk-reviewer` sein "GO" gibt, erhältst du:
1. **Das CFO-Dashboard:** Deine aktuelle Finanzierungsstruktur, Cashflow und EKR im Vergleich zur Vorperiode (Deltas).
2. **Den Szenario-Vergleich:** Wie wirken sich die geplanten Kredite A vs. B auf deine zukünftige EKR und deinen Cashflow aus?
3. **Die Exakte Eingabemaske:** Eine Tabelle, die dir genau sagt, welche Zahl du im TOPSIM-Browser in welches Feld eintippen musst.

---

## 📚 Lernen mit dem Kennzahlen-Lexikon
Du bist dir unsicher, was ein guter Verschuldungsgrad ist oder warum der Überziehungskredit vermieden werden muss? 
Öffne die Datei `Sources/Kennzahlen-Lexikon.md`. Dort findest du zu jeder Kennzahl, die das Tool ausspuckt:
- Die genaue Formel
- Die Relevanz speziell für TOPSIM
- Einen Richtwert (🟢 Gut / 🔴 Schlecht)
