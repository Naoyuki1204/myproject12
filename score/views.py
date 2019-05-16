from django.shortcuts import render
from django.http import HttpResponse
from .models import game
from .models import result
from .models import before
from .models import player
from .forms import FindForm
from PIL import Image, ImageDraw, ImageFont
from django.db.models import Q




def index(request):
    params = {
            'title': 'SofttennisDB',
            'msg':'ようこそ！',
            'goto':'index',
            'goto1':'add',
            'goto3':'video',
            'goto2':'find',
        }
    return render(request, 'score/index.html', params)

def add(request):    
    params = {
                'title':'ソフトテニスデータベース',
                'msg':'戻るを押したらタイトルに戻れるよ！',
                'goto':'index',
                'goto2':'addpoint',
                'abc1':request.GET.get('skill'),
            }
    return render(request, 'score/index_add.html', params)

def person(request,num):
    rdata4 = player.objects.filter(id=num).values_list('pname').get()
    data5 = rdata4[0]
    data4 = result.objects.filter(pname=data5).values_list('result', flat=True)
    re = list(data4)
    IN = re.count('Ace')
    N = re.count('Net')
    RS = re.count('rso')
    LS = re.count('lso')
    T = re.count('特殊')
    B = re.count('BO')   
    
    msg = 'search result:'
    data = game.objects.filter(Q(keioS=data5)|Q(keioV=data5))
    params = {
                'title':'ソフトテニスデータベース',
                'msg':'戻るを押したらタイトルに戻れるよ！',
                'goto':'index',
                'goto2':'addpoint',
                'abc1':request.GET.get('skill'),
                're':re,
                'IN':IN,
                'N':N,
                'RS':RS,
                'LS':LS,
                'T':T,
                'B':B,
                'data5':data5,
                'title': 'Hello',
                'message': msg,
                'data':data,
                'goto':'index',
                }
    return render(request, 'score/person.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = game.objects.filter(Q(keioS__contains=str)|Q(keioV__contains=str))
    else:
        msg = 'search words...'
        form = FindForm()
        data =game.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
        'goto':'index',
        
    }
    return render(request, 'score/find.html', params)

def addpoint(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = game.objects.filter(Q(keioS__contains=str)|Q(keioV__contains=str))
    else:
        msg = 'search words...'
        form = FindForm()
        data =game.objects.all()
    
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
        'goto':'index',
        
    }
    return render(request, 'score/index_add_point.html', params)




def video(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = player.objects.filter(Q(keioS__contains=str)|Q(keioV__contains=str))
    else:
        msg = 'search words...'
        form = FindForm()
        data =player.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
        'goto':'index',
        }
    return render(request, 'score/index_video.html', params)

ccc3 = ""

