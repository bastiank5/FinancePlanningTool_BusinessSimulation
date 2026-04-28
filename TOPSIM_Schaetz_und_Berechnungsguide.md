# TOPSIM Planung: Was muss geschätzt, was kann berechnet werden?

Wenn du planst, teilt sich dein Excel-Tool in zwei Kategorien: Werte, die du **exakt ausrechnen** kannst (weil sie auf fixen Regeln basieren), und Werte, die du **schätzen** musst (weil sie von Markt oder Konkurrenz abhängen).

Hier ist deine Checkliste für die korrekte Planung der nächsten Periode:

---

## 1. Diese Werte MUSST du schätzen (Risikofaktoren)

Diese Werte hängen vom Marktwachstum, Konkurrenzverhalten oder internen weichen Faktoren (Motivation, Qualität) ab.

| Position | Wie du sie schätzt / planst | Risiko-Tipp |
| :--- | :--- | :--- |
| **Tatsächlicher Absatz** | Plan-Wert aus deiner Strategie. Hängt von deinem Preis, Werbung, Technologie und Marktwachstum (siehe News) ab. | Plane für die GuV mit deinem Ziel-Absatz. Für die **Liquidität** solltest du jedoch einen Stresstest machen (Was, wenn wir 10 % weniger absetzen?). |
| **Fluktuation (Personal)** | Mitarbeiter kündigen (in P2 waren es z.B. 53 in der Fertigung = ca. 6 %). Hängt vom Motivationsindex ab. | Plane pauschal mit **5 bis 8 % Fluktuation** des Vorjahresbestands. Diese musst du durch Neueinstellungen ausgleichen, um die Kapazität zu halten! |
| **Nacharbeit & Ausschuss** | Hängt von der Auslastung der Mitarbeiter (>100 % = mehr Fehler) und der Prozessoptimierung ab. | Setze als Erfahrungswert ca. **1,5 bis 2,0 MEUR** an. Wenn deine Auslastung der Mitarbeiter auf über 105 % steigt, verdopple diesen Wert zur Sicherheit. |

---

## 2. Diese Werte kannst du EXAKT berechnen (Regelbasierend)

### A. Umsatz und Absatz
* **Umsatzerlöse:** `Geplanter Absatz × Geplanter Preis`
* **Einzahlungen aktueller Umsatz (Cashflow):** `Umsatzerlöse × 80 %` (Die restlichen 20 % fließen in die Forderungen für die nächste Periode).
* **Forderungen Vorperiode (Cashflow):** Nimm **exakt den Wert aus der Bilanz** der Vorperiode (Forderungen aus LuL).

### B. Material & Produktion
* **Bestandsveränderung (GuV):** `(Geplante Fertigungsmenge - Geplanter Absatz) × Herstellkosten pro Stück`. (Bei Aufbau: Plus in der Gesamtleistung / Minus im Cashflow).
* **Materialverbrauch (GuV):** `Geplante Fertigungsmenge × Kosten pro Einsatzstoff`. (Preise je nach Staffel aus den aktuellen News ablesen!).
* **Materialeinkauf (Liquidität):** `Geplante Einkaufsmenge × Staffelpreis aus den News`.
* **Betriebsstoffe:** `Geplante Fertigungsmenge × ca. 46 EUR` (Der Satz pro Stück bleibt meist sehr konstant, in P1+P2 waren es ~46 €).
* **Lagerkosten:** `Lagerendbestand (Stück) × ca. 120 EUR`.

### C. Personal
* **Personalbestand:** `Bestand Vorperiode + Geplante Einstellungen - Geplante Entlassungen - Geschätzte Fluktuation`.
* **Löhne & Gehälter:** `Neuer Personalbestand × Durchschnittsgehalt` (Gehälter stagnieren oder steigen leicht laut Wirtschafts-News).
* **Personalnebenkosten:** `Löhne & Gehälter × 40 %` (oder der aktuelle Satz aus den News).
* **Einstellungskosten:** `Anzahl Einstellungen × Satz aus den News` (In P2 stieg dieser auf 14.000 EUR pro Kopf).

