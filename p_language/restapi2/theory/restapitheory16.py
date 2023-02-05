# Rest framework includes support for customizable pagination styles.This allows you to modify how large result sets are split into individual pages of data.
# Pagenumber pagination
# limitoffsetpagination
# Cursorpagination


# PAGINATION GLOBAL SETTINGS 
# The pagination style may be set globally,using the default_pagination_class and page_size setting keys.
# REST_FRAMEWORK={
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination'
# }

# PAGINATION PER VIEW
# You can set the pagination class on an individual view by using the pagination_class attribute.
# Class StudentList(ListApiView):
    #  queryset=Student.objects.all()
    #  serailizet_class=StudentSerializer()
    #  pagination_class=PageNumberPagination


# PAGENUMBERPAGINATION
# This pagination style accepts a single number page number in the request qeury parameters.
# To enable the pagenumberpagination style globally,use the following configuration,and set the page_size as desired.
# REST_FRAMEWORK={
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination','PAGE_SIZE':5
# }

# PAGENUMBERPAGINATION
# The pagenumberpagination class includes a number of attributes that may be overriden to modify the pagination style.
# django_pagination_class
# page_size
# page_query_param
# page_size_query_param(http://127.0.0.1:8000/?p=1&records=5)
# max_page_size
# last_page_strings
# template

# class MypageNumberPagination(PageNumberPagination):
#     page_size=5
#     page_size_query_param='records'
#     max_page_size=7

# class StudentList(ListApPIView):
#     querset=Student.objects.all()
#     serializer_class=StudentSerializer
#     pagination_class=MypageNumberPagination