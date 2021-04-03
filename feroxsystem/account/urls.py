from django.urls import path
import account.views
urlpatterns = [
    path('', account.views.login, name='login'),
    # path('signup', account.views.signup1, name='signup'),
    path('signup1/', account.views.signup1, name='signup1'),
    path('signup2/', account.views.signup2, name='signup2'),
    path('signup3/', account.views.signup3, name='signup3')
    # path('', account.views.formview),
    # path('logout/', account.views.logout, name='logout')
]