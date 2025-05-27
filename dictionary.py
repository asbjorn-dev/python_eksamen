import polars as pl

#gruppering, SR, Dictionary, Polars

# Eksempeldata
df1 = pl.DataFrame([
    ['dk-34922423', 'pja', 55_960_00],
    ['dk-34927049', 'pja', 35_905_31],
    ['dk-34929950', 'ssk', 1_000_000_00],
    ['dk-34929950', 'pja', 72_048_67]
], schema=["order_id", "agent_id", "sales_volume"])

def sales_volume_per_agent(df: pl.DataFrame) -> pl.DataFrame:
    # Gruppér efter agent_id og summer sales_volume
    result = df.group_by("agent_id").agg(
        pl.col("sales_volume").sum().alias("total_sales_volume")
    )
    return result

# Test funktionen
output = sales_volume_per_agent(df1)
print(output)

