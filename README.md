# 计算机科学与编程入门课程第一次作业
## 2000013073 王煜楷
## 1. 作业1 《倚天屠龙记》前十出现人名词频分析
首先读取指定路径下的小说《倚天屠龙记》文本文件，使用课上所学的jieba分词工具对txt文本进行初步分词，统计每个词在文本中出现的次数，之后按照观察与经验进行忽略词、添加词与合并词来增加分词精准度，即得到《倚天屠龙记》中前十出现人名的词频列表，程序会将排名前 N（由用户指定，默认为10，实际上也只保证前十的精准度）的词和它们的出现次数输出到屏幕上，并写入到一个 CSV 文件中（文件路径为 ./output/倚天屠龙记-人物词频.csv）。
而后再使用matplotlib库中的绘图工具读取output目录下统计到的前十出现人名的词频列表，将词频列表以柱状图形式展示（注意要先引入os库设置中文字体，否则展示图里无法显示中文字符），具体操作与展示结果可在作业仓库链接里的github库中查看。

[作业1展示链接](https://github.com/ewykric/ewykric.github.io/blob/master/%E5%80%9A%E5%A4%A9%E5%B1%A0%E9%BE%99%E8%AE%B0-%E4%BA%BA%E7%89%A9%E8%AF%8D%E9%A2%91.png)

## 2. 作业2 2021GDP世界前十国家地图（map）展示


[作业2展示链接](https://ewykric.github.io/map_gdp_series.html)
## 3. 作业3 2021GDP世界前十国家人均GDP与恩格尔系数组合分析


[作业3展示链接](https://ewykric.github.io/gdpEngel.html)

[作业仓库链接](https://github.com/ewykric/ewykric.github.io/)
