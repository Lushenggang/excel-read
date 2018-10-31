# coding:utf-8
import os
import os.path

lstLarge = [
  "gov",            # 外催机构
  "No",             # 案件号
  "getStyle",       # 委托外催方式
  "name",           # 姓名
  "cardNo",         # 卡号
  "account",        # 账号
  "cityBank",       # 城市分行
  "date",           # 交易日期
  "repayment",      # 还款金额
  "money",          # 业绩金额
  "restMoney",      # 当天委案剩余金额
  "sysRest",        # 系统剩余金额
  "helpDate",       # 委托日期
  "satisfied",      # 是否满意
  "handTimes",      # 手数
  "moneyType",      # 币种
  "repayType",      # 还款类型
  "origin",         # 案件来源
  "smark",          # 交易描述
  "delay",          # 委案时拖欠周期
  "trueMoney",      # 实际委案金额
  "repayDays",      # 还款天数
  "special",        # 特殊账户标记
  "dollarRate",     # 美元汇率
  "computedMoney",  # 算后业绩金额
  "common",         # 共债标识
  "dataDate",       # 数据日期
  "inAccountDate",  # 入账日期
]

lstSmall = [
  "RowNo",          # 序号
  "gov",            # 外催机构
  "batch",          # 批次
  "helpDate",       # 委托日期
  "name",           # 姓名
  "cardNo",         # 卡号
  "IDcard",         # 身份证号
  "helpMoney",      # 委案金额
  "litigationPrice",# 诉讼费用
  "litigationDaTE", # 诉讼受理日期
  "invoiceDate",    # 发票时间
  "caseNo",         # 案件号
]

lstMerge = [
  "gov",            # 外催机构
  "helpDate",       # 委托日期
  "name",           # 姓名
  "cardNo",         # 卡号
  "account",        # 账号
  "date",           # 交易日期
  "inAccountDate",  # 入账日期
  "repayment",      # 还款金额
  "helpMoney",      # 实际计算金额
  "helpRate",       # 佣金费率
  "helpMoney2",     # 佣金
  "pay",            # 支付对象
]

def ReadSmall():
  file = open('small.txt', 'r')
  lstLines = file.readlines()
  lstLines = lstLines[2:]
  lstData = []
  for idx in range(len(lstLines)):
    line = lstLines[idx]
    lst = line.split('\t')
    data = {}
    for index in range(len(lstSmall)):
      value = ''
      if index < len(lst):
        value = lst[index].replace(' ', '')
        value = value.replace('\n', '')
      data[lstSmall[index]] = value
    lstData.append(data)
  return lstData

def ReadLarge():
  file = open('large.txt', 'r')
  lstLines = file.readlines()
  lstLines = lstLines[1:]
  lstData = []
  for idx in range(len(lstLines)):
    line = lstLines[idx]
    lst = line.split('\t')
    data = {}
    for index in range(len(lstLarge)):
      value = ''
      if index < len(lst):
        value = lst[index].replace(' ', '')
        value = value.replace('\n', '')
      data[lstLarge[index]] = value
    lstData.append(data)
  return lstData

def MergeInfo():
  smallList = ReadSmall()
  largeList = ReadLarge()
  print(largeList[0])
  # return
  lstData = []
  for idx in range(len(smallList)):
    data = {}
    smallData = smallList[idx]
    if not smallData["cardNo"]:
      continue
    flag = 0
    for index in range(len(largeList)):
      largeData = largeList[index]
      if largeData["cardNo"] == smallData["cardNo"] and largeData['name'] == smallData['name']:
        flag = 1
        for key in lstMerge:
          # print(smallData)
          value = largeData.get(key)
          if value is None:
            value = smallData.get(key) 
            if value:
              value = '小表：' + value
          if value is None:
            value = ''
          data[key] = value
        lstData.append(data)
        break
      elif (largeData["cardNo"] == smallData["cardNo"] or largeData['name'] == smallData['name']):
        print(largeData["cardNo"], smallData["cardNo"], largeData["name"], smallData["name"])
    if not flag:
      for key in lstMerge:
        value = smallData.get(key)
        if value is None:
          value = ''
        data[key] = value
      lstData.append(data)
  # print(lstData)
  lstLines = []
  for idx in range(len(lstData)):
    data = lstData[idx]
    lst = []
    for key in lstMerge:
      print(data.get(key))
      value = data.get(key) or ''
      lst.append(value)
    line = '\t'.join(lst)
    line = line + '\n'
    lstLines.append(line)
  print('~~~~~~~~~~~')  
  print(lstLines)
  print('~~~~~~~~~~~')
  file = open('merge.txt', 'w+')
  file.writelines(lstLines)
  file.close()
MergeInfo()

