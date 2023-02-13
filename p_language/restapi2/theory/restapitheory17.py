# LIMITOFFSETPAGINATION
# This pagination style mirrors the syntax used when looking up multiple database records.The client includes both a 'limit' and an 'offset' query parameter.The limit indicates the maximum number of item to return,and is equivalent to the page_size in other styles.The offser indicates the staring positio of the query in relation to the complete set of unpaginated items.
# To enable the LimitOffsetPagination style globally,use the following configuration:
REST_FRAMEWORK={
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination'
}
# http://127.0.0.1:8000/studentapi/?limit=4&offset=6
# The limitoffsetpagination class includes a number of attributes that may be overriden to modify the pagination style.
# To set these attributes you should override the limitoffsetpagination class, and then enable your customer pagination class.
# default_limit-A numeric value indicating the limit to use if one is not provided by the client in a query parameter.Defaults to the same value as the PAGE_SIZE settings key.
# limit_query_param
# offset_query_param
# max_limit
# template


# CURSORPAGINATION
# The cursor-based pagination presents an opaque 'cursor' indicator that the client may use to page through the result set.This pagination style only presents forward and reverse controls ,and does not allow the client to navigate to arbiatary positions.
# Cursor based pagination requires that there is a unique ,unchaning ordering of items in the result set.This ordering might typically be a certain timestamp field on the model instances and will present a 'timeline' style paginated view,with the most recently added items first.
# The cursor pagination class includes  a number of attributes that may be overridden to modify the pagination style.
# To set these attributes you should override the CursorPagination class,and then enable your custom pagination class.
# page_size
# cursor_query_param
# ordering
# templates 