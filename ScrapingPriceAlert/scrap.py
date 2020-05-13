import requests
import re
from bs4 import BeautifulSoup
import smtplib


# request
url = "https://www.dealabs.com/groupe/informatique"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


# we retrieve the degree of each article in the current page
alldegree = soup.findAll("span", {"class": "cept-vote-temp"})


# retrieve the degree > threshold
def check_degree(hot_thresold):
    degree_list = [d.text for d in alldegree]
    converted_degree_list = []

    for degree in degree_list:
        extract_degree = re.findall('\d+', degree)
        if (len(extract_degree) > 0):
            extract_degree = int(extract_degree[0])
            print(extract_degree)
            converted_degree_list.append(extract_degree)

    for degree in converted_degree_list:
        if (degree > hot_thresold):
            send_email()
            break 


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # extended simple mail transfer protocol command sent by an email
    # to identify iterself when connecting to another email server to start
    # the process of sendig an email
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gaetan.verdinpol@gmail.com', 'wohmersychenpiju')

    subject = "Here is a hot deal in the informatic categorie!"
    body = "Check this dealabs page : https://www.dealabs.com/groupe/informatique" 

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'gaetan.verdinpol@gmail.com',
        'gaetan.verdin-pol@gadz.org',
        msg
    )

    print('Email has been sent')
    server.quit()
    

check_degree(90)




"""
USELESS FOR NOW

for degree in alldegree:
    print(degree.get_text())
    print(len(degree.get_text()))
    try:
        print(int(degree.get_text())) 
    except:
        print("cannot be converted to an int", degree.get_text())
"""