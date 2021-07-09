<h1 align="center">Document-Management-System</h1>



## Contents

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Preview](#preview)
* [References](#references)



## Introduction

Database Final Project based on MySQL.

<img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/E-R.png" width="800">



## Prerequisites

* Python version: 3.8
* Django version: 3.2.1
* pymysql library version: 1.0.2
* pyecharts library version: 1.9.0

Install requirements with:

```powershell
pip install -r requirements.txt
```



## Usage

1. Set up `DMS/settings.py` :

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': '',  # eg. DMS
           'USER': '',  # eg. root
           'PASSWORD': '',
           'HOST': '127.0.0.1',
           'PORT': '3306',
       }
   }
   
   ...
   
   EMAIL_HOST = 'smtp.xxx.com'  # 'smtp.163.com'
   EMAIL_PORT = '25'
   EMAIL_HOST_USER = ''  # 'xxxxxx@163.com'
   EMAIL_HOST_PASSWORD = ''  # Password to use for the SMTP server, not your e-mail password
   ```

2. Apply migrations to your database ( in command window ) :

   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create super user :

   ```powershell
   python manage.py createsuperuser
   ```

4. Run scripts in `/utils/` to get required data, and connect with your database.

   - `/spider/cvpr2csv_withoutdate.py` : cvpr data, and you can get iccv/wacv in the same way
   - `/fake-users/fake-users.py` : generate some lorem ipsum users
   - `/wordcloud/wc_for_year.py` :  generate word cloud images

5. Run server :

   ```powershell
   python manage.py runserver
   ```



## Preview

1. Get started

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-1.jpg" width="800">

2. Login

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-2.jpg" width="800">

3. Register

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-3.jpg" width="800">

4. E-mail check

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-4.jpg" width="800">

5. Homepage, scroll down to get introductions

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-5.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-6.jpg" width="800">

6. Library & Pagination

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-7.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-8.jpg" width="800">

7. Search bar

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-9.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-10.jpg" width="800">

8. Abstract & Download

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-12.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-11.jpg" width="800">

9. Sidebar

   <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-13.jpg" width="800">

10. Statistics - Author Ranking

    <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-14.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-15.jpg" width="800">

11. Statistics - Paper Statistics

    <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-16.jpg" width="800">

12. Statistics - Word Cloud

    <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-17.jpg" width="800">

13. Collection

    <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-18.jpg" width="800">

14. Admin

    <img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-20.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-21.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-22.jpg" width="800"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Document-Management-System/preview-23.jpg" width="800">



## References

1. [Django documents](https://docs.djangoproject.com/en/3.2/) everything you need to know about Django
2. [W3schools](https://www.w3schools.com/)  learn HTML / CSS / JS / Bootstrap
3. [Django ORM Query](https://docs.djangoproject.com/en/3.2/topics/db/queries/) / [CN](https://www.django.cn/article/show-15.html) Django making queries to MySQL
4. [Looka](https://looka.com/logo-maker/) logo maker
5. [Color Space](https://mycolor.space/) nice color palettes generator
6. [Font Awesome](https://fontawesome.com/v4.7/icons/) icons

