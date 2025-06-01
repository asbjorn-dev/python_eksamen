import csv
import math

# Input/Output, SR & "Streaming med yield, for, next"
def læs_salg_fra_csv(filnavn):
    with open(filnavn) as f:
        reader = csv.DictReader(f)
        for row in reader:
            antal = int(row['antal'])
            enhedspris = float(row['enhedspris'])
            beløb = math.ceil(antal * enhedspris)
            yield antal, enhedspris, beløb

for salg in læs_salg_fra_csv("salg.csv"):
    print(salg)
