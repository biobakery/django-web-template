"""urlconf for the base application"""

from django.conf.urls import url

from .views import home


urlpatterns = [
    url(r'^$', home, name='home'),
]
"""urlconf for the base application"""

from django.conf.urls import url

from .views import home
from .views import charts


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^charts/', charts, name='charts'),
]
