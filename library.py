from selenium import webdriver

def take_and_save_screen_shot(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.save_screenshot("static/screenshot.png")
    driver.quit()

    return True
