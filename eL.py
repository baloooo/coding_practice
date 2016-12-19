import os
import time
import urlparse
import random
from selenium import webdriver
from bs4 import BeautifulSoup


def getPeopleLinks(page):
    """
    Returns every user id on the passed in page.
    """
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if 'profile/view?id=' in url:
                links.append(url)
    return links


def getJobsLinks(page):
    """
    Returns job links from jobs page of your profile.
    """
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        if url:
            if '/jobs' in url:
                links.append(url)
    return links


def getId(url):
    """
    Returns the person's id from a url
    """
    pUrl = urlparse.urlparse(url)
    return urlparse.parse_qs(pUrl.query)['id'][0]


def getCourses(page):
    """
    Returns links for all the courses that needs to be completed
    """
    links = []
    for link in page.find_all('a'):
        url = link.get('href')
        print "url is", url
        if url:
            if '/sf/learning' in url:
                links.append(url)
    return links


def complete_course(course, browser):
    # browser = webdriver.Firefox()
    browser.get('https://performancemanager10.successfactors.com'+course)
    page = BeautifulSoup(browser.page_source)
    # By.xpath("//button[contains(.,'Start Course')]").click()
    time.sleep(25)
    print page

    # from webdriver.common.by import By
    By = webdriver.common.by.By,ID
    browser.switchTo().frame(browser.findElement(By("17:_iframe")))

    # iframe = driver.find_elements_by_tag_name('iframe')[0]
    # driver.switch_to_default_content()
    # driver.switch_to_frame(iframe)
    # driver.find_elements_by_tag_name('iframe')[0]

    browser.find_element_by_xpath("//button[@title='Start Course']").click()
    # print "page source is", page
    exit()


def viewBot(browser):
    visited = {}
    pList = []
    count = 0
    while True:
        # Sleep to make everything load (JS)
        # add random delay to simulate humans.
        time.sleep(5)
        page = BeautifulSoup(browser.page_source)
        courses = getCourses(page)
        print "courses are", courses
        total_courses = len(courses)
        print "Total courses to complete", total_courses
        if courses:
            for course in courses:
                complete_course(course, browser)
                exit()
        # if people:
        #     for person in people:
        #         ID = getId(person)
        #         if ID not in visited:
        #             pList.append(person)
        #             visited[ID] = 1
        if pList:  # If people to visit then look at them
            person = pList.pop()
            browser.get(person)
            count += 1
        else:
            # Find persons using jobs page
            jobs = getJobsLinks(page)
            if jobs:
                job = random.choice(jobs)
                root = 'http://www.linkedin.com'
                roots = 'http://www.linkedin.com'
                if root not in job or roots not in job:
                    job = 'http:/www.linkedin.com' + job
                browser.get(job)
            else:
                print "Can't find any jobs on job page at Linkedin."
                break

        print ("[+] "+browser.title + "visited! \n"+str(count)+"/" +
               str(len(pList))+" Visited/Queue ")


def main():
    from getpass import getpass
    print "Enter Password"
    id = '100009345'
    password = 'Sonyv@io'
    # password = getpass()

    # var webdriver = require('selenium-webdriver'),By = webdriver.By,until = webdriver.until;

    # var driver = new webdriver.Builder().forBrowser('firefox').build();

    browser = webdriver.Firefox()
    browser.get("https://performancemanager10.successfactors.com/"
                "login?company=Atago")

    emailElement = browser.find_element_by_id("username")
    emailElement.send_keys(id)
    passElement = browser.find_element_by_id("password")
    passElement.send_keys(password)
    passElement.submit()

    os.system('clear')

    print "[+] Success ! Logged In, Bot Starting."
    viewBot(browser)
    browser.close()


if __name__ == '__main__':
    main()
