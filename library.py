from selenium import webdriver

def take_and_save_screen_shot(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.set_window_size(1200, 750)
    driver.save_screenshot("static/screenshot.png")
    driver.quit()

    return True