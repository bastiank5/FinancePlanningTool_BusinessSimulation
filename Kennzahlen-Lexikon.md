# Kennzahlen-Lexikon – TOPSIM Finance

> Dieses Lexikon erklärt alle Finanzkennzahlen, die vom Finance Tool berechnet werden.
> Jede Kennzahl enthält: Definition, Formel, TOPSIM-Relevanz und Bewertung.

---

## 1. Kassenbestand / Liquide Mittel

**Was ist das?** Der Betrag an Bargeld (bzw. Bankguthaben), der dem Unternehmen am Ende der Periode tatsächlich zur Verfügung steht.

**Formel:**
```
Kassenendbestand = Kassenanfangsbestand + Summe Einzahlungen - Summe Auszahlungen
```

**Warum wichtig in TOPSIM?** Wenn der Kassenbestand auf 0 fällt, greift automatisch der **Überziehungskredit** – mit deutlich höheren Strafzinsen (bis zu 15%). Das vernichtet Gewinn und Rating.

**Bewertung:**
- 🟢 > 5 MEUR: Komfortable Liquidität
- 🟡 1–5 MEUR: Knapp, aber funktional
- 🔴 < 0 MEUR: Überziehungskredit aktiv → Strafzinsen!

---

## 2. Eigenkapital (EK)

**Was ist das?** Das den Eigentümern gehörende Kapital – also Bilanzsumme minus Schulden. Setzt sich zusammen aus gezeichnetem Kapital, Rücklagen und kumulierten Gewinnen.

**Formel:**
```
Eigenkapital = Gezeichnetes Kapital + Kapitalrücklage + Gewinnrücklage
             + Gewinn-/Verlustvortrag + Periodenüberschuss
```

**Warum wichtig in TOPSIM?** Das Eigenkapital ist der Nenner der EKR und beeinflusst den Aktienkurs und das Rating. Dividenden verringern das EK.

**Bewertung:**
- 🟢 Steigendes EK: Unternehmen baut Substanz auf
- 🔴 Sinkendes EK: Verluste oder zu hohe Dividenden zehren Substanz auf

---

## 3. Eigenkapitalrendite (EKR)

**Was ist das?** Misst die Verzinsung des eingesetzten Eigenkapitals – also wie viel Prozent Rendite die Eigentümer auf ihr investiertes Kapital erhalten.

**Formel:**
```
EKR = (Periodenüberschuss / Eigenkapital) × 100
```

**Warum wichtig in TOPSIM?** Die EKR ist eine der **drei Plangrößen**, die du in TOPSIM eingeben musst. Sie beeinflusst die Planungsqualität (Abweichung Plan vs. Ist kostet Punkte).

**Bewertung (TOPSIM-Benchmark):**
- 🟢 12–20%: Sehr guter Bereich
- 🟡 8–12%: Akzeptabel
- 🔴 < 8%: Unterdurchschnittlich
- ⚠️ > 25%: Kann auf zu niedriges EK hindeuten (Risiko)

---

## 4. Operativer Cashflow

**Was ist das?** Der Geldfluss, der allein aus dem operativen Geschäft (Produktion & Verkauf) stammt – ohne Investitionen und Finanzierung. Zeigt, ob das Kerngeschäft Geld generiert.

**Formel:**
```
Operativer Cashflow = Periodenüberschuss
                    + Abschreibungen (zahlungsunwirksam)
                    + Erhöhung Pensionsrückstellungen (zahlungsunwirksam)
                    +/- Veränderung Working Capital
                        (Vorräte, Forderungen)
```

**Warum wichtig in TOPSIM?** Der Operative Cashflow ist die zweite **Plangröße** in TOPSIM. Er zeigt, ob das Geschäftsmodell „echtes Geld" generiert. Abweichungen vom Planwert beeinflussen die Planungsqualität.

**Bewertung:**
- 🟢 Positiv und steigend: Gesundes Geschäft
- 🔴 Negativ: Operatives Geschäft verbrennt Geld

---

## 5. Free Cashflow

**Was ist das?** Der Cashflow, der nach Abzug aller Investitionen übrig bleibt. Zeigt, wie viel Geld für Schuldentilgung, Dividenden oder Wertpapierkäufe verfügbar ist.

**Formel:**
```
Free Cashflow = Operativer Cashflow + Cashflow aus Investitionstätigkeiten
```
*(Investitions-CF ist typischerweise negativ)*

**Warum wichtig in TOPSIM?** Wenn der Free Cashflow negativ ist, braucht das Unternehmen zwingend externe Finanzierung (Kredite). Positiver Free CF = finanzielle Unabhängigkeit.

**Bewertung:**
- 🟢 Positiv: Spielraum für Dividende, Tilgung, Wertpapiere
- 🔴 Negativ: Kreditbedarf

---

## 6. Verschuldungsgrad

**Was ist das?** Setzt das gesamte Fremdkapital ins Verhältnis zum Eigenkapital. Zeigt, wie stark das Unternehmen "gehebelt" ist.

**Formel:**
```
Fremdkapital = Pensionsrückstellungen + Verbindlichkeiten gesamt
Verschuldungsgrad = (Fremdkapital / Eigenkapital) × 100
```

