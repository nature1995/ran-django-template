
# ran-django-template
[![python3.5](https://img.shields.io/badge/python-3.5-red.svg)]()
[![python3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)]()
[![python3.7](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![django2.1.5](https://img.shields.io/badge/django-2.1.5-orange.svg)]()
[![Build Status](https://travis-ci.com/nature1995/ran-django-template.svg?token=ihxd9jwdJ367UvYy3j9G&branch=master)](https://travis-ci.com/nature1995/ran-django-template)

Author: Ziran Gong

# Preview
http://ranxiaolang.com

![image](https://github.com/nature1995/ran-django-template/raw/master/images/preview.png)

# Compatibility
The codes are tested using Travis-CI platform with django 2.1.5 and Python 3.5, 3.6, 3.6-dev, 3.7, 3.7-dev.

# Requirements
The code requires [Python 3.x](https://www.python.org/download/releases/3.6/), as well as the following python libraries: 

* numpy
* Pillow
* django
* cryptography
* django-allauth  0.37.1
* django-widget-tweaks  1.4.3
* pip  18.0
* qrcode  6.0
* setuptools  40.4.3
* djangorestframework
* django-filter
* markdown
* requests

Those modules can be installed using: `pip3 install xxx` or `pip install xxx`.

# How to run it
```
git clone https://github.com/nature1995/ran-django-template.git
```
```
cd ran-django-template
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Access the web page though this link: http://127.0.0.1:8000/

**Admin Account**

``` 
python manage.py createsuperuser

username: ranxiaolang
email: YOUR EMAIL  
password: ranxiaolang  
```
Access the web page though this link: http://127.0.0.1:8000/admin

**Django Restframework**

Access the web page though this link: http://127.0.0.1:8000/iot/

# License

This software is licensed under the GNU General Public License v3.0 License. For more information, read the file `LICENSE`.

It need send a email to gzr2008@vip.qq.com and just can be used for non-business projects.

