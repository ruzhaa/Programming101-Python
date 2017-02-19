from bs4 import BeautifulSoup
import requests
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import urlparse


def evaluate_path(item, path):
    beautiful_path = "http://"
    nachalo = urlparse(item)
    o = urlparse(path)
    print(o)
    if o.netloc is '':
        beautiful_path += nachalo.netloc
    else:
        beautiful_path += o.netloc

    if o.path is '':
        if nachalo.path is '':
            # print(nachalo.path)
            beautiful_path += '/'
        beautiful_path += nachalo.path
    else:
        beautiful_path += o.path
    if o.params is '':
        beautiful_path += nachalo.params
    else:
        beautiful_path += o.params
        beautiful_path += '?'
    if o.query is '':
        beautiful_path += nachalo.query
    else:
        beautiful_path += o.query
    if o.fragment is '':
        beautiful_path += nachalo.fragment
    else:
        beautiful_path += o.fragment
    # print(beautiful_path)
    return beautiful_path

engine = create_engine("sqlite:///links.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

start = 'http://register.start.bg/'
session.add(HTTP_links(http_link_name=start))

list_column = session.query(HTTP_links.http_link_name).all()

for item in list_column:
    try:
        response = requests.get(url=item[0], timeout=10)
        html_doc = response.content
    except requests.exceptions.ConnectionError:
        print("Connection refused")

    soup = BeautifulSoup(html_doc, 'html.parser')

    for link in soup.find_all('a'):
        beauty_link = ""
        current_link = link.get('href')
        # print(new_link)
        if current_link is not None and '#' not in current_link:
            # print(item[0])
            new_link = evaluate_path(item[0], current_link)
            new_current_link = HTTP_links(http_link_name=new_link)

            list_column.append((new_link,))
            session.add(new_current_link)

    session.commit()

# evaluate_path('http://register.start.bg/', '/link.php?id=54959')
