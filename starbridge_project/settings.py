"""
Django settings for starbridge_project project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qs5j3p9(6o*+%y6#gy&f@==u0bdr3_3_vgal&pp0h58%esn=90'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myapps.users',
    'myapps.activity',
    'myapps.creative',
    'myapps.report',
    'myapps.celebrity',
    'myapps.star',
    'myapps.finance',

    # 'myapps.models'

]

ADMIN_REORDER=(
   ("app_name", ("myapps.star",'myapps.activity','myapps.creative','myapps.report','myapps.celebrity','myapps.finance',)),
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'starbridge_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'starbridge_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_starbridge',
        'USER': 'amuser',
        'PASSWORD': 'amuser',
        'HOST': '122.144.167.178',
        'PROT': '',
    },
    # 'db_200': {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'starbridge',
    #     'USER': 'ssp_test',
    #     'PASSWORD': '1q2w3e4r',
    #     'HOST': '10.0.2.200',
    #     'PROT': '',
    # },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-CN'  # 'en-us'

TIME_ZONE = 'Asia/Shanghai'  # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# DATETIME_FORMAT =

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

##ImageField使用
MEDIA_ROOT = 'media/'
MEDIA_URL = 'media/'

##后台界面配置显示
ADMIN_SITE_HEADER = u'创星纪StarCollection后台管理系统'
ADMIN_SITE_TITLE = u'StarCollection系统'
ADMIN_INDEX_TITLE = u'后台管理'

AUTH_USER_MODEL = 'users.CustomUser'


# 邮件配置
EMAIL_HOST = 'smtp.qq.com'                          # SMTP地址
EMAIL_PORT = 25                                     # SMTP端口
EMAIL_HOST_USER = '2463011462@qq.com'               # admin的邮箱
EMAIL_HOST_PASSWORD = 'eeairubbxfhlebcb'            # admin的邮箱密码
EMAIL_SUBJECT_PREFIX = u'[starbridge]'                 # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True                               # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false

LOGIN_URL='/login/'