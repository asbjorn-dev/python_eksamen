import csv

def læs_antal_fra_csv(filnavn):
    with open(filnavn, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield int(row['antal'])  # <- HER bruger vi yield

def kumuler_salg(input_fil, output_fil):
    total = sum(læs_antal_fra_csv(input_fil))  # <- Streamet kumulation

    with open(output_fil, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Total antal solgte varer'])
        writer.writerow([total])

kumuler_salg('salg.csv', 'output.csv')
