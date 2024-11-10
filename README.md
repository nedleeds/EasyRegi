# EasyRegi

## 개요

- 2024 HD현대로보틱스 해커톤에서 진행한 HD현대로보틱스 비근등록 매크로 프로그램입니다.
- 프로그램을 실행하여 입력한 정보들을 매크로 프로그램이 HiHR 사이트에 입력을 합니다.
- 비근 등록이 불가능한 날에는 outlook 메일 보내기 기능을 활용하여 자동 양식 작성이 가능합니다.
- 사외망, 사내망 모두 동작 가능합니다.

## 요구조건

1. 해당 매크로 프로그램은 크롬을 활용합니다. 최신 버전의 크롬을 다운받아주십시오.
2. 기존 크롬드라이버가 최신 버전이 아닌 경우, 업데이트를 해주시기 바랍니다.
3. 비근 등록 메일 보내기 기능은 Windows 에서만 활성화가 됩니다.

## 설치 메뉴얼

### 1. 실행 파일 다운 받아서 실행

- 최신 소스코드를 통해 빌드된 실행 파일은 [release 페이지]()를 통해서 다운받을 수 있습니다.
- 다운받은 .exe 파일을 실행해주십시오.

### 2. 최신 소스코드를 빌드해서 실행

- 해당 프로그램은 python 기반으로 작성된 프로그램입니다.
- 하기 과정을 통해 직접 python 코드를 받아서 빌드해보실 수 있습니다.
- mac, linux 환경에 맞게 직접 수정하여 사용하셔도 됩니다.

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
