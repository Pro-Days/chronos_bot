import asyncio
import os
import requests
import discord
from bs4 import BeautifulSoup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


async def timer(message, sleeping_time, note):
    await asyncio.sleep(sleeping_time*60)
    mention = message.author.mention
    await message.channel.send(f'{mention}님, 타이머가 종료되었습니다.\n[ {note} ]')


class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="서버에 지도나 BGM은 없나요?", description="#기타, #모드"),
            discord.SelectOption(
                label="랭킹 시스템은 없나요?", description="#기타"),
            discord.SelectOption(
                label="캐시 아이템엔 무엇이 있나요?", description="#캐시"),
            discord.SelectOption(
                label="로비에서 다른 사람들이 멈춰있습니다.", description="#기타"),
            discord.SelectOption(
                label="서버에 사용가능한 모드(클라이언트)가 무엇인가요?", description="#모드"),
            discord.SelectOption(
                label="리소스팩 다운이 안됩니다.", description="#리소스팩"),
            discord.SelectOption(
                label="성장에 따른 보상이나 출석체크, 추천같은 보상이 있나요?", description="#기타"),
            discord.SelectOption(
                label="NPC를 못찾겠어요..", description="#기타"),
            discord.SelectOption(
                label="서버 재화엔 무엇이 있나요?", description="#기타, #캐시"),
            discord.SelectOption(
                label="서버에 컨텐츠는 어떤 것들이 있나요?", description="#기타"),
            discord.SelectOption(
                label="길드는 어떻게 이용하나요?", description="#길드"),
            discord.SelectOption(
                label="스킬, 스텟 초기화할 수 없나요?", description="#스킬, #스텟"),
            discord.SelectOption(
                label="직업 변경할 수 없나요?", description="#직업"),
            discord.SelectOption(
                label="디스코드 계정을 바꾸고 싶어요. (디스코드 인증취소)", description="#기타"),
        ]
        super().__init__(
            placeholder="질문을 선택해주세요", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "서버에 지도나 BGM은 없나요?":
            await interaction.response.send_message("""크로노스 가디언즈는 외부 웹사이트를 두어 플레이에 도움을 줄 수 있는 기능을 구현해두었습니다.

[지도]
'/지도' 명령어를 통해 16000 x 16000 크기의 맵을 한눈에 보면서 자신의 위치와 길드원들의 위치와 채널을 한눈에 볼 수 있습니다.
#옵션에서 '지도위치 표시'토글을 통해 길드원에게 위치를 숨길 수도 있습니다.

[BGM]
'/음악 or /bgm' 명령어를 통해 들을 수 있습니다. BGM은 마을, 사냥터, 컨텐츠 장소에 따라 전부다 다른 음악이 재생되며, 저작권이 무료인 음악으로 방송을 하거나 유튜브에 업로드를 해도 문제가 되지 않습니다.""")
        elif self.values[0] == "랭킹 시스템은 없나요?":
            await interaction.response.send_message("""크로노스 가디언즈에서는 레벨 랭킹은 없습니다.

하지만 훈련장에서의 기록 포인트를 통해 훈련장 랭킹이 존재합니다.

훈련장은 레벨뿐만 아니라 자신의 장비가 좋을수록 기록이 더욱 잘나옵니다.

따라서 레벨과 장비의 수준을 모두 반영할 수 있는 컨텐츠인 훈련장을 통해 랭킹이 기록됩니다.
또한, 직업별로 랭킹이 다르게 표시됩니다.

명령어: '/랭킹'


크로노스 가디언즈 서버는 캐릭터를 5개까지 만들 수 있습니다.

그에 따라 특정 플레이어의 랭킹 독식을 방지하고자 캐릭터 별 랭킹이 아닌 마인크래프트 계정기준으로 랭킹에 최고 기록 1개씩만 기록됩니다. 
""")
        elif self.values[0] == "캐시 아이템엔 무엇이 있나요?":
            await interaction.response.send_message("""기본적으로 서버에서 '/캐시충전' 명령어를 이용하여, 충전 웹사이트 링크를 볼 수 있습니다.

캐시충전 시 금화 아이템과 아크 포인트가 지급되며, 해당 재화들은 서버의 '포탈 -> 금화상점'에서 이용이 가능합니다.""")
        elif self.values[0] == "로비에서 다른 사람들이 멈춰있습니다.":
            await interaction.response.send_message("""로비는 유저가 가장 많이 몰리는 서버입니다.

상위 버젼의 특성과 여러가지 기술적인 문제로 서버의 트래픽을 최소화 시키기 위해서 로비에서는 관리자를 제외한 플레이어의 움직임을 차단하고, 스킨데이터 로드를 최소화시켰습니다.

(실제로 다른 유저들은 움직이고 있으나 자신에겐 멈춰있는 것으로만 보입니다.)


로비를 제외한 RPG채널 등에서는 정상적으로 이용이 가능합니다. 
""")
        elif self.values[0] == "서버에 사용가능한 모드(클라이언트)가 무엇인가요?":
            await interaction.response.send_message("""크로노스 가디언즈 서버는 모든 모드를 허용하지 않습니다.
'허용 모드': 옵티파인, 쉐이더, 미니맵, 한글채팅 등

#패브릭 모드는 자동차단됩니다.""")
        elif self.values[0] == "리소스팩 다운이 안됩니다.":
            await interaction.response.send_message("""리소스팩 적용 실패 메시지가 뜰 때는 마인크래프트 폴더 내 server-resource-packs 폴더에 들어가신 후 안에 있는 파일들을 모두 삭제 후 로비 서버에서 '/리소스팩' 명령어를 입력 해 보세요.

#주의: 많은 분들이 server-resource-packs 폴더가 아닌 그냥 resourcepacks 폴더의 파일을 지우십니다. 반드시 server-resource-packs 의 파일을 지워주세요!

카페의 자세한 설명 링크: https://cafe.naver.com/minepictures/83807 


*사례: https://discord.com/channels/587152246433775640/1021243480347004948""")
        elif self.values[0] == "성장에 따른 보상이나 출석체크, 추천같은 보상이 있나요?":
            await interaction.response.send_message("""#크로노스 가디언즈는 추천 시스템이 없습니다.

그냥 서버에 접속만 하고있어도 30분마다 보석이 2개씩 지급됩니다.

또한, 매일매일 받을 수 있는 '/출석체크'가 있으며, 레벨5업마다 '/레벨보상'을 통해 보상을 얻을 수도 있습니다.

기간 이벤트로 진행되는 '/시즌패스'로 출석체크처럼 기간동안 매일 미션을 수행하면서 보상을 얻을 수 있습니다.""")
        elif self.values[0] == "NPC를 못찾겠어요..":
            await interaction.response.send_message("""퀘스트를 하다 보면 NPC위치를 설명해주지만, 설명을 스킵하거나 진짜 못찾겠는 경우.

'/포탈 -> NPC포탈(클릭) -> 원하는 NPC클릭(이동)'으로 간편하게 이동할 수 있습니다.

NPC가 수십 종류다 보니 '가나다 순서'로 정렬되어 표시됩니다.""")
        elif self.values[0] == "서버 재화엔 무엇이 있나요?":
            await interaction.response.send_message("""'크로': 크로노스 가디언즈의 '기본 재화'입니다. 

'보석': 서버에 접속해있다면 30분마다 자동지급되며, 여러 컨텐츠에 필요로합니다.

'금화': '캐시충전'을 하면, 지급되는 재화입니다.

'아크포인트': '캐시충전'을 하면, 금화와 함께 자동 지급되는 재화입니다.(전용 상점)

'파티코인': '파티퀘스트'에서 얻을 수 있으며, 파티상점에서 이용가능합니다.

'훈련코인': '훈련장'에서 얻을 수 있으며, 훈련상점에서 이용가능합니다.

'고대주화': 오픈월드 여기저기에 스폰되는 '보물상자'에서 얻을 수 있으며, '떠돌이상인'의 상점에서 이용이 가능합니다.""")
        elif self.values[0] == "서버에 컨텐츠는 어떤 것들이 있나요?":
            await interaction.response.send_message("""크로노스 가디언즈 서버는 기본적으로 16000 x 16000 크기의 광활한 '오픈월드 모험 RPG서버'입니다.

모험을 즐기면서 '히든장소'를 탐색하고, '히든던전'을 찾아 히든 퀘스트를 수행할 수도 있으며, 직접 탐험을 할 수 있습니다.
(그렇다고 히든을 발견한 유저와 그렇지 못한 유저와 밸런스적으로 극복하지못할 차이가 발생하진 않습니다.)

또한, 육지뿐만 아니라 배를 타고 다른유저들과 대륙을 횡단하며, 숨겨진 섬을 찾을 수 도있으며, 바다에서 해양생물들을 채집하고 사냥할 수도 있습니다.


컨텐츠 목록: https://discord.com/channels/587152246433775640/1022747283105792061""")
        elif self.values[0] == "길드는 어떻게 이용하나요?":
            await interaction.response.send_message("""[길드 안내]
길드에 가입하여 '길드 레이드'를 돌거나, 길드 레벨을 올려 '길드 스킬'을 찍어 영구적으로 길드원의 스텟을 올릴 수 도 있습니다. 추후 '길드 공성전'을 즐길 수 있습니다.


[길드 생성]
생성조건: Lv.70↑, '50만크로', 길드창설권(모험을 통해 '보물상자'를 열어 얻을 수 있습니다.)
길드명은 한글만 가능하며, 최대 4글자까지 가능합니다.

길드원수는 기본 10명까지 가능하며, 금화를 이용하여, 최대 30명까지 늘릴 수 있습니다.


[길드 가입]
가입조건: Lv.40↑


[명령어]
'/go': 길드원 목록을 채팅으로 간편하게 확인가능합니다. 오프라인 길드원은 마지막 로그아웃 시간을 확인하며, 온라인 길드원은 어느 채널에 있는지 알 수 있습니다.

'/gc [할말]': 길드원 끼리 채팅을 할 수 있습니다. 채널이 달라도 가능하며, 로비에서도 사용가능합니다.""")
        elif self.values[0] == "스킬, 스텟 초기화할 수 없나요?":
            await interaction.response.send_message("""크로노스 가디언즈 서버에서는 캐릭터가 Lv.70 이하까지는 초기화가 '무료'입니다.

Lv.71부터는 금화 5개를 소모하여 초기화할 수 있습니다.""")
        elif self.values[0] == "직업 변경할 수 없나요?":
            await interaction.response.send_message("""방법-1)
기본적으로 크로노스 가디언즈는 총 4개의 직업군이 있으며, 2차 전직을 통해 총 8가지의 직업이 존재합니다.

따라서 전직관이 4명이 존재하며, 해당 전직관을 통해 직업을 바꿀 수 있습니다.(레벨 유지)

'직업 변경은 직업 관계없이 전직관을 찾아가면 됩니다.'

전직관을 통해 직업을 변경 시 '금화 15개' 또는 '직업변경권'이 필요합니다.


방법-2)
크로노스 가디언즈는 캐릭터 슬롯이 총 5개까지 가능하며, 기본적으로 2개의 슬롯을 제공합니다.

따라서 2개의 직업을 무료로 즐길 수 있습니다.

또한, 남은 3칸의 캐릭터슬롯을 개방하기 위해선 금화상점에서 '캐릭터슬롯확장권'을 구매하여야 합니다.""")
        elif self.values[0] == "디스코드 계정을 바꾸고 싶어요. (디스코드 인증취소)":
            await interaction.response.send_message("""현재 마크 계정과 디스코드 계정이 이미 인증하여 연동되었지만, 디스코드 계정을 다른것으로 바꾸고 싶다면, 인증취소 후 다른 디스코드 계정으로 인증하여 바꿀 수 있습니다.

[인증취소 방법]
기존 디스코드 인증 방식과 동일하되 로비서버에서 명령어만 '/인증 {발급코드}' 대신
'/인증취소 {발급코드}'를 입력하면 됩니다.

#해당 인증취소의 경우 인증하여 연동된 디스코드 계정으로만 가능합니다.""")


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=10):
        super().__init__(timeout=timeout)
        self.add_item(Select())


