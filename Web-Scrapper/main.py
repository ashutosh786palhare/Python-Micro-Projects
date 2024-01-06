import re
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def crawl(url, num, done_list, crawl_list, email_list, filt):
    ul = urlparse(url)
    base_url = ul.scheme + '://' + ul.netloc
    
    if num <= 0:
        return email_list
    
    done_list.append(url)
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
        })
        page = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(soup))
        numbers = re.findall(r'[@\s][69]\d{3}[-\s]?\d{4}[\s\.]', str(soup))
        
        for email in emails:
            if not email.endswith(('png', 'jpg')) and email not in email_list:
                email_list.append(email)
                print(email)
                
        for number in numbers:
            number = re.sub('[^0-9]', '', number)
            if number not in email_list:
                email_list.append(number)
                print(number)
                
        ban = ['Login', 'login', 'css']
        for link in soup.find_all('a', href=True):
            link = link['href']
            if 'http' in link and not any(x in link for x in ban) and filt in link:
                if link not in done_list and link not in crawl_list:
                    crawl_list.append(link)
            elif not any(x in link for x in ban):
                if link.startswith('//'):
                    link = 'http:' + link
                elif link.startswith('/'):
                    link = base_url + link
                    if link not in done_list and link not in crawl_list and filt in link:
                        crawl_list.append(link)
        num -= 1
        if crawl_list:
            crawl(crawl_list.pop(0), num, done_list, crawl_list, email_list, filt)
        else:
            return email_list
    except Exception as e:
        print(f"Exception occurred: {e}")
    return email_list

if __name__ == "__main__":
    url = input("Enter URL: ")
    pages = int(input("Enter the number of pages to crawl: "))
    filt = input("Enter filter (optional): ") or '.'
    
    if 'http' not in url:
        url = 'http://' + url
    
    emails = crawl(url, pages, [], [], [], filt)
    print("Emails and phone numbers collected:")
    print(emails)