**Warum wichtig in TOPSIM?** Ein hoher Verschuldungsgrad verschlechtert das Kreditrating. Schlechtes Rating → höhere Zinsen → weniger Gewinn → noch schlechteres Rating (Teufelskreis).

**Bewertung:**
- 🟢 < 100%: Solide finanziert
- 🟡 100–200%: Noch tragbar
- 🔴 > 200%: Hochverschuldet, Rating-Gefahr

---

## 7. Fremdkapitalquote

**Was ist das?** Anteil des Fremdkapitals an der Bilanzsumme. Gegenstück zur Eigenkapitalquote.

**Formel:**
```
Fremdkapitalquote = (Fremdkapital / Bilanzsumme) × 100
```

**Warum wichtig in TOPSIM?** Wird direkt im Executive Summary angezeigt und beeinflusst das Kreditrating.

**Bewertung:**
- 🟢 < 50%: Eigenkapitaldominiert
- 🟡 50–70%: Ausgeglichen
- 🔴 > 70%: Fremdkapitallastig

---

## 8. Verbindlichkeiten (kurzfristig / langfristig)

**Was ist das?**
- **Kurzfristig** (Restlaufzeit unter 1 Periode): Kredite, die am Ende der Periode fällig werden und vollständig zurückgezahlt werden müssen.
- **Langfristig** (Restlaufzeit über 10 Perioden): Kredite, die über viele Perioden laufen.

**Warum wichtig in TOPSIM?** Kurzfristige Kredite müssen jede Periode erneuert werden → der volle Betrag fließt als Auszahlung ab und belastet die Liquidität. Langfristige Kredite werden nicht getilgt und belasten nur über Zinsen.

**Bewertung:**
- 🟢 Fristenkongruenz: Langfristige Investitionen mit langfristigen Krediten finanzieren
- 🔴 Fristenmismatch: Langfristige Anlagen mit kurzfristigen Krediten → jede Periode Refinanzierungsrisiko

---

## 9. Überziehungskredit

**Was ist das?** Ein automatisch gewährter Notkredit, wenn der Kassenbestand unter 0 fällt. Hat deutlich höhere Zinsen als reguläre Kredite.

**Warum wichtig in TOPSIM?** Der Überziehungskredit ist ein **Warnsignal**. Er zeigt, dass die Liquiditätsplanung versagt hat. Die Strafzinsen fressen den Gewinn.

**Bewertung:**
- 🟢 0,0 MEUR: Kein Überziehungskredit (Soll-Zustand)
- 🔴 > 0 MEUR: Liquiditätsplanung gescheitert

---

## 10. Kreditrating

**Was ist das?** Eine Bonitätsbewertung (z.B. AAA, AA, A, BBB, BB, B, CCC), die widerspiegelt, wie kreditwürdig das Unternehmen ist.

**Warum wichtig in TOPSIM?** Das Rating bestimmt den **Zinszuschlag- oder -abschlag** der nächsten Periode. Besseres Rating = günstigere Kredite.

**Bewertung:**
- 🟢 A oder besser: Zinsvorteil
- 🟡 BBB: Neutral (Standard-Startwert)
- 🔴 BB oder schlechter: Zinsnachteil

---

## 11. Aktienkurs

**Was ist das?** Der simulierte Börsenwert einer Aktie. Berechnet sich aus Eigenkapital, Periodenüberschuss und anderen Faktoren.

**Warum wichtig in TOPSIM?** Neben der EKR die wichtigste Kennzahl für die Gesamtbewertung des Unternehmens im Planspiel.

**Bewertung:**
- 🟢 Steigend: Gutes Management
- 🔴 Fallend: Probleme in Rendite, Wachstum oder Finanzstruktur

---

## 12. Unternehmenswert

**Was ist das?** Der Gesamtwert des Unternehmens, berechnet als Aktienkurs × Anzahl Aktien / 2 (vereinfacht in TOPSIM).

**Warum wichtig in TOPSIM?** Fließt in die Gesamtbewertung am Spielende ein.

---

## 13. Dividendenbasis / Gewinnvortrag

**Was ist das?** Der kumulierte, noch nicht ausgeschüttete Gewinn. Bildet die Obergrenze für mögliche Dividendenzahlungen.

**Formel:**
```
Gewinnvortrag = Gewinnvortrag Vorperiode - Dividende + Periodenüberschuss
Dividendenbasis = MAX(0, Gewinnvortrag)
```

**Warum wichtig in TOPSIM?** Eine Dividende steigert den Aktienkurs, entzieht aber Liquidität. Keine Dividende bei negativem Gewinnvortrag möglich.

---

## 14. Planungsqualität

**Was ist das?** Ein TOPSIM-Index, der misst, wie genau deine Planwerte (EKR, Operativer Cashflow, Absatz) mit den tatsächlichen Ergebnissen übereinstimmen.

**Formel (gewichtet):**
```
50% Abweichung tatsächlicher Absatz
25% Abweichung Eigenkapitalrendite
25% Abweichung Operativer Cashflow
```

**Warum wichtig in TOPSIM?** Ein hoher Planungsqualitäts-Index zeigt gutes Management. Abweichungen vom Plan kosten Punkte – daher ist es besser, konservativ zu planen als zu optimistisch.

**Bewertung:**
- 🟢 > 95: Hervorragende Planung
- 🟡 80–95: Akzeptabel
- 🔴 < 80: Starke Planabweichungen
