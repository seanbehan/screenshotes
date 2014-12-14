from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from hashlib import md5
import datetime
import os
import urlparse
from collections import OrderedDict

def getenv():
    if os.environ.get("FLASK_ENV"):
        return "production"
    return "development"

def domain():
    if getenv()=="production":
        return "http://fullpagescreenshots.com"
    else:
        return "http://localhost:5000"

def format_url(url):
    _url = urlparse.urlparse(url)
    if '' == _url.scheme:
        return 'http://%s' % url
    return url

def take_screenshot(url):
    url = format_url(url)
    data = OrderedDict()

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
    # document_title = driver.title
    data["title"] = driver.title

    driver.set_page_load_timeout(10)
    driver.set_window_size(1200, 750)
    # document_url = driver.current_url
    data["url"] = driver.current_url
    data["screenshot"] = {}

    file_name = "%s.png" % md5(url).hexdigest()
    file_path = "static/screenshots/%s" % file_name
    full_url = "%s/%s" % (domain(), file_path)

    driver.save_screenshot(file_path)
    driver.quit()

    # data["screenshot"]["file"] = file_name
    data["screenshot"]["url"] = full_url
    data["screenshot"]["taken_at"] = str(datetime.datetime.now())
    data["screenshot"]["size"] = os.path.getsize(str(file_path))

    return data
