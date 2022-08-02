from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import constants



def loginMethod():
    login = browser.find_element(By.XPATH, constants.loginXPath)
    login.click()
    time.sleep(5)
    userName = browser.find_element(By.XPATH, constants.userNameXPath)
    userName.send_keys(constants.myUserName)
    next = browser.find_element(By.XPATH, constants.nextXPath)
    next.click()
    time.sleep(2)
    password = browser.find_element(By.XPATH, constants.passwordXPath)
    password.send_keys(constants.myPassword)
    loginButton = browser.find_element(By.XPATH, constants.loginButtonXPath)
    loginButton.click()
    time.sleep(5)
def search():
    searchArea = browser.find_element(By.XPATH, constants.searchAreaXPath)
    searchArea.send_keys(constants.searchText)
    searchArea.send_keys(Keys.ENTER)
    time.sleep(5)
def scrollingMethod():
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while (match == False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
def writeToFile():
    tweets = browser.find_elements(By.CSS_SELECTOR, constants.cssClassOfTweets)
    files = []
    for tweet in tweets:
        files.append(tweet.text)
    tweetCount = 1
    with open("tweets.txt", "w", encoding="UTF-8") as file:
        for tweet in files:
            file.write(str(tweetCount) + ".\n" + tweet + "\n")
            file.write("-----------------------------------------\n")
            tweetCount += 1


browser = webdriver.Chrome()
browser.get(constants.url)

time.sleep(3)

loginMethod()
search()
scrollingMethod()
writeToFile()


browser.close()


