# news_spider
This is a simple scrapy based spider that you can use to
crawl latest news of Jiangsu province from 163 website.

### How to install scrapy
***
  Refer to offical tutorial:  
  [https://scrapy.org/](https://scrapy.org/)  
  
  
### How to run this project?
***
  Execute command:  
  `scrapy runspider jsnews/jsnews/spiders/netease.py`


### How to solve "win32api" error on Windows
***
You need to install **pywin32** package according to you Windows and Python version.  
**pywin32** is difficult to install on windows, I recommand you download pre-builded wheel from below unofficial website:  
[http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/)  
* Download wheel  
* Install it  
   `pip install pywin32‑220.1‑cp27‑cp27m‑win_amd64.whl`  
* Go to Python scripts path, e.g. "C:\Python27\Scripts".   
   Execute command:  
   `python.exe pywin32_postinstall.py -install`  
 
 ### How to deploy spider to shub(Scraping Cloud)
 * Install shub  
  `pip install shub`  
 * Login shub
  `shub login`  
  API Key: 0e1e5f22532c41e594e71891b069132c  
* Deploy spider  
  `shub depoly`  
* Schedule spider  
  `shub schedule Netease`  
  
