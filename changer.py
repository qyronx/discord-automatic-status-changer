import discord
import random
from discord.ext import tasks

TOKEN = 'YOUR_DISCORD_TOKEN'

# 상태 리스트 (discord.Status를 활용)
# online: 온라인, idle: 자리비움, dnd: 방해 금지(빨간색), invisible: 오프라인(보이지 않음)
# 1. 상태 아이콘 리스트
STATUS_TYPES = [
    discord.Status.online,
    discord.Status.idle,
    discord.Status.dnd,
    discord.Status.invisible
]

# 2. 상태 메시지 리스트
# 원하는 메시지들을 바꿔넣으세요
STATUS_MESSAGES = [
    "1",
    "2",
    "3",
    "4"
]

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_status = None
        self.last_message = None

    async def on_ready(self):
        print(f'로그인 성공: {self.user}')
        if not self.change_status.is_running():
            self.change_status.start()

    @tasks.loop(seconds=25.0)
    async def change_status(self):
        # 이전과 다른 상태 아이콘 선택
        while True:
            new_status = random.choice(STATUS_TYPES)
            if new_status != self.last_status:
                break
        
        # 이전과 다른 상태 메시지 선택
        while True:
            new_message = random.choice(STATUS_MESSAGES)
            if new_message != self.last_message:
                break
        
        # 값 업데이트 및 적용
        self.last_status = new_status
        self.last_message = new_message
        
        await self.change_presence(
            status=new_status, 
            activity=discord.Game(name=new_message)
        )
        print(f'상태 변경됨: [아이콘: {new_status.name}] [메시지: {new_message}]')

client = MyClient()
client.run(TOKEN)
