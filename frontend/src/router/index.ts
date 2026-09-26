import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Crop = () => import('@/views/crop/index.vue')
const Zone = () => import('@/views/zone/index.vue')
const Envdata = () => import('@/views/envdata/index.vue')
const Irrigation = () => import('@/views/irrigation/index.vue')
const Fertilizer = () => import('@/views/fertilizer/index.vue')
const Pesticide = () => import('@/views/pesticide/index.vue')
const Pollination = () => import('@/views/pollination/index.vue')
const Pruning = () => import('@/views/pruning/index.vue')
const Harvest = () => import('@/views/harvest/index.vue')
const Grading = () => import('@/views/grading/index.vue')
const Packing = () => import('@/views/packing/index.vue')
const Shipping = () => import('@/views/shipping/index.vue')
const Nutrient = () => import('@/views/nutrient/index.vue')
const Lighting = () => import('@/views/lighting/index.vue')
const Co2 = () => import('@/views/co2/index.vue')
const Sensor = () => import('@/views/sensor/index.vue')
const Failure = () => import('@/views/failure/index.vue')
const BatchTrace = () => import('@/views/batch_trace/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/crop', name: 'crop', component: Crop },
    { path: '/zone', name: 'zone', component: Zone },
    { path: '/envdata', name: 'envdata', component: Envdata },
    { path: '/irrigation', name: 'irrigation', component: Irrigation },
    { path: '/fertilizer', name: 'fertilizer', component: Fertilizer },
    { path: '/pesticide', name: 'pesticide', component: Pesticide },
    { path: '/pollination', name: 'pollination', component: Pollination },
    { path: '/pruning', name: 'pruning', component: Pruning },
    { path: '/harvest', name: 'harvest', component: Harvest },
    { path: '/grading', name: 'grading', component: Grading },
    { path: '/packing', name: 'packing', component: Packing },
    { path: '/shipping', name: 'shipping', component: Shipping },
    { path: '/nutrient', name: 'nutrient', component: Nutrient },
    { path: '/lighting', name: 'lighting', component: Lighting },
    { path: '/co2', name: 'co2', component: Co2 },
    { path: '/sensor', name: 'sensor', component: Sensor },
    { path: '/failure', name: 'failure', component: Failure },
    { path: '/batch_trace', name: 'batch_trace', component: BatchTrace },
  ],
})

export default router
