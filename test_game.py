# test_zahlenratespiel.py

from game import generiere_zufallszahl, benutzereingabe, spiele_runde

def test_generiere_zufallszahl():
    """Testet, ob die generierte Zahl im gültigen Bereich liegt."""
    zahl = generiere_zufallszahl()
    assert 1 <= zahl <= 100, f"Test fehlgeschlagen: {zahl} liegt nicht im Bereich 1 bis 100."

def test_benutzereingabe():
    """Testet, ob die Benutzereingabe korrekt verarbeitet wird."""
    # Hier simulieren wir die Benutzereingabe mit einem Patch
    from unittest.mock import patch
    with patch('builtins.input', side_effect=['50']):
        eingabe = benutzereingabe()
    assert eingabe == 50, f"Test fehlgeschlagen: Erwartet 50, aber erhalten {eingabe}."

def test_spiele_runde_richtig():
    """Testet, ob das Spiel korrekt endet, wenn die richtige Zahl erraten wird."""
    zahl = 50
    # Hier simulieren wir die Benutzereingabe mit einem Patch
    from unittest.mock import patch
    with patch('builtins.input', side_effect=['50']):
        with patch('builtins.print') as mock_print:
            spiele_runde(zahl)
            mock_print.assert_any_call(f"Glückwunsch! Du hast die Zahl {zahl} in 1 Versuchen erraten.")

def test_spiele_runde_falsch():
    """Testet, ob das Spiel weiterhin fragt, wenn die Zahl falsch geraten wird."""
    zahl = 50
    # Simulieren von mehreren falschen Eingaben
    from unittest.mock import patch
    with patch('builtins.input', side_effect=['40', '60', '50']):
        with patch('builtins.print') as mock_print:
            spiele_runde(zahl)
            mock_print.assert_any_call("Zu niedrig! Versuche es erneut.")
            mock_print.assert_any_call("Zu hoch! Versuche es erneut.")
            mock_print.assert_any_call(f"Glückwunsch! Du hast die Zahl {zahl} in 3 Versuchen erraten.")

# Alle Tests ausführen
def run_tests():
    test_generiere_zufallszahl()
    test_benutzereingabe()
    test_spiele_runde_richtig()
    test_spiele_runde_falsch()
    print("Alle Tests wurden erfolgreich bestanden!")

if __name__ == '__main__':
    run_tests()
