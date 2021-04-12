from django.urls import path
import account.views
import feroxsystemapp.views
urlpatterns = [
    path('', account.views.login, name='login'),
    # path('signup', account.views.signup1, name='signup'),
    path('signup1/', account.views.signup1, name='signup1'),
    path('signup2/', account.views.signup2, name='signup2'),
    path('home', feroxsystemapp.views.home, name='home'),
    path('shop', feroxsystemapp.views.shop, name='shop'),
    path('bank', feroxsystemapp.views.bank, name='bank'),
    path('settings', feroxsystemapp.views.settings, name='settings'),
    path('history', feroxsystemapp.views.history, name='history'),
    # path('signup3/', account.views.signup3, name='signup3')
    # path('', account.views.formview),
    # path('logout/', account.views.logout, name='logout')
]
