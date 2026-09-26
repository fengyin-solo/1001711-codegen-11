<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "作物批次", "created": 0, "pending": 0, "abnormal": 0}, {"name": "种植分区", "created": 0, "pending": 0, "abnormal": 0}, {"name": "环境监测", "created": 0, "pending": 0, "abnormal": 0}, {"name": "灌溉计划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "施肥记录", "created": 0, "pending": 0, "abnormal": 0}, {"name": "植保作业", "created": 0, "pending": 0, "abnormal": 0}, {"name": "授粉管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "植株整枝", "created": 0, "pending": 0, "abnormal": 0}, {"name": "采收计划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "品级分拣", "created": 0, "pending": 0, "abnormal": 0}, {"name": "包装管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "出货管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "营养液管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "补光控制", "created": 0, "pending": 0, "abnormal": 0}, {"name": "CO2调控", "created": 0, "pending": 0, "abnormal": 0}, {"name": "传感器管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "设备故障", "created": 0, "pending": 0, "abnormal": 0}, {"name": "批次追溯", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
