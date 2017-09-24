import csv
from math import floor
stock_lst = []
flag = 0

code_t = ""
max_time_gap_t=-999
volume_t = 0
max_trade_t = 0
weighted_avg_price_t = 0
    
class Stock:
    code = ""
    max_time_gap=0
    prev_ts = 0
    curr_ts = 0
    volume = 0
    max_trade = 0
    weighted_avg_price = 0
    
    def __init__(self, stock_code, timestamp, volume, trading_price, weighted_avg_price):
        
        self.code = stock_code
        self.prev_ts = self.curr_ts
        self.curr_ts = timestamp
        self.volume = volume
        
        self.max_trade = trading_price
        self.weighted_avg_price = weighted_avg_price
        
    def displayVolume(self):
        print("Total Employee %d" % Stock.volume)

    def displayStock(self):
        print("Name : ", self.code,  ", Maximum Time Gap: ", self.max_time_gap, ",  Volume : ", self.volume, ", Weighted Average : ", self.weighted_avg_price, " , MaxTrade : ", self.max_trade)
        
    def updateStock(self, stock_code, timestamp, volume, trading_price, weighted_avg_price):        
        weighted_avg_price_old = self.weighted_avg_price
        volume_old =self.volume
        
        print('****** Inside Update Stock Method ********')
        print('Updating Stock : ', self.code)
        ##Update Weighted Average Price
        print('Old Weighted Average : ', weighted_avg_price_old, ' , Old Volume : ',volume_old )
        self.weighted_avg_price = ((volume_old * weighted_avg_price_old + volume  * trading_price)/(volume + volume_old))
        print('New Weighted Average : ', self.weighted_avg_price)
        ##Update Volume
        self.volume = int(self.volume) + int(volume)
        
        ##Update Maximum traded price
        if int(self.max_trade) < trading_price:
            self.max_trade = trading_price
        
        ##Update current and new values of timestamp
        self.prev_ts = self.curr_ts
        self.curr_ts = timestamp
        temp_time_stamp_difference = self.curr_ts - self.prev_ts
        
        if temp_time_stamp_difference > self.max_time_gap:
            self.max_time_gap = temp_time_stamp_difference 
        
        
        
with open('E:\input1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    stock_master = []
    temp1 = []
    temp2 = []
    
    
    for row in readCSV:
        stock_t = Stock(row[1], int(row[0]), int(row[2]), int(row[3]), int(row[3]))
        if flag== 0:
            stock_lst.append(row[1])            
            stock_master.append(stock_t)
            flag = 1
            print(stock_master[0].displayStock())
        else:
            print("Next item traversal starts...")
            try:
                stock_index = stock_lst.index(row[1])
                print('Stock index of ', row[1], ' is :', stock_index)
                weighted_avg_price_old = stock_master[stock_index].weighted_avg_price
                
                volume_old = stock_master[stock_index].volume
                print('weighted_avg_price_old : ', weighted_avg_price_old, ' , Old Volume : ', volume_old)
                
                stock_master[stock_index].updateStock(row[1], int(row[0]), int(row[2]), int(row[3]), int(row[3]))
                print(stock_master[stock_index].displayStock())
            except:
                stock_lst.append(row[1])
                print('The given stock : ', row[1] ,' is being updated')
                stock_master.append(stock_t)
                stock_master[-1].displayStock() 
    
                        
    print(stock_lst)
    
    for i in range(0,len(stock_master),1):
        stock_master[i].weighted_avg_price = floor(stock_master[i].weighted_avg_price)
        
    stock_master.sort(key= lambda x: x.code, reverse=False)
    for item in stock_master:
        print(item.displayStock())    

