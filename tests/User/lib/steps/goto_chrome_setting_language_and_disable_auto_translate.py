
from time import sleep

# KEYCODE_DPAD_DOWN=20
from lib.keycode import *

DEVICE_MOBILE=1
DEVICE_TABLET=2

def gotoChromeSettingLanguageAndDisableAutoTranslate(driver, device_type=DEVICE_MOBILE):
  if device_type==DEVICE_MOBILE:
    driver.switch_to.context("NATIVE_APP")

    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="More options"]').click()
    sleep(0.1)


    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Settings"]').click()
    sleep(0.1)



    for i in range(0,12+1):
      driver.press_keycode(KEYCODE_DPAD_DOWN)

    driver.press_keycode(KEYCODE_ENTER)

    # off to translate page in other languages
    driver.find_element_by_id('com.android.chrome:id/switchWidget').click()

    # back to chrome main screen
    driver.press_keycode(KEYCODE_BACK)
    driver.press_keycode(KEYCODE_BACK)

    driver.switch_to.context("WEBVIEW_chrome")

  if device_type==DEVICE_TABLET:
    driver.switch_to.context("NATIVE_APP")

    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="More options"]').click()
    sleep(0.1)


    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Settings"]').click()
    sleep(0.1)

    for i in range(0,9+1):
      driver.press_keycode(KEYCODE_DPAD_DOWN)
      sleep(0.2)

    driver.press_keycode(KEYCODE_ENTER)
    sleep(0.2)

    driver.find_element_by_xpath('//android.widget.LinearLayout[1]').click()

    # back to chrome main screen
    driver.press_keycode(KEYCODE_BACK)
    sleep(0.2)

    # NOTES: delete
    driver.press_keycode(KEYCODE_BACK)
    sleep(0.2)
