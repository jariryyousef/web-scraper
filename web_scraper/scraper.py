import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
def get_citations_needed_count(url):
    
    countter = BeautifulSoup(requests.get(url).content
    , "html.parser").find_all(text = "citation needed")
    
    return len(countter)

# def get_citations_needed_report(url):
#     content = []
#     countter = BeautifulSoup(requests.get(url).content
#     , "html.parser").find_all("p")
    
#     for p in countter:
#         citations_needed=p.find_all('a',title='Wikipedia:Citation needed')
#         for citation in citations_needed:
#             content.append(p.text)
#     return(content)


def get_citations_needed_report(url):
    
    
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    result = soup.find_all('sup', class_='Inline-Template')
    content = []
    for p in result:
        content.append(p.parent.text.strip())
        
    return '\n'.join(content)
