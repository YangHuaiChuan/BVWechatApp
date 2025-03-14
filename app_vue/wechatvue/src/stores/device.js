import { defineStore } from 'pinia'
import axios from 'axios'

export const useDeviceStore = defineStore('device', {
  state: () => ({
    boundDevices: [],
    loading: false
  }),
  
  actions: {
    async fetchBoundDevices() {
      this.loading = true
      try {
        const response = await axios.get('/api/devices/bound')
        this.boundDevices = response.data
      } catch (error) {
        throw error
      } finally {
        this.loading = false
      }
    },

    async bindDevice(deviceData) {
      try {
        await axios.post('/api/devices/bind', deviceData)
        await this.fetchBoundDevices()
      } catch (error) {
        throw error
      }
    },

    async unbindDevice(deviceId) {
      try {
        await axios.post('/api/devices/unbind', { deviceId })
        await this.fetchBoundDevices()
      } catch (error) {
        throw error
      }
    }
  }
})