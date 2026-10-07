from selenium.webdriver.common.by import By
from utils.saucedemo_helpers import (
    login,
    obtener_primer_producto
)
def test_login_exitoso(driver):
    login(driver)
    assert "inventory.html" in driver.current_url
    assert driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text == "Products"
    assert "Swag Labs" in driver.title
def test_catalogo_productos(driver):
    login(driver)
    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text
    assert titulo == "Products"
    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )
    assert len(productos) > 0
    nombre, precio = obtener_primer_producto(
        driver
    )
    print(f"\nPrimer producto: {nombre}")
    print(f"Precio: {precio}")
    assert nombre != ""
    assert precio != ""
    assert driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    ).is_displayed()
    assert driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    ).is_displayed()
def test_carrito_compras(driver):
    login(driver)
    nombre_producto = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text
    boton_agregar = driver.find_element(
        By.CSS_SELECTOR,
        "button.btn_inventory"
    )
    boton_agregar.click()
    badge = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )
    assert badge.text == "1"
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()
    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text
    assert nombre_producto == producto_carrito