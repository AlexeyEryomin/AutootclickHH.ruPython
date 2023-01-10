def get_job_ids(x, y): 

  import requests

  url = f"https://api.hh.ru/vacancies/?text=QA инженер&per_page={x}&page={y}"

  payload={}
  headers = {
  'Cookie': '__ddg1_=FwJ1xHbIfZSbyIEqZAU1; __ddg5_=dMGJBW5MBvd34iEV; hhtoken=ShN6UOBAZ0UsP9aJsPsg3NakVW55; hhuid=uB9hTejzPz!txWLc9JQwgA--'
  }

  request = requests.request("GET", url, headers=headers, data=payload)
  response = request.json()
  #print(response)


  ids = []
  for i in response['items']:
    ids.append(i['id'])
 
  #print(ids)

  return ids

all_ids_1 = []
k = 0

while k <= 100:
  z = get_job_ids(1, k)
  all_ids_1 = all_ids_1 + [z]
  k = k + 1

new_all_ids_1 = [x[0] for x in all_ids_1]
#print(all_ids)
#print(new_all_ids_1)


import time
time.sleep(30)


all_ids_2 = []
k = 101

while k <= 200:
  z = get_job_ids(1, k)
  all_ids_2 = all_ids_2 + [z]
  k = k + 1

new_all_ids_2 = [x[0] for x in all_ids_2]
#print(all_ids)
#print(new_all_ids_2)

import time
time.sleep(30)


all_ids_3 = []
k = 201

while k <= 300:
  z = get_job_ids(1, k)
  all_ids_3 = all_ids_3 + [z]
  k = k + 1

new_all_ids_3 = [x[0] for x in all_ids_3]
#print(all_ids)
#print(new_all_ids_3)


time.sleep(30)


all_ids_4 = []
k = 301

while k <= 400:
  z = get_job_ids(1, k)
  all_ids_4 = all_ids_4 + [z]
  k = k + 1

new_all_ids_4 = [x[0] for x in all_ids_4]
#print(all_ids)
#print(new_all_ids_4)



time.sleep(30)


all_ids_5 = []
k = 401

while k <= 500:
  z = get_job_ids(1, k)
  all_ids_5 = all_ids_5 + [z]
  k = k + 1

new_all_ids_5 = [x[0] for x in all_ids_5]
#print(all_ids)
#print(new_all_ids_5)


time.sleep(30)


all_ids_6 = []
k = 501

while k <= 600:
  z = get_job_ids(1, k)
  all_ids_6 = all_ids_6 + [z]
  k = k + 1

new_all_ids_6 = [x[0] for x in all_ids_6]
#print(all_ids)
#print(new_all_ids_6)


time.sleep(30)


all_ids_7 = []
k = 601

while k <= 700:
  z = get_job_ids(1, k)
  all_ids_7 = all_ids_7 + [z]
  k = k + 1

new_all_ids_7 = [x[0] for x in all_ids_7]
#print(all_ids)
#print(new_all_ids_7)


time.sleep(30)


all_ids_8 = []
k = 701

while k <= 800:
  z = get_job_ids(1, k)
  all_ids_8 = all_ids_8 + [z]
  k = k + 1

new_all_ids_8 = [x[0] for x in all_ids_8]
#print(all_ids)
#print(new_all_ids_8)


time.sleep(30)


all_ids_9 = []
k = 801

while k <= 900:
  z = get_job_ids(1, k)
  all_ids_9 = all_ids_9 + [z]
  k = k + 1

new_all_ids_9 = [x[0] for x in all_ids_9]
#print(all_ids)
#print(new_all_ids_9)


time.sleep(30)


all_ids_10 = []
k = 901

while k <= 1000:
  z = get_job_ids(1, k)
  all_ids_10 = all_ids_10 + [z]
  k = k + 1

new_all_ids_10 = [x[0] for x in all_ids_10]
#print(all_ids)
#print(new_all_ids_10)


time.sleep(30)


all_ids_11 = []
k = 1001

while k <= 1100:
  z = get_job_ids(1, k)
  all_ids_11 = all_ids_11 + [z]
  k = k + 1

new_all_ids_11 = [x[0] for x in all_ids_11]
#print(all_ids)
#print(new_all_ids_11)


time.sleep(30)


all_ids_12 = []
k = 1101

while k <= 1200:
  z = get_job_ids(1, k)
  all_ids_12 = all_ids_12 + [z]
  k = k + 1

new_all_ids_12 = [x[0] for x in all_ids_12]
#print(all_ids)
#print(new_all_ids_12)


time.sleep(30)


all_ids_13 = []
k = 1201

while k <= 1300:
  z = get_job_ids(1, k)
  all_ids_13 = all_ids_13 + [z]
  k = k + 1

new_all_ids_13 = [x[0] for x in all_ids_13]
#print(all_ids)
#print(new_all_ids_13)


time.sleep(30)


all_ids_14 = []
k = 1301

while k <= 1400:
  z = get_job_ids(1, k)
  all_ids_14 = all_ids_14 + [z]
  k = k + 1

new_all_ids_14 = [x[0] for x in all_ids_14]
#print(all_ids)
#print(new_all_ids_14)


time.sleep(30)


all_ids_15 = []
k = 1401

while k <= 1500:
  z = get_job_ids(1, k)
  all_ids_15 = all_ids_15 + [z]
  k = k + 1

new_all_ids_15 = [x[0] for x in all_ids_15]
#print(all_ids)
#print(new_all_ids_15)


time.sleep(30)


all_ids_16 = []
k = 1501

while k <= 1600:
  z = get_job_ids(1, k)
  all_ids_16 = all_ids_16 + [z]
  k = k + 1

new_all_ids_16 = [x[0] for x in all_ids_16]
#print(all_ids)
#print(new_all_ids_16)


time.sleep(30)


all_ids_17 = []
k = 1601

while k <= 1700:
  z = get_job_ids(1, k)
  all_ids_17 = all_ids_17 + [z]
  k = k + 1

new_all_ids_17 = [x[0] for x in all_ids_17]
#print(all_ids)
#print(new_all_ids_17)

res_all_ids = new_all_ids_1 + new_all_ids_2 + new_all_ids_3 + new_all_ids_4 + new_all_ids_5 + new_all_ids_6 + new_all_ids_7 + new_all_ids_8 + new_all_ids_9 + new_all_ids_10 + new_all_ids_11 + new_all_ids_12 + new_all_ids_13 + new_all_ids_14 + new_all_ids_15 + new_all_ids_16 + new_all_ids_17


def send_resume(zeta):
  import requests

  url = "https://api.hh.ru/negotiations"

  payload = {'vacancy_id': {zeta},
  'resume_id': 'f5c1c9bdff0b0e2c9a0039ed1f37746c534869',
  'message': 'Сообщение'}
  files=[

  ]
  headers = {
  'Authorization': 'Bearer TOKEN',
  'Cookie': '__ddg1_=AtUknwq2C4H1hxF8dV97; hhuid=Mv5vtxCZeT4afmLelk02mw--; redirect_host=barnaul.hh.ru; region_clarified=NOT_SET'
  }

  response = requests.request("POST", url, headers=headers, data=payload, files=files)

  #print(response.text)

  if response.status_code == 201:
    print ('Заявка отправлена!')
  else:
    print ('Пропуск!')



for i in res_all_ids:
  send_resume(i)






