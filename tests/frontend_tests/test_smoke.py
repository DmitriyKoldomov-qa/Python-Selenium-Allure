import pytest

from selenium.webdriver.common.by import By

url = "https://testqastudio.me/"
# каждый тест должен начинаться с test_
def test_product_view_sku(browser):
    """
    Test case TC-1: [AUTO][PRE PROD] Проверка артикула товара "ДИВВИНА журнальный столик"
    """
	  # ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value='#main > div.catalog-toolbar.layout-v3 > div.catalog-toolbar-tabs__content > a.tab-best_sellers')
    element.click()
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    
    element = browser.find_element(by=By.CSS_SELECTOR, value='#rz-shop-content > ul > li.layout-v2.product-thumbnails-vertical.product-add-to-cart-ajax.razzi-play-video--popup.product.type-product.post-11341.status-publish.first.instock.product_cat-122.product_tag-121.product_tag-141.product_tag-135.product_tag-124.product_tag-142.has-post-thumbnail.featured.shipping-taxable.purchasable.product-type-simple > div > div.product-summary > h2 > a')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"