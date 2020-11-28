from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setupRemoteChrome(device_simulation="Nexus 5"):
  caps = webdriver.DesiredCapabilities.CHROME.copy()

  selenium_url = 'http://{}:4444/wd/hub'.format('localhost')

  mobile_emulation = { "deviceName": device_simulation }
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
  chrome_options.add_experimental_option('w3c', False)

  # chrome_options.add_argument("--headless")

  caps=chrome_options.to_capabilities()
  caps['acceptInsecureCerts'] = True


  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = chrome_options.to_capabilities()
  )

  return browser

  # selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)
  # chrome_options = webdriver.ChromeOptions()
  # mobile_emulation = { "deviceName": "Nexus 5" }
  # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

  # browser = webdriver.Remote(
  #   command_executor=selenium_url,
  #   desired_capabilities = chrome_options.to_capabilities()
  # )
  # pass