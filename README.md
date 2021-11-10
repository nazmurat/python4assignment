# python4assignment
## Title
News and blogs for cryptocurrency

##
Team Members

Tulep Zarina
Ali Kaysarbek
## Installation
## PyPI
```bash
Flask
Flask_sqlalchemy
JWT
flaskweb
pip install -U selenium
pip install bs4
```
## Usage
```bash
Import those libraries
Generate and set SECRET_KEY
Set SQLALCHEMY_DATABASE_URI as postgreSQL or sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:port/database_name'
```
## Example
```bash
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from flaskblog import db
from flaskblog.models import Users
db.create_all()
```
```bash
url = 'https://coinmarketcap.com/currencies/' + cryptoName + '/news/'
```

## Output
Enter the cryptocurrency name and press button check.
