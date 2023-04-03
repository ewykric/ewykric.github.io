# 计算机科学与编程入门课程第一次作业
## 2000013073 王煜楷
## 1. 作业1 《倚天屠龙记》前十出现人名词频分析
首先读取指定路径下的小说《倚天屠龙记》文本文件，使用课上所学的jieba分词工具对txt文本进行初步分词，统计每个词在文本中出现的次数，之后按照观察与经验进行忽略词、添加词与合并词来增加分词精准度，即得到《倚天屠龙记》中前十出现人名的词频列表，程序会将排名前 N（由用户指定，默认为10，实际上也只保证前十的精准度）的词和它们的出现次数输出到屏幕上，并写入到output目录下的CSV 文件中（文件路径为 ./output/倚天屠龙记-人物词频.csv）。

而后再使用matplotlib库中的绘图工具读取output目录下统计到的前十出现人名的词频列表，将词频列表以柱状图形式展示（注意要先引入os库设置中文字体，否则展示图里无法显示中文字符），具体操作与展示结果可在作业仓库链接里的github库中查看。

[作业1展示链接](https://github.com/ewykric/ewykric.github.io/blob/master/%E5%80%9A%E5%A4%A9%E5%B1%A0%E9%BE%99%E8%AE%B0-%E4%BA%BA%E7%89%A9%E8%AF%8D%E9%A2%91.png)

## 2. 作业2 全球GDP地图（map）展示
作业2中我们用了pyecharts库生成了一张世界地图图表，以百万美元为单位展示了各个国家的GDP。
我们首先从pyecharts库中导入了options模块，pyecharts.charts中的Map模块以及pyecharts.global中的ChartType和SymbolType模块来实现调整各项参数以及数据，然后从文本文件“gdp_data.txt”中读取数据，我们假定该文件包含各个国家/地区的 GDP 数据（作业中有附上示例数据）。 数据逐行读取，去除任何空白字符，并使用制表符作为分隔符拆分为多个字段，结果数据存储在名为数据（data）的列表中。
将数据列表转化为格式化数据列表（formatted_data），其中每一项都是一个包含国家名称（原始数据中的第一个字段）及其 GDP 值的元组。
按照老师上课使用的“地图”类来创建地图图表，调整各项参数并渲染成html文件存入output目录下，具体操作与展示结果可在作业仓库链接里的github库中查看。

[作业2展示链接](https://ewykric.github.io/map_gdp.html)
## 3. 作业3 国家人均GDP与恩格尔系数组合分析
首先需要说明的是，人均GDP一直被视为衡量一个国家经济水平，尤其是人均收入的重要指标，因此人均GDP在一定程度上反映各国的贫富情况；而恩格尔指数是国民食品支出占总消费支出的比例，一般认为越先进富足的国家的恩格尔指数会越小。

作业3里我们选择十个较为常见的国家作为分析对象，从世界银行和美国农业经济研究局里分别获取各国在2018年的人均GDP以及恩格尔指数。先按人均GDP从大到小排序，并用柱状图的方式呈现；恩格尔系数则用折线图的方式呈现，以此绘制出一份横坐标为国家，左侧纵坐标为人均GDP（柱状图），右侧纵坐标为恩格尔系数（折线图）的组合图表。此作业主要运用pyechart中的Bar与Line模组进行数据展示，最后用Grid将两个图表组合起来。

从最后的展示结果可以发现，人均GDP确实和恩格尔系数呈负相关的关系。具体操作与展示结果可在作业仓库链接里的github库中查看。

[作业3展示链接](https://ewykric.github.io/gdpEngel.html)

[作业仓库链接](https://github.com/ewykric/ewykric.github.io/)
