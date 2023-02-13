from django.urls import path
from api import views
from .forms import MyPasswordResetForm,MySetPasswordChangeForm,MySetPasswordForm
from django.contrib.auth import views as auth_views
# from django.contrib import admin
app_name='api'
urlpatterns = [
    # path('',views.home,name='index'),
    path('teams/',views.team,name='team'),
    path('contact/',views.contact,name='contact'),
    path('innerpage/',views.innerpage,name='innerpage'),
    path('login/',views.login1,name='user_login'),


    path('',views.index,name='index'),
    path('register/',views.register,name='signup'),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('accounts/login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('success/',views.success,name='success'),
    path('token/',views.token_send,name='token_send'),
    path('error/',views.error_page,name='error'),
    path('details/',views.DetailView.as_view(),name='details'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='api/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='api/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='api/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='api/password_reset_complete.html'),name='password_reset_complete'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='api/passwordchange.html',form_class=MySetPasswordChangeForm),name='password_change'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='api/passwordchangedone.html')),
]

    # path('admin/',admin.site.urls)

