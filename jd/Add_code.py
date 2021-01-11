import requests
import json

zdUrl = 'http://api.turinglabs.net/api/v1/jd/bean/create/' #种豆 
ncUrl = 'http://api.turinglabs.net/api/v1/jd/farm/create/' #农场
mcUrl = 'http://api.turinglabs.net/api/v1/jd/pet/create/'  #萌宠
ddUrl = 'http://api.turinglabs.net/api/v1/jd/ddfactory/create/' #东东工厂
jxUrl = 'http://api.turinglabs.net/api/v1/jd/jxfactory/create/' #京喜工厂
joyUrl = 'https://code.chiang.fun/api/v1/jd/jdcrazyjoy/create/' #京东Crazy

Defalt_ncShareCode= ['535587d2d2134c05b72d532e5648fca4','d8f30abd6b09497b81502e328e6822ae','c777008122e34854b7bf243d9027b0b3','6373073b2a774b85b5844ce1b6d9d94b']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_mcShareCode= ['MTAxODc2NTEzMTAwMDAwMDAyNjg3ODA3Nw==','MTAxODc2NTEzMTAwMDAwMDAyNzM1OTgyOQ==','MTE1NDAxNzYwMDAwMDAwNDA0NjI0MDk=','MTAxODc2NTEzMTAwMDAwMDAyMTE1NzkyNw==']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_zdShareCode= ['2gih437f3cx52vug2oxzjdhkoa','eeexxudqtlampttwqsjgtjinenirfsmkhcanvfq','uwgpfl3hsfqp3onctpv6qufih5slnir6rura7fy','4npkonnsy7xi2eincnwavowy6ohblizjt5go7ra']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_ddShareCode= ['P04z54XCjVWnYaS5mRUVDWmnD1Ll4CY','P04z54XCjVWnYaS5m9cZxqYhAUtywhKqBmvOA','P04z54XCjVWnYaS5m9cZz6DtAs01UPsoL1lIQ','P04z54XCjVWnYaS5m9cZ2f42y4Yl-YMYPx33g8']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_jxShareCode= ['Z-OXyhGaVPX6ImRJwOb_pQ==','CIAftU-mPs00k7FnlPTLgg==']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_joyShareCode= ['Pmrn8BfQgW_xKbqC2JEUpg==','9cECOkO-B1QumNPkdm3wHA==','w_Eq03-4WUM-ScZ_jeNqzA==','6NYgYjfcy0N2YUB1685BE6t9zd5YaBeE']#读取参数djj_sharecode为空，开始读取默认参数

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
AddhelpCode(ddUrl,Defalt_ddShareCode)
AddhelpCode(jxUrl,Defalt_jxShareCode)
AddhelpCode(joyUrl,Defalt_joyShareCode)
