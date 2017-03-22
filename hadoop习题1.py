#coding:utf-8
import sys

pre_product_no = ""
pre_lac_id = ""
pre_start_time = ""
pre_staytime = 0
pre_moment = ""
pre_user_id = ""
pre_country_id = ""
pre_city_id = ""

def process(line):
	global pre_product_no
	global pre_lac_id
	global pre_row_list
    global pre_staytime
    global pre_moment
    global pre_user_id
    global pre_country_id
    global pre_city_id

	if line.strip() == "clearbuffer":
		printResult() #输出最后一个数据
		return 0

	row_list = line.strip().split('\t')
	product_no = row_list[0]
	start_time = row_list[1]
	lac_id = row_list[2]
	staytime = row_list[3]
	moment = row_list[4] 
	user_id = row_list[5]
	country_id = row_list[6]
	city_id = row_list[7]

	if pre_produce_no == "" or (pre_product_no == product_no and pre_lac_id =lac_id):
		pre_staytime = pre_staytime + staytime
    else:
    	printResult()
    	pre_staytime = staytime

    pre_product_no = product_no 
	pre_lac_id = lac_id
	pre_start_time = start_time
	pre_moment = moment
	pre_user_id = user_id
	pre_country_id = country_id
	pre_city_id = city_id

def printResult():
	global pre_product_no
	global pre_lac_id
	global pre_row_list
    global pre_staytime
    global pre_moment
    global pre_user_id
    global pre_country_id
    global pre_city_id

    row_list=[pre_product_no,pre_lac_id,pre_row_list,pre_staytime,pre_moment,pre_user_id,pre_country_id,pre_city_id]
    print(row_list.join('\t'))

if __name__ == "__main__":
	for line in sys.stdin:
		process(line)
	process




