# EasyRegi

## 개요

- 2024 HD현대로보틱스 해커톤에서 진행한 HD현대로보틱스 비근등록 매크로 프로그램입니다.
- 프로그램을 실행하여 입력한 정보들을 매크로 프로그램이 HiHR 사이트에 입력을 합니다.
- 비근 등록이 불가능한 날에는 outlook 메일 보내기 기능을 활용하여 자동 양식 작성이 가능합니다.
- 사외망, 사내망 모두 동작 가능합니다.

## 요구조건

1. 해당 매크로 프로그램은 크롬을 활용합니다. 최신 버전의 크롬을 다운받아주십시오.
2. 기존 크롬드라이버가 최신 버전이 아닌 경우, 업데이트를 해주시기 바랍니다.
3. 비근 등록 `메일 보내기` 기능은 `Windows 에서만 활성화`가 됩니다.  
   → `비근등록` 기능은 mac, linux 사용 가능.

## 사용 메뉴얼

1. `비근등록` 기능  
   | 클릭 가능한 경우 | 클릭 시 결과 |
   | :--- | :--- |
   |<img width="387" alt="image" src="https://github.com/user-attachments/assets/b315aaf3-0ac8-431c-97c4-b595f4ac9f1b">|<img width="460" alt="image" src="https://github.com/user-attachments/assets/f4bbcc3a-e526-457e-bc3a-b3490d36e64e">|
   |HiHR에서 비근 등록이 가능한 날은, 근무 당일 전일.|해당 기능이 정상적으로 동작하는 경우, 비근 등록이 자동으로 완료되어집니다.|
   |통합인증 비밀번호는 서버로 절대 전송되지 않습니다. </br> 본인의 폴더에 저장됩니다. 안심하고 사용하셔도 됩니다. | 중간 비근 등록이 불가한 경우, 크롬에서 팝업을 띄운채로 멈춥니다.|


   | 클릭 불가능한 경우 |
   | :--- |
   |<img height="280" alt="image" src=https://github.com/user-attachments/assets/78ce9f75-fd2b-4aa9-bf43-215b6d7e06f3><img height="281" alt="image" src="https://github.com/user-attachments/assets/a6c72666-f22e-4b62-ac0b-b057ef0a3ba5">|
   |당일, 전일이 아니거나 근태 생성시간(00:00~02:30)인 경우 비근등록 버튼 비활성화. 윈도우 환경에서는 메일 보내기를 이용. |  

2. `비근 등록 메일 생성` 기능  
   | 클릭 가능한 경우 | 클릭 시 결과|
   | :--- |:--- |
   |<img height="280" alt="image" src="https://github.com/user-attachments/assets/08a9ba3f-7623-4d7c-bd72-de10a739e0b5">|<img height="300" alt="image" src="https://github.com/user-attachments/assets/d447b114-4672-4767-ba0a-b56b0b77232a">|
   |윈도우 환경에서 날짜에 상관없이 동작.|버튼 클릭 시, 등록정보를 캡쳐하여 자동으로 아웃룩 메일 양식 작성.|

   | 클릭 불가능한 경우 |
   | :--- |
   |<img width="380" alt="image" src="https://github.com/user-attachments/assets/1998e92c-bdb8-49a0-bd07-7c68a00f19ea">|
   | Mac 또는 Linux 인 경우 |


## 설치 메뉴얼

### 1. 실행 파일 다운 받아서 실행

- 최신 소스코드를 통해 빌드된 실행 파일은 [release 페이지](https://github.com/nedleeds/EasyRegi/releases/tag/v1.0.0)를 통해서 다운받을 수 있습니다.
- 다운받은 .exe 파일을 실행해주십시오.

### 2. 최신 소스코드를 빌드해서 실행

- 해당 프로그램은 python 기반으로 작성된 프로그램입니다.
- 하기 과정을 통해 직접 python 코드를 받아서 기능을 수정하고, 빌드하여 커스텀할 수 있습니다.
- 사용중 기능 이상이 있는 경우, 직접 고쳐서 새로 빌드하거나 issue 페이지에 등록해주십시오.
- 빌드는 하기 기술된 과정을 통해 진행할 수 있습니다.

#### 빌드 과정

- python 버전 정보 : 3.8.0 이상

1. 소스 코드 다운

```bash
$cd ~ && git clone https://github.com/nedleeds/EasyRegi.git && cd ./EasyRegi
```

2. 파이썬 패키지 설치

```bash
~/EasyRegi$pip install -r requirements.txt
```

> [INFO] Windows 경우, pip install win32 를 통해 outlook 관련 라이브러리를 추가로 설치 하셔야합니다.

3. 설치된 소스코드 동작 확인

```bash
~/EasyRegi$python main.py
```

4. 소스코드 빌드하기

- 프로그램 실행 시 콘솔 창을 띄우고 싶으면, --windowed 옵션 또는 --no-console 옵션을 끄십시오.
- 아래 명령어는 bash 기준으로 작성됐습니다. Windows 사용자는 git 을 다운받아 git bash 를 활용하십시오.

> 빌드 용 디렉토리 생성

```bash
~/EasyRegi$mkdir pyinstaller
```

> 소스코드 빌드 디렉토리로 복사

```bash
~/EasyRegi$cp -r bot.py data.py main.py ui ./pyinstaller && cd ./pyinstaller

```

> 복사가 정상적으로 됐는지 확인

```bash
~/EasyRegi/pyinstaller$ls
bot.py
data.py
main.py
ui
```

> Mac / Linux 에서 빌드

```bash
~/EasyRegi/pyinstaller$pyinstaller --onefile \
    --add-data "ui:ui" \
    --windowed \
    --log-level "DEBUG" \
    --name "HRBot" \
    --icon "ui/img/rabbit.icns" \
    main.py
```

> Windows 에서 빌드

```bash
~/EasyRegi$pyinstaller --onefile \
    --add-data "ui;ui" \
    --log-level "DEBUG" \
    --no-console \
    --name "HRBot" \
    --icon "ui/img/logo.ico" \
    main.py
```

> 빌드된 결과 확인

```bash
~/EasyRegi/pyinstaller$ls
HRBot.spec
bot.py
build
data.py
dist
main.py
ui
```

> 실행파일 위치

```
EasyRegi
│
└── pyinstaller
      │
      └── dist
           │
           └── HRBot.exe <-- mac/linux 는 바이너리 파일이 생성 됨
```
