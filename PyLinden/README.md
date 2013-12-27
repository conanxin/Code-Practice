PyLinden
========

clone自：[https://github.com/lingyunyumo/PyLinden](https://github.com/lingyunyumo/PyLinden)

A static blog generator. Python and BAE.

PyLinden是python实现的一个静态博客生成系统，支持BAE等Python环境中部署。


生成系统实现了增量生成，只有逻辑上改动过的文件才会重新生成。


文档说明：[http://pylindendocs.duapp.com/](http://pylindendocs.duapp.com/)

###BAE部署：
新建Web应用，python后台。 创建新版本，上传程序包。 开启NFS功能，上线（非必要，不过可以使url好看点）。 写日志：site_source/_posts目录下新建日志（utf-8 without BOM）即可，格式参考此目录下的示例。 假设你的应用url为example.duapp.com，访问example.duapp.com/admin，点击“生成”。 访问example.duapp.com。

上传程序包时注意：程序包应是直接包含admin、pylinden、site_source等内容的zip格式压缩包，切勿放到一个文件夹里再打包。

BAE提供了定时任务Cron功能。登录BAE，找到“Cron（定时任务）”，新建一个。



