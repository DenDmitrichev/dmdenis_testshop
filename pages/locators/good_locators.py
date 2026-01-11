from selenium.webdriver.common.by import By


count_input_loc = (By.CSS_SELECTOR, '[class="form-control quantity text-center"]')
add_button_loc = (By.ID, "add_to_cart")
card_tool_tip_loc = (By.CSS_SELECTOR, '[class="w-100 btn btn-primary"]')
card_header_loc = (By.CSS_SELECTOR, '[class="mb-4"]')
card_price_loc = (By.CSS_SELECTOR, '[class="oe_currency_value"]')
price_in_card_loc = (By.CSS_SELECTOR, '''[data-oe-expression="combination_info['price']"] .oe_currency_value''')
terms_button_loc = (By.LINK_TEXT, "Terms and Conditions")
header_loc = (By.TAG_NAME, "h1")
