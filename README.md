# 图书管理系统

这是一个powerful的图书管理系统，具有一个基本的图书管理系统都有的功能，但是与普通管理系统相比，该系统基于MVC架构分层构建，扩展性强，高内聚低耦合，
数据持久化上采用`cushy-storage`进行文件存储，大大减少文件操作的开发成本，减少自定义存储协议所需要的工作量。项目的架构和设计思想适合新手学习借鉴。

<div style="text-align: center;">
    <img src="https://zeeland-bucket.oss-cn-beijing.aliyuncs.com/images/20230416125322.png"/>
    <p>系统架构图</p>
</div>

## 特性

- 查询图书信息
- 添加图书信息
- 修改图书信息
- 删除图书信息
- 图书数据持久化保存

## 快速上手

```shell
git clone https://github.com/Undertone0809/library-management-sysmen
```

- 导包：打开终端命令行，输入下面的命令

```shell
pip install -r requirements.txt
```

- 在第三方包下载完之后，运行`init_data.py`初始化数据
- 直接运行`app.py`就好了


## TODO
- 增加用户登陆的功能
- 提供普通用户和管理员的功能
