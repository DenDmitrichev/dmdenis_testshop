def test_search_by_name(table):
    table.open_page()
    table.search_by_good_name("Customizable Desk")


def test_sort_by_name(table):
    table.open_page()
    table.sort_by_name()


def test_add_to_card(table):
    table.open_page()
    table.put_into_basket()
