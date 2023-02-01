# Third party packages:
# DJANGO OAUTH TOOLKIT,JSON WEB TOKEN AUTHENTICATION,HAWK HTTP AUTHENTICATION,DJOSER,DJANGO-REST-AUTH/dj-rest-auth,django-rest-framework-social-oauth2,django-rest-knox,drfpasswordless
# JSON Web Token(JWT)
# JSON Web Token is a fairly new standard which can be used token based authentication.Unlike the built-in token authentication scheme,JWT Authentication doesn't need to use a database validate to validate a token.
# https://jwt.io/

# Simple JWT
# Simple JWT provides a JSON web token authentication backend for the django rest framework .It aims to cover the most common use cases of JWT by offering a conservative set of default features.It also aims to be easily extensible in case a desired feature is not present.
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest.

# How to install simple jwt
# pip install djangorestframework-simplejwt

# Configure simple JWT
# global
# settings.py
# REST_FRAMEWORK={
# "DEFAULT_AUTHENTICATION_CLASSES":("rest_framework.authentication.JWTAuthentication",)}

# urls.py
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# urlPatterns=[
#     path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair').
#     path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh')
# ]
# You can also include a route for simple JWT's tokenverifyview if you wish to allow api users to verify HMAC-signed tokens without access to your signing key.
# urls.py
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
# urlPatterns=[
#     path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair').
#     path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
#     path('verifytoken/',TokenVerifyView.as_view(),name='token_verify')
# ]

# JWT DEFAULT SETTINGS
# from datetime import timedelta
# SIMPLE_JWT={
    # 'ACCESS_TOKEN_LIFETIME':timedelta(minute=5),
    # 'REFRESH_TOKEN_LIFETIME':timedelta(days=1),
    # 'ROTATE_REFRESH_TOKENS':False,
    # 'BLACKLIST_AFTER_ROTATION:True,
    # 'ALGORITHM':'HS256'
    # 'SIGNING_KEY':settings.SECRET_KEY,
    # 'VERIFYING_KEY':None,
    # 'AUDIENCE':None,
    # 'ISSUSER':None,
    # 'AUTH_HEADER_TYPES':('Bearer',),
    # 'USER_ID_FIELD':'id,
    # 'AUTH_TOKEN_CLASSES':('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM':'token_type',
    # 'JTI_CLAIM':'jti',
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM':'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME':timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME':timedelta(days=1),
    # }
# ACCESS_TOKEN_LIFETIME-A datetime.timedelta object which specifies how long access tokens are valid.
# REFRESH_TOKEN_LIFETIME-A datetime.timedelta object which specifies how long refresh tokens are valid.

# USE JWT
# GET Token
# http POST http:127.0.0.1:8000/gettoken/ username='user1' password='geekshows'
# verify token
# http POST http:127.0.0.1:8000/verifytoken/ token="bdkjbfsbk8888888888888888888uskbka"
# refresh token
# http POST http:127.0.0.1:8000/refreshhtoken/ refresh="bdkjbfsbk8888888888888888888uskbka"



# }
#  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1MTQwMjcxLCJpYXQiOjE2NzUxMzk5NzEsImp0aSI6ImYzNDNlZmRlZGUxNDRjMTNiNjIxNTI5N2ZhNTdjZjRkIiwidXNlcl9pZCI6Mn0.OJqI3awrwkPgr8KIi5j14MQpEP2-MVlAwuZ0nD66Qko",
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NTIyNjM3MSwiaWF0IjoxNjc1MTM5OTcxLCJqdGkiOiI2MWI5MTJkYTQyMDA0MjIwOWY5MDIxZTQyOWI5YzU4ZSIsInVzZXJfaWQiOjJ9.F7bWBTvTQ5nLkNoduuQn2YyEbMPl_5eWbJDjupiTi20"
# }

# USE HTTPIE
# http http://127.0.0.1:8000/studentapi/(GET REQUEST)
# http http://127.0.0.1:8000/studentapi/ 'Authorization:bearer 62626626mdmd2222'(GET REQUEST with jwttoken)
# http -f POST http://127.0.0.1:8000/studentapi/ name=jay roll=105 city=dhanbad 'Authorization:bearer 2662626nndhdh222'(POST REQUESTING SUBMITTING FORM)
# http PUT http://127.0.0.1:8000/studentapi/4/ name=jay roll=105 city=dhanbad 'Authorization:bearer 2662626nndhdh222'(PUT REQUESTING SUBMITTING FORM)
# http DELETE http://127.0.0.1:8000/studentapi/3/'Authorization:bearer 2662626nndhdh222'(DELETE REQUESTING SUBMITTING FORM)
