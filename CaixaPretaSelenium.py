import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configuração do driver do Selenium WebDriver
driver_path = 'caminho do drive' # Caminho para o driver do Chrome
driver = webdriver.Chrome(driver_path)

# Acessa o site Sauce Demo e faz login com as credenciais fornecidas
driver.get("https://www.saucedemo.com/")

time.sleep(1)

driver.find_element("css selector", "input#user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element("css selector", "input#password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element("css selector", "input.btn_action").click()
time.sleep(1)

#driver.find_element_by_css_selector("input#user-name").send_keys("standard_user")
#driver.find_element_by_css_selector("input#password").send_keys("secret_sauce")
#driver.find_element_by_css_selector("input.btn_action").click()

time.sleep(1)


# Verifica se o login foi bem-sucedido
pageTitle = driver.find_element("css selector", "span.title")
assert pageTitle.text == "Products"

# Adiciona um produto ao carrinho de compras
time.sleep(1)
driver.find_element("css selector", "button.btn_primary").click()
time.sleep(1)
driver.find_element("css selector", "a.shopping_cart_link").click()
time.sleep(1)
cartItem = driver.find_element("css selector", "div.inventory_item_name")
assert cartItem.text == "Sauce Labs Backpack"

#remover a compra
driver.find_element("css selector", "button#remove-sauce-labs-backpack").click()
driver.find_element("css selector", "button#continue-shopping").click()

#verificar dados faltantes na finalização da compra
driver.find_element("css selector", "button#add-to-cart-sauce-labs-backpack")
time.sleep(1)
driver.find_element("css selector", "button#add-to-cart-sauce-labs-bike-light")
time.sleep(1)
driver.find_element("css selector", "a.shopping_cart_link").click()
time.sleep(1)
driver.find_element("css selector", "button#checkout").click()
time.sleep(1)
driver.find_element("css selector", "button#continue").click()
folder = driver.find_element("css selector", "button.error-button")
assert folder.text == "Error: First Name is required"

#voltar para o inicio
driver.find_element("css selector", "button#react-burger-menu-btn")
driver.find_element("css selector", "a#inventory_sidebar_link")



#finalizar uma compra
driver.find_element("css selector", "button.btn_primary").click()
time.sleep(1)
driver.find_element("css selector", "a.shopping_cart_link").click()
time.sleep(1)
driver.find_element("css selector", "button#checkout").click()
time.sleep(1)
driver.find_element("css selector", "input#first-name").send_keys("Jheymesson")
time.sleep(1)
driver.find_element("css selector", "input#last-name").send_keys("Cavalcanti")
time.sleep(1)
driver.find_element("css selector", "input#postal-code").send_keys("55555555")
time.sleep(1)
driver.find_element("css selector", "input#continue").click()
time.sleep(1)
driver.find_element("css selector", "button#finish").click()
banner = driver.find_element("css selector", "h2.complete-header")
assert banner.text == "Thank you for your order!"


# Remove um produto do carrinho de compras
#driver.find_element("css selector", "button.cart_button").click()
#driver.find_element("css selector", "button.btn_secondary").click()
#emptyCartMsg = driver.find_element("css selector", "div.subheader")
#assert "Your cart is currently empty" in emptyCartMsg.text

# Realiza uma pesquisa por um produto específico
#driver.find_element("css selector", "input#search_input").send_keys("Sauce Labs Bike Light" + Keys.RETURN)
#searchResultsPageTitle = driver.find_element("css selector", "div.title")
#assert "Search Results" in searchResultsPageTitle.text
#searchResultsItem = driver.find_element("css selector", "div.inventory_item_name")
#assert searchResultsItem.text == "Sauce Labs Bike Light"

# Fecha o navegador
driver.quit()
