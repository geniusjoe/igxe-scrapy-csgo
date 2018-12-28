# igxe-scrapy-csgo
igxe csgo 物品交易 历史 抓取

## 功能介绍
- 通过IPProxy代理池的设计自动获取ip进行访问,防止ip被封
- 设置定时开启爬虫
- 将收集到的数据用csv格式保存
- 由于igxe的物品采用动态加载,需要通过splash解决原生scrapy无法渲染js的问题
- 通过splash,效率比selenium高

## 使用方式
### 环境要求
scrapy-splash 的docker环境

https://github.com/scrapy-plugins/scrapy-splash

https://splash.readthedocs.io/en/latest/install.html

IPProxy中的所需环境

https://github.com/qiyeboy/IPProxyPool

*注意并不需要再clone IPProxy中的仓库,只需要安装所需环境*

以及*pip*中的相关包

当满足要求后,在命令行输入命令后应该会得到如下结果:

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/sqlite3.png)
![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/docker.png)

### Quick Start:

首先启动docker,在terminal中输入下列命令

`$ docker run -p 8050:8050 scrapinghub/splash`

应该会得到如下结果

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/splash.png)

之后启动python IDE,此处使用pycharm为例

应该会得到如下结果

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/IPProxy.png)

使用浏览器访问
` http://localhost:8050/ `

应该会得到如下结果

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/8050%20splash.png)
**这样则说明splash配置成功**

接下来激活IPProxy,首先移动到IPProxy的文件夹

`$ cd IPProxyPool`

运行脚本

`$ python IPProxy.py`

应该会得到如下结果

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/IPProxy.png)

使用浏览器访问

` http://localhost:8000/ `

应该会得到如下结果

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/8000%20IPProxy.png)

**这样则说明IPProxy配置成功,注意splash和IPProxy需要在后台保持**

最后,移动到spiders文件夹

`$ cd tutorial/tutorial/spiders`

运行脚本

`$ python time_control.py`

应该会得到如下结果

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/run.png)

最后,在相同文件夹应该会输出一个以时间命名的csv文件,内容大致如下:

![success_flag](https://github.com/geniusjoe/igxe-scrapy-csgo/blob/dev/pictures/target_csv.png)

则说明文件执行成功.

### settings:

#### 修改端口和地址
IPProxy的端口配置请参考IPProxy的配置教程,其中端口名,最大IP数等可以进行相关的配置.从而达到在服务器上部署的能力.

当修改IPProxy的端口和IP后,在*tutorial.middlewares.py*

`r = requests.get('http://127.0.0.1:8000/?types=0&count=1&country=国内')`

修改相关ip或者端口

#### splash
splash的设置由于设置在docker中,改动较少.

#### 修改再次启动的时间

在*time_control.py*中
```
def mymain():
    schedule.enter(0, 0, perform1, (21600,))
```
21600表示21600秒,可以根据实际需要更改再次启动的时间

## 声明
仅限个人学习和研究使用，切勿用于其他用途。

如果将程序用于商业用途或其他非法用途，一切后果由用户自负。

如果您发现有侵犯到您的合法权益，请与我联系删除相关代码，同时我对无意冒犯到您致以深深的歉意。

如果喜欢麻烦给个star,谢谢

## 许可协议
MIT
