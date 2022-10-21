# 1.Django is a free and open source web framework.
# Django is used by many sites including pinterest,PBS,instagram,BitBucket,Mozila and more.
# Django is an excellent choice for any developer who wants to build modern,robust web application with a minimal amount of code.
# it is popular,under active development and thorougly battle tested by the largest websites in the world.
# 2.why django ?
# Ridiculously fast:Django was designed to help  developers take application from concept to completion  as quickly as possible.
# Reassuringly secure:Django takes security seriously and helps developers avoid many common security mistakes.
# Exceedingly scalable:Some of the busiest sites on the web leverage django's ability to quickly and flexible  scale.
# 3.create project:
# django-admin startproject helloworld 
# lets took at what startproject created:
# helloworld/
# manage.py
# helloworld/
# __init__.py
# settings.py
# urls.py
# wsgi.py
# The inner helloworld/directory.it's the python package for your project.it's the name.you will use to import anything inside it.(ex :hellowworlds.urls)
# __init__.py:an empty file that tells python that this directory should be considered a python package.
# settings.py:setting/configuration for this django project.
# urls.py:the url declarations for this django projects;a table of contents of your django-powered site.
# wsgi.py:an entry point for wsgi-compatible web servers to serve yor project.
# manage.py:this is a python script that we will use a lot.it will be associates with many commands as we build our web app.
# 4.create an app ?
# Django uses the conecpt of projects and apps to keep code learn and readable.A single Django project contains one or more  apps within it that all work together to power a web applications
# we need to create our first app which we will call pages.from the command line,quit the serverwith control+c.then use the startapp command
# python manage.py startapp pages
# 4.lets review what each new pages app file does:
# admin.py:is a configuration file for the built-in django app.
# apps.py: is a configurations for the app itself.
# migrations /keep track of any changes to our models.py file so our database and model.py stay in sync.
# models.py:is where we define our database models,which django automatically translates into database tables.
# test.py:is for our app-specific test.\
# views.py:is where we handle the request/response logic for our web app.

