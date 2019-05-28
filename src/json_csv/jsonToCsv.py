import json
import csv

#解析json字符串
def jsonStrAnalysis():
    json_str = '{"common_status":"30","refund_status":"0","order_id":"810768553445776"}'
    data_dict = json.loads(json_str)
    print(data_dict)
    print(data_dict['common_status'])
    #'add_date'字段存在则返回，不存在则
    print(data_dict.get('add_date',-1))


#转化json文件为csv
def jsonToCsv():
    #newline 换行符 encoding 编码方式
    csvfile = open('./data/csvdata.csv', 'w', newline='', encoding='utf-8')
    #csvfile = open('./data/csvdata.csv', 'wb') python 2
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    flag = True
    #一个文件里有多行json只能逐行读取
    with open('./data/data.json', 'r') as f:
        for line in f:
            dict = json.loads(line)
            if flag:
                keys = list(dict.keys())
                writer.writerow(keys)
                flag = False
            writer.writerow(list(dict.values()))
    csvfile.close()


#只读取指定字段的信息
def jsonToCsvByKey():
    csvfile = open('./data/csvdata1.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
    with open('./data/data1.json', 'r') as f:
        keys= ['id','common_status','order_id','x','y']
        writer.writerow(keys)
        i=1
        for line in f:
            dict = json.loads(line)
            coordinates=dict.get('coordinates')
            x,y=0,0
            #coordinates字段不一定存在，需要判断
            if(coordinates):
                x = coordinates[0]
                y = coordinates[1]
            writer.writerow([i,dict[keys[1]],dict['order_id'],x,y])
            i = i+1
    csvfile.close()




