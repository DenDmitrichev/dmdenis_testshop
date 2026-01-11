from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import cart_locators as cart_loc
from pages.tables import Table


class CartPage(Table):
    page_url = '/shop/cart'

    def check_empty_message(self):
        empty_message = self.find(cart_loc.empty_message_loc)
        assert empty_message.text == "Your cart is empty!"

    def clear(self):
        self.put_into_basket()
        continue_button = self.find(cart_loc.continue_button_loc)
        continue_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                cart_loc.cart_quantity_loc,
                "1"
            )
        )
        cart_button = self.find(cart_loc.cart_button_loc)
        cart_button.click()
        remove_button = self.find(cart_loc.remove_button_loc)
        remove_button.click()
        empty_message = self.find(cart_loc.empty_message_loc)
        assert empty_message.text == "Your cart is empty!"

    def discount_code(self, code):
        self.put_into_basket()
        continue_button = self.find(cart_loc.continue_button_loc)
        continue_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                cart_loc.cart_quantity_loc,
                "1"
            )
        )
        cart_button = self.find(cart_loc.cart_button_loc)
        cart_button.click()
        discount_field = self.find(cart_loc.discount_field_loc)
        discount_field.send_keys(code)
        apply_button = self.find(cart_loc.apply_button_loc)
        apply_button.click()
        alert = self.find(cart_loc.alert_loc)
        assert alert.text == "This promo code is not available."
