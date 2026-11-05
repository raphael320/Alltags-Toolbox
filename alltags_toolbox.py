def main_menu():
    while True:

        print("=== Alltags-Toolbox ===")
        print("1 - Einkaufsliste")
        print("2 - Einheiten umrechnen")
        print("3 - Beenden")

        gewaehltes_tool = input("Wähle ein Tool.")

        if gewaehltes_tool == "1":
            einkaufsliste_menu()

        #if gewaehltes_tool == "2"

        elif gewaehltes_tool == "3":
            print("Programm beendet.")
            break
        
def einkaufsliste_menu():
    einkaufsliste = []

    while True:
        print("--- Einkaufsliste ---")
        print("1 - Artikel hinzufügen")
        print("2 - Liste anzeigen")
        print("3 - Artikel löschen")
        print("4 - Liste leeren")
        print("5 - Zurück")

        gewaehltes_tool = input("Was möchtest du tun?")

        if gewaehltes_tool == "1":

            hinzuzufügender_artikel = input("Welchen Artikel möchtest du hinzufügen?")

            einkaufsliste.append(hinzuzufügender_artikel)

            if hinzuzufügender_artikel == "":
                print("Bitte füge einen Namen ein.")

            elif hinzuzufügender_artikel in einkaufsliste:
                print(f"{hinzuzufügender_artikel} steht bereits auf der Einkaufsliste.")
                einkaufsliste.remove(hinzuzufügender_artikel)

        elif gewaehltes_tool == "2":
            print(einkaufsliste)

        elif gewaehltes_tool == "3":

            zu_löschender_artikel = input("Welchen Artikel möchtest du löschen?")
            einkaufsliste.remove = zu_löschender_artikel
            
        elif gewaehltes_tool == "4":
            einkaufsliste.clear

        elif gewaehltes_tool == "5":
            main_menu()

#Hauptprogramm
main_menu()