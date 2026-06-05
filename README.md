# Discord Auto-Status Changer (Self-bot)

디스코드 계정의 상태(온라인, 자리비움 등)와 활동 메시지를 일정 간격으로 무작위 변경하는 Python 기반 셀프봇 스크립트입니다.

---

## ⚠️ 주의사항

### Discord ToS 위반

이 프로젝트는 일반 사용자 계정을 자동화하는 **셀프봇(Self-bot)** 방식으로 동작합니다.

디스코드는 셀프봇 사용을 서비스 약관(ToS)으로 금지하고 있으며, 사용 시 계정 제재가 발생할 수 있습니다.

### 계정 정지 위험

본 스크립트 사용으로 인해 발생하는 계정 정지, 제한, 기타 불이익에 대한 책임은 전적으로 사용자 본인에게 있습니다.

**실사용 계정이 아닌 테스트 계정에서만 사용을 권장합니다.**

### Rate Limit 주의

상태를 너무 짧은 주기로 변경할 경우 Discord API의 Rate Limit에 도달하여 일시적인 차단 또는 추가 제재가 발생할 수 있습니다.

---

## ✨ 주요 기능

* 🎲 상태 아이콘 무작위 변경

  * 온라인 (`online`)
  * 자리비움 (`idle`)
  * 방해 금지 (`dnd`)
  * 오프라인 (`invisible`)

* 📝 활동 메시지 무작위 변경

* 🔄 중복 방지

  * 직전에 사용한 상태 아이콘 재선택 방지
  * 직전에 사용한 활동 메시지 재선택 방지

* ⚙️ 간편한 커스터마이징

  * 상태 목록 수정 가능
  * 활동 메시지 목록 수정 가능
  * 변경 주기 설정 가능

---

## 📦 설치

필수 라이브러리 설치:

```bash
pip install discord.py-self
```

---

## 🔑 토큰 설정

1. Discord 웹 버전 접속
2. `F12` → **Developer Tools** 실행
3. **Network** 탭 이동
4. 아무 채널에서 메시지 전송
5. `messages` 요청 선택
6. **Request Headers**의 `Authorization` 값 복사
7. 코드의 `TOKEN` 변수에 입력

예시:

```python
TOKEN = "YOUR_DISCORD_TOKEN"
```

---

## ▶️ 실행

```bash
python test.py
```

---

## ⚙️ 설정 커스터마이징

상단의 배열을 수정하여 원하는 상태를 추가할 수 있습니다.

```python
STATUS_TYPES = [
    "online",
    "idle",
    "dnd",
    "invisible"
]

STATUS_MESSAGES = [
    "Working...",
    "Coding",
    "Listening to Music",
    "AFK"
]
```

변경 주기 설정:

```python
@tasks.loop(seconds=25.0)
```

---

## 💡 권장 설정

* 최소 변경 주기: **25초 이상**
* 권장 변경 주기: **30~60초**
* 너무 잦은 변경은 Discord API 제한에 걸릴 수 있습니다.

---

## 📄 면책 조항

이 프로젝트는 교육 및 연구 목적으로 제공됩니다.

사용자는 Discord 서비스 약관을 준수할 책임이 있으며, 본 프로젝트 사용으로 발생하는 모든 문제에 대해 개발자는 책임을 지지 않습니다.
