import pymysql
import MySQLdb

class MySqlOpr:
    def __init__(self, username='root', passname='123456', ip='localhost', datebasename='test', ipport=3306):
        try:
            self.connStatus = '未连接'  # 连接状态
            self.queryStatus = 0  # 查询状态
            self.updateStatus = 0  # 更新状态
            self.deleteStatus = 0  # 删除状态
            self.insertStatus = 0  # 插入状态
            self.__conn = ''
            self.__conn = MySQLdb.connect(host=ip, port=ipport, db=datebasename, user=username, passwd=passname,charset='utf8')
            self.connStatus = 0
        except MySQLdb.Error as e:
            self.connStatus = e

    def closeconnection(self):
        try:
            if self.__conn:
                self.__conn.close()
                self.connStatus = '连接已断开'
        except MySQLdb.Error as e:
            self.connStatus = e

    def query(self, table='groupinfo', queryby=''):
        self.queryStatus = 0
        result = ''
        cursor = ''
        title = ''
        try:
            sql = 'select * from ' + table + ' ' + queryby
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            title = [i[0] for i in cursor.description]
            cursor.close()
            cursor = ''
        except MySQLdb.Error as e:
            self.queryStatus = e
        finally:
            if cursor:
                cursor.close()
            return result

