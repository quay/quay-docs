import pymysql.cursors        # python2-PyMySQL.noarch

# Connect to the database
connection = pymysql.connect(host='quay.quaylab.lan',
                             user='coreosuser',
                             password='notsecure',
                             db='enterpriseregistrydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT VERSION();"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
