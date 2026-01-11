def test_terms(goods):
    goods.open_page()
    goods.term_and_conditions()


def test_check_price(goods):
    goods.open_page()
    goods.check_price()


def test_add_to_cart(goods):
    goods.open_page()
    goods.add_to_cart_lot_of_goods()
