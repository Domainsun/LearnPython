# coding=gbk

# import pymysql
#
# # ��������
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='domaindb')
# # �����α�
# cursor = conn.cursor()
#
# # ִ��SQL����������Ӱ������
# effect_row = cursor.execute("select * from student")
# print(effect_row)
#
# print(cursor.fetchall())
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")

# ִ��SQL����������Ӱ������
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# ִ��SQL����������Ӱ������
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])


# �ύ����Ȼ�޷������½������޸ĵ�����
# conn.commit()
#
# # �ر��α�
# cursor.close()
# # �ر�����
# conn.close()