from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import cart_locators as cart_loc
from pages.tables import Table


class CartPage(Table):
    page_url = '/shop/cart'

    def check_empty_message(self, text):
        empty_message = self.find(cart_loc.empty_message_loc)
        assert empty_message.text == text

    def clear(self, text):

        remove_button = self.find(cart_loc.remove_button_loc)
        remove_button.click()
        empty_message = self.find(cart_loc.empty_message_loc)
        assert empty_message.text == text

    def open_cart(self):
        cart_button = self.find(cart_loc.cart_button_loc)
        cart_button.click()

    def discount_code(self, code, text):
        discount_field = self.find(cart_loc.discount_field_loc)
        discount_field.send_keys(code)
        apply_button = self.find(cart_loc.apply_button_loc)
        apply_button.click()
        alert = self.find(cart_loc.alert_loc)
        assert alert.text == text

    def continue_purchase(self):
        continue_button = self.find(cart_loc.continue_button_loc)
        continue_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                cart_loc.cart_quantity_loc,
                "1"
            )
        )

    def check_price_in_basket(self, price):
        cart_price = self.find(cart_loc.cart_price_loc)
        assert cart_price.text == price
