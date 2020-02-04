
# ran-django-template

<div align="center">
    <a href=""><img src="https://s2.ax1x.com/2019/03/24/AYmuIf.png" width="100" hegiht="100"/></a>
</div>
<br>

[![python3.5](https://img.shields.io/badge/python-3.5-red.svg)]()
[![python3.6](https://img.shields.io/badge/python-3.6-brightgreen.svg)]()
[![python3.7](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![django3.0](https://img.shields.io/badge/django-3.0.0-green.svg)]()
[![Build Status](https://travis-ci.com/nature1995/ran-django-template.svg?token=ihxd9jwdJ367UvYy3j9G&branch=master)](https://travis-ci.com/nature1995/ran-django-template)

## Feature
For Site
- [x] Create Django web server in local
- [x] Gallery and carousel control in home page
- [x] Beautify site admin interface
- [x] Restful API for IOT control
- [x] Oauth2.0 for third party account login，such as: Github
- [x] QR code generator
- [x] PC, Mobile auto adaptation
- [x] Support [Font awesome](https://fontawesome.com/), [django-jet](http://jet.geex-arts.com/), [Bootstrap](https://getbootstrap.com/), [Animate.css](https://daneden.github.io/animate.css/)

For Blog
- [x] Rich text editor
- [x] Article management and counting, including adding, deleting and editing
- [x] Tag management, including adding, deleting and editing
- [x] Classified management, including adding, deleting and editing
- [x] Read more


## Documentation

#### Add INSTALLED_APPS setting:
```
    INSTALLED_APPS = [
		'jet.dashboard', #  before your django admin
		'jet',	#  before your django admin
	    	'apps.gallery.apps.GalleryConfig',
		'allauth',
		'allauth.account',
		'allauth.socialaccount',
		'allauth.socialaccount.providers.github',
		'myauth',
		'widget_tweaks',
		'werkzeug_debugger_runserver',
		'django_extensions',
		'rest_framework',
		'apps.myapp',
		'apps.blogs',
		'apps.qrcreate',
		'apps.blog',    # Blog for new version
		'django_summernote',
    ]
```

#### How to run it
```
git clone https://github.com/nature1995/ran-django-template.git
```
```
cd ran-django-template
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Access the web page though this link: http://0.0.0.0:8000/

## Compatibility

The codes are tested using Travis-CI platform with django 2.1.5 and Python 3.5, 3.6, 3.7. 
Django\Python  	| 3.5 | 3.6 | 3.7 
--------------- | --- | --- | ---
2.0.x   	|  *  |  *  |  *
2.1.x    	|  *  |  *  |  *
3.0.0		|  *  |  *  |  *  

**Notice:**

1. Because the jet admin do not support django==3.0.0. Please remove jet in setting.py and urls.py, if you would like to use django == 3.0.0

2. Django 2.1.x need to using the following change:**

If you have the ERROR message with `render() got an unexpected keyword argument 'renderer'；`, 
please find Python folder: `\lib\site-packages\django\forms\boundfield.py`. 
Then, comment the as_widget, line 93, like the follow:

```
return widget.render(
	name=self.html_initial_name if only_initial else self.html_name,
	value=self.value(),
	attrs=attrs,
	# renderer=self.form.renderer,
)
```
## Demo

Web Page: https://ranxiaolang.com or https://www.zran.xyz

![image](https://github.com/nature1995/ran-django-template/raw/master/images/preview2.2.png)

<div>
<img src="https://s2.ax1x.com/2019/03/24/AYu7IP.png" width="820" height="400" alt="Result01.png" title="Result01.png" />
</div>
<br>
<div>
<img src="https://s2.ax1x.com/2019/03/24/AYuVEt.png" width="410" height="250" alt="Result01.png" title="Result01.png" />
<img src="https://s2.ax1x.com/2019/03/24/AYuAHI.png" width="410" height="250"  alt="Result03.png" title="Result03.png" />
</div>
<br>
<div>
<img src="https://s2.ax1x.com/2019/03/23/A8XvGD.png" width="270" height="550" alt="Result01.png" title="Result01.png" />
<img src="https://s2.ax1x.com/2019/03/23/A8XxRe.png" width="270" height="550" alt="Result03.png" title="Result03.png" />
<img src="https://s2.ax1x.com/2019/03/23/A8XjPO.png" width="270" height="550" alt="Result02.png" title="Result02.png" />  
</div>

## Site Admin installation

Add 'jet.dashboard' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'jet'):
```
INSTALLED_APPS = (
    ...
    'jet.dashboard',  # before your django admin
    'jet',  # before your django admin
    'django.contrib.admin',
    ...
)
```

Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):
before 'jet'):
```
urlpatterns = patterns(
    ...
    path(r'admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    ...
)
before 'jet'):
```
For Google Analytics widgets only install python package:
```
pip install google-api-python-client==1.4.1
```
Create database tables:
```
python manage.py migrate dashboard
# or
python manage.py syncdb
```
Collect static if you are in production environment:
before 'jet'):
```
python manage.py collectstatic
```

## Others

**Admin Account**  
``` 
python manage.py createsuperuser

username: ranxiaolang
email: YOUR EMAIL  
password: ranxiaolang  
```
Access the web page though this link: http://0.0.0.0:8000/admin

**Django Restframework**  
Access the web page though this link: http://0.0.0.0:8000/iot/

## TODO
- [ ] Add more social Oauth2.0
- [ ] Add comment
- [ ] Add site map

## Author

* **Ziran Gong** - [Web Page](http://ranxiaolang.com)

## License

This software is licensed under the GNU General Public License v3.0 License. For more information, read the file `LICENSE`.  
Just can be used for non-business projects.

