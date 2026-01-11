def test_check_empty_massage(cart):
    cart.open_page()
    cart.check_empty_message()

def test_clear_cart(cart):
    cart.open_main_page()
    cart.clear()

def test_check_invalid_promo(cart):
    cart.open_main_page()
    cart.discount_code('sdgdfghdfshdfhdf')
