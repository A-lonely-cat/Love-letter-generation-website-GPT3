import pymysql
def redom_select():

    connection = pymysql.connect(
        host='192.168.176.132',
        user='root',
        password='root',
        database='beautifulcopy'
        )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 获取表内数据量
        cursor.execute("SELECT COUNT(*) FROM copylist")
        data_count = cursor.fetchone()[0]

        # 随机查询
        cursor.execute("SELECT copy FROM copylist ORDER BY RAND() LIMIT 1")
        random_data = cursor.fetchone()
        return random_data[0]

    except pymysql.Error as e:

        return 0

    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()

