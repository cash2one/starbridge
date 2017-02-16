# starbridge项目说明

项目原型:

启动服务器:  http://127.0.0.1:8000/ <p>
首页页面URL:  http://127.0.0.1:8000/home/ <p>
后台URL:  http://127.0.0.1:8000/admin/   


<font color=#0099ff size=3 face="黑体">**后台用户名：admin    密码：Admin2017**</font>

##项目目录说明

###1、根目录文件
######1.1 requirements.txt
>为了让他人 拷贝该项目代码后可以快速地根据此文件中内容安装好必须的python依赖包。

**命令：**

	pip install -r requirements.txt
	
######1.2 README.md

>项目说明
	
######1.3 .gitignore


>把要忽略的文件名填进去，Git就会自动忽略这些文件

-----

###2、MYAPPS文件夹：

######2.1 home (首页)
>链接：[首页](http://127.0.0.1:8000/home/)

######2.2 activity (活动)
>链接：[活动](http://127.0.0.1:8000/activity/)

######2.3 creative (素材)
>链接：[素材](http://127.0.0.1:8000/creative/)

######2.4 report (数据报表)
>链接：[数据报表](http://127.0.0.1:8000/report/)

######2.5 celebrity (红人库)
>链接：[红人库](http://127.0.0.1:8000/celebrity/)

######2.6 star (明星库) 
>链接：[明星库](http://127.0.0.1:8000/star/)

######2.7 finance (财务报表)
>链接：[财务报表](http://127.0.0.1:8000/finance/)

######2.8 users (用户)
>使用abstractuser扩充AUTH_USER_MODEL的fields

-----

###3、templates（模版）

	存放django中的所有模板文件
<p>

>其下分别创建各个app对应的子目录，子目录中存放html，html命名参照app命名

###4、static（静态文件）

    存放css/js/image文件
<p>

>其中分三个子目录：**1、css；2、js；3、image。**

###5、media（媒体文件夹）
    存放用户上传的 文件
<p>

>其中一级子目录：**1、img_good **  素材中的商品图像文件

>其中二级子目录  格式为 %Y-%m-%d  如“2016-07-07”

>子文件

-----
###6、项目容器starbridge_project

-----
###7、manage.py 用于管理任务的命令行工具
