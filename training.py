django-admin startproject CRUD
  settings
      INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',]
    import os
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = 'static/'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
  urls
    from django.contrib import admin
    from django.urls import path, include ,re_path
    from django.conf import settings #added
    from django.conf.urls.static import static ,serve
    from django.views import *

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('App_name.urls')), #added

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #added


  media
  python manage.py startapp student
    templates
      create
      download
      edit
      home
      index
    admin
      from .models import *
      admin.site.register(Table_Name)

    forms
      from .models import *

      class CustomerForm(ModelForm):
        class Meta:
          model = Table_Name
		      fields = '__all__'

    models
      class Table_Name(models.Model):
        filed_name = models.Data_Type(max_length=200, null=True)

    urls
      urlpatterns = [
	    path('page_name/', views.views_name, name="page_name"),
    views
