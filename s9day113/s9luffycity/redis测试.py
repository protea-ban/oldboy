"""
-----> 第一版
{
    luffy_shopping_car:{
        6:{
            11:{
                'title':'21天入门到放弃',
                'src':'xxx.png'
            },
            12:{
                'title':'21天入门到放弃',
                'src':'xxx.png'
            }
        }
    }
}
-----> 第二版 此版本更方便进行删除与更改
{
    luffy_shopping_car_6_11:{
        'title':'21天入门到放弃',
         'src':'xxx.png'
    },
    luffy_shopping_car_6_12:{
        'title':'21天入门到放弃',
         'src':'xxx.png'
    },
    luffy_shopping_car_6_14:{
        'title':'21天入门到放弃',
         'src':'xxx.png'
    }
}
"""

import redis
import json


conn = redis.Redis(host="127.0.0.1", port=6379)

# 删除所有键
# conn.flushall()

# 添加课程
# redis_key = "luffy_shopping_car_%s_%s"%(6, 13)
# conn.hmset(redis_key, {"title":"23天从入门到放弃", "src":"x3.png"})

# 删除课程
# conn.delete('luffy_shopping_car_7_12')
# print(conn.keys())

# 修改课程
# conn.hset('luffy_shopping_car_6_12', 'src', 'x1.png')
# print(conn.hget('luffy_shopping_car_6_12', 'title'))

# 查看所有课程
# print(conn.keys("luffy_shopping_car_6_*"))  # redis支持通配符
# for item in conn.scan_iter("luffy_shopping_car_6_*", count=10):
#     course = conn.hgetall(item)
#     print(course)

course_title = conn.hget("luffy_shopping_car_6_12", 'title')
# print(type(course_title.decode('utf-8')))
print(course_title.decode('utf-8'))

