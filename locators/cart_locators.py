from selenium.webdriver.common.by import By

cart_price_loc = (By.CSS_SELECTOR,
                  "div.mb-0.h6.fw-bold.text-end[name='website_sale_cart_line_price'] span.oe_currency_value")
card_good_name_loc = (By.CSS_SELECTOR, '[class="product-name product_display_name"]')
continue_button_loc = (By.CSS_SELECTOR, '[class="btn btn-secondary"]')
cart_button_loc = (By.CSS_SELECTOR, '[href="/shop/cart"]')
cart_quantity_loc = (By.CSS_SELECTOR, "sup.my_cart_quantity")
empty_message_loc = (By.CSS_SELECTOR, '[class = "js_cart_lines alert alert-info"]')
remove_button_loc = (By.CSS_SELECTOR, '[class="js_delete_product d-none d-md-inline-block small"]')
discount_field_loc = (By.CSS_SELECTOR, '[name="promo"]')
apply_button_loc = (By.CSS_SELECTOR, '[class="btn btn-secondary a-submit ps-2"]')
alert_loc = (By.CSS_SELECTOR, '[class="alert alert-danger text-start"]')
