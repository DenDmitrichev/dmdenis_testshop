from selenium.webdriver.common.by import By


add_basket_button_loc = (By.CSS_SELECTOR, '[class="o_wsale_product_btn"]')
goods_loc = (By.CSS_SELECTOR, '[itemprop="image"]')
search_loc = (By.XPATH, '//input[contains(@class, "oe_search_box") and @data-search-type="products"]')
search_button_loc = (By.CSS_SELECTOR, '[class="btn oe_search_button btn btn-light"]')
price_loc = (By.CSS_SELECTOR, "span.oe_currency_value")
dropdown_element_loc = (By.XPATH, '//a[@class="dropdown-toggle btn btn-light" and .//span[normalize-space()="Featured"]]')
goods_name_loc = (By.CSS_SELECTOR, '[class="text-primary text-decoration-none"]')
alphabet_filtration_loc = (By.XPATH, '//a[@class="dropdown-item"]/span[text()="Name (A-Z)"]')
