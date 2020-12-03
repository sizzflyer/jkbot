from config import keys
from selenium import webdriver
import time

# will cookies improve load time?
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=www.supremenewyork.com')


driver = webdriver.Chrome('./chromedriver')

driver.get(keys['login_url'])

# login config
driver.find_element_by_name('email').send_keys(keys['email'])
driver.find_element_by_name('password').send_keys(keys['password'])
driver.find_element_by_xpath("//button[@class='login__button login__button--submit _loginSubmitButton']").click()
print("로그인 완료")

# product
driver.get(keys['product_url'])
time.sleep(30)
while True:
    xpath = "//button[@class='prod-buy-btn']"
    buy = driver.find_element_by_xpath(xpath)
    print(buy.text)

    if buy.text == '바로구매':
        print("구매합니다.")
        buy.click()
        break
    else :
        print("상품이 아직 안뜸")
        driver.refresh()
        driver.implicitly_wait(10)


