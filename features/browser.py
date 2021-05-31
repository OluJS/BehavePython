from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser(object):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
