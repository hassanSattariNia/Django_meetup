multiple smaller packages called apps => to create our website in Django


python manage.py => Django command line


python manage.py startapp => for add an app (module) 
for example we use 
python manage.py startapp meetup to create app with meetup name
Url AND Views


**Template**
inside every app is default folder for tempates => if you want more directory or you want change it you can set in settings
another point is inside every app/template we create another folder using name of app because at finally every templates collect from all apps and is for separate template for different apps that have simmilar templates 

**statics**
all static files like 
css, 
scrips for javascript codes
images

**danamic-data-from-view-to-template**
<p>{{ meetups.0.title}}</p>

**daynamic-path-segment-in-urls**
path('meetups/<slug:meetup_slug>',views.meetup_details)#using dynamic path segment

we can define name or tag for urls 

**base-template**
you can define a base template once and use it in pages that you want

one example
    the block section can be overwritten 
    <title> {% block title %} My Meetups(Default Value) {% endblock %}</title>

**include**
include tage - path of html file - with keyword - name of variable used in template used with values of them
        {% include 'meetups/includes/meetup-item.html' with title=item.title location=item.location slug=item.slug %}


**images-upload-urls**
in settings
MEDIA_ROOT = BASE_DIR/'uploads'
MEDIA_URL ='/files/'

and also you need to install pillow package 

**/admin-area**
for manage a model in adminstration area have to register that model inside admin.py
