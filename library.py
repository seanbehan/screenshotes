from selenium import webdriver

def take_screenshot(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.set_window_size(1200, 750)
    driver.save_screenshot("static/screenshot.png")
    driver.quit()

    return True
