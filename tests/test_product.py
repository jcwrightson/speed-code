from src.product.core import update_product


def test_update_product_unchanged():

    # Given products
    # User enters None
    # Product remains unchanged

    test_products = [{"name": "Test Product", "price": 1}]

    def mock_view_products(products):
        pass

    def mock_input(msg):
        if msg == "Select: ":
            return 0
        else:
            return None

    def mock_save(data):
        pass

    actual = update_product(test_products, mock_view_products, mock_save, mock_input)
    expected = [{"name": "Test Product", "price": 1}]
    assert actual == expected
    print("test_update_product_unchanged: PASSED")


test_update_product_unchanged()


def test_update_product():

    test_products = [{"name": "Test Product", "price": 1}]
    expected = [{"name": "New Product", "price": 2.5}]

    def mock_view_products(products):
        pass

    def mock_input(msg):
        if msg == "Select: ":
            return 0
        elif msg == "name: ":
            return "New Product"
        else:
            return 2.5

    def mock_save(data):
        pass

    actual = update_product(test_products, mock_view_products, mock_save, mock_input)

    assert actual == expected
    print("test_update_product: PASSED")


test_update_product()