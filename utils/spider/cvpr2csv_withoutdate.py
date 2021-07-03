# coding:utf-8
import requests
from bs4 import BeautifulSoup

def main():
    root_link = 'http://openaccess.thecvf.com/'
    conference = 'WACV'         # conference name
    year = 2020                # conference year
    filename = conference + str(year) + '.csv'
    with open(filename, 'w') as f:
        f.write('id, title, authors, conference, year, download_link, abstract\n')
    from_page(root_link=root_link, conference=conference, year=year, filename=filename)

def from_page(root_link, conference, year, filename):
    url = root_link + conference + str(year)
    r = requests.get(url)
    id = 1
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        for ptitle in soup.find_all('dt', class_='ptitle'):
            title = ptitle.a.string
            link = ptitle.a['href']
            link = root_link + link
            r1 = requests.get(link)
            soup1 = BeautifulSoup(r1.text, "html5lib")
            ab = soup1.find('div', id='abstract')
            if ab.string:
                abstract = ab.string
            elif ab.nn:
                abstract = ab.contents[0] + ab.nn.string
            abstract = abstract.replace('\n', '')
            abstract = abstract.replace('"', '""')
            link = link.replace('html/', 'papers/')
            link = link.replace('.html', '.pdf')
            authors = []
            dd = ptitle.next_sibling.next_sibling
            for form in dd.find_all('form'):
                authors.append(form.a.string)
            for author in authors:
                author = author.replace('"', '""')
            write_row(filename, id, conference, year, authors, title, link, abstract)
            id += 1
        print('Successfully completed.')
    else:
        print("ERRORS occur!")

def write_row(csv_path, id, conference, year, authors, title, link, abstract):
    '''
    write data into data.csv
    '''
    with open(csv_path, 'a', encoding = "utf-8") as data:# id, title, authors, conference, year, download_link, abstract
        data.write(','.join([str(id), '"' + title + '"', '"' + ','.join(authors) + '"',conference, str(year), link, '"' + abstract + '"']) + '\n')
    print("Completed Writing: {}: {:30}".format(id, title))
if __name__ == "__main__":
    main()