def analys(request, num):
    
    video = 'https://www.youtube.com/embed/ju2vERQCg4g'
    data1000 = game.objects.filter(id=num).values_list('gamename').get()
    data1001 =data1000[0]
    data1004 = game.objects.filter(id=num).values_list('score').get()
    data1005 =data1004[0]
    data1006 = game.objects.filter(id=num).values_list('eS').get()
    data1007 =data1006[0]
    data1008 = game.objects.filter(id=num).values_list('eV').get()
    data1009 =data1008[0]
    data1006a = game.objects.filter(id=num).values_list('keioS').get()
    data1007a =data1006a[0]
    data1008a = game.objects.filter(id=num).values_list('keioV').get()
    data1009a =data1008a[0]
    data1 = '【' + data1001 + '】'+data1007a +':'+data1009a+'    _対_    ' + data1007 + ':' + data1009 +'【スコア】' + data1005 
    data108a = game.objects.filter(id=num).values_list('keioS').get()
    data108b = data108a[0]
    data109a = game.objects.filter(id=num).values_list('keioV').get()
    data109b = data109a[0]
    rdata42 = result.objects.filter(gameid=num,pname=data108b).values_list('result', flat=True)
    rdata43 = result.objects.filter(gameid=num,pname=data109b).values_list('result', flat=True)
    rdata44 = list(rdata42) + list(rdata43)
    re = rdata44
    IN = re.count('Ace')
    N = re.count('Net')
    RS = re.count('rso')
    LS = re.count('lso')
    T = re.count('特殊')
    B = re.count('BO')
    
    data1081a = game.objects.filter(id=num).values_list('eS').get()
    data1081b = data1081a[0]
    data1091a = game.objects.filter(id=num).values_list('eV').get()
    data1091b = data1091a[0]
    rdata52 = result.objects.filter(pname= data1081b).values_list('result', flat=True)
    rdata53 = result.objects.filter(pname= data1091b).values_list('result', flat=True)
    rdata54 = list(rdata52) + list(rdata53)
    re7 = rdata54
    IN7 = re7.count('Ace')
    N7 = re7.count('Net')
    RS7 = re7.count('rso')
    LS7 = re7.count('lso')
    T7 = re7.count('特殊')
    B7 = re7.count('BO')
    
    
    data10 = result.objects.filter(gameid=num).values_list('result','pname')
    data10a = game.objects.filter(id=num).values_list('keioS').get()
    data10b = data10a[0]
    data11 = data10.filter(pname=data10b).values_list('result', flat=True)
    re1 = list(data11)
    IN1 = re1.count('Ace')
    N1 = re1.count('Net')
    RS1 = re1.count('rso')
    LS1 = re1.count('lso')
    T1 = re1.count('特殊')
    B1 = re1.count('BO')
    
    data12 = result.objects.filter(gameid=num).values_list('result','pname')
    data12a = game.objects.filter(id=num).values_list('keioV').get()
    data12b = data12a[0]
    data13 = data12.filter(pname=data12b).values_list('result', flat=True)
    re2 = list(data13)
    IN2 = re2.count('Ace')
    N2 = re2.count('Net')
    RS2 = re2.count('rso')
    LS2 = re2.count('lso')
    T2 = re2.count('特殊')
    B2 = re2.count('BO')
    
    data104a = game.objects.filter(id=num).values_list('eS').get()
    data104b = data104a[0]
    data11b = data10.filter(pname=data104b).values_list('result', flat=True)
    re3 = list(data11b)
    IN3 = re3.count('Ace')
    N3 = re3.count('Net')
    RS3 = re3.count('rso')
    LS3 = re3.count('lso')
    T3 = re3.count('特殊')
    B3 = re3.count('BO')
    
    data120a = game.objects.filter(id=num).values_list('eV').get()
    data120b = data120a[0]
    data130b = data12.filter(pname=data120b).values_list('result', flat=True)
    re4 = list(data130b)
    IN4 = re4.count('Ace')
    N4 = re4.count('Net')
    RS4 = re4.count('rso')
    LS4 = re4.count('lso')
    T4 = re4.count('特殊')
    B4 = re4.count('BO')
    
    
    cy = 0
    cx = 0
    by = 0
    bx = 0
    
    rdata2 = result.objects.filter(gameid=num).values('id','placeS')
    rdata3 = result.objects.filter(gameid=num).values('id','placeF')
    
    global ccc3
    bbb = request.get_full_path
    bbbb = str(bbb)
    
    if len(bbbb) == 80:
        ccc3 = 0
        ddd = request.get_full_path
        ddd2 = request.get_full_path
    else:
        ccc = str(bbb) 
        ddd = ccc[62:85]
        ccc2 = ddd[22]
        ccc3 = int(ccc2)+1
        ddd1 = ddd[:21]
        ddd2 = ddd1 + "="+ str(ccc3) +"&変換=送信#example"
    ii = int(ccc3)
    
    changec = rdata2[ii]['placeS']
    changeb = rdata3[ii]['placeF']
    
    resultco = result.objects.filter(gameid=num).values_list('pname')
    if resultco[ii] == game.objects.filter(id=num).values_list('keioS').get():
        resultco1 = 'red'
    if resultco[ii] == game.objects.filter(id=num).values_list('keioV').get():
        resultco1 = 'blue'
    if resultco[ii] == game.objects.filter(id=num).values_list('eS').get():
        resultco1 = 'orange'
    if resultco[ii] == game.objects.filter(id=num).values_list('eV').get():
        resultco1 = 'limegreen'
    
    beforeco = before.objects.filter(gameid=num).values_list('pname')
    if beforeco[ii] == game.objects.filter(id=num).values_list('keioS').get():
        beforeco1 = 'red'
    if beforeco[ii] == game.objects.filter(id=num).values_list('keioV').get():
        beforeco1 = 'blue'
    if beforeco[ii] == game.objects.filter(id=num).values_list('eS').get():
        beforeco1 = 'orange'
    if beforeco[ii] == game.objects.filter(id=num).values_list('eV').get():
        beforeco1 = 'limegreen'
    
    
    
    if changec < 11:
        cy = +1
    elif  10 < changec < 21:
        cy = +2
    elif  20 < changec < 31:
        cy = +3
    elif  30 < changec < 41:
        cy = +4
    elif  40 < changec < 51:
        cy = +5
    elif  50 < changec < 61:
        cy = +6
    elif  60 < changec < 71:
        cy = +7
    elif  70 < changec < 81:
        cy = +8
    elif  80 < changec < 91:
        cy = +9
    elif  90 < changec < 101:
        cy = +10

    
    if changeb < 11:
        by = +1
    elif  10 < changeb < 21:
        by = +2
    elif  20 < changeb < 31:
        by = +3
    elif  30 < changeb < 41:
        by = +4
    elif  40 < changeb < 51:
        by = +5
    elif  50 < changeb < 61:
        by = +6
    elif  60 < changeb < 71:
        by = +7
    elif  70 < changeb < 81:
        by = +8
    elif  80 < changeb < 91:
        by = +9
    elif  90 < changeb < 101:
        by = +10

    
    if changec < 11:
        changec = changec+10
    cx = changec % 10
    if cx == 0:
        cx = +10
    
    if changeb < 11:
        changeb = changeb+10
    bx = changeb % 10
    if bx == 0:
        bx = +10
        
    rdata10 = result.objects.filter(gameid=num).values('id','skill')
    data19 = rdata10[ii]['skill']
    data20 = str(data19)

    rdata11 = result.objects.filter(gameid=num).values('id','result')
    data191 = rdata11[ii]['result']
    data201 = str(data191)
    
    cy2 = 0
    cx2 = 0
    by2 = 0
    bx2 = 0

    
    
    rdata2b = before.objects.filter(gameid=num).values('id','placeS')
    rdata3b = before.objects.filter(gameid=num).values('id','placeF')
    
    changecb = rdata2b[ii]['placeS']
    changebb = rdata3b[ii]['placeF']
        
    if changecb < 11:
        cy2 = +1
    elif  10 < changecb < 21:
        cy2 = +2
    elif  20 < changecb < 31:
        cy2 = +3
    elif  30 < changecb < 41:
        cy2 = +4
    elif  40 < changecb < 51:
        cy2 = +5
    elif  50 < changecb < 61:
        cy2 = +6
    elif  60 < changecb < 71:
        cy2 = +7
    elif  70 < changecb < 81:
        cy2 = +8
    elif  80 < changecb < 91:
        cy2 = +9
    elif  90 < changecb < 101:
        cy2 = +10

    
    if changebb < 11:
        by2 = +1
    elif  10 < changebb < 21:
        by2 = +2
    elif  20 < changebb < 31:
        by2 = +3
    elif  30 < changebb < 41:
        by2 = +4
    elif  40 < changebb < 51:
        by2 = +5
    elif  50 < changebb < 61:
        by2 = +6
    elif  60 < changebb < 71:
        by2 = +7
    elif  70 < changebb < 81:
        by2 = +8
    elif  80 < changebb < 91:
        by2 = +9
    elif  90 < changebb < 101:
        by2 = +10

    
    if changecb < 11:
        changecb = changecb+10
    cx2 = changecb % 10
    if cx2 == 0:
        cx2 = +10
    
    if changebb < 11:
        changebb = changebb+10
    bx2 = changebb % 10
    if bx2 == 0:
        bx2 = +10
        
    rdata10b = before.objects.filter(gameid=num).values('id','skill')
    data19b = rdata10b[ii]['skill']
    data20b = str(data19b)
    
    countname = result.objects.filter(gameid=num).values('id','count')
    countname2 = countname[ii]['count']

    im = Image.new('RGB', (230, 500), (248, 249, 250))
    draw = ImageDraw.Draw(im)
    
    draw.rectangle((46/2, 100/2, 414/2, 900/2),fill=(255,255,255),outline=(0,0,0))
    #ベースとサイドライン
    
    draw.line((92/2, 100/2, 92/2, 900/2),fill=(0,0,0))
    #あれーライン左
    
    draw.line((368/2, 100/2, 368/2, 900/2),fill=(0,0,0))
    #あれーライン右
    
    draw.line((40/2, 500/2, 420/2, 500/2),fill=(0,0,0))
    #ネット
    
    draw.line((92/2, 285/2, 368/2, 285/2),fill=(0,0,0))
    #サービスライン上 正規の縮尺で
    
    draw.line((92/2, 715/2, 368/2, 715/2),fill=(0,0,0))
    #サービスライン下
    
    draw.line((230/2, 285/2, 230/2, 715/2),fill=(0,0,0))
    #サービスセンターライン
    
    draw.line(((23+46*(bx))/2,(50+100*(by-1))/2,(23+46*(cx))/2,(50+100*(cy-1))/2),fill=resultco1, width=6) 
    #ボールの起動（赤色の線）
    
    draw.line(((23+46*(bx2))/2,(50+100*(by2-1))/2,(23+46*(cx2))/2,(50+100*(cy2-1))/2),fill=beforeco1, width=2) 
    #ボールの起動（青色の線）

    
    font = ImageFont.truetype("/Library/Fonts/Futura.ttc", 22)
    draw.text(((46*(bx-1))/2, (100*(by-1))/2),data201 , fill=(0, 0, 0),font=font)
    #フォアクロスとかの文字が出る位置
    
    draw.text(((23+46*(cx2-1)+5)/2, (50+100*(cy2-1)+5)/2), '['+data20b+']', fill=(0, 0, 0),font=font)
    #bフォアクロスとかの文字が出る位置

    
    draw.text(((23+46*(cx-1)+5)/2, (50+100*(cy-1)+5)/2), '['+data20+']', fill=(0, 0, 0),font=font)
    #インとかサイドアウトとかが出る位置
    
    draw.text((0,-4), countname2, fill=(255, 0, 0),font=font)
    #スコアのでる位置
    aa = 'score/static/score/tenniscourt0.jpg'
    imagename = aa
    im.save(imagename, quality=95)
    params = {
        'title':'Hello',
        'id':num,
        'data1':data1,
        're':re,
        're':re,
        'IN':IN,
        'N':N,
        'RS':RS,
        'LS':LS,
        'T':T,
        'B':B,
        'IN1':IN1,
        'N1':N1,
        'RS1':RS1,
        'LS1':LS1,
        'T1':T1,
        'B1':B1,
        'IN2':IN2,
        'N2':N2,
        'RS2':RS2,
        'LS2':LS2,
        'T2':T2,
        'B2':B2,
        'IN3':IN3,
        'N3':N3,
        'RS3':RS3,
        'LS3':LS3,
        'T3':T3,
        'B3':B3,
        'IN4':IN4,
        'N4':N4,
        'RS4':RS4,
        'LS4':LS4,
        'T4':T4,
        'B4':B4,
        'IN7':IN7,
        'N7':N7,
        'RS7':RS7,
        'LS7':LS7,
        'T7':T7,
        'B7':B7,
        'goto':'index',
        'bx':bx,
        'video':video,
        'data10b':data10b,
        'bbb':bbb,
        'ddd':ddd,
        'ddd2':ddd2,
    }
    
    return render(request, 'score/analys.html', params)




