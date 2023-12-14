from flask import Flask, render_template, request
import pymysql
import requests

# 测试是否更新到代码
app = Flask(__name__)


@app.route("/HeroClub/index")
def show_checklist():
    # 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="shujukutiancai9527", charset='utf8',  db='checkindata')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 发送指令
    sql = "select * from online_check_in"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    # 关闭连接
    cursor.close()
    conn.close()

    print(data_list)
    return render_template("hero.html", data_list=data_list)


@app.route("/HeroClub/Study_Use", methods=["POST"])
def upload_data_study():
    # 1、获取json中的time
    study_time = request.get_json()["time"]
    # print(study_time)
    # 2、将time写入数据库
    # 2.1 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="shujukutiancai9527", charset='utf8',  db='checkindata')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.2 发送指令
    sql = "insert into online_check_in(study_use) values (%s)"
    cursor.execute(sql, [study_time])
    conn.commit()
    # 判断是否坚持了一天
    check_sql = "select * from online_check_in where ID = ( select MAX(ID) from online_check_in )"
    cursor.execute(check_sql)
    check_data_list = cursor.fetchall()
    check_study_use = check_data_list['study_use']
    check_strong_use = check_data_list['strong_use']
    MAX_ID = check_data_list['ID']
    print(check_study_use, check_strong_use)
    if check_study_use and check_strong_use is None:
        return("打卡成功！")
    else:
        if check_study_use > 3600 and check_strong_use > 1800:
            Second_ID = MAX_ID - 1
            print(Second_ID)
            check_stilled_day_sql = "select still_day from online_check_in where ID = %s"
            cursor.execute(check_stilled_day_sql, [Second_ID])
            stilled_day_value = cursor.fetchall()
            stilled_day = stilled_day_value['still_day']
            new_still_day = stilled_day + 1
            update_stillday_sql = "UPDATE `checkindata`.`online_check_in` SET `still_day` = %s WHERE `ID` = %s"
            cursor.execute(update_stillday_sql, [new_still_day, MAX_ID])
            conn.commit()
            return ("打卡成功！")
        else:
            update_stillday_sql_2 = "UPDATE `checkindata`.`online_check_in` SET `still_day` = 0 WHERE `ID` = %s"
            cursor.execute(update_stillday_sql_2, [MAX_ID])
            conn.commit()
            return ("打卡成功！")
    # 2.3 关闭连接
    cursor.close()
    conn.close()

    # return ("添加成功")


@app.route("/HeroClub/Strong_Use", methods=["POST"])
def upload_data_Strong():
    # 1、获取json中的time
    strong_time = request.get_json()["time"]
    # print(study_time)
    # 2、将time写入数据库
    # 2.1 连接MySQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="shujukutiancai9527", charset='utf8',  db='checkindata')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 2.2 发送指令
    sql = "insert into online_check_in(strong_use) values (%s)"
    cursor.execute(sql, [strong_time])
    conn.commit()
    # 判断是否坚持了一天
    check_sql = "select * from online_check_in where ID = ( select MAX(ID) from online_check_in )"
    cursor.execute(check_sql)
    check_data_list = cursor.fetchall()
    check_study_use = check_data_list['study_use']
    check_strong_use = check_data_list['strong_use']
    MAX_ID = check_data_list['ID']
    print(check_study_use, check_strong_use)
    if check_study_use and check_strong_use is None:
        return("打卡成功！")
    else:
        if check_study_use > 3600 and check_strong_use > 1800:
            Second_ID = MAX_ID - 1
            print(Second_ID)
            check_stilled_day_sql = "select still_day from online_check_in where ID = %s"
            cursor.execute(check_stilled_day_sql, [Second_ID])
            stilled_day_value = cursor.fetchall()
            stilled_day = stilled_day_value['still_day']
            new_still_day = stilled_day + 1
            update_stillday_sql = "UPDATE `checkindata`.`online_check_in` SET `still_day` = %s WHERE `ID` = %s"
            cursor.execute(update_stillday_sql, [new_still_day, MAX_ID])
            conn.commit()
            return ("打卡成功！")
        else:
            update_stillday_sql_2 = "UPDATE `checkindata`.`online_check_in` SET `still_day` = 0 WHERE `ID` = %s"
            cursor.execute(update_stillday_sql_2, [MAX_ID])
            conn.commit()
            return ("打卡成功！")
    # 2.3 关闭连接
    cursor.close()
    conn.close()

    # return ("添加成功")


if __name__ == '__main__':
    app.run()
