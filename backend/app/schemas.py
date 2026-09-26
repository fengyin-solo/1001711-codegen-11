"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class CropEntry(BaseModel):
    """种植批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 作物品种
    field_2: str | None = None  # 所属温室
    field_3: str | None = None  # 播种日期
    field_4: str | None = None  # 预计采收日
    field_5: str | None = None  # 种植面积
    field_6: str | None = None  # 育苗方式
    field_7: str | None = None  # 批次状态

class ZoneEntry(BaseModel):
    """种植分区明细结构。"""

    field_0: str | None = None  # 分区编号
    field_1: str | None = None  # 所属温室
    field_2: str | None = None  # 分区面积
    field_3: str | None = None  # 当前批次
    field_4: str | None = None  # 基质类型
    field_5: str | None = None  # 栽种行数
    field_6: str | None = None  # 滴灌带数
    field_7: str | None = None  # 分区状态

class EnvdataEntry(BaseModel):
    """环境数据明细结构。"""

    field_0: str | None = None  # 采集点编号
    field_1: str | None = None  # 温室内温度
    field_2: str | None = None  # 温室内湿度
    field_3: str | None = None  # 光照强度
    field_4: str | None = None  # 二氧化碳浓度
    field_5: str | None = None  # 基质温度
    field_6: str | None = None  # 采集时间
    field_7: str | None = None  # 数据状态

class IrrigationEntry(BaseModel):
    """灌溉任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 目标分区
    field_2: str | None = None  # 灌溉方式
    field_3: str | None = None  # 灌溉时长
    field_4: str | None = None  # 营养液EC值
    field_5: str | None = None  # pH设定
    field_6: str | None = None  # 计划执行日
    field_7: str | None = None  # 任务状态

class FertilizerEntry(BaseModel):
    """施肥记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 目标分区
    field_2: str | None = None  # 肥料类型
    field_3: str | None = None  # 用量公斤
    field_4: str | None = None  # 稀释倍数
    field_5: str | None = None  # 施肥方式
    field_6: str | None = None  # 施肥日期
    field_7: str | None = None  # 记录状态

class PesticideEntry(BaseModel):
    """植保记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 目标分区
    field_2: str | None = None  # 药剂名称
    field_3: str | None = None  # 稀释倍数
    field_4: str | None = None  # 防治对象
    field_5: str | None = None  # 安全间隔期
    field_6: str | None = None  # 施药日期
    field_7: str | None = None  # 记录状态

class PollinationEntry(BaseModel):
    """授粉记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 目标分区
    field_2: str | None = None  # 授粉方式
    field_3: str | None = None  # 蜂箱编号
    field_4: str | None = None  # 授粉启动日
    field_5: str | None = None  # 授粉结束日
    field_6: str | None = None  # 辅助授粉
    field_7: str | None = None  # 记录状态

class PruningEntry(BaseModel):
    """整枝任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 目标分区
    field_2: str | None = None  # 整枝类型
    field_3: str | None = None  # 作业人员
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 完成日期
    field_6: str | None = None  # 作业工时
    field_7: str | None = None  # 任务状态

class HarvestEntry(BaseModel):
    """采收批次明细结构。"""

    field_0: str | None = None  # 采收编号
    field_1: str | None = None  # 所属批次
    field_2: str | None = None  # 采收日期
    field_3: str | None = None  # 计划产量
    field_4: str | None = None  # 实际产量
    field_5: str | None = None  # 采收人员
    field_6: str | None = None  # 品质初评
    field_7: str | None = None  # 采收状态

class GradingEntry(BaseModel):
    """分拣记录明细结构。"""

    field_0: str | None = None  # 分拣编号
    field_1: str | None = None  # 采收编号
    field_2: str | None = None  # 特级品数
    field_3: str | None = None  # 一级品数
    field_4: str | None = None  # 二级品数
    field_5: str | None = None  # 次品数
    field_6: str | None = None  # 分拣员
    field_7: str | None = None  # 分拣状态

class PackingEntry(BaseModel):
    """包装记录明细结构。"""

    field_0: str | None = None  # 包装编号
    field_1: str | None = None  # 货品等级
    field_2: str | None = None  # 包装规格
    field_3: str | None = None  # 包装数量
    field_4: str | None = None  # 包装材料
    field_5: str | None = None  # 包装日期
    field_6: str | None = None  # 包装线
    field_7: str | None = None  # 包装状态

class ShippingEntry(BaseModel):
    """出货单明细结构。"""

    field_0: str | None = None  # 出货单号
    field_1: str | None = None  # 收货方
    field_2: str | None = None  # 出货品级
    field_3: str | None = None  # 出货数量
    field_4: str | None = None  # 运输方式
    field_5: str | None = None  # 发车时间
    field_6: str | None = None  # 到达时间
    field_7: str | None = None  # 出货状态

class NutrientEntry(BaseModel):
    """营养液明细结构。"""

    field_0: str | None = None  # 液罐编号
    field_1: str | None = None  # 营养液配方
    field_2: str | None = None  # A液存量
    field_3: str | None = None  # B液存量
    field_4: str | None = None  # pH调节剂
    field_5: str | None = None  # 母液浓度
    field_6: str | None = None  # 上次补充日
    field_7: str | None = None  # 液罐状态

class LightingEntry(BaseModel):
    """补光灯组明细结构。"""

    field_0: str | None = None  # 灯组编号
    field_1: str | None = None  # 所属温室
    field_2: str | None = None  # 灯组功率
    field_3: str | None = None  # 光谱类型
    field_4: str | None = None  # 每日开启
    field_5: str | None = None  # 每日关闭
    field_6: str | None = None  # 累计照明
    field_7: str | None = None  # 灯组状态

class Co2Entry(BaseModel):
    """CO2供应点明细结构。"""

    field_0: str | None = None  # 供应点编号
    field_1: str | None = None  # 所属温室
    field_2: str | None = None  # 气源类型
    field_3: str | None = None  # 当前浓度
    field_4: str | None = None  # 目标浓度
    field_5: str | None = None  # 供气速率
    field_6: str | None = None  # 上次补充
    field_7: str | None = None  # 供应状态

class SensorEntry(BaseModel):
    """传感器明细结构。"""

    field_0: str | None = None  # 传感器编号
    field_1: str | None = None  # 所属温室
    field_2: str | None = None  # 传感器类型
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 精度等级
    field_5: str | None = None  # 校准日期
    field_6: str | None = None  # 电池电量
    field_7: str | None = None  # 传感器状态

class FailureEntry(BaseModel):
    """故障报告明细结构。"""

    field_0: str | None = None  # 故障编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 故障类型
    field_3: str | None = None  # 发生时间
    field_4: str | None = None  # 影响分区
    field_5: str | None = None  # 抢修人员
    field_6: str | None = None  # 修复时间
    field_7: str | None = None  # 故障状态

class BatchTraceEntry(BaseModel):
    """追溯记录明细结构。"""

    field_0: str | None = None  # 追溯编号
    field_1: str | None = None  # 种植批次
    field_2: str | None = None  # 种苗来源
    field_3: str | None = None  # 基质批次
    field_4: str | None = None  # 肥料批号
    field_5: str | None = None  # 药剂批号
    field_6: str | None = None  # 质检结果
    field_7: str | None = None  # 追溯状态
