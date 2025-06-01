import csv
import math


# Extract: Generatorfunktion der læser CSV og producerer datastrøm
def læs_salg_fra_csv(filnavn):
    with open(filnavn) as f:
        reader = csv.DictReader(f)
        for row in reader:
            antal = int(row['antal'])
            enhedspris = float(row['enhedspris'])
            beløb = math.ceil(antal * enhedspris)
            yield antal, enhedspris, beløb

# Filter: Fjern salg med beløb <= 700
def filtrer_store_salg(salg_data):
    for salg in salg_data:
        # Tildel værdierne fra tuplen (antal, enhedspris, beløb)
        antal = salg[0]
        enhedspris = salg[1]
        beløb = salg[2]
        # Hvis beløbet er større end 700, yield salget
        if beløb > 500:
            yield antal, enhedspris, beløb

# Map: Giv 10 kr rabat på hvert beløb
def giv_rabat(stream):
    for salg in stream:
        # Træk værdierne ud af tuplen
        antal = salg[0]
        enhedspris = salg[1]
        beløb = salg[2]

        # Træk 10 kr fra beløbet
        beløb_med_rabat = beløb - 10

        # Returner en ny tuple med rabat anvendt
        yield antal, enhedspris, beløb_med_rabat


# Reduce: Summer alle beløb
def beregn_total(stream):
    total = 0
    for _, _, beløb in stream: # _ i python betyder at vi ignorerer værdien
        total += beløb
    return total

# ETL pipeline: extract → transform → load
def kør_pipeline(filnavn):
    stream = læs_salg_fra_csv(filnavn)         # Extract. Producer datastrøm med antal * beløb logik
    stream = filtrer_store_salg(stream)        # Transform 1
    stream = giv_rabat(stream)                 # Transform 2

    # # uden sum
    # for salg in stream:
    #     print(salg)

    # med sum
    total = beregn_total(stream)               # Load (eller aggregering)
    return total

# Brug pipeline m. det hele
print("Totalbeløb efter rabat:", kør_pipeline("salg.csv"))
# # kør uden sum
#kør_pipeline("salg.csv")




# Tests
def test_filtrer_store_salg():
    # Eksempeldata med beløb under og over 500
    input_data = [
        (1, 100.0, 100),     # Skal filtreres væk
        (2, 400.0, 800),     # Skal med
        (3, 300.0, 700),     # Skal med
        (5, 160.0, 1200)     # Skal med
    ]

    result = list(filtrer_store_salg(input_data))

    expected = [
        (2, 400.0, 800),
        (3, 300.0, 700),
        (5, 160.0, 1200)
    ]

    assert result == expected
