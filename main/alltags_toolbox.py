import sys
import datetime
import pandas
from models import als_csv_json_exportieren as cje

#Zeit Anzeige initialisieren
zeit_anzeige = datetime.datetime.now()

def main_menu():
    while True:
        print(zeit_anzeige.strftime("%A"), zeit_anzeige.strftime("%x"), zeit_anzeige.strftime("%X"))
        print("=== ALLTAGS-TOOLBOX ===")
        print("1 - Einkaufsliste")
        print("2 - Temperatur Einheit umrechnen")
        print("3 - Beenden")

        gewaehltes_tool = input("Wähle ein Tool.")

        if gewaehltes_tool == "1":
            einkaufsliste_menu()

        if gewaehltes_tool == "2":
            temperaturen_umrechnen()

        elif gewaehltes_tool == "3":
            print("Programm beendet.")
            sys.exit()

def einkaufsliste_menu():
    einkaufsliste = {}

    while True:
        print("=== EINKAUFSLISTE ===")
        print("1 - Artikel hinzufügen")
        print("2 - Liste anzeigen")
        print("3 - Artikel bearbeiten oder löschen")
        print("4 - Liste leeren")
        print("5 - Liste als Datei exportieren")
        print("6 - Zurück")

        gewaehltes_tool = input("Was möchtest du tun?")

        if gewaehltes_tool == "1":

            hinzuzufügender_artikel = input("Welchen Artikel möchtest du hinzufügen?")
            hinzuzufügende_anzahl = input("Wie viel möchtest du hinzufügen?")

            if hinzuzufügender_artikel == "":
                print("Bitte füge einen Namen ein.")

            elif hinzuzufügender_artikel in einkaufsliste:
                print(f"{hinzuzufügender_artikel} steht bereits auf deiner Einkaufsliste.")
                
            else:
                einkaufsliste.update({"name" : hinzuzufügender_artikel, "anzahl" : hinzuzufügende_anzahl})
                print(f"{hinzuzufügender_artikel} wurde zur Einkaufsliste hinzugefügt.")


        elif gewaehltes_tool == "2":
            i = 0
            for e in einkaufsliste:
                i += 1
                print(i, e)

            if einkaufsliste === {}:
                print("Keine Artikel auf der Einkaufsliste.")
                    

        elif gewaehltes_tool == "3":
            art_zu_bearbeiten = input("Möchtest du einen Artikel bearbeiten 'b' oder löschen 'l'?")

            if art_zu_bearbeiten == "b":
            
            elif art_zu_bearbeiten == "l":
                zu_löschender_artikel = input("Welchen Artikel möchtest du löschen?")
                einkaufsliste.pop(zu_löschender_artikel)
                print(f"{zu_löschender_artikel} wurde von der Einkaufsliste gelöscht.")
            
        elif gewaehltes_tool == "4":
            einkaufsliste.clear()

        elif gewaehltes_tool == "5":
            cje.datei_umwandeln(einkaufsliste)
            
        elif gewaehltes_tool == "6":
            return

def temperaturen_umrechnen():
    while True:
        print("--- Temperatur-Umrechner ---")
        print("1 - Celsius nach Fahrenheit")
        print("2 - Fahrenheit nach Celsius")
        print("3 - Celsius nach Kelvin")
        print("4 - Kelvin nach Clesius")

        gewaehltes_tool = input("Was möchtest du tun?")

        if gewaehltes_tool == "1":
            celsius = int(input("Geben sie eine Zahl ein."))
            
            try:
                return float(celsius)
                
            except ValueError:
                print("Bitte geben sie eine Zahl (int/float) ein.")
                break
                
            fahrenheit = (celsius * 9 / 5) +32
            print(fahrenheit)

        if gewaehltes_tool == "2":
            fahrenheit = int(input("Geben sie eine Zahl ein."))
            celsius = (fahrenheit - 32) * 5 / 9
            
            try:
                return float(celsius)
                
            except ValueError:
                print("Bitte geben sie eine Zahl (int/float) ein.")
                break
            print(celsius)

        elif gewaehltes_tool == "3":
            celsius = int(input("Geben sie eine Zahl ein."))
            
            try:
                return float(celsius)
                
            except ValueError:
                print("Bitte geben sie eine Zahl (int/float) ein.")
                break
            kelvin = celsius + 273.15
            print(kelvin)

        elif gewaehltes_tool == "4":
            kelvin = int(input("Geben sie eine Zahl ein."))
            
            try:
                return float(celsius)
                
            except ValueError:
                print("Bitte geben sie eine Zahl (int/float) ein.")
                break
            celsius = kelvin - 273.15
            print(celsius)
        
#Hauptprogramm
main_menu()
