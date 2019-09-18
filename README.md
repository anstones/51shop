# 51商城
##### 功能：

	1. 商品首页图片展示和轮播图
 	2. 展示新品，促销商品，热门商品
 	3. 商品详情
 	4. 商品收藏，取消收藏
 	5. 加入购物车
 	6. 购物车商品展示，清空、增加、减少购物车
 	7. 填写订单信息，地址信息
 	8. 提交订单显示支付宝收款码
 	9. 订单详情
 	10. 用户模块：登陆，退出，注册
 	11. 后台：增加商品，编辑商品，删除商品，查看商品
 	12. 后台：查看会员信息
 	13. 后台：查看订单信息

##### 数据库表：

	1. User   用户表
 	2. Admin  管理员表
 	3. SuperCat  一级分类表
 	4. SubCat  二级分类表
 	5. Goods  商品表
 	6. Cart  购物车表
 	7. Orders  订单表
 	8. OrderDetail   订单详情表
 	9. Collect   收藏表

##### 主要库：

​	Flask, SQLAlchemy

##### 依赖：

​	requirements.txt

#### 配置：

​	config.py

##### quick start

​	python manage.py db init    初始化数据库

​	python manage.py db migrate    创建迁移脚本

​	python manage.py db upgrade    迁移数据库

​	python manage.py  runserver    开始


![image]()
