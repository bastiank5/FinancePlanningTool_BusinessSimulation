# 🎓 TOPSIM Finance – Strategie-Tutor & Dashboard

Entscheidungen im Blindflug treffen war gestern. Dieses Hybrid-Projekt stattet dich mit einem fehlerfreien **Echtzeit-Berechnungstool in Excel** aus und kombiniert es mit einem **virtuellen Strategie-Tutor (CFO Mentor)** via Gemini CLI.

Dieses Tool übernimmt keine Rechenaufgaben für dich, es liefert dir echtes Strategie-Feedback und TOPSIM-Verständnis!

---

## 🚀 Wie das System arbeitet (Hybrid-Ansatz)

1. **Die Berechnungen:** Du nutzt das eigens generierte `TOPSIM_CFO_Dashboard.xlsx` in deinem Hauptordner. Keine Skripte, keine Wartezeit. Ändere Kreditsumme oder Werbebudgets und lies sofort die exakte Eigenkapitalrendite und den Cashflow für TOPSIM ab.
2. **Die Beratung:** Du gibst die Ergebnisse deines Excel-Tools oder allgemeine Theorie-Fragen in die Gemini CLI ein. Das intelligente Multi-Agenten System spielt Strategieberater.

### Die Agenten
- `@finance-advisor`: Ein Tutor, der dir erklärt, was eine geringe EKR in TOPSIM verursacht, oder dir Feedback zu deiner Kreditauswahl im Spreadsheet gibt.
- `@strategy-challenger`: Ein gnadenloser Kritiker, der dich davor schützt, mit 0 Liquiditätspuffer den Straf-Überziehungskredit von TOPSIM zu triggern.

---

## 🛠️ Der Workflow Runde für Runde

### 1) Daten aus TOPSIM importieren
- Wenn die Periode um ist, lad die Excel (`reports-X.xls`) herunter.
- Öffne das `TOPSIM_CFO_Dashboard.xlsx` auf Blatt 1 (`1_Ist_Daten`) und aktualisiere rasch Kasse & Eigenkapital der Vorperiode.

### 2) Kommilitonen ausfragen
- Frage das Vertriebsteam und die Produktionsteram nach ihren Budgetplänen.
- Trage deren Budgets (Fabriken, Werbung, Absatz) in Blatt 2 (`2_Team_Inputs`) ein.

### 3) Echtzeit-Simulieren
- Spiele im Reiter `3_Szenario_Rechner` verschiedene Kredithöhen und Dividenden durch.
- Finde die bestmögliche Balance aus EKR und freier Cash-Liquidität.

### 4) Das KI-Mentor-Feedback einholen
Bevor du die final berechneten Werte der Excel in das echte TOPSIM-Portal eingibst, hole dir Feedback bei deinem virtuellen Mentor:

> **"Mein Team hat riesige Budgets angemeldet. Mein Excel sagt mir: Wenn ich Szenario A (15 Mio Baukredit) mache, sinkt meine Kasse auf 0,5 MEUR, EKR ist aber 18%. Was sagst du als CFO-Mentor dazu?"**

---

## 📚 Was gibt es noch?
Schau dir `Sources/Kennzahlen-Lexikon.md` an. Dort hast du als CFO jederzeit die wichtigsten Definitionen für TOPSIM sofort griffbereit!
