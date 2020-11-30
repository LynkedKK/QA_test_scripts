def dismissTestDevice(browser, package="com.android.chrome"):
  browser.terminate_app(package)
  browser.reset()
  browser.close_app()
  browser.quit()
