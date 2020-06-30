import time
from selenium import webdriver


def extract(url, debug=False):
    driver = webdriver.Chrome('/Users/taek/Documents/WebDriver/chromedriver')
    driver.implicitly_wait(30)
    driver.get(url)

    # Turn off the 'clean bot' at comments.
    try:
        cleanbot = driver.find_element_by_css_selector('a.u_cbox_cleanbot_setbutton')
        cleanbot.click()
        time.sleep(0.1)

        cleanbot_check = driver.find_element_by_id('cleanbot_dialog_checkbox_cbox_module')
        cleanbot_check.click()
        time.sleep(0.1)

        ok_button = driver.find_element_by_css_selector('button.u_cbox_layer_cleanbot2_extrabtn')
        ok_button.click()
        time.sleep(0.1)
    except:
        print('There is no clean bot in this page.')

    while True:
        try:
            more_button = driver.find_element_by_css_selector('a.u_cbox_btn_more')
            more_button.click()
            time.sleep(1)
        except:
            break

    contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
    # Debugging -> print the comments.
    if debug:
        for content in contents:
            print(content.text)

    return contents


if __name__ == "__main__":
    url = 'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=102&oid=022&aid=0003479487'
    extract(url, debug=True)
