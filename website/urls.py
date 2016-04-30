"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.controller),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', auth_views.login, name='login'), # If user is not login it will redirect to login page
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),
    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^contact/$', views.contact, name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
