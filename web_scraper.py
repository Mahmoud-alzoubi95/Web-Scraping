from bs4 import BeautifulSoup
import requests


def get_citations_needed_count(URL):
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.findAll(text='citation needed')
    return len(soup)



def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citation = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    result = ''
    # counter = 0
    for i  in citation:
        result+= f"{i.parent.text}\n"
        #     counter = 1}'

        # if counter == 0:
        #     li.append(i.parent.text)
        #     counter = 1
        # else:
        #     if i.parent.text in li:
        #         continue
        #     else:
        #         li.append(i.parent.text)
        #         counter = counter + 1
        # print(li[counter-1])
    return result


URL ="https://en.wikipedia.org/wiki/History_of_Mexico"
print("The citation needed =",get_citations_needed_count(URL))
print(get_citations_needed_report(URL))
