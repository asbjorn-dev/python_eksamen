#dictionary løsning

data = [
    ['dk-34922423', 'pja', 55_960_00],
    ['dk-34927049', 'pja', 35_905_31],
    ['dk-34929950', 'ssk', 1_000_000_00],
    ['dk-34929950', 'pja', 72_048_67]
]

def sales_volume_per_agent_dict(data):
    dictionary = {}

    for row in data:
        agent = row[1]
        sale = row[2]

        if agent in dictionary:
            total_sale, count = dictionary[agent]
            dictionary[agent] = (total_sale + sale, count + 1)
        else:
            dictionary[agent] = (sale, 1)

    return dictionary

output = sales_volume_per_agent_dict(data)
print(output)