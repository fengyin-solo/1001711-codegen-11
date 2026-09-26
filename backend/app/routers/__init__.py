"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import crop as router_crop
from app.routers import zone as router_zone
from app.routers import envdata as router_envdata
from app.routers import irrigation as router_irrigation
from app.routers import fertilizer as router_fertilizer
from app.routers import pesticide as router_pesticide
from app.routers import pollination as router_pollination
from app.routers import pruning as router_pruning
from app.routers import harvest as router_harvest
from app.routers import grading as router_grading
from app.routers import packing as router_packing
from app.routers import shipping as router_shipping
from app.routers import nutrient as router_nutrient
from app.routers import lighting as router_lighting
from app.routers import co2 as router_co2
from app.routers import sensor as router_sensor
from app.routers import failure as router_failure
from app.routers import batch_trace as router_batch_trace

ROUTERS = [router_crop, router_zone, router_envdata, router_irrigation, router_fertilizer, router_pesticide, router_pollination, router_pruning, router_harvest, router_grading, router_packing, router_shipping, router_nutrient, router_lighting, router_co2, router_sensor, router_failure, router_batch_trace]
