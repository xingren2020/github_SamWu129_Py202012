import requests
import json

zdUrl = 'http://api.turinglabs.net/api/v1/jd/bean/create/'
ncUrl = 'http://api.turinglabs.net/api/v1/jd/farm/create/'
mcUrl = 'http://api.turinglabs.net/api/v1/jd/pet/create/'

Defalt_ncShareCode= ['ae6488dc5f0c4669bfa432b9bc884191','268e797816f340bc9ad3656fa249d1a6','010bcbf67bf54e7cae65b00d252f462c','b2e08a4105674c6680a3ba687627e9f2','34e1ac7416f34d1e86ebffb1f9f1ce72']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_mcShareCode= ['MTAxODExNDYxMTEwMDAwMDAwMzk4NzYxOTc=','MTAxODExNDYxMTEwMDAwMDAwNDA1NDQwNzE=','MTAxODc2NTEzMzAwMDAwMDAyODk1OTQ4OQ==','MTAxODc2NTEzOTAwMDAwMDAyODY1NzEzMw==']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_zdShareCode= ['7oivz2mjbmnx4bddymkpj42u75jmba2c6ga6eba','2vgtxj43q3jqzr2i5ac4uj2h6wxl66n4i326u3i','4npkonnsy7xi2rt6qcajwzdp3qjmazppr5fwo6a','fsvcjluk7rhd74kwgrelr3aoeu','olmijoxgmjutykb27yfwpryuu5cot5fj3frld5q']#读取参数djj_sharecode为空，开始读取默认参数
#学习与测试  by 2020.12
def AddhelpCode(Url,Defalt_ShareCode):
   for code in Defalt_ShareCode:
      try:
         AddcodeRes=hongliyu(Url+code+'/')
         print(AddcodeRes)
      
         if AddcodeRes['code']==200:
           print("互助码添加成功✅")
         elif AddcodeRes['code']==400:
           print("互助码已存在")
         else:
           print('互助码添加异常')
      except Exception as e:
          	pass
def hongliyu(url):
   try:
     return json.loads(requests.get(url).text)
   except Exception as e:
      print(f'''初始化函数:''', str(e))
      
AddhelpCode(mcUrl,Defalt_mcShareCode)
AddhelpCode(ncUrl,Defalt_ncShareCode)
AddhelpCode(zdUrl,Defalt_zdShareCode)
