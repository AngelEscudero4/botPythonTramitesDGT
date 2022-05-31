from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pygame import mixer

from time import sleep

from random import randrange


def intenta():
    # MUSICA
    mixer.init()
    mixer.music.set_volume(1)
    i = randrange(6)+1
    print("Seleccionada la cancion ", i)
    mixer.music.load('musica/sound' + str(i) + '.mp3')
    mixer.music.play()

    # abrir chromium
    my_url = f'https://sedeclave.dgt.gob.es/WEB_NCIT_CONSULTA/solicitarCita.faces'
    option = Options()
    option.add_argument("start-maximized")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.headless = False
    driver = webdriver.Chrome(options=option)
    driver.get(my_url)

    # ofi
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div[1]/fieldset/div/div[1]/select"))).click()
    # alcorcon
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div[1]/fieldset/div/div["
                                    "1]/select/optgroup[10]/option[3]"))).click()
    # tramite
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div[1]/fieldset/div/div[2]/select"))).click()
    # de oficina
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/div[1]/div[2]/div/div[2]/div[2]/form/div[1]/fieldset/div/div["
                                    "2]/select/option[2]"))).click()

    # Google recaptcha
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

    # bajar sonido de la musica
    sleep(2)
    while mixer.music.get_volume() > 0.01:
        print(mixer.music.get_volume())
        mixer.music.set_volume(mixer.music.get_volume() / 1.07)
        sleep(0.5)
    mixer.music.stop()

    # wait 1 min para siguiente
    sleep(5*60)

    return 0


if __name__ == '__main__':
    val = 0

    while val == 0:
        val = intenta()
