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

output = sales_volume_per_agent(df1)
print(output)

#Test
def test_sales_volume_per_agent():
    # Arrange
    df_input = pl.DataFrame([
        ['dk-34922423', 'pja', 55_960_00],
        ['dk-34927049', 'pja', 35_905_31],
        ['dk-34929950', 'ssk', 1_000_000_00],
        ['dk-34929950', 'pja', 72_048_67]
    ], schema=["order_id", "agent_id", "sales_volume"])

    expected = pl.DataFrame([
        ('pja', 55_960_00 + 35_905_31 + 72_048_67),
        ('ssk', 1_000_000_00)
    ], schema=["agent_id", "total_sales_volume"]).sort("agent_id")

    # Act
    result = sales_volume_per_agent(df_input).sort("agent_id")

    # Assert
    assert result.frame_equal(expected)

