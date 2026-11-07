import pandas

def datei_umwandeln(einkaufsliste):
    dateiart = input("In welche Dateiart willst du die Liste exportieren? (json/csv)")

    if not dateiart == "csv" or not dateiart == "json":
        print("Wähle Dateiart .json oder .csv")

    if dateiart == "csv":
        pandas.DataFrame(einkaufsliste).to_csv("einkaufsliste.csv", index=False)

    elif dateiart == "json":
        pandas.DataFrame(einkaufsliste).to_json("einkaufsliste.json", index=False)