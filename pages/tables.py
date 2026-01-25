from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import tables_locators as loc, cart_locators as card_loc


class Table(BasePage):
    page_url = '/shop/category/desks-1'

    def check_found_good(self, price_value, good_name):
        goods = self.find_all(loc.goods_loc)
        assert len(goods) == 1
        goods_names = self.find_all(loc.goods_name_loc)
        assert goods_names[0].text == good_name
        price = self.find(loc.price_loc)
        assert price.text == price_value, f"Цена {price.text} не равна 750.00"

    def click_search_button(self):
        search_button = self.find(loc.search_button_loc)
        search_button.click()
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(*loc.goods_loc)) == 1
            )
        except:
            pass

    def send_query_in_search_field(self,query):
        search_field = self.find(loc.search_loc)
        actions = ActionChains(self.driver)
        actions.click(search_field).send_keys(query).perform()

    def sort_by_name(self,good1_name):
        goods_names = self.find_all(loc.goods_name_loc)
        assert goods_names[0].text == good1_name
        dropdown_element = self.find(loc.dropdown_element_loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown_element).click().perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.alphabet_filtration_loc)
        )
        alphabet_filtration = self.find(loc.alphabet_filtration_loc)
        actions.move_to_element(alphabet_filtration).click().perform()


    def check_good_name(self, good2_name):
        goods_names = self.find_all(loc.goods_name_loc)
        assert goods_names[0].text == good2_name



    def put_into_basket(self, good_name):
        goods = self.find_all(loc.goods_loc)
        ActionChains(self.driver).move_to_element(goods[0]).perform()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.add_basket_button_loc)
        )
        button = self.find(loc.add_basket_button_loc)
        button.click()
        good_in_card = self.find(card_loc.card_good_name_loc)
        assert good_in_card.text == good_name
