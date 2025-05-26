## Crawler_house_price

此放假爬虫脚本以深圳市为例，对[房天下网站](https://sz.esf.fang.com/house-a0)进行小区的房价、地址等信息爬取。

### Getting Started
1）电脑需安装python3.11，下载项目本地，并从终端或命令行进入该文件夹路径。可通过以下代码实现：
> `git clone https://github.com/GaoXieQing/Crawler_house_price` \
> `cd Crawler_house_price`

2）安装requirements.txt中的工具包，可以通过以下代码实现：
> `pip install -r requirements.txt`

3）通过`python Crawler_shenzhen_fangtianxia.py`命令运行代码

### Attention

1) 由于网站的反爬机制，可能会中断爬虫，但是该脚本为批量化保存，即使中断也会保存以获取的数据
2) 若网站发生框架重构等改变，可能需要修改代码关键部分，具体流程可在[Wiki](https://github.com/GaoXieQing/Crawler_house_price/Wiki)中查看

