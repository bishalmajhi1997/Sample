from django.urls import path
from accounts import views
urlpatterns =[
    path('',views.signin),
    path('signup/',views.signup),
    path('auth/',views.auth_view),
    path('^signout/',views.signout),
    path('dashboard/',views.dashboard),
    path('invalid/',views.invalid),
    path('registered/',views.register_success),
    path('not_active/',views.not_active),
    path('confirm/(?P<activation_key>\w+)/', views.register_confirm),
    #path('change_password/', 'django.contrib.auth.views.password_change', name='change_password'),
    #path('change_password/done/', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    #path('password_reset/', 'django.contrib.auth.views.password_reset', name='password_reset'),
    #path('password_reset/done/', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    #path('(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    #path('reset_done/', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]
