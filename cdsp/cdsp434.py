import requests
import json
import time
import timeit
import os
import re
import urllib
from datetime import datetime
from dateutil import tz



result=''
djj_bark_cookie=''
djj_sever_jiang=''
cd_tk=''
cd_token=''
cd_body434=''

tklist= []
tokenlist=[]

headers={"Accept": "*/*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-US;q=0.9, zh-Hant-CN;q=0.8","As-Version": "v1","Content-Type": "application/json","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 qapp","Version": "1211","Version-Name": ""}

def watch_video():
   msg='watch_video'
   print('\n💎'+msg)
   try:
      response=requests.post('https://api-ddvideo.1sapp.com/h5/task/submit',headers=headers,body=cd_body434,timeout=10)
      print(response.text)
   except Exception as e:
      msg+=str(e)
      print(msg)
   loger(msg)
      
   
def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
def notice(b,e):
    ll=False
    start_time = datetime.strptime(str(datetime.now().date())+b, '%Y-%m-%d%H:%M')
    end_time =  datetime.strptime(str(datetime.now().date())+e, '%Y-%m-%d%H:%M')
    now_time = datetime.now()
    if now_time > start_time and now_time<end_time:
       ll=True
    else:
    	ll=False
    return ll
	
  
def check(st,flag,list):
   result=''
   global djj_bark_cookie
   global djj_sever_jiang
   if "DJJ_BARK_COOKIE" in os.environ:
     djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in os.environ:
      st = os.environ[flag]
   if st:
       for line in st.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print('DTask is over.')
       exit()
	
def all():
   check(cd_tk,'CD_TK',tklist)
   check(cd_token,'CD_TOKEN',tokenlist)
   check(cd_body434,'CD_BODY434')
   index=0
   global result
   for item in tklist:
       headers['Tk']=item
   for item in tokenlist:
       headers['Token']=item
       index+=1
       result+=f'''【Count】{index}'''
       watch_video()
   if notice('4:00','5:00') or notice('22:00','23:00') or notice('13:00','14:00'):
      pushmsg('CDSP',result)
   print('its over')
   
   
   
   
   
def pushmsg(title,txt,bflag=1,wflag=1):
   txt=urllib.parse.quote(txt)
   title=urllib.parse.quote(title)
   if bflag==1 and djj_bark_cookie.strip():
      print("\n【通知汇总】")
      purl = f'''https://api.day.app/{djj_bark_cookie}/{title}/{txt}'''
      response = requests.post(purl)
      print(response.text)
   if wflag==1 and djj_sever_jiang.strip():
      print("\n【微信消息】")
      purl = f'''http://sc.ftqq.com/{djj_sever_jiang}.send'''
      headers={
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
      body=f'''text={txt})&desp={title}'''
      response = requests.post(purl,headers=headers,data=body)
      print(response.text)
def loger(m):
   print(m)
   global result
   result +=m
@clock
def start():
   
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   all()
def main_handler(event, context):
    return start()
if __name__ == '__main__':
       start()
