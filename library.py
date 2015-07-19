from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from hashlib import md5
from collections import OrderedDict
import os, datetime, urlparse
import requests
from os import environ as env

def _url(url):
    if url.startswith('http'):
        return url
    try:
        _https = 'https://%s' % url
        requests.head(_https)
        return _https
    except:
        pass
    return 'http://%s' % url

def take_screenshot(opts):
    url = _url(opts['url'])
    width, height = opts['width'], opts['height']
    background = opts['background']

    data = OrderedDict()

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
        "(KHTML, like Gecko) Chrome/15.0.87"
    )
    dcap['init.service_args'] = ('--web-security=false', '--ignore-ssl-errors=true', '--ssl-protocol=any')
    driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
    driver.get(url)
    driver.set_page_load_timeout(10)
    driver.set_window_size(width, height)

    data["title"] = driver.title
    data["url"] = driver.current_url
    data["screenshot"] = {}

    file_name = "%s.png" % md5(url).hexdigest()
    file_path = "static/screenshots/%s" % file_name
    full_url = "%s/%s" % (env.get("DOMAIN", 'http://localhost:5555'), file_path)

    if background:
        driver.execute_script("""(function() {
            var style = document.createElement('style'), text = document.createTextNode('body { background: %s }');
            style.setAttribute('type', 'text/css');
            style.appendChild(text);
            document.head.insertBefore(style, document.head.firstChild);
        })();""" % background)

    driver.save_screenshot(file_path)
    driver.quit()

    data["screenshot"]["url"] = full_url
    data["screenshot"]["taken_at"] = str(datetime.datetime.now())
    data["screenshot"]["size"] = os.path.getsize(str(file_path))

    return data
