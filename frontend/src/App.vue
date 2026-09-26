<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">智慧温室种植管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向温室作物批次管理、环境监测调控、灌溉施肥计划、植保作业、采收分拣与批次追溯的一体化智慧温室种植管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "作物批次", path: "/crop" }, { label: "种植分区", path: "/zone" }, { label: "环境监测", path: "/envdata" }, { label: "灌溉计划", path: "/irrigation" }, { label: "施肥记录", path: "/fertilizer" }, { label: "植保作业", path: "/pesticide" }, { label: "授粉管理", path: "/pollination" }, { label: "植株整枝", path: "/pruning" }, { label: "采收计划", path: "/harvest" }, { label: "品级分拣", path: "/grading" }, { label: "包装管理", path: "/packing" }, { label: "出货管理", path: "/shipping" }, { label: "营养液管理", path: "/nutrient" }, { label: "补光控制", path: "/lighting" }, { label: "CO2调控", path: "/co2" }, { label: "传感器管理", path: "/sensor" }, { label: "设备故障", path: "/failure" }, { label: "批次追溯", path: "/batch_trace" }]
</script>
