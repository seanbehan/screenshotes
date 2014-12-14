from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def take_screenshot(url):


    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87"
    )
    dcap["phantomjs.cli.jargs"] = (
    "--web-security=false --ignore-ssl-errors=true --ssl-protocol=any"
    )

    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    driver.get(url)
    # --ignore-ssl-errors=true --ssl-protocol=any
    driver.set_window_size(1200, 750)
    driver.save_screenshot("static/screenshot.png")
    driver.quit()

    return True
