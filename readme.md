# bcy_picture_spider

> 请勿用于商业用途 尊重coser的版权 转载图片请注明出处

保存coser的脚本GitHub里别的大佬已经实现过了，这个脚本用于保存[半次元](https://bcy.net)指定搜索内容下的全部作品的高清原图




## 依赖

* python
* beautifulsoup4
* requests 


## 使用
* `pip install bs4 requests`

* 运行脚本`python getpic.py`

   
## 注意
* 由于下载的是原图请保证足够大的硬盘空间
* 某些关键字会被半次元过滤，出现无法下载的情况，输入一般的作品名都不会有事
* 伪断点续传，之间保存过的作品不会二次保存


## 样例

以下载关键字 Love Live 下所有作品为例

* 运行样例
    ![image](https://github.com/jososo/bcy_picture_spider/blob/master/README/run.PNG)

* 保存图片样例
    ![image](https://github.com/jososo/bcy_picture_spider/blob/master/README/picture.PNG)



