# Afbildning, IP & Imperativ
def add_vat(v, p):
    if len(v) == 0:
        raise ValueError("List is empty")

    i = 0
    while i < len(v):
        v[i] = v[i] * p
        i += 1
    return v

# Filtrering, SR & Imperativ
def filter_vektor_between_2numbers(v, min_val, max_val):
    result = []
    i = 0
    while i < len(v):
        x = v[i]
        if min_val <= x <= max_val:
            result.append(x)
        i += 1
    return result



# Tests
def test_of_add_vat():
    # arrange
    input_v = [100, 200, 300]
    input_p = 1.25
    expected = [125.0, 250.0, 375.0]
    # act
    result = add_vat(input_v, input_p)
    # assert
    assert expected == result

def test_of_add_vat_null():
    try:
        add_vat([], 1.25)
        assert False
    except ValueError:
        assert True

def test_filter_vektor_between_2numbers():
    assert filter_vektor_between_2numbers([1, 4, 7, 10, 12], 3, 8) == [4, 7]

