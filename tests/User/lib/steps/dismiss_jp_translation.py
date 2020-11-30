from time import sleep

def dismiss_jp_translation_in_chrome_browser(driver):
  driver.switch_to.context("NATIVE_APP")
  # driver.find_element_by_id("com.android.chrome:id/infobar_close_button").click()
  # sleep(0.1)

  driver.find_element_by_id("com.android.chrome:id/translate_infobar_menu_button").click()
  sleep(0.1)

  driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]").click()
  sleep(0.1)

  driver.switch_to.context("WEBVIEW_chrome")
