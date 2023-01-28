# WHY USE AUTHENTICATIONS AND PERMISSIONS
# Currently our API doesn't have any restrications on who can edit or delete data.
# We'd like to have some more advanced behaviour in order to make sure that:
# Data is always associated with a creator.
# Only authenticated users may create data.
# only the creator of data may update or delete it.
# unauthenticated requests should have full-read only process.

# AUTHENTICATIONS
# authentications is the mechanism of associating an incoming requests with a set of identifying credentials,such as the user the request came from,or the token it was signed with.The permission nad throttling policies can then use those credentials to determine if the request should be permitted.
# Authentication is always run at very start of the view,before the permissions and throtting checks occurs,and before any other code is allowed to proceed.
# Rest framework provides  a number of authentication schemes out of the box,and also allows you to implement custom schemes.
# BASIC AUTHENTICATION,SESSION AUTHENTICATION,CUSTOM AUTHENTICATION,TOKEN AUTHENTICATION,REMOTEUSERAUTHENTICATION.

# BASIC AUTHENTICATION
# this authentication scheme uses HTTP basic authentication,signed against a user's name and password.
# basic authentication is generally only appropriate for testing.
# if successfully authenticated,basicauthentication provides the following credentials.
# request.user will be a django user instance.
# request.auth will be none.
# Unauthenticated responses that are denied permissions will result in an HTTP 401
# Unauthorized responses with an appropriate WWW-Authenticate header.
# eg-www-authenticate:basic realm="api"
# n.b:
# if you use basicauthentication in production you must ensure that your api is only available over https.
# you should ensure that your api clients will always re-request the username nad password at login,and will never store those details to persistent storage.

# PERMISSIONS
# permissions are used to grant or deny access for different classes of users to different parts of the api.
# permissions are always checks runsat very start of the view,before any other code is allowed to proceed.
# permission checks will typically use the authentication informationin the request.user and request.auth properties to determine if the incoming request should be permitted.
# PERMISSION CLASSES 
# permissions in rest framework are always defined as a list of permission classes.
# ALLOWANY,ISAUTHENTICATED,ISADMINUSER,ISAUTHENTICATEDORREADONLY,DJANGOMODELPERMISSIONS,DJANGOMODELPERMISSIONSORANREADOLY,DJANGOOBJECTPERMISSIOS,CUSTOM PERMISSIONS
# AllowAny:
# the allowany permission classes will allow unrestricated access,regardlessof of it the request was authenticated or unauthenticated.
# This permission is not strictly required,since you can achieve the same result by using an empty list or tuple for the permissions settings,but you may find it useful to specify this class becuase it makes intention explicit.
# IsAuthenticated:
# The isauthenticated permissions class will deny permission to any unauthenticated user,and allow permission otherwise.
# This permission is suitable if you want your api to only be aceessible to registered users.
# IsAdminUser:
# The isadminuser permission class will deny permission to any user,unless user.is_staff is truein which case permission will be allowed.
# This permission is suitable if you want your api to only be accessible to a subset of trusted administrators.



# SESSION AUTHENTICATION
# This authentication scheme uses django's default session backend for authentication.Session authentication is appropriate for AJAX Clients 
# that are running in the same session context as your website.
# if successfully authenticated,session authenticated provides the following credentials
# request.user will be a django user insatnce.
# request.auth will be none.
# Unauthenticated responses that are denied permission will result in an HTTP 403 Forbidden response.
# if you are using an AJAX Style api with sessionauthentication,you will need to make sure you include a valid csrf token for any "unsafe" http method calls,sucha s PUT,PATCH,DELETE,UPDATE requests.
# Permissions
# permissions are used to grant or deny access for different classes of users to different parts of the api.
# permissions are always checks runsat very start of the view,before any other code is allowed to proceed.
# permission checks will typically use the authentication informationin the request.user and request.auth properties to determine if the incoming request should be permitted.
# PERMISSION CLASSES 
# permissions in rest framework are always defined as a list of permission classes.
# ALLOWANY,ISAUTHENTICATED,ISADMINUSER,ISAUTHENTICATEDORREADONLY,DJANGOMODELPERMISSIONS,DJANGOMODELPERMISSIONSORANREADOLY,DJANGOOBJECTPERMISSIOS,CUSTOM PERMISSIONS
# AllowAny:
# the allowany permission classes will allow unrestricated access,regardlessof of it the request was authenticated or unauthenticated.
# This permission is not strictly required,since you can achieve the same result by using an empty list or tuple for the permissions settings,but you may find it useful to specify this class becuase it makes intention explicit.
# IsAuthenticated:
# The isauthenticated permissions class will deny permission to any unauthenticated user,and allow permission otherwise.
# This permission is suitable if you want your api to only be aceessible to registered users.
# IsAdminUser:
# The isadminuser permission class will deny permission to any user,unless user.is_staff is truein which case permission will be allowed.
# This permission is suitable if you want your api to only be accessible to a subset of trusted administrators.
# IsAuthenticatedOrReadOnly:
# The IsAuthenticatedOrReadOnly will allow authenticated users to perform any request.Requests for unauthorized users only be permitted if the
# request method is one of the "safe" methods;"GET",HEAD OR OPTIONS.
# This permission is suitable if you want to your api to allow read permissions to anonymouus users,and only allow write permissions to authenticated users.
# DjangoModelPermissions:
# This permission class ties into Django's standard django.contrib.auth model permissions.This permissions must only be applied to views that 
# have a queryset property set.Authorization will only be granted if the user is authenticated and has the relevant model permission assigned.
# POST requests require the user to have the add permission on the model.
# PUT and patch requests require the user to have the change permissions on the model.
# DELETE requests require the user to have the delete permissions on the model.
# The default behaviour can also be overridden to support custom model permissions.
# for example,you might want to include a view model permission for get requests.
# To use custom model permissions,override DjangoModelPermissons and set the params_map property.
# DjangoModelPermissionsOrAnonReadOnly
# Similar to DjangoModelPermissionsOnAnReadOnly,but also allows unauthenticated users to have read-only access to the api.
# MODELOBJECTPERMISSIONS
# CUSTOMPERMISSIONS
# To implement a custom permissions,override BasePermissions and implement either,or both ,of the following methods:
# has_permissions(self,request,view)
# has_object_permissions(self,request,object,view)
# The method should return True if the request should be granted access,and false otherwise.
# Custompermissions.py
# class MyPermission(BasePermission):
#     def has_permission(self,request,view):
# Third Party Packages:DRF-ACCESS-POLICY,Composed Permissions,REST Condition,DRY REST PERMISSIONS,DJANGO REST FRAMEWORK ROLES,DJANGO REST FRAMEWORK API KEYS
# DJANGO REST FRAMEWORK ROLE FILTERS
# DJANGO REST FRAMEWORK PSQ