def edit(request, num):
    if (request.method == 'GET'):
        if request.GET.get('gameour') is None:
            next
        else:
            gc1 = request.GET.get('gameour')
            gc2 = request.GET.get('gameenemy')
            pc1 = request.GET.get('pointour')
            pc2 = request.GET.get('pointenemy')
            count2 = gc1 +'-'+ gc2 +','+ pc1 +'-'+ pc2   
            gameid2 = num
            pname2 = int(request.GET.get('s5'))
            if pname2 == 1:
                keioS = game.objects.filter(id=num).values_list('keioS').get()
                pname2 = keioS[0]
            if pname2 == 2:
                keioV = game.objects.filter(id=num).values_list('keioV').get()
                pname2 = keioV[0]
            if pname2 == 3:
                ES = game.objects.filter(id=num).values_list('eS').get()
                pname2 = ES[0]
            if pname2 == 4:
                EV = game.objects.filter(id=num).values_list('eV').get()
                pname2 = EV[0]
                
            pname3 = int(request.GET.get('s3'))
            if pname3 == 1:
                keioS = game.objects.filter(id=num).values_list('keioS').get()
                pname3 = keioS[0]
            if pname3 == 2:
                keioV = game.objects.filter(id=num).values_list('keioV').get()
                pname3 = keioV[0]
            if pname3 == 3:
                ES = game.objects.filter(id=num).values_list('eS').get()
                pname3 = ES[0]
            if pname3 == 4:
                EV = game.objects.filter(id=num).values_list('eV').get()
                pname3 = EV[0]

            placeS3 =int(request.GET.get('courtnum1'))
            placeF3 =int(request.GET.get('courtnum2')) 
            skill3 = int(request.GET.get('s4'))
            if skill3 == 1:
                skill3 ='F'
            if skill3 == 2:
                skill3 ='B'
            if skill3 == 3:
                skill3 ='SA'
            if skill3 == 4:
                skill3 ='FV'
            if skill3 == 5:
                skill3 ='BV'
            if skill3 == 6:
                skill3 ='Sm'
        
        
        
            placeS2 =int(request.GET.get('courtnum3'))
            placeF2 =int(request.GET.get('courtnum4'))
            skill2 = int(request.GET.get('s6'))
            if skill2 == 1:
                skill2 ='F'
            if skill2 == 2:
                skill2 ='B'
            if skill2 == 3:
                skill2 ='SA'
            if skill2 == 4:
                skill2 ='FV'
            if skill2 == 5:
                skill2 ='BV'
            if skill2 == 6:
                skill2 ='Sm'
            result2 = int(request.GET.get('r1'))
            if result2 == 1:
                result2 = 'lso'
            if result2 == 2:
                result2 = 'BO'
            if result2 == 3:
                result2 = 'rso'
            if result2 == 4:
                result2 = 'Net'
            if result2 == 5:
                result2 = 'Ace'
            if result2 == 6:
                result2 = '特殊'
            resultq = result(gameid=gameid2,pname=pname2,placeS=placeS2,placeF=placeF2,skill=skill2,result=result2,count=count2)
            resultq.save()
            beforeq = before(gameid=gameid2,pname=pname3,placeS=placeS3,placeF=placeF3,skill=skill3,)
            beforeq.save()
    params = {
       'goto':'index',
    }

    
    return render(request, 'score/edit.html', params)



