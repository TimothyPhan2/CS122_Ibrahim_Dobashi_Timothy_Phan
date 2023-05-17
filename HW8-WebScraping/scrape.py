# ----------------------------------------------------------------------
# Name:        scrape.py
# Purpose:     Homework 8 - practice web scraping
#
# Author(s): Timothy Phan & Ibrahim Dobashi
# ----------------------------------------------------------------------
"""
Scrapes information from multiple webpages and saves it to a csv file

This program scrapes information from multiple webpages, saving the info
to a csv file. The urllib module is used to read the base url that is
"https://sjsu.edu/people/" which contains links to multiple webpages.
The beautifulsoup module is then used to parse the url bytes as
html text, so we can begin scraping info from it. We first get all the
people links that are on the index webpage and store them into a list.
After, we extract the name,email,phone number and education of each
person using the people links list and save to a csv file on the user's
computer
"""
import urllib.request
import urllib.error
import urllib.parse
import bs4
import re
import sys
import os

# Enter your constants here
faculty_url = "https://sjsu.edu/people/"


def read_url(url):
    """
    Open the given url and return the corresponding soup object.
    :param url:(string) - the address of the web page to be read
    :return: (Beautiful Soup object) corresponding Beautiful Soup
    object or None if an error is encountered.
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            url_bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    except Exception as other_err:  # safer on the web
        print(f'Other error with url: {url}\n{other_err}')
    else:
        soup = bs4.BeautifulSoup(url_bytes, 'html.parser')
        return soup


def get_people_links(url):
    """
    Read the given url and return the relevant referenced links.
    :param url:(string) - the address of the faculty index page
    :return: (list of strings) - the relevant people links
    """
    # Enter your code below and remove the pass statement
    soup = read_url(url)

    pattern = r'/people/+\S+'
    people_links = [urllib.parse.urljoin(url,
                                         anchor.get('href', None))
                    for anchor in soup('a') if
                    re.match(pattern, anchor.get('href', None))]

    return people_links


def extract_name(soup):
    """
    Extract the first and last name from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: a tuple of strings representing the first and last names
    """
    # Enter your code below and remove the pass statement

    if soup is not None:
        h1 = soup('h1')
        if len(h1) > 0:
            if "," in h1[0].get_text():
                names = h1[0].get_text().strip().split(', ')
                name = names[0].strip(), names[1].strip()
            else:
                names = h1[0].get_text().strip().split()
                name = names[-1].strip(), names[0].strip()

            return name

    return "", ""


def extract_email(soup):
    """
    Extracts the faculty email from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: string
    """
    # Enter your code below and remove the pass statement
    if soup is not None:
        pattern = re.compile(r'\S+@\S+\.\S+(?: \(.+\))?', re.IGNORECASE)
        emails = soup.find_all(string=pattern)
        visible = [email.get_text() for email in emails if email.get_text()]
        if visible:
            return visible[0].strip()
    return ''


def extract_phone(soup):
    """
    Extracts the faculty phone number from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: string
    """
    pattern = r"\(?\d{3}\)?\W?\d{3}\W*\d{4}"
    if soup is not None:
        regex = re.compile(r'telephone|telephone:', re.IGNORECASE)
        phone_header = soup.find_all(string=regex)
        for phone in phone_header:
            phone_header_next = phone.find_next()
            if phone_header_next:
                if re.search(pattern, phone_header_next.get_text()):
                    match = re.search(pattern, phone_header_next.get_text())
                else:
                    phone_text = phone_header_next.find_next()
                    match = re.search(pattern, phone_text.get_text())
                if match:
                    return match.group()
    return ''


def extract_education(soup):
    """
    Extracts the faculty education from the soup object
    :param soup: (Beautiful Soup object) representing the faculty/staff
                web page
    :return: string
    """
    # Enter your code below and remove the pass statement
    if soup is not None:
        education_header = soup.find("h2", string="Education")
        if education_header:
            if education_header.find_next().name == "ul":
                result = education_header.find_next().find("li").get_text()
            else:
                result = education_header.find_next().get_text()
            results = result.replace(',', '-').replace('\n', ' ').strip()

            return results

    return ''


def get_info(url):
    """
    Extract the information from a single faculty/staff web page
    :param url: (string) the address of the faculty/staff web page
    :return: a comma separated string containing: the last name,
    first name, email, phone and education
    """
    # Enter your code below and remove the pass statement
    # 1.  Call read_url to get the soup object
    # 2.  Call extract_name, extract_email, extract_phone, and
    #     extract_education to get the relevant information
    # 3.  Combine the info in one comma seperated string and return it.

    soup = read_url(url)
    name = extract_name(soup)
    email = extract_email(soup)
    phone = extract_phone(soup)
    education = extract_education(soup)

    return name, email, phone, education


def harvest(url, filename):
    """
    Harvest the information starting from the url specified and write
    that information to the file specified.
    :param url: (string)the main faculty index url
    :param filename: (string) name of the output csv file
    :return: None
    """
    # Enter your code below and remove the pass statement
    # 1.  Call get_people_links to get the relevant links from the url
    # 2.  Open the file with a context manager
    # 3.  Write the column headers to the file
    # 4.  Iterate over the links and call get_info on each one.
    # 5.  Write that information in the file
    people_links = get_people_links(url)

    with open(filename, 'w', newline='', encoding='UTF-8') as file:
        file.write('Last Name,First Name,Email,Phone Number,Education\n')

        for link in people_links:
            info = get_info(link)
            if len(info[0]) > 1 and info[0][0] != '':
                file.write(f'{info[0][0]},{info[0][1]},{info[1]},{info[2]},'
                           f'{info[3]}\n')


def main():
    # Enter your code below and remove the pass statement
    # Check the command line argument then call the harvest function

    if len(sys.argv) != 2:
        print('Error: Invalid number of arguments')
        print('Usage: scrape.py filename')
    else:
        filename = sys.argv[1]

        if not os.path.splitext(filename)[1] == ".csv":
            print('Please specify a csv filename')
            return
        harvest(faculty_url, filename)


if __name__ == '__main__':
    main()

