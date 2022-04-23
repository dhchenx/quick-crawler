# 存储到数据库中
from sqlalchemy import create_engine
import pandas as pd

mssql_db="USystem"
mssql_user="sa"
mssql_password="123456"
mssql_host="DESKTOP-EKA5VDD\\SQLEXPRESS"


engine = create_engine(
    'mssql+pymssql://' + mssql_user + ':' + mssql_password + '@' + mssql_host + '/' + mssql_db + '')  # 初始化数据库连接
print(engine.table_names())

csv_path="global_news_site_urls_lang.csv"
print("read")
df = pd.read_csv(csv_path, sep=',', encoding='utf-8', chunksize=100, iterator=True,
                 low_memory=False)

for chunk in df:
    chunk.to_sql('global_news_site', engine, if_exists='append', index=False)
    print(" running Write to sqlserver...")