### D. Anlagevermögen & Investitionen
* **Abschreibungen Anlagen:** Schau in den **Fertigungsbericht** der Vorperiode! Dort steht für jede Maschine die "Restlaufzeit" und die "Abschreibung MEUR/Periode". Wenn die Restlaufzeit 0 erreicht hat, entfällt die Abschreibung in der neuen Periode.
* **Abschreibungen Umwelttechnik:** `Kumulierte Investitionen in Umweltanlagen × 10 %` (in der Regel).
* **Umweltabgabe:** Sinkt, wenn euer Umweltbelastungsindikator sinkt. (Meist zwischen 0,5 und 1,2 MEUR). Wenn ihr weiter in Prozessoptimierung und Umweltanlagen investiert, sinkt dieser Wert. Setze sicherheitshalber 0,8 MEUR an.

### E. Zinsen & Steuern
* **Zinsaufwand langfristig:** `Höhe langfristiger Kredit × Euer alter Basiszins` (Fixiert bei Aufnahme! Bei euch: 6,0 % auf die 5 MEUR).
* **Zinsaufwand kurzfristig:** `Benötigter Überziehungskredit / Kurzfristiger Kredit × Neuer Zinssatz`. (Neuer Zinssatz = Basis 8,0 % + Änderung Leitzins laut News + Euer aktueller Rating-Auf/Abschlag).
* **Steuern:** **Exakt 45 %** auf den "Gewinn vor Steuern" (EBT). *Achtung: Steuern fallen nur an, wenn der Gewinn vor Steuern positiv ist UND kein Verlustvortrag aus Vorperioden mehr besteht!*

---

## 3. Der wichtigste Zirkelschluss in deinem Tool: Zinsen vs. Liquidität

Das schwierigste bei der Planung ist der **Überziehungskredit bzw. die kurzfristige Kreditaufnahme**.
1. Du weißt erst, wie viel Kredit du brauchst, wenn du alle Auszahlungen kennst.
2. Du kennst aber deine Auszahlungen erst, wenn du weißt, wie hoch die Zinsen für den Kredit sind.

**Wie du das in Excel löst:**
Lass Excel die Zinsen basierend auf dem kurzfristigen Kredit **vor** der aktuellen Zinszahlung berechnen. Wenn am Ende der Liquiditätsplanung ein negativer Kassenbestand herauskommt, trägst du diesen Wert (mit kleinem Puffer) als "Geplante Aufnahme kurzfristiger Kredit" ein. Dann berechnet Excel die Zinsen -> der Kassenbestand sinkt noch leicht -> du passt den Kredit nochmal minimal an.

---

## 4. Die ultimative Kontroll-Checkliste vor Abgabe

Bevor du im TOPSIM-System auf "Abgeben" drückst, prüfe im Dashboard diese 4 Punkte:

1. [ ] **Ist die Fertigungskapazität ausreichend?** (Personalbestand × Produktivität UND Maschinenkapazität prüfen. Wenn beides nicht reicht -> Es werden teure Überstunden fällig oder ihr könnt nicht liefern).
2. [ ] **Sind die Herstellkosten pro Stück richtig geschätzt?** (Wichtig für die Bewertung der Bestandsveränderung).
3. [ ] **Reicht die Liquidität im Worst-Case?** (Was passiert in der Liquiditätsrechnung, wenn ihr 10 % weniger verkauft als geplant? Wenn die Kasse dann ins Minus rutscht, nehmt von vornherein etwas mehr kurzfristigen Kredit auf – Überziehungskredite sind extrem teuer!).
4. [ ] **Passen Preis & Werbung zum Technologie-Index?** (Ein veraltetes Produkt für einen Premium-Preis wird sich nicht verkaufen).
