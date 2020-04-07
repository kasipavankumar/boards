from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from accounts import views as account_views
from boards import views

urlpatterns = [
    # Home route.
    path('', views.BoardListView.as_view(), name='home'),
    
    # Signup route.
    re_path(r'^signup/$', account_views.signup, name='signup'),

    # Login route.
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout route.
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Boards route.
    re_path(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    
    # New post route.
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),

    # Password reset routes.
    re_path(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
            ),
        name='password_reset'
        ),

    # Password reset done route.
    re_path(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Password reset confirmation route.
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    # Password reset complete route.
    re_path(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    
    re_path(r'^settings/password/$', 
        auth_views.PasswordChangeView.as_view(
            template_name='password_change.html'
        ),
        name='password_change'
    ),
    
    re_path(r'^settings/password/done/$', 
        auth_views.PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'
            ),
        name='password_change_done'
    ),

    re_path(r'^settings/account/$', 
        account_views.UserUpdateView.as_view(),
        name='my_account'
    ),

    # Topic view route.
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', 
        views.topic_posts,
        name='topic_posts'
    ),

    # Reply view route.
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$',
        views.reply_topic,
        name='reply_topic'
    ),

    # Post edit view route.
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),

    # Admin dashboard route.
    path('admin/', admin.site.urls),
]
