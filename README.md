# 🎓 TOPSIM Finance – Strategie-Tutor & Dashboard

Entscheidungen im Blindflug treffen war gestern. Dieses Hybrid-Projekt stattet dich mit einem fehlerfreien **Echtzeit-Berechnungstool in Excel** aus und kombiniert es mit zwei **virtuellen Fach-Agenten** via Gemini CLI.

Dieses Tool übernimmt keine Rechenaufgaben für dich, es liefert dir echtes Strategie-Feedback und TOPSIM-Verständnis!

---

## 🚀 Die Zwei-Agenten-Architektur

1. **Die Berechnungen:** Du nutzt das `TOPSIM_CFO_Dashboard.xlsx` in deinem Hauptordner. Keine Wartezeit. Ändere Kreditsumme oder Werbebudgets und lies sofort die exakte Eigenkapitalrendite und den Cashflow ab.
2. **Die Beratung:** Du nutzt die Gemini CLI, um mit den zwei spezialisierten KI-Beratern zu sprechen:

- **`@theorie-tutor`**: Dein "Handbuch auf Abruf". Verstehst du nicht, wie der Überziehungskredit reinhaut? Ließ im `Kennzahlen-Lexikon.md` oder frag den Tutor, er erklärt es dir anhand der offiziellen Unterlagen.
- **`@entscheidungs-pruefer`**: Dein gnadenloser Risiko-Prüfer. Bevor du deine Werte am Ende in das TOPSIM-Interface einträgst, fütterst du diesen Agenten mit deinem Setup und er deckt blinde Flecken auf.

---

## 🛠️ Der Workflow Runde für Runde

### Schritt 1: Daten-Import & Team-Abstimmung
- Lad die Excel (`reports-X.xls`) der Vorperiode herunter und speichere sie z.B. in `Sources/Periode X/`.
- Lad die neuen Marktnachrichten in `Sources/News/`.
- Aktualisiere in `TOPSIM_CFO_Dashboard.xlsx` Blatt 1 (`1_Ist_Daten`) die Kasse, Eigenkapital & Co.
- Trage die Budgetpläne deines Vertriebs- und Produktionsteams in Blatt 2 (`2_Team_Inputs`) ein.

### Schritt 2: Strategie entwickeln & Fragen klären
- Du simulierst im Excel-Reiter `3_Szenario_Rechner` deine Kredithöhen und möglichen Dividenden.
- *Unklarheiten?* Ruf den `@theorie-tutor` in Gemini auf: *"Welche Auswirkungen hat es genau, wenn wir in die Gewinnrücklage statt in die Kapitalrücklage investieren?"*

### Schritt 3: Der Härtetest
Sobald du ein Szenario ausgewählt hast, das für dich im Excel am besten aussieht, holst du dir das Feedback vom `@entscheidungs-pruefer` ab.

**Optimaler Eingabe-Prompt für den Prüfer:**
```text
@entscheidungs-pruefer Das sind meine Entscheidungen für Periode X. Bitte prüfe auf Risiken:
Kurzfristiger Kredit: 15 MEUR
Langfristiger Kredit: 5 MEUR
Dividende: 0 MEUR
Plan-EKR: 14%
Plan-Operativer Cashflow: 22 MEUR
Plan-Absatz: 45.000 Stück
Wir haben massiv ins Marketing investiert, weil die Konjunktur laut News stark steigen soll.
```

### Schritt 4: Finale Eingabe
Nachdem der Agent dir womöglich den Kopf gewaschen hat ("Die Liquidität ist zu eng, du läufst bei -5% Absatz direkt in den Notkredit!"), besserst du im Excel nochmal nach oder bestätigst den Plan. Danach trägst du die Werte in TOPSIM ein.
