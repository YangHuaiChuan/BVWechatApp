from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DATABASE

class BVWechatDB(object):
    def __init__(self): #创建对象同时要执行的代码 
        self.conn = connect(
            host = MYSQL_HOST,
            port = MYSQL_PORT,
            user = MYSQL_USERNAME,
            password = MYSQL_PASSWORD,
            database = MYSQL_DATABASE,
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor(DictCursor) #按照字典的形式返回
    
    def __del__(self): #释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()

    def get_device_info(self):
        sql = 'select * from bv_device_ainfo'
        data = []
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    def device_is_exist(self,device_id):
        sql = f"select * from bv_device_ainfo where user = '{device_id}';"
        data_count = self.cursor.execute(sql)
        if(data_count == 0):
            return False
        return True

    def deviceId_password_right(self,device_id,password):
        sql = f"select * from bv_device_ainfo where user = '{device_id}' and pwd = '{password}'"
        data_count = self.cursor.execute(sql)
        if(data_count == 0):
            return False
        return True

    def bind_device_openid(self,device_id,openid):
        sql = f"INSERT openid_deviceid VALUE('{device_id}','{openid}',NULL);"
        reslut = self.cursor.execute(sql)
        if reslut > 0:
            return True
        return False 


