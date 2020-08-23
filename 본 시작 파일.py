import discord
from discord.ext import commands
from discord.utils import get
import os
import asyncio
from captcha.image import ImageCaptcha
import random
import datetime
import urllib
from urllib.request import Request
import bs4
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen 
from urllib.request import Request, urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib import parse
import warnings
import requests
import json
import re
import openpyxl
import koreanbots
import os, random, time

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print('-------------')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

    user = len(client.users)
    server = len(client.guilds)

    while True:
        messages = ["문의는∑」Apple#9999에게 문의 하세요!", "저는 Team MB에서 개발, 관리 되고 있어요!", "제 접두사는 $ 입니다!", str(user) + "명의 유저들과 함께 하는중입니다.", str(server) + "개의 서버에 참가되어있습니다.", "도움말 : $도움말 , $명령어"]
        for (m) in range(6):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(5)
owner = [735855317606465636, 695634417300799579]

@client.event
async def on_message(message):
    if message.content.startswith("$도움말") or message.content.startswith("$명령어"):
        embed = discord.Embed(title="[ ABOT 도움말 ]", timestamp=message.created_at,
        colour=discord.Colour.gold()
    )
        embed.add_field(name="$도움말, $명령어", value="ABOT의 명령어 목록을 보여드려요!", inline=False)
        embed.add_field(name="$핑", value="ABOT의 반응속도를 확인해요!", inline=False)
        embed.add_field(name="$계산 [더하기 / 빼기 / 곱하기 / 나누기] 숫자...", value="[더하기,뺴기,곱하기,나누기] 중에서 선택한 기호로 숫자... 를 계산해요! \n ( ex : $계산 더하기 1 1 ) ", inline=False)
        embed.add_field(name="$실검", value="네이버 실시간 검색어 순위를 확인해요!", inline=False)
        embed.add_field(name="$캡챠, $캡차", value="캡챠 인증코드가 생성된 후, 해당 인증코드를 작성하면 인증됩니다.")
        embed.add_field(name="〈 관리자 권한 필요 〉$청소 [청소할 메시지수]", value="[청소할 메시지수]에 해당하는 숫자만큼의 메시지를 삭제해요! \n ( 사용한 명령어 포함이므로 만약 3을 입력하면 실질적으로 2개가 삭제되는것과 같습니다. )", inline=False)
        embed.add_field(name="〈 관리자 권한 필요 〉$킥 [멘션]", value="[멘션]한 유저를 해당 서버에서 추방해요!", inline=False)
        embed.add_field(name="〈 관리자 권한 필요 〉$밴 [멘션]", value="[멘션]한 유저를 해당 서버에서 차단해요!", inline=False)
        embed.add_field(name="$피드백 [내용]", value="[내용]에 해당하는 메시지를 운영자에게 보냅니다.", inline=False)
        embed.add_field(name="$코로나", value="현재 코로나 상태를 알려줍니다.", inline=False)
        embed.add_field(name="$투표 제목&투표1&투표2", value="ex:$투표 좋다&?&?", inline=False)
        embed.add_field(name="$돈명령어", value="돈 기능 도움말입니다.", inline=False)
        embed.add_field(name="$내정보", value="자신의 정보를 확인합니다.", inline=False)
        embed.add_field(name="$지식명령어", value="지식 관련 명령어 도움말을 확인합니다.", inline=False)
        embed.add_field(name="$날씨 [ 지역 ]", value="[ 지역 ] 에 해당하는 날씨를 불러옵니다!", inline=False)
        embed.add_field(name="$이미지 [ 검색할 내용 ]", value="[ 검색할 내용 ] 에 해당하는 이미지를 불러옵니다! ** ( 정확하지 않음 ) **", inline=False)
        embed.add_field(name="$정보 [ @멘션 ]", value="[ @멘션] 애 해당하는 유저의 정보를 불러옵니다. [ 자신의 정보를 보려면 $내정보 ]", inline=False)
        embed.add_field(name="$시간", value="현재 시간을 불러옵니다.", inline=False)
        embed.set_footer(text="[ 도움말 명령어 임베드 도움 : ∑」Cookie ] [ 제작자 : ∑」 Apple#9999 ]")
        await message.channel.send(embed=embed)
    if message.content == '$자기소개':
       await message.channel.send(f'<@!{message.author.id}> 안녕하세요 저는 사과에게서 만들어진 봇입니다!')  
    if message.content == '$제작자':
       await message.channel.send(f'<@!{message.author.id}> ```∑」Apple#9999```')
    if message.content.startswith("$초대"):
       embed=discord.Embed(color=0xff00, title="BCBOT 초대하기", description="[초대하기](https://discord.com/api/oauth2/authorize?client_id=735466302680072212&permissions=8&scope=bot)||||||||||[서포트 서버](https://discord.gg/TF2gz5s)", timestamp=message.created_at)
       embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
       await message.channel.send(embed=embed)
    if message.content.startswith("$내아이디"):
       await message.channel.send(f"<@!{message.author.id}>님의 아이디는 `{message.author.id}` 입니다.")    
    if message.content.startswith("$킥"):
        if message.author.guild_permissions.administrator:
            kickusermention = message.content[4:]
            kickuserid = kickusermention[2:20]
            kickuser = message.guild.get_member(int(kickuserid))
            await message.guild.kick(kickuser)
            await message.channel.send( str(kickuser) + "님을 관리자 권한으로 추방했어요!")
        else:
            await message.channel.send("권한이 부족해요!")
    if message.content.startswith("$버그제보"):
       embed=discord.Embed(color=0xff00, title="버그 제보", description="버그 제보는 [서포트 서버](https://discord.gg/TF2gz5s) 에 있는 `건의방` 채널에서 해주세요.", timestamp=message.created_at)
       embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
       await message.channel.send(embed=embed)
    if message.content.startswith("$밴"):
       if message.author.guild_permissions.administrator:
            kickusermention = message.content[4:]
            kickuserid = kickusermention[2:20]
            kickuser = message.guild.get_member(int(kickuserid))
            await message.guild.ban(kickuser)
            await message.channel.send( str(kickuser) + "님을 관리자 권한으로 밴했어요!")
       else:
            await message.channel.send(f"<@!{message.author.id}> 밴은 관리자만 할수있어요.")
    if message.content.startswith("$안녕"):
            await message.channel.send(f"<@!{message.author.id}>님, 안녕하세요!")
    if message.content.startswith("$크시봇"):
            await message.channel.send("...? 씹덕봇?")
    if message.content.startswith("$배추봇"):
            await message.channel.send("배추 먹고싶다")
    if message.content.startswith("$팀 MB"):
            await message.channel.send("https://discord.gg/TF2gz5s")
    if message.content.startswith("$핑"): 
        latency = client.latency  
        await message.channel.send(str(round(latency * 1000)) + "ms")
        await message.channel.send("반응 속도가 너무 느리면 `∑」 Apple#9999` 한테 DM 으로 문의 주세요. ")
    if message.content.startswith("$바보"):
            await message.channel.send("나 바보 아니야(무지개반사!)")
    if message.content.startswith("$캡챠") or message.content.startswith("$캡차"):
            Image_captcha = ImageCaptcha()
            msg = ""
            a = ""
            for i in range(6):
                a += str(random.randint(0, 9))

            name = "Captcha.png"
            Image_captcha.write(a, name)

            await message.channel.send(f"{message.author.mention} 님의 인증 코드, **인증 코드를 __10초__ 내에 입력해주세요.**")
            await message.channel.send(file=discord.File(name))

            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            try:
                msg = await client.wait_for("message", timeout=10, check=check)
            except:
                    embed = discord.Embed(title="Captcha 인증", description=f"{message.author.mention}, __**Captcha**__ 인증 시간 초과. 다시 시도해주세요.", timestamp=message.created_at,
                    colour=discord.Colour.red()
    )
                    embed.set_footer(text="by Apple", icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                    await message.channel.send(embed=embed)


            if msg.content == a:
                    embed = discord.Embed(title="Captcha 인증", description=f"{message.author.mention}, __**Captcha**__ 인증에 성공 했어요!", timestamp=message.created_at,
                    colour=discord.Colour.green()
    )
                    embed.set_footer(text="by Apple", icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                    await message.channel.send(embed=embed)
            else:
                    embed = discord.Embed(title="Captcha 인증", description=f"{message.author.mention},  __**Captcha**__ 인증에 실패했어요.", timestamp=message.created_at,
                    colour=discord.Colour.red()
    )
                    embed.set_footer(text="by Apple", icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                    await message.channel.send(embed=embed)
    if message.content.startswith("$dm"):
        userdm = message.content[4:].split("/")
        getuser = userdm[0]
        getuserid = getuser[2:20]
        getusermention = client.get_user(int(getuserid))
        userdes = userdm[1]
        await getusermention.send(userdes)
        await getusermention.send(f"`{message.author}`님이 보내심.")
        await message.channel.send("**DM이 성공적으로 발신되었습니다** __절대 이 명령어를 나쁜 목적으로 이용하지 마십시오.__")
    if message.content.startswith("$낚시") or message.content.startswith("$물고기낚시"):
        randomlist = ['못잡았습니다...', '잡았습니다!!', '못잡았습니다...', '잡았습니다!', '못잡았습니다...', '잡았습니다!']
        ran = random.randint(0, len(randomlist)-1)
        embed = discord.Embed(title="결과는...", description=randomlist[ran])
        await message.channel.send(embed=embed)
    if message.content.startswith("$쓰레기"):
        await message.channel.send("자기소개 잘하네")
    if message.content.startswith("$병X"):
        await message.channel.send("자기소개 엄청 잘하네") 
    if message.content.startswith("$청소"):
            if message.author.guild_permissions.manage_messages:
                try:
                    amount = message.content[4:]
                    await message.channel.purge(limit=int(amount))
                    embed = discord.Embed(title="청소 완료!", description=f"{message.author.mention}, **{amount}** 개의 메시지를 청소했어요!",
                    colour=discord.Colour.green()
    )
                    embed.set_footer(text="by Apple", icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                    await message.channel.send(embed=embed)
                except ValueError:
                    embed=discord.Embed(title="청소 실패", description="청소할 메시지 개수를 입력하세요.", timestamp=message.created_at,
                    colour=discord.Colour.orange()
    )
                    embed.set_footer(text="By Apple", icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                    await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="권한 부족", description="권한이 없습니다 권한을 확인하세요!", timestamp=message.created_at,
                colour=discord.Colour.red()
    )
                embed.set_footer(text="by Apple", icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                await message.channel.send(embed=embed)
  
    if message.content.startswith('$투표'):
            vote = message.content[4:].split("&")
            await message.channel.send(f"<@!{message.author.id}>님의    투표⭐ - **" + vote[0] + "**")
            for i in range(1, len(vote)):
                choose = await message.channel.send("**" + vote[i] + "**")
                await choose.add_reaction('👍') 
                await choose.add_reaction('👎')   
    
    if message.content == "$실검":
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class" : "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i+1))+"위 | "+e.text+"\n"
        await message.channel.send(result)
    if message.content.startswith('$말해'):
      vote = message.content[4:].split("-:")
      for i in range(1, len(vote)):
        await message.delete()
        choose = await message.channel.send("" + vote[i] + "")
    if message.content.startswith("$공지"):
            if message.author.id in owner:
                if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                    await message.channel.send("메세지를 쓰세요.")
                try:
                    msg = message.content[4:]
                    oksv = 0
                    embed = discord.Embed(
                        title = msg.split('&&')[0],
                        description = msg.split('&&')[1] + f"\n\n [ 공지 코드 원제작자 : 삼성해피트리#7612 ] 이 채널에 공지가 오기 싫다면 `봇-공지` 채널을 만들어주세요.\n [서포트 서버](https://discord.gg/g5cEJzk) | [오픈소스](https://github.com/samsunghappytree123/Sisby/)",
                        colour = discord.Colour.blue(),
                        timestamp = message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - Developer') .set_thumbnail(url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                except IndexError:
                    await message.channel.send("형식이 틀렸습니다. ``$공지 <제목>&&<내용>``으로 다시 시도해보세요.")
                m = await message.channel.send("아래와 같이 공지가 발신됩니다.", embed=embed)
                await m.add_reaction('✅')
                await m.add_reaction('❎')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
                except asyncio.TimeoutError:
                    await message.channel.send('시간이 초과되었습니다.')
                else:
                    if str(reaction.emoji) == "❎":
                        await message.channel.send(f"<@!{message.author.id}>, 공지발신이 취소되었습니다.")
                    elif str(reaction.emoji) == "✅":
                        await m.edit(content="발신중입니다...", embed=embed)
                        for i in client.guilds:
                            arr = [0]
                            alla = False
                            flag = True
                            z = 0
                            for j in i.channels:
                                arr.append(j.id)
                                z+=1
                                if "ABOT-공지" in j.name or"봇-공지" in j.name or "봇_공지" in j.name or "봇공지" in j.name or "bot_announcement" in j.name or "공지" in j.name:
                                    if str(j.type)=='text':
                                        try:
                                            oksv += 1
                                            await j.send(embed=embed)
                                            alla = True
                                        except:
                                            pass
                                        break
                            if alla==False:
                                try:
                                    chan=i.channels[1]
                                except:
                                    pass
                                if str(chan.type)=='text':
                                    try:
                                        oksv += 1
                                        await chan.send(embed=embed)
                                    except:
                                        pass
                        await message.channel.send(f"**📢 공지 가 성공적으로 발신되었습니다. 📢**\n\n{len(client.guilds)}개의 서버 중에서  {oksv}개의 서버에 발신 완료했습니다., {len(client.guilds) - oksv}개의 서버에 발신 실패했습니다.")
                        await m.edit(content="발신이 완료되었습니다!", embed=embed)
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.')
    if message.content.startswith("$계산"):
            global calcResult
            param = message.content.split()
            try:
                if param[1].startswith("더하기"):
                    calcResult = int(param[2])+int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
                if param[1].startswith("빼기"):
                    calcResult = int(param[2])-int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
                if param[1].startswith("곱하기"):
                    calcResult = int(param[2])*int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
                if param[1].startswith("나누기"):
                    calcResult = int(param[2])/int(param[3])
                    await message.channel.send("답 : "+str(calcResult))
            except IndexError:
                await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
            except ValueError:
                await message.channel.send("숫자로 넣어주세요.")
            except ZeroDivisionError:
                await message.channel.send("You can't divide with 0.")
    if message.content.startswith("$피드백"):
        Dansdml1 = message.content[5:]
        Dansdml = discord.Embed(title="**[ ABOT ] [피드백 명령어 제작 도움:djs226587#1243]**", color=0x6777ff)
        Dansdml.add_field(name="문의내용", value=f"{Dansdml1}\n\n- 서버 : {message.guild.name}\n- 문의자 : {message.author}", inline=False)
        Dansdml.set_thumbnail(url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
        Dansdml.set_footer(text=message.author , icon_url=message.author.avatar_url)
        m = await message.channel.send("문의발송 여부를 선택하여주세요.", embed=Dansdml)
        await m.add_reaction('✅')
        await m.add_reaction('❎')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
        except asyncio.TimeoutError:
            Drhdwltlrks = discord.Embed(title="**[ ABOT ]**", color=0xff0000)
            Drhdwltlrks.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송 선택 시간초과입니다.**", inline=False)
            Drhdwltlrks.set_thumbnail(url=message.author.avatar_url)
            Drhdwltlrks.set_footer(text="ABOT#0896 [제작 도움:djs226587#1243]" , icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
            await m.edit(content="문의발송이 취소되었습니다.", embed=Drhdwltlrks)
        else:
            if str(reaction.emoji) == "❎":
                Drhdwlcnlth = discord.Embed(title="**[ BBOT ]**", color=0xff0000)
                Drhdwlcnlth.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송이 취소되었습니다.**", inline=False)
                Drhdwlcnlth.set_thumbnail(url=message.author.avatar_url)
                Drhdwlcnlth.set_footer(text="ABOT#0896 [제작 도움:djs226587#1243]" , icon_url="https://cdn.discordapp.com/avatars/735466302680072212/0993007c055680c5f868f8c692b7825a.png?size=256")
                await m.edit(embed=Drhdwlcnlth)
            elif str(reaction.emoji) == "✅":
                await m.edit(content="서포터 서버에 정상적으로 보내졌어요 :).", embed=Dansdml)
                await client.get_channel(int(737471922199199825)).send(embed=Dansdml)
    if message.content.startswith("$코로나"):
        covidSite = "http://ncov.mohw.go.kr/index.jsp"
        covidNotice = "http://ncov.mohw.go.kr"
        html = urlopen(covidSite)
        bs = BeautifulSoup(html, 'html.parser')
        latestupdateTime = bs.find('span', {'class': "livedate"}).text.split(',')[0][1:].split('.')
        statisticalNumbers = bs.findAll('span', {'class': 'num'})
        beforedayNumbers = bs.findAll('span', {'class': 'before'})

        briefTasks = []
        mainbrief = bs.findAll('a',{'href' : re.compile('\/tcmBoardView\.do\?contSeq=[0-9]*')})
        for brf in mainbrief:
            container = []
            container.append(brf.text)
            container.append(covidNotice + brf['href'])
            briefTasks.append(container)
        print(briefTasks)

        statNum = []
        beforeNum = []
        for num in range(7):
            statNum.append(statisticalNumbers[num].text)
        for num in range(4):
            beforeNum.append(beforedayNumbers[num].text.split('(')[-1].split(')')[0])

        totalPeopletoInt = statNum[0].split(')')[-1].split(',')
        tpInt = ''.join(totalPeopletoInt)
        lethatRate = round((int(statNum[3]) / int(tpInt)) * 100, 2)
        embed = discord.Embed(title="코로나 19 정보", description="",color=0x5CD1E5)
        embed.add_field(name="데이터 제공", value="http://ncov.mohw.go.kr/index.jsp", inline=False)
        embed.add_field(name="기준 시간",value="해당 자료는 " + latestupdateTime[0] + "월 " + latestupdateTime[1] + "일 "+latestupdateTime[2] +" 자료입니다.", inline=False)
        embed.add_field(name="확진환자(누적)", value=statNum[0].split(')')[-1]+"("+beforeNum[0]+")",inline=True)
        embed.add_field(name="완치환자(격리해제)", value=statNum[1] + "(" + beforeNum[1] + ")", inline=True)
        embed.add_field(name="치료중(격리 중)", value=statNum[2] + "(" + beforeNum[2] + ")", inline=True)
        embed.add_field(name="사망", value=statNum[3] + "(" + beforeNum[3] + ")", inline=True)
        embed.add_field(name="누적확진률", value=statNum[6], inline=True)
        embed.add_field(name="치사율", value=str(lethatRate) + " %",inline=True)
        embed.add_field(name="- 최신 브리핑 1 : " + briefTasks[0][0],value="Link : " + briefTasks[0][1],inline=False)
        embed.add_field(name="- 최신 브리핑 2 : " + briefTasks[1][0], value="Link : " + briefTasks[1][1], inline=False)
        embed.set_thumbnail(url="https://wikis.krsocsci.org/images/7/79/%EB%8C%80%ED%95%9C%EC%99%95%EA%B5%AD_%ED%83%9C%EA%B7%B9%EA%B8%B0.jpg")
        embed.set_footer(text='해당 자료는 J-hoplin님의 소스코드를 이용했습니다.',
                         icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
        await message.channel.send("코로나 19 관련 임베드.", embed=embed)
    if message.content == '$내정보':
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        roles=[role for role in message.author.roles]
        embed=discord.Embed(timestamp=message.created_at,
        colour = discord.Colour.green()
)
        embed.set_author(name=f"{message.author}님의 정보!")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=f"{message.author}님에 의해 제공되었어요!", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=message.author.id, inline = False)
        embed.add_field(name="닉네임", value=message.author.display_name,  inline = False)
        embed.add_field(name="계정 생성 시간", value=message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=message.author.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =message.author.status, inline = False)
        if 'Custom Status' in str(message.author.activity):
            embed.add_field(name = '하는 게임', value = message.author.activity.state, inline = False)
        await message.channel.send(embed=embed)
    if message.content.startswith('$봇현황'):
        if message.author.id in owner:
            embed = discord.Embed(title="ABOT", description=f"{len(client.guilds)}개의 서버에 있습니다. {len(client.users)}명의 이용자와 함께합니다.", color=0xe38f4e)
            value = ""
            for guild in client.guilds:
                value += f"{guild.name}\n"
            embed.add_field(name="저는 어느 서버에 있을까요?", value=value)
            await message.channel.send(f"{message.author.mention} DM으로 전송해 드렸어요!")
            await message.author.send(embed=embed)
        else:
            await message.channel.send("해당 명령어는 Owner 등급 이상만 사용 가능합니다.")
    if message.content.startswith("$날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지
        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태


        await message.channel.send(embed=embed)
    if message.content.startswith('$이미지'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 3) # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location) # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        # 크롤링 하는데 있어서 가끔씩 안되는 사이트가 있습니다.
        # 그 이유는 사이트가 접속하는 상대를 봇으로 인식하였기 때문인데
        # 이 코드는 자신이 봇이 아닌것을 증명하여 사이트에 접속이 가능해집니다!
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img') # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source') # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(title="이미지 검색 결과입니다!", timestamp=message.created_at, 
            colour=discord.Colour.green()
        )
        embed.set_image(url=imgsrc) # 이미지의 링크를 지정해 이미지를 설정합니다.
        await message.channel.send(embed=embed) # 메시지를 보냅니다.

        embed = discord.Embed(title="🔎ㅣ날씨", timestamp=message.created_at,
        colour = discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
        await message.channel.send(embed=embed)
    if message.content.startswith("$eval"):
            if message.author.id in owner:
               try:
                   cmd = message.content[6:]
                   output = eval(cmd)
                   await message.channel.send(output)
               except:
                   await message.channel.send("오류가 발생했습니다.")
            else:
                   await message.channel.send("권한 부족")
            
    if message.content.startswith("$정보"):
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
        roles=[role for role in user.roles]
        embed=discord.Embed(colour=message.author.color, timestamp=message.created_at)
        embed.set_author(name=f"{user}님의 정보!")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"{message.author}님에 의해 제공되었어요!", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=user.id, inline = False)
        embed.add_field(name="닉네임", value=user.display_name, inline = False)
        embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=user.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =user.status, inline = False)
        await message.channel.send(embed=embed)
    if message.content == '$시간':
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await message.channel.send(str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에요!")



@client.event
async def on_member_join(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(f"{member.mention} 님, ``" + member.guild.name + "``에 오신걸 환영합니다!")
        role = discord.utils.get(member.guild.roles, name='USER')
        await member.add_roles(role)
    except:
        pass

@client.event
async def on_member_remove(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(member.name + "님이 ``" + member.guild.name + "`` 서버에서 나가셨어요.")
    except:
        pass

client.run('NzM1NDY2MzAyNjgwMDcyMjEy.XxgqXg.71JToYhybj9kgg58JnjUDSKspEQ')
