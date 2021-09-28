import time, math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


answer = str(math.log(int(time.time())))
lessons = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

class TestMarksTask:
    ans = ''
    @pytest.mark.parametrize('lesson', lessons)
    def test_navigate_by_links(self, browser, lesson):
        link = f'https://stepik.org/lesson/{lesson}/step/1'
        browser.get(link)
        browser.find_element_by_css_selector('.ember-text-area.textarea').send_keys(answer)
        browser.find_element_by_css_selector('.submit-submission').click()
        hint = browser.find_element_by_css_selector("pre[class='smart-hints__hint']")
        if hint.text != 'Correct!':
            TestMarksTask.ans += hint.text
        #assert hint.text == 'Correct!', f'Answer should be {hint.text}'
            print(TestMarksTask.ans)