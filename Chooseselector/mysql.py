import pymysql as mdb
# 所有数据库操作


def savetopice(topic):
    con = mdb.connect(host='localhost', user='root', passwd='949494', db='test', charset='utf8');
    with con:
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO choiceselector(question,choice_A,choice_B,choice_C,choice_D,choice_ABCD,answer) SELECT '" + topic[0] + "','" + topic[1] + "','" + topic[2] + "','" + topic[3] + "','" + topic[4] + "','" + topic[1]+topic[2]+topic[3]+topic[4] + "','" + topic[5] + "' FROM DUAL WHERE NOT EXISTS(SELECT * FROM choiceselector WHERE question='" + topic[0] + "')")
        except:
            pass

