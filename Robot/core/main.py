import requests,itchat
# from wxpy import *
def get_news():
    '''
    获取金山词霸 每日一句
    :return:
    '''
    url="http://open.iciba.com/dsapi"
    r = requests.get(url)
    english_content=r.json()['content']
    chinese_content=r.json()['note']
    return  english_content,chinese_content
def send_message():
    try:
        itchat.auto_login(hotReload=True)
        name=u'小月'
        friend=itchat.search_friends(name=name)
        xiao_yue=friend[0]['UserName']
        chinese=get_news()[0]
        english=get_news()[1]
        message="%s\n翻译:\n%s"%(english,chinese)
        itchat.send(message, xiao_yue)
    except SyntaxError as e:
        print(e)
send_message()

print('hello')



