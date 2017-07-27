#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import fileinput
import csv
import datetime

class UserInfo(object):
	def __init__(self, code, count):
		self.code = code
		self.count = count
	def getInfo(self):
		return self.code, self.count

result = {}
logFiles = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.getsize(x) > 0 and os.path.splitext(x)[1]=='.txt']
#print(logFiles)
with fileinput.input(files=(logFiles)) as f:
	sum = 0
	for line in f:
		lineDic = eval(line[1:-2])
		user_key = lineDic["sNetNo"]
		ser_value = result.setdefault(user_key, UserInfo(user_key, 0))
		ser_value.count += 1
		sum += 1
		if fileinput.isfirstline():
			per_count = 1
			print("开始扫描文件", fileinput.filename())
		per_count += 1
		if per_count % 10000 == 0:
			print("已经扫描了", per_count, "行.")
print("共扫描了", len(logFiles), "个文件.", sum, "行数据. 扫描完毕!")

now = datetime.datetime.now()
result_file = "result_" + now.strftime('%Y_%m_%d_%H_%M_%S') + ".csv"
with open(result_file, 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')
	for v in result.values():
		spamwriter.writerow(v.getInfo())
print("结果已经保存到,", result_file,  ". 共写入了", len(result), "行数据!")