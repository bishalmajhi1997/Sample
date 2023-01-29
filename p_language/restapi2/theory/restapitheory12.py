# TOKENAUTHENTICATION
# This authentication scheme uses  a simple-token based HTTP authentication scheme.Token authentication is appropriate for client-server setups,such as native-desktop and mobile.To use the tokenauthentication scheme you will need to configure the authentications classes to include tokenauthentication,additionally include rest_framework.authtoken in your installed_apps settings:INSTALLED APPS=[.... 'rest_framework.authtoken']
# note:Make sure to run manage.py migrate after changing your settings.The rest_framework app provides Django database migrations.
# If successfully authenticated,TokenAuthentication provides the following credentials
# request.user will be Django User Instance.
# request.auth will be a rest_framework.authtoken.models.Token instance
# unauthenticated responses that are denied permission will result in an HTTP 401 .
# unauthorized response with an appropriate www.authenticate header.For example 
# www-authenticate:token
# the http command line tool may be useful for testing token authenticated apis.for example
# https:127.0.0.1:8000/studentapi/'authorization:token'
# '8772727727bdbdbdedjjj'
# note:if you use tokenauthentication in production you must ensure that your api is only available over https.

# Generate token:
# Using Django application
# Using DJango manage.py command
# python manage.py drf_create_token<username>.This command will return API token for the given user or creates a token.If token does't exists for user.
# By exposing an api endpoint.
# Using singnals.

# How client can ask/create token.
# When using tokenauthentication ,you may want to provide a mechanism for clients to obtain  a token given the username and password.
# rest_framework provides a built_in view to provide the behaviour .To use it,add the obtain_auth_token view to your URLconf.
# from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns=[
# path('gettoken/',obtain_auth_token)]
# The obtain_auth_token view will return  a json response when valid username and password fields are posted to the view using from data or json.
# http POST http://127.0.0.1:8000/gettoken/username="name" password="pass"
# {'token':'9299999999999hhshdh8882'}
# It also generates token if the token is not generated for the provided user.

# HTTPIE
# Httpie(pronounced aitech-tee-tee-pie) is a command line HTTP client.Its goal is to make CLI interaction with web services as human-friendly as possible.It provides a simple http command that allow for sending arbitary HTTp requests using a simple and natural syntax,and display colorized output.HTTPie can be used for testing,debugging,and generally interacting with HTTP servers.
# Syntax:http [flags] [METHOD] URL [ITEM[ITEM]]
# How to install
# pip install httpie

# USE HTTPIE
# http http://127.0.0.1:8000/studentapi/(GET REQUEST)
# http http://127.0.0.1:8000/studentapi/ 'Authorization:Token 62626626mdmd2222'(GET REQUEST with token)
# http -f POST http://127.0.0.1:8000/studentapi/ name=jay roll=105 city=dhanbad 'Authorization:Token 2662626nndhdh222'(POST REQUESTING SUBMITTING FORM)
# http PUT http://127.0.0.1:8000/studentapi/4/ name=jay roll=105 city=dhanbad 'Authorization:Token 2662626nndhdh222'(PUT REQUESTING SUBMITTING FORM)
# http DELETE http://127.0.0.1:8000/studentapi/'Authorization:Token 2662626nndhdh222'(DELETE REQUESTING SUBMITTING FORM)



# CUSTOM AUTHENTICATION
# To implement a custom authentication scheme,subclass baseauthentication and override the the authenticate(self,request) method.
# The method should return  a two-tuple of(user,auth)if authentication succeeds or None otherwise.
# http://127.0.0.1:8000/student/1/?username=bishalmajhi1997@gmail.com(put)


