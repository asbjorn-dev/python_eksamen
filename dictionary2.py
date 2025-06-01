#dictionary løsning

data = [
    ['dk-34922423', 'pja', 55_960_00],
    ['dk-34927049', 'pja', 35_905_31],
    ['dk-34929950', 'ssk', 1_000_000_00],
    ['dk-34929950', 'pja', 72_048_67]
]

def sales_volume_dictionary(d):
    dictionary = {}
    for row in d:
        agent = row[1]
        sales = row[2]

        if agent in dictionary:
            dictionary[agent]['total_sales'] += sales
            dictionary[agent]['num_sales'] += 1
        else:
            dictionary[agent] = {'total_sales': sales, 'num_sales': 1}

    return dictionary

output = sales_volume_dictionary(data)
print(output)