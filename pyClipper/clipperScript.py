from selenium import webdriver
import time
import getpass

def obtain_histories():
    YOUR_PASSWORD = getpass.getpass("Password: ")
    YOUR_USERNAME = raw_input("Username: ")
    ### Set options on headless browser to download PDFs upon click
    options = webdriver.ChromeOptions()
    download_folder = "./ridehistories/"
    profile = {"plugins.plugins_list": [{"enabled": False,
                                              "name": "Chrome PDF Viewer"}],
                    "download.default_directory": download_folder,
                    "download.extensions_to_open": ""}
    options.add_experimental_option("prefs", profile)

    ### Open headless browser and login to your Clipper dashboard
    browser = webdriver.Chrome('./chromedriver', chrome_options = options)
    time.sleep(3)
    browser.get("https://www.clippercard.com/ClipperWeb/index.do")
    time.sleep(2)
    login_button = browser.find_element_by_id("mytranslinkModuleRollover")
    login_button.click()
    time.sleep(1)
    browser.switch_to.frame('headeriFrame')
    username = browser.find_element_by_id("j_idt13:username")
    password = browser.find_element_by_id("j_idt13:password")
    username.send_keys(YOUR_USERNAME)
    time.sleep(1)
    password.send_keys(YOUR_PASSWORD)
    time.sleep(1)
    submit_login_button = browser.find_element_by_name("j_idt13:submitLogin")
    submit_login_button.click()
    time.sleep(5) # Might take a few seconds to load page

    ### Iterate through cards on account and click on card history
    hist_list = browser.find_elements_by_link_text("Last 30 Days")
    for item in hist_list:
        item.click()
        time.sleep(2)

        ### TESTING -- you only get 2 history clicks per card per day
    """
    for i in range(3,6):
        hist_list[i].click()
        time.sleep(1)
    """
        ### /TESTING

    time.sleep(3) # Because abruptness is unpleasant for humans
    browser.close()

if __name__ == "__main__":
    obtain_histories()
