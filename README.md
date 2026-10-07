# Pre Entrega Automation Testing - SauceDemo
Proyecto final de automatización web utilizando Selenium WebDriver y Pytest.
## Objetivo
Automatizar casos de prueba funcionales sobre la aplicación SauceDemo.
Las pruebas incluyen:
- Login exitoso.
- Verificación del catálogo.
- Visualización de productos.
- Obtención de nombre y precio de producto.
- Agregado de producto al carrito.
- Validación del carrito de compras.
## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- WebDriver Manager
- Git
- GitHub
## Instalación
Clonar el repositorio:
```bash
git clone 
Crear entorno virtual:
```bash
python -m venv venv
```
Activar entorno:
Windows:
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```
Instalar dependencias:
```bash
pip install -r requirements.txt
```
## Ejecución de pruebas
```bash
pytest tests/test_saucedemo.py -v
```
## Generación de reporte HTML
```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```
## Capturas automáticas
Cuando una prueba falla se genera automáticamente una captura en:
```text
reports/screenshots/
```
## Estructura
```text
tests/
utils/
reports/
```