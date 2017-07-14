#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import fileinput
import csv
import simplejson as json

result = {}
lineDic = {}
logFiles = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.log']
#print(logFiles)
with fileinput.input(files=(logFiles)) as f:
	sum = 0
	for line in f:
		lineDic = json.loads(line[1:-2])
		user_key = lineDic["sNetNo"]
		ser_value = result.setdefault(user_key, 0)
		result[user_key] += 1
		sum += 1
		if fileinput.isfirstline():
			per_count = 1
			print("开始扫描文件", fileinput.filename())
		per_count += 1
		if per_count % 10000 == 0:
			print("已经扫描了", per_count, "行.")
	print("已经扫描了", per_count - 1, "行. ")
print("共扫描了", len(logFiles), "个文件.", sum, "行数据. 扫描完毕!")

with open('result.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')
	for item in result.items():
		spamwriter.writerow(item)
print("结果已经保存到 result.txt , 共写入了", len(result), "行数据!")