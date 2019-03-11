# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 【配套电子书】网址：
#       百度阅读：
#       https://yuedu.baidu.com/ebook/5823871e59fafab069dc5022aaea998fcc2240fc
# 代码文件：chapter9/ch9.4.5.py

input_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

output_dict = {k: v for k, v in input_dict.items() if v % 2 == 0}
print(output_dict)

keys = [k for k, v in input_dict.items() if v % 2 == 0]
print(keys)
