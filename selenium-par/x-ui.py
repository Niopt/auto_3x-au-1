from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

url = os.getenv("URL_3X_UI")

options = Options()
options.add_argument("--headless=new") # Без графики 
options.add_argument("--no-sandbox") # Без песочницы от хрома
options.add_argument("--disable-dev-shm-usage") # Отключаем кэш в /dev/shm
options.add_argument("--disable-gpu") # Отключаем рендеринг страниц
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
)
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get(url)

                                                        
driver.implicitly_wait(1)
# Ищем элементы
element_user = driver.find_element(By.NAME, "username") # Поле Логина
element_passwd = driver.find_element(By.NAME, "password") # Поле пароля
check_input = driver.find_element(By.XPATH, '//button[contains(@class, "ant-btn-primary-login")]') # кнопки войти
# Данные
user = os.getenv("LOGIN")
passwd = os.getenv("PASSWORD")
# Действия 
element_user.send_keys(user) # Ввод 
element_passwd.send_keys(passwd) # Ввод
check_input.click() # Нажимание
# Взаисодействие с новым окном
driver.implicitly_wait(7)
# Выбираем то-то
Inbounds = driver.find_element(By.XPATH, '(//div[@class="ant-sidebar"]//aside//div[1]//ul[2]//li[2])')
driver.execute_script("arguments[0].click();", Inbounds)
# Добовляем новое подключение 
Add_Inbound = driver.find_element(By.XPATH, '(//div[@class="ant-row"]//div[2]//div//div[1]//div[1]//div//div[1]//button)')
print(Add_Inbound.is_displayed())
Add_Inbound.click()
# Вписываем Remark
rema = "VLESS"
Remark = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form[1]//div[2]//div[2]//div//span//input)')
Remark.send_keys(rema)
# Выбираем Reality
Security = driver.find_element(By.XPATH, '//label[.//span[text()="Reality"]]')
Security.click()
# Настроили первый 
Dest  = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form[7]//div[6]//div[2]//div//span//input)')
dest_value = os.getenv("DEST")
driver.execute_script("arguments[0].click();", Dest)
Dest.send_keys(Keys.CONTROL, 'a')  # выделить всё
Dest.send_keys(Keys.DELETE)        # удалить
Dest.send_keys(f"{dest_value}:443")
# Настроили второй
SNI  = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form[7]//div[7]//div[2]//div//span//input)')
driver.execute_script("arguments[0].click();", SNI)
SNI.send_keys(Keys.CONTROL, 'a')  # выделить всё
SNI.send_keys(Keys.DELETE)        # удалить
SNI.send_keys(f"www.{dest_value}")
# Генерируем секрет
Get_Cert = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form[7]//div[13]//div[2]//div//span//button)')
Get_Cert.click()
# Открываем вкладку
Sniffin = driver.find_element(By.XPATH, '//div[@class="ant-modal-body"]//div[@class="ant-collapse ant-collapse-icon-position-left"][2]//div//div')
Sniffin.click()
# Переключаем свитч
Enabled = driver.find_element(By.XPATH,'//div[@class="ant-modal-body"]//div[@class="ant-collapse ant-collapse-icon-position-left"][2]//div[2]//div//form//div//div[2]//div//span//button')
Enabled.click()
# Создаем 
Create = driver.find_element(By.XPATH, '(//div[@class="ant-modal-content"]//div[3]//div//button[2])')
Create.click()



                                                        # Настройка WRAP
# Кликаем на Xray
Xray = driver.find_element(By.XPATH, '(//div[@class="ant-sidebar"]//aside//div[1]//ul[2]//li[4])')
driver.execute_script("arguments[0].click();", Xray)
# Кликаем на Xray
Routing = driver.find_element(By.XPATH, '(//div[@class="ant-row"]//div[2]//div//div[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]//div[1]//div[@class="ant-collapse ant-collapse-icon-position-left"]//div[4]//div)')
Routing.click()
# Нажимаем на кнопку wrap
Wrap = driver.find_element(By.XPATH, '(//div[@class="ant-row"]//div[2]//div//div[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]//div[1]//div[@class="ant-collapse ant-collapse-icon-position-left"]//div[4]//div[2]//div//li[@class="ant-list-item"][7]//div//div[2]//button)')
Wrap.click()
# Создаем Wrap
Create_wrap = driver.find_element(By.XPATH, '(//div[@class="ant-modal-content"]//div[@class="ant-modal-body"]//button)')
Create_wrap.click()
# Добовляем чтобы появилась новая кнопка
more_info = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//button[2])')
more_info.click()
# Нажимаем на кнопку чобы сохранить
Rules = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form//button)')
Rules.click()
# Переходим на марщрутизацию
Add_Rules = driver.find_element(By.XPATH, '(//div[@class="ant-tabs-bar ant-tabs-top-bar"]//div//div//div//div//div//div[2])')
Add_Rules.click()
# Сохдаем новое правило
Add_New_Rules = driver.find_element(By.XPATH, '(//div[@class="ant-row"]//div[2]//div//div[@class="ant-tabs-content ant-tabs-content-animated ant-tabs-top-content"]//div[2]//div[@class="ant-space ant-space-vertical"]//div[1]//button)')
Add_New_Rules.click()
# Заполняем домен 
Domain = 'geosite:category-gov-ru,regexp:.*\.ru$,regexp:.*\.su$'
Domain_add = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form//div[9]//div[2]//div//span//input)')
Domain_add.send_keys(Domain)
# Порты проставляем 
Port = '80,443'
Port_add = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form//div[11]//div[2]//div//span//input)')
Port_add.send_keys(Port)
# Нажимаем на список
Tag = driver.find_element(By.XPATH, '(//div[@class="ant-modal-body"]//form//div[13]//div[2]//div//span//div//div//div)')
Tag.click()
# Выбираем Warp

# ожидание появления dropdown
print(driver.page_source)
wait = WebDriverWait(driver, 10)
option_click = wait.until(EC.visibility_of_element_located((
    By.XPATH,
    '(//div[@class="ant-select-dropdown light ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]//div//ul//li[4])'
)))
option_click.click()



#option_click = driver.find_element(By.XPATH, '(//div[@class="ant-select-dropdown light ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]//div//ul//li[4])')
#option_click.click()
# Нажимаем на кнопку добовления
Add_rules = driver.find_element(By.XPATH, '(//div[@class="ant-modal-footer"]//div//button[2])')
Add_rules.click()
# нажимаем на кнопку сохранения 
Save = driver.find_element(By.XPATH, '(//div[@class="ant-row"]//div[1]//div//div//div//div[1]//div//div[1]//button)')
Save.click()
# Презапускаем Xray
Restart = driver.find_element(By.XPATH, '(//div[@class="ant-row"]//div[1]//div//div//div//div[1]//div//div[2]//button)')
Restart.click()
# Завершаем сеанс
driver.quit()