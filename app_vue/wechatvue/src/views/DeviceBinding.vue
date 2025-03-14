<template>
  <div class="device-binding">
    <div class="container">
      <div class="page-header">
        <h1>设备管理中心</h1>
      </div>

      <el-row :gutter="20">
        <!-- 左侧绑定表单 -->
        <el-col :xs="24" :sm="24" :md="10" :lg="8">
          <div class="card binding-form">
            <h2>添加新设备</h2>
            <el-form :model="bindingForm" :rules="rules" ref="bindingForm" label-position="top">
              <el-form-item label="设备ID" prop="deviceId">
                <el-input
                  v-model="bindingForm.deviceId"
                  placeholder="请输入设备ID"
                  prefix-icon="el-icon-cpu"
                >
                </el-input>
              </el-form-item>
              <el-form-item label="设备密码" prop="password">
                <el-input
                  v-model="bindingForm.password"
                  type="password"
                  placeholder="请输入设备密码"
                  prefix-icon="el-icon-lock"
                  show-password
                >
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="handleBinding" class="submit-btn">
                  绑定设备
                </el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-col>

        <!-- 右侧设备列表 -->
        <el-col :xs="24" :sm="24" :md="14" :lg="16">
          <div class="card device-list">
            <div class="card-header">
              <h2>已绑定设备</h2>
              <span class="device-count">共 {{ mockDevices.length }} 台设备</span>
            </div>

            <div v-if="mockDevices.length" class="device-table">
              <el-table
                :data="mockDevices"
                style="width: 100%"
                :header-cell-style="{ background: '#f5f7fa' }"
                :height="cardHeight - 100"
              >
                <el-table-column prop="deviceId" label="设备ID" min-width="120">
                  <template #default="{ row }">
                    <div class="device-id">
                      <el-icon><Monitor /></el-icon>
                      <span>{{ row.deviceId }}</span>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column prop="bindTime" label="绑定时间" min-width="160">
                  <template #default="{ row }">
                    <span class="bind-time">{{ row.bindTime }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="操作" width="100" fixed="right">
                  <template #default="scope">
                    <el-button type="danger" link @click="handleUnbind(scope.row)">
                      解除绑定
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>

            <div v-else class="empty-state">
              <el-empty description="暂无绑定设备"></el-empty>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Monitor } from '@element-plus/icons-vue'
import { useRoute } from 'vue-router';
import request from '@/utils/request';

export default {
  name: 'DeviceBinding',
  components: {
    Monitor,
  },
  setup() {
    const cardHeight = ref(500) // 设置一个初始值

    const updateCardHeight = () => {
      const viewportHeight = window.innerHeight
      const headerHeight = 100
      const padding = 40
      cardHeight.value = viewportHeight - headerHeight - padding
    }

    onMounted(() => {
      updateCardHeight()
      window.addEventListener('resize', updateCardHeight)
    })

    onBeforeUnmount(() => {
      window.removeEventListener('resize', updateCardHeight)
    })

    // 获取传送过来的openid
    const route = useRoute();
    // 从查询参数中获取 openid
    const openid = route.query.openid;

    return {
      cardHeight,openid
    }
  },
  data() {
    return {
      bindingForm: {
        deviceId: '',
        password: '',
      },
      rules: {
        deviceId: [
          { required: true, message: '请输入设备ID', trigger: 'blur' },
          { min: 6, message: '设备ID长度不能小于6位', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入设备密码', trigger: 'blur' },
          { min: 6, message: '密码长度不能小于6位', trigger: 'blur' },
        ],
      },
      mockDevices: [
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 10:00:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
        {
          deviceId: 'Y23170000003',
          bindTime: '2024-03-15 11:30:00',
        },
      ],
    }
  },
  mounted() {
    this.updateCardHeight()
    window.addEventListener('resize', this.updateCardHeight)
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.updateCardHeight)
  },
  methods: {
    async handleBinding() {
      // ElMessage.success("绑定设备")
      this.$refs["bindingForm"].validate((valid) => {
          if(valid){
            // ElMessage.success("发送请求")
            // ElMessage.success(this.openid)
            // ElMessage.success(this.bindingForm.deviceId + this.bindingForm.password)
            request({
              method:"post",
              url:"/wechat/bind_device",
              params:{
                deviceId: this.bindingForm.deviceId,
                password: this.bindingForm.password,
                openid:this.openid
              }
            }).then((res) => {
              ElMessage.success("回调成功")
              if(res.code === 200){
                ElMessage.success('设备绑定成功')
              }else{
                ElMessage.error(res.message)
              }
            })
          }else{
            ElMessage.error("验证失败")
          }
      })
      try {
        await this.$refs.bindingForm.validate()
        this.mockDevices.unshift({
          deviceId: this.bindingForm.deviceId,
          bindTime: new Date().toLocaleString(),
        })
        this.$refs.bindingForm.resetFields()
      } catch (error) {
        ElMessage.error('请检查输入信息')
      }
    },
    async handleUnbind(device) {
      try {
        await ElMessageBox.confirm(`确认解除设备 ${device.deviceId} 的绑定？`, '解除绑定', {
          confirmButtonText: '确认解除',
          cancelButtonText: '取消',
          type: 'warning',
        })
        const index = this.mockDevices.findIndex((d) => d.deviceId === device.deviceId)
        if (index > -1) {
          this.mockDevices.splice(index, 1)
        }
        ElMessage.success('设备解绑成功')
      } catch (error) {
        if (error !== 'cancel') {
          ElMessage.error('操作失败')
        }
      }
    },
    updateCardHeight() {
      // 计算可用高度（减去页面头部和内边距）
      const viewportHeight = window.innerHeight
      const headerHeight = 100 // 页面标题的大约高度
      const padding = 40 // 上下内边距总和
      this.cardHeight = viewportHeight - headerHeight - padding
    },
  },
}
</script>

<style scoped>
.device-binding {
  padding: 20px 0;
  min-height: 100vh;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
}

.page-header h1 {
  font-size: 28px;
  color: var(--primary-color);
  margin: 0;
}

.subtitle {
  color: #666;
  margin-top: 8px;
}

.card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: 24px;
  height: 100%;
  box-sizing: border-box;
}

.card h2 {
  font-size: 20px;
  margin: 0 0 24px;
  color: var(--text-color);
}

.binding-form {
  margin-bottom: 20px;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  font-size: 16px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.device-count {
  color: #666;
  font-size: 14px;
}

.device-id {
  display: flex;
  align-items: center;
  gap: 8px;
}

.bind-time {
  color: #666;
}

.empty-state {
  padding: 40px 0;
}

.device-list {
  height: v-bind(cardHeight + 'px');
  display: flex;
  flex-direction: column;
}

.device-table {
  flex: 1;
  overflow: hidden;
}

.el-table {
  height: 100% !important;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .device-list {
    height: v-bind(cardHeight * 0.8 + 'px');
  }
}
</style>
