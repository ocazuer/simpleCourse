# 项目简介
生成课程手册文档
# 功能
用户可以进行注册和登录。
已登录用户可以：
- 注册新的公司。
- 为任意某个公司编写课程，其中课程的学习点的数量可以由用户自行决定。
- 预览所有的课程，并下载课程的 pdf 版本。下载的 pdf 文件封面的“姓名”一栏显示的是创建这份文档的用户的用户名。
# 数据库
users：包含用户的用户名和密码。
companies：包含所有的公司的名字和 logo
lessons：包括所有的课程的名称、对应的公司以及对应的作者。
points：包含所有的学习点的标题、学习目标和正文以及学习点对应的课程。每门课程有多个学习点，每个学习点仅属于一门课程。
# PDF 实现
在用户下载 PDF 时，使用 `weasyprint` ，根据下载者的姓名生成 pdf 文档供用户下载。
# 遇到的问题
## 未解决
1. 打印 PDF 时候无法打印下载者姓名
## 已经解决
1. WeasyPrint 不支持 flexbox，[详见](https://github.com/Kozea/WeasyPrint/issues/324)，导致一些排版工作上的重复劳动
```
Ignored `display: flex` at 11:5, invalid value.
Ignored `flex-direction: row` at 12:5, unknown property.
Ignored `align-items: center` at 16:5, unknown property.
Ignored `justify-content: space-between` at 21:5, unknown property.
```
2. ~~生成的 pdf 文件会在特定缩放倍率下出现细边框~~（已解决）
#一些未来可以实现的功能
- 修改课程的功能
- 上传 logo
- 给学习点添加复杂的排版功能，如居中
- 将生成的 PDF 文件储存起来，减少重复运算