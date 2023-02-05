# Throttling is similar to permission,in that it determines if a request should be authorized.Throttles indicate a temporary state and are used to control the rate of requests that client can make to an api.
# Your api might have a restrictive throttle for unauthenticated requests,and a less restricative throttle for unauthenticated requests.
# The default throttling policy may be set globally,using the
# DEFAULT_THORTTLE_CLASSES AND DEFAULT_THROTTLE_RATES settings.For example.
REST_FRAMEWORK={
    'DEFAULT_THROTTLE_CLASSES':[
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',

    ],
    'DEFAULT_THROTTLE_RATES':{
        'anon':'100 day',
        'user':'1000/day'
    }   
 }
#  Note The rate descriptions used in default_throttle_rates may include second,minute,hour or day  as the throttle period.


# AnonRateThrottle:
# The AnonRateThrottle will only ever throttle unauthenticated users.The IP Address of the incoming requests is used to generate a unique key to throttle against.
# The allowed request rate is determined from one of the following (in order of preference)
# The rate property on the class,which may be provided by overriding AnonRateThrottle and setting the property.
# The DEFAULT_THROTTLE_RATES['anon'] setting.
# AnonRateThrottle is suitable if you want to restricate the rate of requests from unknown sources.



# UserRateThrottle
# The UserRateThrottle will throttle users to agiven rate of requests  across the api.
# The user id is used to generate a unique key to throttle against.Unauthenticated requests will fall back to using the IP address of the incoming requests to generate a unique key to throttle against.
# The allowed request rate is determined from one of the following (in order of preferences)
# The rate property on the class, which may be provided by overriding UserRateThrottle and settings the property.
# The DEFAULT_THROTTLE_RATES["user"] setting.

# ScopeRateThrottle
# The ScopeRateThrottle class can be used to restrict access to specific parts of the API.
# This throttle will only be applied if the view that is being accessed includes a throttle_scope property.The unique throttle key will .
# then be formed by concatenating the 'scope' of the requests with the unique user id or IP address.