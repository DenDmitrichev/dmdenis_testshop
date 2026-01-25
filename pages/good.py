from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import good_locators as good_loc



class Good(BasePage):
    page_url = '/shop/furn-6666-acoustic-bloc-screens-23?category=1&order=name+asc'

    def term_and_conditions(self, text):
        terms_button = self.find(good_loc.terms_button_loc)
        terms_button.click()
        header = self.find(good_loc.header_loc)
        assert header.text == text


    def check_price(self, price):
        price_in_card = self.find(good_loc.price_in_card_loc)
        assert price_in_card.text == price


    def open_good_in_card(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(good_loc.card_tool_tip_loc)
        )
        card_tool_tip = self.find(good_loc.card_tool_tip_loc)
        card_tool_tip.click()


    def check_card_header(self, header_text):
        card_header = self.find(good_loc.card_header_loc)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(good_loc.card_header_loc))
        assert card_header.text == header_text


    def add_some_goods_into_card(self):
        count_input = self.find(good_loc.count_input_loc)
        count_input.clear()
        count_input.send_keys('2')
        add_button = self.find(good_loc.add_button_loc)
        add_button.click()
