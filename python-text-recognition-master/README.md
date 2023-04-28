# python-text-recognition
PyQt5做界面，使用百度文字识别API接口来实现识别图片中的文字，可以采用截图和浏览图片文件方式进行，

截图功能使用github的位作者的开源项目https://github.com/SeptemberHX/screenshot

## Prerequisite
1. PyQt5，使用pip install -U pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple更新安装，其中 "-i https://pypi.tuna.tsinghua.edu.cn/simple"是使用清华源，加速下载
2. 百度aip，pip安装
`pip install -U baidu-aip`

## Simple Tutorial
下载整个软件包后进入src目录，执行
`python baidu-api.py`

1. 可以选择选取图片来识别图中的文字，选取后点击“转换”
2. 可以点击“截图”截取想要识别的内容，默认保存截图到目录"./temp/temp.png"，然后再
	选择"浏览文件"选择刚才的截图，最后点击“转换图片为文字”

## Need to Improve
- 百度文字识别API需要自己在百度云注册然后建立一个实例来获取，本程序中appid，apikey，screet key可以修改成自己的，但是在界面上修改不了，需要修改代
- 截图方式和选取图片方式通过一个状态变量来区分，程序稳固性不够强，有时操作错误就会死掉
