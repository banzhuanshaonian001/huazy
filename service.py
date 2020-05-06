#coding=utf-8
#from grovepi import *

import requests
import sys
import json
import math
import Adafruit_DHT

	
def  get_tem_hum_by_yueqie():  #get temp and hum by huazy  
    print("")
    print("开始获取温湿度...")
    y,x= Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
    if x is None: 
        x = 0
        print("获取温度失败")
    if y is None:
        y = 0
        print("获取湿度失败")
    print("获取结束..")
    return x,y

def calculateData(data):
	avgTemp = 0
	avgHum = 0
	#maxTemp = -sys.maxint - 1
	#maxHum = -sys.maxint - 1 
	#minTemp = sys.maxint
	#minHum = sys.maxint

	maxTemp = -sys.maxsize - 1
	maxHum = -sys.maxsize - 1 
	minTemp = sys.maxsize
	minHum = sys.maxsize
	sumTemp = 0
	sumHum = 0
	for value in data:
		temp = value.get("temp")
		hum = value.get("hum")
		if temp > maxTemp:
			maxTemp = temp
		if hum > maxHum: 
			maxHum = hum
		if temp < minTemp and temp != 0:
			minTemp = temp
		if hum < minHum and temp != 0:
			minHum = hum
		sumTemp += temp
		sumHum += hum
	avgTemp = sumTemp / len(data)
	avgHum = sumHum / len(data)

	return [{"key":"temp", "data":[{"avg":avgTemp, "max":maxTemp, "min": minTemp}]}, {"key":"hum", "data":[{"avg":avgHum, "max":maxHum, "min": minHum}]}]


def sendRequest(data):
        print("调用fogcell项目....")
	host = "http://172.17.0.1:8081"
	data_str = json.dumps(data) 
	print(host+"/compunit/serviceData - data:"+data_str)
	response = requests.post(host+"/compunit/serviceData", data=data_str, headers={"Content-Type": "application/json"})
	print(response.text)


# -------------------------------------------------------------------------------------------------------------------------------------------------

dht_sensor_port = 7             # Connect the DHt sensor to port 7
dht_sensor_type = 0             # change this depending on your sensor type - see header comment

data = []
counter = 0
#MAX = 200
MAX = 3
while True:
    try:
        #[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)             #Get the temperature and Humidity from the DHT sensor
        [ temp,hum ] = get_tem_hum_by_yueqie()     # get tem and hum by  huazy
        #temp = 0
        #hum = 0
        print("进入判断温温度环节....") 
        if temp ==0  or temp == 0  :
            print("数据无效")
            print("")
            continue 

        print("temp =", temp, "C, humidity =", hum,"%")

        # calculate the average, max, min of a specific size of measurements and send it to the cloud
        data.append({"temp": temp, "hum": hum})
        counter = counter + 1
        print("%d"%counter)
        if counter > MAX:
            counter = 0
            calculatedData = calculateData(data)
            sendRequest(calculatedData)
           # counter = 0
    except (IOError,TypeError) as e:
        print("Error:"+str(e))
