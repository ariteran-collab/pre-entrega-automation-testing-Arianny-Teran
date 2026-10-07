# Pre Entrega Automation Testing - SauceDemo
## Descripción
Proyecto de automatización de pruebas funcionales desarrollado con Selenium WebDriver y Pytest sobre la aplicación de práctica SauceDemo.
El objetivo es validar funcionalidades críticas del sitio mediante pruebas automatizadas garantizando la correcta operación del login, navegación de productos y gestión del carrito de compras.
---
## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- WebDriver Manager
- Git
- GitHub
---
## Estructura del proyecto
```text
pre-entrega-automation-testing-arianne-teran/
├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   └── saucedemo_helpers.py
│
├── reports/
│   ├── reporte.html
│   └── screenshots/
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore
```
---
## Casos de Prueba Automatizados
### Caso de Prueba 1: Login Exitoso
**Objetivo:**
Validar que un usuario registrado pueda acceder correctamente al sistema.
**Pasos:**
1. Navegar a https://www.saucedemo.com
2. Ingresar usuario válido:
   - standard_user
3. Ingresar contraseña válida:
   - secret_sauce
4. Hacer clic en Login
**Validaciones:**
- Redirección a `/inventory.html`
- Visualización del título "Products"
- Presencia de "Swag Labs"
**Resultado esperado:**
El usuario accede correctamente al catálogo de productos.
---
### Caso de Prueba 2: Navegación y Catálogo
**Objetivo:**
Verificar la correcta visualización del inventario.
**Pasos:**
1. Iniciar sesión.
2. Acceder a la página de inventario.
**Validaciones:**
- Título igual a "Products"
- Existencia de productos visibles
- Obtención del nombre del primer producto
- Obtención del precio del primer producto
- Presencia del menú lateral
- Presencia del filtro de ordenamiento
**Resultado esperado:**
El catálogo se carga correctamente mostrando productos y controles de navegación.
---
### Caso de Prueba 3: Carrito de Compras
**Objetivo:**
Validar el agregado de productos al carrito.
**Pasos:**
1. Iniciar sesión.
2. Seleccionar el primer producto.
3. Agregar producto al carrito.
4. Acceder al carrito.
**Validaciones:**
- Incremento del contador del carrito
- Visualización del producto agregado
- Coincidencia entre producto seleccionado y producto almacenado
**Resultado esperado:**
El producto se agrega correctamente al carrito.
---
## Instalación
Clonar el repositorio:
```bash
git clone https://github.com/ariteran-collab/pre-entrega-automation-testing-Arianny-Teran.git
```
Crear entorno virtual:
```bash
python -m venv venv
```
Activar entorno virtual:
### Windows
```bash
.\venv\Scripts\Activate.ps1
```
### Linux/Mac
```bash
source venv/bin/activate
```
Instalar dependencias:
```bash
pip install -r requirements.txt
```
---
## Ejecución de pruebas
Ejecutar todos los tests:
```bash
pytest -v
```
Ejecutar archivo específico:
```bash
pytest tests/test_saucedemo.py -v
```
---
## Generación de Reporte HTML
```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```
El reporte se almacenará en:
```text
reports/reporte.html
```
---
## Evidencias de Fallos
Si una prueba falla se genera automáticamente una captura de pantalla en:
```text
reports/screenshots/
```
---
## Autor
Arianny Alejandra Teran Cordero