def test_check_empty_massage(cart):
    cart.open_page()
    cart.check_empty_message("Your cart is empty!")

def test_clear_cart(cart):
    cart.open_main_page()
    cart.put_into_basket()
    cart.continue_purchase()
    cart.open_cart()
    cart.clear("Your cart is empty!")

def test_check_invalid_promo(cart):
    cart.open_main_page()
    cart.put_into_basket()
    cart.continue_purchase()
    cart.open_cart()
    cart.discount_code('sdgdfghdfshdfhdf', "This promo code is not available.")
