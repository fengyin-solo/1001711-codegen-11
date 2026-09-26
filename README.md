# 智慧温室种植管理平台

面向温室作物批次管理、环境监测调控、灌溉施肥计划、植保作业、采收分拣与批次追溯的一体化智慧温室种植管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 作物批次 | `crop` | 种植批次 | 批次编号、作物品种、所属温室 |
| 种植分区 | `zone` | 种植分区 | 分区编号、所属温室、分区面积 |
| 环境监测 | `envdata` | 环境数据 | 采集点编号、温室内温度、温室内湿度 |
| 灌溉计划 | `irrigation` | 灌溉任务 | 任务编号、目标分区、灌溉方式 |
| 施肥记录 | `fertilizer` | 施肥记录 | 记录编号、目标分区、肥料类型 |
| 植保作业 | `pesticide` | 植保记录 | 记录编号、目标分区、药剂名称 |
| 授粉管理 | `pollination` | 授粉记录 | 记录编号、目标分区、授粉方式 |
| 植株整枝 | `pruning` | 整枝任务 | 任务编号、目标分区、整枝类型 |
| 采收计划 | `harvest` | 采收批次 | 采收编号、所属批次、采收日期 |
| 品级分拣 | `grading` | 分拣记录 | 分拣编号、采收编号、特级品数 |
| 包装管理 | `packing` | 包装记录 | 包装编号、货品等级、包装规格 |
| 出货管理 | `shipping` | 出货单 | 出货单号、收货方、出货品级 |
| 营养液管理 | `nutrient` | 营养液 | 液罐编号、营养液配方、A液存量 |
| 补光控制 | `lighting` | 补光灯组 | 灯组编号、所属温室、灯组功率 |
| CO2调控 | `co2` | CO2供应点 | 供应点编号、所属温室、气源类型 |
| 传感器管理 | `sensor` | 传感器 | 传感器编号、所属温室、传感器类型 |
| 设备故障 | `failure` | 故障报告 | 故障编号、设备名称、故障类型 |
| 批次追溯 | `batch_trace` | 追溯记录 | 追溯编号、种植批次、种苗来源 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
