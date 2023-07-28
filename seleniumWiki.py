from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Encrypt_Decrypt import *
import pymysql

# =============== Encrypt_Decrypt ====================

host = '41785A3245774C6D41775232446D4C3441784C335A6D7030'
user = '416D563245774D54416D443D'
password = '41515A3245774D5141784C3245514C6C417778325A475A6B5A78563D'
database = '417744325A77706A41484C335A6D4C3141785A3241474D534177783341474D5241484C335A6D4C6D416D56335A4E3D3D'

# ================== CONEXIÓN BD =====================

def conntDB():
    try:    
        connectionMySQL = pymysql.connect(host=DeCrypt(host), user=DeCrypt(user), password=DeCrypt(password
            ), db=DeCrypt(database), charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        connectionMySQL.autocommit(True)    
        print('Conexión establecida correctamente')
        return connectionMySQL
    except Exception as e:
        print('Sin conexión a la base de datos', e)

# Hasta acá va la conexión

def insertar_datos(titulo, primer_parrafo, historia, componentes):
    try:
        conn = conntDB()
        query = "INSERT INTO tbl_rscrp (SCR_CTITULO, SCR_CPRIMER_PARRAFO, SCR_CHISTORIA, SCR_CCOMPONENTES) VALUES (%s, %s, %s, %s)"
        values = (titulo, primer_parrafo, historia, componentes)
        cursor = conn.cursor()
        cursor.execute(query, values)
        cursor.close()
    except Exception as error:
        print('Error insertando datos')
        ControlERROR(error)

# ===================== SCRAPING =====================

def botSelenium():
    try:
        driver_path = 'chromedriver/chromedriver.exe'
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)

        driver.get("https://www.google.com/")
        time.sleep(2)
        xpath_elemento = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'
        elemento = driver.find_element(By.XPATH, xpath_elemento)
        elemento.send_keys('Selenium')
        time.sleep(3)
        # print('Se escribió correctamente')
        elemento.send_keys(Keys.ENTER)
        time.sleep(3)
        # print('Se obturó buscar')
        wait = WebDriverWait(driver, 10)
        enlace_wikipedia = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Wikipedia')))
        enlace_wikipedia.click()
        time.sleep(5)
        # print('Se accedió a la página correctamente' + "\n\n")
        wait = WebDriverWait(driver, 10)
        
        titulo = '/html/body/div[2]/div/div[3]/main/header/h1/span'
        titulo1 = driver.find_element(By.XPATH, titulo)
        # print(titulo1.text)
        time.sleep(3)

        primerParrafo = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[1]'
        parrafoprim = driver.find_element(By.XPATH, primerParrafo)
        # print(parrafoprim.text + "\n\n")
        time.sleep(3)

        historia = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]'
        historia1 = driver.find_element(By.XPATH, historia)
        # print(historia1.text + "\n\n")
        
        subtitulo = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/h3[1]/span[1]'
        subtitulo1 = driver.find_element(By.XPATH, subtitulo)
        time.sleep(3)
        seleniumIDE1 = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[3]'
        ide1 = driver.find_element(By.XPATH, seleniumIDE1)
        seleniumIDE2 = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[4]'
        ide2 = driver.find_element(By.XPATH, seleniumIDE2)
        seleniumIDE3 = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[5]'
        ide3 = driver.find_element(By.XPATH, seleniumIDE3)
        complementos = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/ul[1]'
        complementos1 = driver.find_element(By.XPATH, complementos)
        componentes = subtitulo1.text + "\n\n" + ide1.text + "\n\n" + ide2.text + "\n\n" + ide3.text + "\n\n" + complementos1.text
        # print(componentes)

        insertar_datos(titulo1.text, parrafoprim.text, historia1.text, componentes)
        driver.quit()
    except Exception as error:
        ControlERROR(error)
        print(error)

# ================= CONTROL DE ERRORES ==================

def ControlERROR(e):
    connectionMySQL = conntDB()
    try:
        with connectionMySQL.cursor() as cursor:
            cadena1 = str(e).replace('"','*')
            cadena2 = cadena1.replace("'","*")
            sql = "INSERT INTO " + str(DeCrypt(database)) + \
                ".tbl_error (ERR_CERROR, ERR_CNOMBRE_BOT) VALUES ('" + str(cadena2) + "', '" + str('botSelenium') + "');"
            cursor.execute(sql)
            connectionMySQL.close()
    except:
        print('Error ControlERROR')
        connectionMySQL.close()


# =================== CONTROL BOT =======================

def controlBot():
    connectionMySQL = conntDB()
    try:
        while True:
            with connectionMySQL.cursor() as cursor:
                function = "SELECT * FROM tbl_control WHERE SCR_CESTADO = 'Activo'"
                cursor.execute(function)
                result_rows = cursor.fetchall()
                if len(result_rows) > 0: 
                    if result_rows[0]['SCR_CARGUMENTO'] == 'Activo':
                        botSelenium()
                    else:
                        print('Bot inactivo desde base de datos')
                else: 
                    print('Sin parametros en la tabla')
            time.sleep(7)
    except Exception as error:
        print(error)
        ControlERROR(error)
controlBot()