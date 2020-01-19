# 项目说明

> by: chinanoahli<br/>Python简单，只是业余写写，所以基本都是Python。

1. [集思录数据小工具](./jisilu_web)

# 我的笔记

1. [长投学堂](https://github.com/chinanoahli/investment_note)

-------------------------

## 集思录数据小工具说明

集思录可转债页面有一个选项是“自动刷新”。

忽然有一天想起某篇公众号写了有些网站的走势折线图是用JSON来格式化数据的，就打开浏览器控制台稍微分析了一下。

然后就发现了，其实集思录的可转债数据也是一样用JSON格式化数据，但是请求的地址后面似乎加上了目前时间的秒数（UNIX Epoch time）。

所以就简单用`Python + pandas`清洗了一下，就得出了这个工具。

#### 核心代码：

1. 集思录的数据请求地址是代码的第[30行](https://github.com/chinanoahli/investment_tools/blob/master/jisilu_web/cb.py#L30)。

  > `url = 'https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=' + now_time_str`

-------------------------

