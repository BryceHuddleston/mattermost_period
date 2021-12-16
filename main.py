import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


def main():
    time_to_post = False
    number_of_swaps = 0

    driver.get("https://chat.il4.dso.mil/oauth/gitlab/login")
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    continue_button = driver.find_element_by_id("kc-login")
    continue_button.click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    accept_button = driver.find_element_by_id("kc-accept")
    accept_button.click()
    time.sleep(10)
    an_general_channel = driver.find_element_by_id(
        "sidebarItem_16ws---alphanumerics")
    an_watercooler_channel = driver.find_element_by_id(
        "sidebarItem_an---development-discussion")
    bryce_huddleston_channel = driver.find_element_by_id(
        "sidebarItem_bryce_huddleston")
    bryce_huddleston_channel.click()
    time.sleep(4)

    while time_to_post == False:
        number_of_swaps = 1 + number_of_swaps

        current_hour = time.localtime().tm_hour
        current_minute = time.localtime().tm_min

        # current hour will be 6 and current minute will be 55
        if current_hour == 6 and current_minute >= 55:
            time_to_post = True

        if number_of_swaps % 2 == 0:
            an_watercooler_channel.click()
        else:
            # bryce_huddleston_channel.click()
            an_general_channel.click()

        print(number_of_swaps)
        time.sleep(60)

    # In production it will be an-general
    an_general_channel.click()
    # bryce_huddleston_channel.click()
    message_box = driver.find_element_by_id("post_textbox")
    time.sleep(10)
    message_box.send_keys("Good Morning")
    message_box.send_keys(Keys.ENTER)


main()
