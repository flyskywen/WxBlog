# 报错了，这是因为Django在连接MySQL数据库时默认使用的是MySqldb驱动，
# 然而我们没有安装该驱动，因为它并不支持Python3，我们现在安装的是PyMySQL驱动
# import pymysql
#
# pymysql.install_as_MySQLdb()


# 暂时用sqlite测试
# 而且django2.2不支持pymysql模块
