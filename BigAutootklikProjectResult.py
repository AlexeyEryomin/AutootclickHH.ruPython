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

import time
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


import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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

import time
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
  'message': 'Привет, меня зовут Ерёмин Алексей и я начинающий тестировщик! \n Прошу рассмотреть мое резюме на должность QA инженер / Тестировщик \n Ищу работу с возможностью работать удаленно, так как скорее всего нахожусь далеко от вашего места расположения офиса. \n\n Небольшая предыстория! \n Когда я начал искать работу, я подготавливал сопроводительное письмо индивидуально для каждой кампании, хотел подчеркнуть свои сильные стороны, которые подходили под описание требований, так же хотел сказать как мне важно будет работать в вашей кампании, как буду полезен и что ни в коем случае не подведу. Но мои ожидания разбились о скалы реальности - слово ,начинающий, для работодателя — это первостепенный триггер для того чтобы отказать мне сразу и даже без возможности показать свой навык - выполнить тестовое задание или пройти собеседование. В результате чего мною было принято решение написать программку для автоматической отсылки резюме используя Python Request и Head Hunter API. Этот отклик и это письмо является результатом работы моей программы. Может это письмо и не выражает особое обращение к вашей кампании, но тем не менее для меня будет особенной та кампания, которая предложит мне оффер. Если вы не готовы дать возможность показать себя начинающему тестировщику, то просто нажмите отказ для этого отклика. \n Немного о себе! \n Мое самое большое увлечение это компьютер, различные гаджеты и программы. К сожалению, на сегодняшний день моя работа никак не связана с компьютерами, телефонами, программами или другими интересными вещами из сферы технологий. И я прилагаю все возможные усилия чтобы это изменить. \n Что я делаю для этого. \n - Увлекаюсь созданием простых программ на языке Python(смотрю различные ролики на ютубе, читаю статьи и пытаюсь использовать это для себя, например создал эту программку для автоотклика на вакансии. \n - Прохожу обучение в SkyPro по направлению тестирование и здесь я изучил \n    1) Основы тестирования (техники тест дизайна, виды тестирования, как вести документацию и многое многое другое) \n    2) Подробно разобрали как работать с REST в инструменте Postman, изучили как отправлять запросы в терминале используя CURL \n    3) Изучили тестирование SOAP сервисов в SOAPUI \n    4) Изучили запросы SQL на примере PostgreSQL и его графической утилиты PgAdmin (предпочитаю работать с запросами SQL из терминала Linux мне кажется так даже быстрее получается чем в PgAdmin) \n    5) Поработали немного в JMeter, создали нагрузочный тест для работы из терминала \n\nЕсли вы готовы рассмотреть меня, то буду очень рад стать частью вашей профессиональной команды! \n Готов обсудить с вами свои навыки и знания подробнее. \n Напишите мне на электронную почту ShiraiRyuFireGarden@yandex.ru \n Или можете связаться по телефону +79994762172 или в WhatsApp \n Так же отвечу вам в телеграм @alexeyfighter'}
  files=[

  ]
  headers = {
  'Authorization': 'Bearer NI20FC4GHT3MB8A95EBQN02DE2HRJDOL7P3HQAV8INQF01L4NHV00UV01IMI68EE',
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