@client.event
async def on_ready():

    print('ready')


@client.event
async def on_message(message):

    if message.author.bot:
        return None

    elif message.content == "!서버정보":

        print(f"log.{message.content}")

        url = "https://mcapi.us/server/status?ip=chronos.skhidc.kr&port=25565"
        data = requests.get(url).json()
        del data["favicon"]

        status = data["status"]
        max_player = data["players"]["max"]
        now_player = data["players"]["now"]

        embed = discord.Embed(title='크로노스 가디언즈 정보', color=0x00ff56)

        if status == "success":
            embed.add_field(name='서버 상태', value="접속 가능", inline=True)
        else:
            embed.add_field(name='서버 상태', value="접속 불가능", inline=True)

        embed.add_field(
            name='플레이어', value=f"{now_player} / {max_player}", inline=True)

        await message.channel.send(embed=embed)

    elif message.content == "!지도":

        print(f"log.{message.content}")

        await message.channel.send('http://chronosmap.skhidc.kr/')

    elif message.content == "!카페":

        print(f"log.{message.content}")

        await message.channel.send('https://cafe.naver.com/minepictures')

    elif message.content == "!디스코드":

        print(f"log.{message.content}")

        await message.channel.send('https://discord.gg/f6zYFyP3VP')

    elif message.content == "!후원":

        print(f"log.{message.content}")

        await message.channel.send('https://skhcs.com/chronos')

    elif message.content == "!리소스팩":

        print(f"log.{message.content}")

        await message.channel.send('기본적으로 서버 접속 시 자동으로 리소스팩이 적용됩니다.\n\n서버 접속 시 정상적으로 적용되시는 분들은 수동 적용할 필요가 없습니다.\n\n무선인터넷 등 인터넷 환경이 좋지 않을 경우 자동 접속 중 튕길 수 있습니다.\n서버에 접속 중 리소스팩을 정상적으로 받지 못해 튕기시는 분은\n\n" AppData\Roaming.minecraft\server-resource-packs " 경로의 파일을 모두 지운 후\n\n같은 경로에 아래 파일을 그대로 넣은 후 서버에 다시 접속하시면 됩니다.\nhttp://tx-cdn.skhidc.kr:1205/SUDRA/3200bb9bcf4d27b09d7554f41075c35b44055588\n파일명이나 확장자를 절대 변경하지 말고 그대로 server-resource-packs 폴더에 넣어주세요.')

    elif message.content == "!직업설명":

        print(f"log.{message.content}")

        embed = discord.Embed(title='직업설명', color=0x00ff56)

        embed.add_field(
            name='발리언트 직업군 설명', value="https://cafe.naver.com/minepictures/88635", inline=False)
        embed.add_field(
            name='파우스트 직업군 설명', value="https://cafe.naver.com/minepictures/88637", inline=False)
        embed.add_field(
            name='어쌔신 직업군 설명', value="https://cafe.naver.com/minepictures/88636", inline=False)
        embed.add_field(
            name='트러블슈터 직업군 설명', value="https://cafe.naver.com/minepictures/88639", inline=False)

        await message.channel.send(embed=embed)

    elif message.content == "!규칙":

        print(f"log.{message.content}")

        embed = discord.Embed(title='규칙', color=0x00ff56)

        embed.add_field(
            name='규칙관련 공지', value="투다이스 컨텐츠 내의 규칙상 서버내(카페,게임,디스코드 등) 노출되는 텍스트 형식의 글 중 규칙 위반사항이 있을 시 처벌됩니다.\n이는 디스코드 내 상태메세지, 닉네임 또한 마찬가지 이므로 주의 바랍니다.", inline=False)
        embed.add_field(
            name='서버 규칙', value="https://cafe.naver.com/minepictures/83716", inline=False)
        embed.add_field(
            name='카페 규칙', value="https://cafe.naver.com/minepictures/12920", inline=False)
        embed.add_field(
            name='디스코드 규칙', value="https://cafe.naver.com/minepictures/78355", inline=False)

        await message.channel.send(embed=embed)

    elif str(message.content).startswith("!타이머"):

        print(f"log.{message.content}")

        try:
            msg = str(message.content).split()
            sleeping_time = int(msg[1])
            note = " ".join(msg[2:])
        except:
            await message.channel.send('!타이머 <시간(분)> <메모>')
        else:
            await message.channel.send(f'타이머가 시작되었습니다. ( {str(sleeping_time)}분 )\n[ {note} ]')
            await timer(message, sleeping_time, note)

    elif message.content == "!질문":

        print(f"log.{message.content}")

        await message.channel.send("자주 묻는 질문", view=SelectView())

    elif str(message.content).startswith("!랭킹"):

        print(f"log.{message.content}")

        msg = str(message.content).split()
        try:
            job = msg[1]
        except:
            await message.channel.send("!랭킹 <직업> <페이지>")
        else:
            try:
                page = int(msg[2])
            except:
                await message.channel.send("!랭킹 <직업> <페이지(1, 2)>")
            else:
                if job == "로드나이트":
                    url_job = "val_1"
                elif job == "로드워리어":
                    url_job = "val_2"
                elif job == "다크디발러":
                    url_job = "fau_1"
                elif job == "라이트가디언":
                    url_job = "fau_2"
                elif job == "버서커블레이드":
                    url_job = "ass_1"
                elif job == "쉐도우워커":
                    url_job = "ass_2"
                elif job == "프로슈터":
                    url_job = "trb_1"
                elif job == "샤프슈터":
                    url_job = "trb_2"
                url = f"http://chronosrank.skhidc.kr/ranking.php?job={url_job}"

                response = requests.get(url)
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                # print(soup)

                gray = soup.select("td.gray")
                white = soup.select("td.white")

                gray_list = []
                for i in range(0, len(gray), 4):
                    gray_list.append(
                        [gray[i].get_text().replace(" ", ""), gray[i+1].get_text().replace(" ", ""), gray[i+2].get_text().replace(" ", ""), gray[i+3].get_text().replace(" ", "")])

                white_list = []
                for i in range(0, len(white), 4):
                    white_list.append([white[i].get_text(
                    ).replace(" ", ""), white[i+1].get_text().replace(" ", ""), white[i+2].get_text().replace(" ", ""), white[i+3].get_text().replace(" ", "")])

                rank_list = []
                for i in range(10):
                    rank_list.append(gray_list[i])
                    rank_list.append(white_list[i])

                embed = discord.Embed(title=f'{job}랭킹', color=0x00ff56)

                if 0 <= page*10 <= len(rank_list):
                    for i in range((page-1)*10, page*10):
                        embed.add_field(
                            name=f"{i+1}위", value=f"닉네임: {rank_list[i][0]},  레벨: {rank_list[i][1].replace('Lv.', '')},  점수: {rank_list[i][2]}점", inline=False)

                await message.channel.send(embed=embed)

    elif str(message.content).startswith("!길드랭킹"):

        print(f"log.{message.content}")

        msg = str(message.content).split()
        try:
            page = int(msg[1])
        except:
            await message.channel.send("!길드랭킹 <페이지>")
        else:

            url = "http://chronosrank.skhidc.kr/guild.php"

            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)

            gray = soup.select("td.gray")
            white = soup.select("td.white")

            gray_list = []
            for i in range(0, len(gray), 3):
                gray_list.append(
                    [gray[i].get_text().replace(" ", ""), gray[i+1].get_text().replace(" ", ""), gray[i+2].get_text().replace(" ", "")])

            white_list = []
            for i in range(0, len(white), 3):
                white_list.append([white[i].get_text(
                ).replace(" ", ""), white[i+1].get_text().replace(" ", ""), white[i+2].get_text().replace(" ", "")])

            rank_list = []
            if len(gray_list) % 2 == 0:
                for i in range(len(white_list)):
                    rank_list.append(gray_list[i])
                    rank_list.append(white_list[i])
            else:
                for i in range(len(white_list)):
                    rank_list.append(gray_list[i])
                    rank_list.append(white_list[i])
                rank_list.append(gray_list[-1])

            # print(rank_list)

            embed = discord.Embed(title='길드랭킹', color=0x00ff56)
    # 4, 49
    # 0 <= 40 < 49
            if 0 <= page*10 <= len(rank_list):
                for i in range((page-1)*10, page*10):
                    embed.add_field(
                        name=f"{i+1}위", value=f"길드: {rank_list[i][0]},  길드장: {rank_list[i][1]},  레벨: {rank_list[i][2].replace('Lv.', '')}", inline=False)

                await message.channel.send(embed=embed)

            elif page*10 > len(rank_list) > (page-1)*10:
                for i in range((page-1)*10, len(rank_list)):
                    embed.add_field(
                        name=f"{i+1}위", value=f"길드: {rank_list[i][0]},  길드장: {rank_list[i][1]},  레벨: {rank_list[i][2].replace('Lv.', '')}", inline=False)

                await message.channel.send(embed=embed)
            else:
                await message.channel.send("페이지가 존재하지 않습니다.")

    elif message.content == "!명령어":

        print(f"log.{message.content}")

        embed = discord.Embed(title='명령어', color=0x00ff56)

        embed.add_field(
            name='!서버정보', value="서버의 정보를 확인합니다.", inline=False)
        embed.add_field(
            name='!지도', value="서버지도의 링크를 확인합니다.", inline=False)
        embed.add_field(
            name='!카페', value="카페의 링크를 확인합니다.", inline=False)
        embed.add_field(
            name='!디스코드', value="디스코드의 링크를 확인합니다.", inline=False)
        embed.add_field(
            name='!후원', value="후원링크를 확인합니다.", inline=False)
        embed.add_field(
            name='!리소스팩', value="리소스팩 수동적용에 관한 정보를 확인합니다.", inline=False)
        embed.add_field(
            name='!직업설명', value="각 직업에 대한 설명을 확인합니다.", inline=False)
        embed.add_field(
            name='!규칙', value="규칙을 확인합니다.", inline=False)
        embed.add_field(
            name='!타이머 <시간(분)> <메모>', value="타이머를 작동시킵니다.", inline=False)
        embed.add_field(
            name='!질문', value="자주 묻는 질문 목록을 확인합니다.", inline=False)
        embed.add_field(
            name='!명령어', value="사용할 수 있는 명령어 목록을 확인합니다.", inline=False)

        await message.channel.send(embed=embed)



TOKEN = os.environ.get('BOT_TOKEN')
client.run(TOKEN)
