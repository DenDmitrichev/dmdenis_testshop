from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import tables_locators as loc
from pages.locators import cart_locators as card_loc


class Table(BasePage):
    page_url = '/shop/category/desks-1'

    def search_by_good_name(self, query):
        search_field = self.find(loc.search_loc)
        actions = ActionChains(self.driver)
        actions.click(search_field).send_keys(query).perform()
        search_button = self.find(loc.search_button_loc)
        search_button.click()
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(*loc.goods_loc)) == 1
            )
        except:
            pass
        goods = self.find_all(loc.goods_loc)
        assert len(goods) == 1
        price = self.find(loc.price_loc)
        assert price.text == "750.00", f"Цена {price.text} не равна 750.00"

    def sort_by_name(self):
        goods_names = self.find_all(loc.goods_name_loc)
        assert goods_names[0].text == "Customizable Desk"
        dropdown_element = self.find(loc.dropdown_element_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown_element).click().perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.alphabet_filtration_loc)
        )
        alphabet_filtration = self.find(loc.alphabet_filtration_loc)
        actions.move_to_element(alphabet_filtration).click().perform()
        goods_names = self.find_all(loc.goods_name_loc)
        assert goods_names[0].text == "Acoustic Bloc Screens"


    def put_into_basket(self):
        goods = self.find_all(loc.goods_loc)
        ActionChains(self.driver).move_to_element(goods[0]).perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.add_basket_button_loc)
        )
        button = self.find(loc.add_basket_button_loc)
        button.click()
        good_in_card = self.find(card_loc.card_good_name_loc)
        assert good_in_card.text == "[FURN_0096] Customizable Desk (Steel, White)"
