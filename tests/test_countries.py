from src.countries.core import get_countries, get_country_code, transform


def test_get_country_code():

    test_countries = [
        {
            "name": "Test Country",
            "alpha3Code": "TC"
        }
    ]

    actual = get_country_code(test_countries, "Test Country")
    expected = "TC"

    assert expected == actual
    print("test_get_country_code: PASSED")


test_get_country_code()


def test_get_country_code_none():

    test_countries = [
        {
            "name": "Test Country",
            "alpha3Code": "TC"
        }
    ]

    actual = get_country_code(test_countries, "Unknown")
    expected = None

    assert expected == actual
    print("test_get_country_code_none: PASSED")


test_get_country_code_none()


def test_transform():

    def mock_get_countries():
        return [
            {
                "name": "Test Country",
                "alpha3Code": "TC",
                "currencies": [
                    {"code": "TCP"}
                ]
            }
        ]

    actual = transform("Test Country", mock_get_countries)

    expected = {"name": "Test Country",
                "country_code": "TC", "currency_code": "TCP"}

    assert expected == actual
    print("test_transform: PASSED")

test_transform()