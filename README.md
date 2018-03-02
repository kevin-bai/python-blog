# python-blog
python3.6  django2.0  blog 练手



## 启动  
python manage.py runserver

http://localhost:8000/blog/index
http://localhost:8000/admin/

## orm系统
1. python manage.py makemigrations  生成数据迁移文件
2. python manage.py migrate   执行数据迁移文件
3. python manage.py sqlmigrate blog 0001  根据迁移文件生成sql``
