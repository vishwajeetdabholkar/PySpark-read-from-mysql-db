def read_from_mysql_db(table_name, db_name):
    df = sqlContext.read.format('jdbc').options(
          url='jdbc:mysql://localhost/'+db_name,
          driver='com.mysql.jdbc.Driver',
          dbtable= table_name,
          user='db_username',
          password='db_password').load()
    return df
    
source_df = read_from_mysql_db('table_name','db_name')
source_df.show()


def save_to_mysql_db(df,table_name, db_name):
    df.write.format('jdbc').options(
          url='jdbc:mysql://localhost/'+db_name,
          driver='com.mysql.jdbc.Driver',
          dbtable= table_name,
          user='db_username',
          password='db_password').mode('append').save()
