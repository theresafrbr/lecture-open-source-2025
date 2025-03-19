# Zahlenratespiel Lecture Open-Source Energy System Modeling 2025

Copyright by Theresa Freibauer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is released under an MIT LICENSE.

# Zahlenratespiel

## Beschreibung
Das Zahlenratespiel ist ein einfaches Spiel, bei dem der Benutzer eine zufällig generierte Zahl zwischen 1 und 100 erraten muss. Das Spiel gibt dem Benutzer Hinweise, ob seine Eingabe zu niedrig oder zu hoch ist, und zählt, wie viele Versuche der Benutzer benötigt, um die richtige Zahl zu erraten.

generiere_zufallszahl()
Erstellt eine zufällige Zahl im Bereich von 1 bis 100.
Rückgabewert: Eine zufällige ganze Zahl zwischen 1 und 100.

benutzereingabe()
Fordert den Benutzer zur Eingabe einer Zahl auf und stellt sicher, dass diese korrekt ist.
Eingabe: Eine ganze Zahl zwischen 1 und 100.
Falls der Benutzer eine ungültige Eingabe macht (z. B. Buchstaben oder eine Zahl außerhalb des Bereichs), wird eine Fehlermeldung angezeigt und eine erneute Eingabe verlangt.
Rückgabewert: Eine gültige, vom Benutzer eingegebene Zahl zwischen 1 und 100.

spiele_runde(zahl)
Der Benutzer gibt Zahlen ein, falls die Zahl zu hoch oder zu niedrig ist, wird ein Hinweis gegeben.
Sobald die richtige Zahl erraten wurde, wird die Anzahl der Versuche ausgegeben und das Spiel beendet.
Parameter:
zahl (int): Die zufällig generierte Zielzahl, die erraten werden muss.

zahlenratespiel()
Startet das Spiel, indem es eine Zufallszahl generiert und die Raterunde startet.
Begrüßt den Benutzer, generiert eine zufällige Zahl und startet das eigentliche Spiel (spiele_runde()).