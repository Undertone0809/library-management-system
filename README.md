# 图书管理系统

这是一个powerful的图书管理系统，具有一个基本的图书管理系统都有的功能，但是与普通管理系统相比，该系统基于MVC架构分层构建，扩展性强，高内聚低耦合，
数据持久化上采用`cushy-storage`进行文件存储，大大减少文件操作的开发成本，减少自定义存储协议所需要的工作量。项目的架构和设计思想适合新手学习借鉴。

<div style="text-align: center;">
    <img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230416125322.png"/>
    <p>系统架构图</p>
</div>

## 特性

- 批量查询、查询所有图书信息
- 添加图书信息
- 修改图书信息
- 删除图书信息
- 采用`cushy-storage`进行图书数据持久化保存
- 采用`rich`进行更好看的终端显示

## 快速上手

先不说太多了，直接把代码拉下来跑一遍看看效果吧。

```shell
git clone https://github.com/Undertone0809/library-management-sysmen
```

- 导包：打开终端命令行，输入下面的命令

```shell
pip install -r requirements.txt
```

- 在第三方包下载完之后，运行`init_data.py`初始化数据
- 直接运行`app.py`就好了

## 运行效果

<img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230416153204.png"/>

<img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230416153232.png"/>

## 代码剖析

- 本项目开发严格遵循高内聚、低耦合、支持扩展、架构分层的设计思想进行设计，专门的层做专门的事情，本项目基本的架构如下所示：

<div style="text-align: center;">
    <img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230416125322.png"/>
    <p>系统架构图</p>
</div>

- 进入项目的主入口，你会发现唯一暴露的就是`menu_service.base_menu()`的函数，本项目通过`menu_service`来封装需要显示的模块。
- 在数据存储上，最底层将`cushy-storage`进行二次封装，形成了`cache_service`，使用`cache_service`，可以轻松地对对象进行增删改查。
- 对Book的对象级别操作，我们叫做ORM，通过ORM架构，我们可以直接通过操作Book对象来进行增删改查的操作，让代码更加稳定。`book_service`进一步封装了
`cache_service`的功能，让Book操作更加便捷
- 对于日志打印，`app.py`中运行`utils.enable_log()`即可开启日志打印，将数据流转的关键信息打印出来。
- `utils.py`封装了一些简单的工具类，如日志的打印、id自动生成等功能，具有通用性，因此放在一起方便调用。
- 在终端显示上，使用`rich` 可以有更好看终端效果，如在批量显示Book上，可以将Books以表格的形式展现出来，效果如下所示：

<img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230416153923.png"/>


## TODO
- 增加用户登陆的功能
- 提供普通用户和管理员的功能
- 按照图书价格排序