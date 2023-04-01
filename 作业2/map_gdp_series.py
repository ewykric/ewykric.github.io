"""
Date: 2023.4.1
Author: 王煜楷

"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
   

c = (
    Map()
    .add("2022名义GDP（单位：百万美元）",  #数据来源：世界银行
         [('United States',25035164), ('China',18321197), ('Japan',4300621), ('Germany',4031149), ('India',3468566),
          ('United Kingdom',3198470), ('France',2778090), ('Canada',2200352), ('Russia',2133092), ('Italy',1996934)],
         maptype="world",
         is_map_symbol_show=False, # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="GDP前十世界地图（数据来源：IMF）"),
        visualmap_opts=opts.VisualMapOpts(min_=1000000, max_=25500000),
    )
)

c.render('./output/map_gdp_series.html')