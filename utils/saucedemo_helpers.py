from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
def login(driver):
    """
    Realiza login en SauceDemo.
    """
    driver.get(URL)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )
    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys(USERNAME)
    driver.find_element(
        By.ID,
        "password"
    ).send_keys(PASSWORD)
    driver.find_element(
        By.ID,
        "login-button"
    ).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
def obtener_primer_producto(driver):
    """
    Devuelve nombre y precio del primer producto.
    """
    nombre = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text
    precio = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text
    return nombre, precio
