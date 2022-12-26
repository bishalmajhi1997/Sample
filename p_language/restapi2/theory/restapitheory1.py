# An API is a software intermediary that allows two or more applications to talk to each other.
# API Types in term of Release Policies
# Private:it can be used within the organisation.
# Partner:It can be used within the business Partners
# Public:It can be used any third party developer.

# WEB API:
# An api,which is interface for web is called as WEB API
# It may consists of one or more endpoints to define request and response.

# How web api works ?
# Client makes HTTP request to API
# API will communicate to webapplications/database.
# web application provides required data to api.
# api returns to client data.

# How to use web api ?
# register/sign-up in api
# api may provide api key for authentication purpose.
# whenever we need to communicate with server make request to api and api key.
# if api key authentication succeed,api will provide required data.

# REST AND REST API ?
# IT is an archtectural guideline to develop web api.
# The api which is developed using rest is known as restapi/resful api.

# how rest web api works ?
# Client makes http request to api
# api will communicate to web applications/database.(if needed)
# web application /database provides required data to api.
# api returns response data to client.
# json data,xml data
 
#  crud operations
# opeartions    HTTP methods   Descriptions
# Create        POST            Creating/Posting/Inserting Data
# Read          GET             Reading/Getting/Retrieve Data
# Update        Put/Patch       Updating Data
                                # Complete update-PUT
                                # Partial UPdate-PATCH
# Delete        DELETE          Deleting Data


# STUDENT API RESOURCE e.g
# http://geekyshows.com/api/students
# 1.Base URL:geekyshows.com
# 2.Naming Convention:api
# 3.Resource of API or END point:students

# Requests and response
# request:                             RESPONSE:
# GET:/API/STUDENTS                    [{"ID":1,"NAME":"RAHUL"},
#                                        {"ID":2,"NAME":"BISHAL"}...]

# REQUEST FOR one student having id=1
# request:                           RESPONSE:
# GET:/API/STUDENTS/1/                  [{"ID":1,"NAME":"RAHUL"},]           

#  http://geekyshows.com/api/students
# GET      /api/students
# GET      /api/students/1
# POST     /api/students 
# PUT      /api/students/1
# PATCH    /api/students/1
# DELETE   /api/students/1

