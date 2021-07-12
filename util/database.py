import pymysql

db = pymysql.connect(host="", user="football", password="", database="football")
cursor = db.cursor()
SQLex = 'SQL/'


def db_init():
    executeSQL("表")


def insertPlayer(table, name, country, role, speed, strength, defense, dribble, pass_, shoot):
    cursor.execute("use football;")
    if table == "球员":
        temp = "'"+name+"'" + ',' + "'"+country+"'" + ',' + "'"+role+"'" + ',' + "'"+speed+"'" + ',' + "'"+strength+"'" + ',' + "'"+defense+"'" + ',' + "'"+dribble+"'" + ',' +"'"+pass_+"'" + ',' + "'"+shoot+"'"
        sql = 'INSERT INTO ' + table + '(名称,国籍,位置,速度,力量,防守,盘带,传球,射门) VALUES(' + str(temp) + ');'
        cursor.execute(sql)
        cursor.connection.commit()
    return


def executeSQL(sql_name):
    with open(SQLex + sql_name + '.sql', encoding='utf-8', mode='r') as f:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            # 判断包含空行的
            if '\n' in x:
                # 替换空行为1个空格
                x = x.replace('\n', ' ')
            # 判断多个空格时
            if '    ' in x:
                # 替换为空
                x = x.replace('    ', '')
            # sql语句添加分号结尾
            sql_item = x + ';'
            # print(sql_item)
            cursor.execute(sql_item)
            print("执行成功sql: %s" % sql_item)


def ConnectMysql():
    cursor.execute("select version()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
