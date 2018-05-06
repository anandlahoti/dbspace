#
# Example :
# 
# python3 json2csv.py -u xxx -p xxxxxx -f xxxx -t xxxxxx
#
# Using REST API
#
#!/usr/bin/python3
import os, json
import csv
import sys, getopt
import pymysql
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

db_username='xxxxxxxx'
db_password='xxxx'
db_name='xxxxx'
rest_api_endpoint='https://xxxxxxxxxxxxxxxx/'
authentication_url='https:/xxxxxxxxxxxxx'
mysql_endpoint='xxxxxxxxxxxxxxx'

def main(argv):   
   auth_username = ''
   auth_password = ''
   from_date = ''
   to_date = ''

   try:
      opts, args = getopt.getopt(argv,"h:u:p:f:t:")
   except getopt.GetoptError:
      print('json2csv.py -r <GET-TIC-TOF-REST-API-ENDPOINT> -m <MYSQL-ENDPOINT>')
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print('json2csv.py -r <GET-TIC-TOF-REST-API-ENDPOINT> -m <MYSQL-ENDPOINT>')
         sys.exit()
      elif opt in ("-u"):
         auth_username = arg
      elif opt in ("-p"):
         auth_password = arg
      elif opt in ("-f"):
         from_date = arg
      elif opt in ("-t"):
         to_date = arg  
   print('mysql_endpoint is', mysql_endpoint)
   print('rest_api_endpoint is', rest_api_endpoint)
   mysqlconnection(mysql_endpoint)

def mysqlconnection(mysql_endpoint):
  try:
    conn = pymysql.connect(mysql_endpoint, user=db_username, passwd=db_password, db=db_name, connect_timeout=15)
    print(conn)
  except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

  logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
  with conn.cursor() as cur:
        empids = cur.execute("""select xxx from xxxxx""")
        cur.fetchall()           
        print("Total No. of employees in EMP_BASE:", empids)

def EmployeeCase(empids):
    print("setUpClass")

    #Run Connection API
    headers = {'Accept': 'application/json','Content-Type': 'application/json',}
    data = {"username": auth_username, "password" : auth_password}
    print(headers)
    try:                
        response = requests.post(authentication_url, headers=headers, data=data)
            
        if "200" not in str(response):
            AssertionError     
        else:  
            print("Response received") 
            string = response.text
            json_obj = json.loads(string)
            idToken= json_obj["AuthenticationResult"]["IdToken"]    #get token
    except requests.exceptions.RequestException as e:
        print(e)   
        AssertionError


    tick_headers ={'Accept': 'application/json','Content-Type': 'application/json','Authorization': str(idToken)}
        
    params = (('fromdate', '2017-12-01'),('todate', '2017-12-31'),)
    #read index for employee list and create expected
    for index in range(len(empids.ids)):
        tick_url=rest_api_endpoint+instance.ids[index]+'?fromdate=2017-12-01&todate=2017-12-31'
        print("---------------")
        tick_response = requests.get(tick_url, headers=tick_headers)
        path_to_json = print(tick_response.text)
        print("__________")

def conver2csv(path_to_json):

# this finds our json files
#path_to_json = print(tick_response.text)
#json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    data = []
# we need both the json and an index number so use enumerate()
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_text = json.load(json_file)
            employeeid = os.path.splitext(js)[0]
            for i, employeedata in enumerate(json_text['xxxxxxxxx']):
            # here you need to know the layout of your json and each json has to have
            # the same structure (obviously not the structure I have here)
                data.append([str(xxxxxx), str(employeedata['xxx']), str(employeedata['xxx']), str(employeedata['xxxx'])])
    
    wtr = csv.writer(open ('xxxxx.csv', 'w'), delimiter=',', lineterminator='\n')
    wtr.writerow(['xxxxxx', 'xxxxx', 'xxx', 'xxxx'])
    for x in data : wtr.writerows([x])

if __name__ == "__main__":
   main(sys.argv[1:])
