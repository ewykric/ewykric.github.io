"""
Date: 2021.3.22
Author: Justin

要点说明：
Map 地图
分多个系列填充颜色
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
   

c = (
    Map()
    .add("2021年GDP（单位：十亿）", 
         [('United States',22939), ('China',17762), ('Japan',5103), ('Germany',4230), ('United Kingdom',3108),
          ('India',2946), ('France',2940), ('Italy',2120), ('Canada',2015), ('Korea',1823)],
         maptype="world",
         is_map_symbol_show=False, # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-GDP前十世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=25000),
    )
)

c.render('./output/map_gdp_series.html')