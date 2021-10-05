from selenium import webdriver
import pyautogui
import keyboard

pyautogui.PAUSE = 0

TILES_DIMENSIONS_X = [300, 400, 500, 700]

CHROME_DRIVER_PATH = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get("https://h5.4j.com/games/Piano-Tiles-2-Online/index.html")


def play_piano():
    try:
        while True:
            for x_dimension in TILES_DIMENSIONS_X:
                pyautogui.moveTo(x_dimension, 550)
                if pyautogui.pixelMatchesColor(x_dimension, 550, (0, 0, 0)):
                    pyautogui.click(x=x_dimension, y=550)
            if keyboard.is_pressed("space"):
                break
    except pyautogui.FailSafeException:
        pass
    except OSError:
        pass
    except KeyboardInterrupt:
        pass


def start_bot():
    try:
        for x_dimension in TILES_DIMENSIONS_X:
            if pyautogui.pixelMatchesColor(x_dimension, 700, (54, 159, 198)):
                pyautogui.click(x=x_dimension, y=700)
                play_piano()
    except pyautogui.FailSafeException:
        pass
    except OSError:
        pass
    except KeyboardInterrupt:
        pass


try:
    while True:
        if keyboard.is_pressed("space"):
            start_bot()
            break
except KeyboardInterrupt:
    pass
