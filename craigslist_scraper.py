import random
from bs4 import BeautifulSoup
import requests
import time
import google_sheets
import re
from datetime import date
from datetime import datetime
import proxy_rotation


def url_getter(url):

    # THERE WILL BE TWO SCRAPING OPTIONS BELOW

    # 1) THE FIRST FUNCTION IS USING THE FREE PROXY SERVICE.
    #    This service will pull the most up-to-date free proxies and will be rotated on each request.
    #    Because the proxies are free, that means they will most likely be blocked on a lot of the requests.
    #    This function automatically retries a random proxy in the list until success.

    # To scrape with the proxy, uncomment this function bellow and comment out function #1

    return proxy_rotation.url_getter_wp(url)

    # 2) THE SECOND FUNCTION IS USING YOUR PERSONAL IP ADDRESS
    #    This will allow you to scrape the website much faster due to less failed requests.
    #    I recommend you keep the time.sleep in place so that you are adhering to general webscraping ethics and codes of conduct.
    #    This will reduce your chances of being blocked by the website.


    # headers = requests.utils.default_headers()
    # headers.update({
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Language': 'en-US,en;q=0.5',
    #     'Connection': 'keep-alive',
    #     'Upgrade-Insecure-Requests': '1',
    #     'Cache-Control': 'max-age=0'
    # })
    #
    # tries = 0
    # connected = False
    # while not connected:
    #     print(f"Sending request to {url}")
    #     try:
    #         response = requests.get(url, headers=headers, timeout=5).content
    #         soup = BeautifulSoup(response, "html.parser")
    #         print(f"Successfully connected! It took {tries} tries")
    #         connected = True
    #     except Exception as e:
    #         print(e)
    #         print(f"Try #{tries}: Failed to connect to site. Trying again...")
    #         tries += 1
    #
    #     time.sleep(random.randint(0, 10))
    #     return soup

def primary_function(url):
    print("Getting ready to scrape Craigslist Services")
    connected = False
    tries = 1
    while not connected:
        try:
            page = 0
            ending = f"search/bbb?s={page}"
            new_cur = url_getter(url+ending)
            pages = new_cur.find("span", {"class": "totalcount"}).text
            total_pages = int(pages)
            pages = (total_pages // 120) - 1
            num = 1
            attempt = 0
            while num < pages:
                print(f"Going to page {num} of Craigslist services")
                new_url = url + ending
                function0(attempt, new_url)
                num += 1
                page += 120

            connected = True

        except Exception as e:
            print(f'Failed to connect to Craigslist services page')
            print(e)
            tries += 1
            time.sleep(random.randint(0, 10))

def function0(page, cl_url):
    c1Attempts = 0
    connected = False
    while not connected:
        print(f"Grabbing all services on page {page}")
        try:
            # urlgetter
            craigslist_data = url_getter(cl_url)
            cl_links = craigslist_data.find_all('li', {"class": "result-row"})
            connected = True
        except:
            c1Attempts += 1
            print(f"Failed to grab services on {page}")

    function1(cl_links)

def function1(cl_posts):

    sh = google_sheets.sh
    sh2 = google_sheets.sh2

    print("Getting each service's header and url")
    for i in cl_posts:
        db_headers = sh.col_values(2)
        dup_headers = sh2.col_values(1)
        db_hdrs = db_headers + dup_headers
        listing_header = i.find('h3')
        hdr = listing_header.text
        link = listing_header.find('a')['href']
        time.sleep(1)
        # Eliminating duplicate posts off rip
        function2(sh, db_hdrs, hdr, link, sh2)

def function2(sh, db_hdrs, hdr, link, sh2):
    print(f"Checking if this is a duplicate: {hdr}")
    if hdr not in db_hdrs:
        print("This service is not a duplicate and is ready for scraping.")
        db_nums = sh.col_values(4)
        db_descriptions = sh.col_values(3)
        attempt = 0
        c2Attempts = 0

        # Getting description from craigslist service
        description = function3(attempt, c2Attempts, link)
        # We can also write similar functions to get: city, neighborhood, and type of services
        # has image
        # open to solicitation

        extra_data = find_nav_info(link)

        city = extra_data[0]
        neighborhood = extra_data[1]
        service_type = extra_data[3]

        solicit = solicitation(link)

        nums = re.findall('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
                          description)
        # may need their own separate function
        # make sure the len of the number is greater that 9
        # Do a little conversion here to convert these numbers into a unison format, helps remove duplicate numbers that have varying formatting

        time.sleep(1)
        # UPDATE db hdrs list
        sh2.insert_row([hdr], 2)
        # Eliminating duplicate numbers off rip
        company_info = [db_nums, db_descriptions, nums, description, link, hdr, sh, city, neighborhood, service_type, solicit]
        print("Extracted company information")
        print(company_info)

        print("")
        function4(db_nums, db_descriptions, nums, description, link, hdr, sh, city, neighborhood, service_type, solicit)

    else:
        print(f"This is a duplicate: {hdr}")

def function3(attempt, c2Attempts, link):
    connected = False

    # Getting company description
    while not connected:
        print("Locating company description")
        try:
            res = url_getter(link)
            textSect = res.find('section', {"id": "postingbody"})
            description = textSect.text.strip('\n').replace('\n', '')
            attempt += 1
            print("Company description extracted")
            connected = True

        except Exception as e:
            print("Failed to locate/extract company description")
            print(e)
            c2Attempts += 1

        return description

def function4(db_nums, db_descriptions, nums, description, link, hdr, sh, city, neighborhood, service_type, solicit):
    print("Duplicate checker stage 2")
    if nums == [] and description not in db_descriptions:
        print("Company is not a duplicate and will now be pushed to the database.")
        # UPDATE db nums desc list
        cl_data = [link, hdr, description, "", city, neighborhood, service_type, solicit]
        print(cl_data)
        sh.insert_row(cl_data, 2)
        time.sleep(1)

    elif nums == []:
        print("Company is not a duplicate and will now be pushed to the database.")
        cl_data = [link, hdr, description, "", city, neighborhood, service_type, solicit]
        print(cl_data)
        sh.insert_row(cl_data, 2)
        time.sleep(1)

    elif nums[0] not in db_nums:
        print("Company is not a duplicate and will now be pushed to the database.")
        cl_data = [link, hdr, description, nums[0], city, neighborhood, service_type, solicit]
        sh.insert_row(cl_data, 2)
        # UPDATE db nums list
        time.sleep(1)

    elif description not in db_descriptions:
        print("Company is not a duplicate and will now be pushed to the database.")
        cl_data = [link, hdr, description, "", city, neighborhood, service_type, solicit]
        print(cl_data)
        sh.insert_row(cl_data, 2)
        # UPDATE db nums list
        time.sleep(1)


def find_nav_info(url):
    nav_bar_info = url_getter(url)
    navbar = nav_bar_info.find("header", {"class": "global-header wide"})
    navcontainer = navbar.find("nav", {"class": "breadcrumbs-container"})
    nav_items = navcontainer.find_all("a")
    nav_data = []
    for i in nav_items:
        nav_data.append(i.text)

    return nav_data


def solicitation(url):
    solicit = url_getter(url)
    notice = solicit.find("ul", {"class": "notices"}).find("li").text
    agree = "n/a"
    try:
        if notice == "do NOT contact me with unsolicited services or offers":
            agree = "No"
        else:
            agree = "Yes"
    except Exception as e:
        print(e)

    return agree


