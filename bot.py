from data import DataManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    MoveTargetOutOfBoundsException,
    ElementClickInterceptedException,
)
from webdriver_manager.chrome import ChromeDriverManager

import os
import time
import chromedriver_autoinstaller


class Bot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Bot, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._chrome_opend = False
            self._driver = None
            self._data_manager = DataManager.instance()
            self._initialized = True
            # chromedriver_autoinstaller.install()

    def start_chrome(self):
        if not self._chrome_opend:
            chrome_options = Options()
            chrome_options.add_argument(
                "--start-maximized"
            )  # 크롬 창을 최대화해서 엽니다.
            chrome_options.binary_location = self._data_manager._chrome_path
            # options.add_argument("--headless=new")  # 새로운 헤드리스 모드

            # Chrome 드라이버 서비스 생성
            chrome_service = Service(
                executable_path=self._data_manager._chromedriver_path
            )
            self._driver = webdriver.Chrome(
                service=chrome_service, options=chrome_options
            )

            self.check_network()
            if self._network == "in":
                print("사내망 입니다.")
                self._driver.get(
                    "https://hihr.hyundai-robotics.com/EHR/websquare/websquare.html?w2xPath=/UI/MAIN/ZCOM_J0000_05_M.xml"
                )
            else:
                print("사외망 입니다.")
                self._driver.get(
                    "https://ex-hihr.hyundai-robotics.com/EHR/websquare/websquare.html?w2xPath=/UI/MAIN/ZCOM_J0000_05_M.xml"
                )

            self._chrome_opend = True
            return True
        else:
            return False

    def quit_chrome(self) -> None:
        if self._driver is not None:
            self._driver.quit()
            self._driver = None
            self._chrome_opend = False
        else:
            print("생성된 크롬창이 없습니다.")

    def __del__(self):
        self.quit_chrome()

    def check_date(self) -> bool:
        """비근 등록 확인"""
        default_categories = self._data_manager.get_categories()
        selected_category = self._data_manager.get_default_data_with_key("category")

        if selected_category not in default_categories:
            print("등록되지 않은 비근 종류입니다.")
            return False
        else:
            print(f"비근 종류: {selected_category}")
            return True

    def check_network(self) -> None:
        self._network = self._data_manager.get_default_data_with_key("network")

    def try_log_in(self) -> bool:
        id = self._data_manager.get_default_data_with_key("id")
        pw = self._data_manager.get_default_data_with_key("pw")

        try:
            # 최대 10초 동안 "inpUserId" 요소가 나타날 때까지 기다림
            id_input = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.ID, "inpUserId"))
            )
            id_input.send_keys(id)

            password_input = self._driver.find_element(By.ID, "sctPassWord")
            password_input.send_keys(pw)
            password_input.send_keys(Keys.ENTER)  # 로그인 버튼을 대신해 Enter 키 입력
            if self.try_press_alert_confirm(wait_time=1):
                # 비밀번호 입력 실패
                return False
            return True

        except Exception as e:
            print("로그인 아이디 입력 창을 찾을 수 없습니다.", e)
            return False

    def try_enter_register_page(self) -> bool:
        def step_1():
            """1.'보상관리'가 나타날 때까지 기다림"""
            try:
                rewards_link = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "보상관리"))
                )
                actions = ActionChains(self._driver)
                try:
                    actions.move_to_element(rewards_link).perform()
                except ValueError as ve:
                    print(f"Error: {ve}")
                    return False
                except NoSuchElementException:
                    print("Error: '보상관리' 요소를 찾을 수 없습니다.")
                    return False
                except MoveTargetOutOfBoundsException:
                    print("Error: '보상관리' 요소가 화면 범위를 벗어났습니다.")
                    return False
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                    return False
            except TimeoutException:
                print("Error: '보상관리' 요소가 나타나지 않았습니다")
                return False

        def step_2():
            """2. '근태관리' 링크 요소 찾기 및 클릭 (최대 10초)"""
            try:
                attendance_link = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "근태관리"))
                )
                attendance_link.click()

            except TimeoutException:
                print("Error: '근태관리' 링크가 나타나지 않았습니다.")
                return False
            except NoSuchElementException:
                print("Error: '근태관리' 링크 요소를 찾을 수 없습니다.")
                return False
            except ElementClickInterceptedException:
                print("Error: '근태관리'클릭불가. 다른 요소가 가려져 있을 수 있습니다.")
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return False

        def step_3():
            """3."비근 등록" 링크가 나타날 때까지 기다리고 클릭 (최대 10초)"""
            try:
                # "비근 등록" 링크 요소를 기다림
                register_link = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "비근 등록"))
                )
                register_link.click()

            except TimeoutException:
                print("Error: '비근 등록' 링크가 나타나지 않았습니다.")
                return False
            except NoSuchElementException:
                print("Error: '비근 등록' 링크 요소를 찾을 수 없습니다.")
                return False
            except ElementClickInterceptedException:
                print(
                    "Error: '비근 등록' 클릭불가. 다른 요소가 가려져 있을 수 있습니다."
                )
                return False
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return False

        def step_4():
            """4.alert 창 유무 확인(최대 3초)"""
            try:
                alert = WebDriverWait(self._driver, 3).until(EC.alert_is_present())
                print(f"{alert.text}")
                alert.accept()
            except TimeoutException:
                print("비근등록 페이지 접속")

        step_1()
        step_2()
        step_3()
        step_4()
        return True

    def press_keyboard(self, key: str = "tab", cnt: int = 1, delay: float = 0.05):
        """키보드 누르기
        종류) tab, shift, enter, up, down, left, right
        """
        key = key.lower()
        key_to_press = None
        if key == "tab":
            key_to_press = Keys.TAB
        elif key == "shift":
            key_to_press = Keys.SHIFT
        elif key == "enter":
            key_to_press = Keys.ENTER
        elif key == "up":
            key_to_press = Keys.ARROW_UP
        elif key == "down":
            key_to_press = Keys.ARROW_DOWN
        elif key == "left":
            key_to_press = Keys.ARROW_LEFT
        elif key == "right":
            key_to_press = Keys.ARROW_RIGHT
        elif key == "shift_tab":
            key_to_press = (Keys.SHIFT, Keys.TAB)
            print("", end="")
            for i in range(cnt):
                self._driver.switch_to.active_element.send_keys(Keys.SHIFT, Keys.TAB)
                print(f"\rshift+tab 키 입력... {i + 1}", end="")
            print("")
            return
        else:
            print(f"문자열 '{key}'를 입력합니다.")
            self._driver.switch_to.active_element.send_keys(key, Keys.ENTER)
            return

        print("", end="")
        for i in range(cnt):
            self._driver.switch_to.active_element.send_keys(key_to_press)
            print(f"\r{key} 키 입력... {i + 1}", end="")
            time.sleep(delay)
        print("")

    def try_enter_date(self):
        def find_input():
            try:
                # iframe으로 전환
                WebDriverWait(self._driver, 10).until(
                    EC.frame_to_be_available_and_switch_to_it((By.ID, "wframe4"))
                )

                # iframe 안의 <input> 요소를 찾고 클릭
                element = WebDriverWait(self._driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "cal_ZZ_WORK_DT_input"))
                )
                element.click()
                print("Input element clicked successfully!")

                self._driver.switch_to.default_content()
            except Exception as e:
                print("Error:", e)

        def write_date():
            # 사용자 입력한 date 입력
            year = self._data_manager.get_default_data_with_key("year")
            month = self._data_manager.get_default_data_with_key("month")
            day = self._data_manager.get_default_data_with_key("day")

            self.press_keyboard(f"{year}{month:02d}{day:02d}")
            if self.try_press_alert_confirm(wait_time=1):
                # 전날 휴가였는데 비근 등록 시 알람 창 뜸.
                raise Exception("비근 등록을 할 수 없습니다.")
            return True

        find_input()
        write_date()
        return True

    def try_select_category(self):
        """비근 항목 선택"""
        self.press_keyboard("tab", 2)
        category = self._data_manager.get_default_data_with_key("category")
        category_idx = int(self._data_manager.get_categories()[category])
        self.press_keyboard("down", category_idx)
        return True

    def try_enter_time(self):
        """비근 등록 시작 시간 설정"""

        def get_displayed_time(key="time_start") -> str:
            return self._data_manager.get_default_data_with_key(key)

        def parse_time(time_str):
            hour_str, minute_str = time_str.split(":")
            hour = int(hour_str)
            minute = int(minute_str)

            # 10분 단위로 분의 인덱스 계산 (0: 00, 1: 10, ..., 5: 50)
            minute_index = minute // 10
            return hour, minute_index

        def press_time_diff(displayed_start_hour):
            current_time = datetime.now()
            cur_hour = current_time.hour
            hour_diff = cur_hour - displayed_start_hour

            if hour_diff < 0:
                # 현재 시간보다 비근을 등록하려는 시간이 더 클때 -> down!
                self.press_keyboard("down", abs(hour_diff))
            else:
                # 현재 시간보다 비근을 등록하려는 시간이 작거나 같을 때 -> up!
                self.press_keyboard("up", abs(hour_diff))

        def set_time(element_id, time_to_select):
            # 각 옵션에 해당하는 실제 ID 매핑
            id_mapping = {
                "start_hour": "slb_ZZ_START_HOUR_label",
                "start_min": "slb_ZZ_START_MINU_label",
                "end_hour": "slb_ZZ_END_HOUR_label",
                "end_min": "slb_ZZ_END_MINU_label",
            }

            # element_id를 통해 실제 HTML ID 값 확인
            actual_id = id_mapping.get(element_id)
            if not actual_id:
                print(f"잘못된 element_id: {element_id}")
                return False

            try:
                # iframe으로 전환
                WebDriverWait(self._driver, 10).until(
                    EC.frame_to_be_available_and_switch_to_it((By.ID, "wframe4"))
                )

                # 선택된 요소를 찾고 현재 선택된 시간 확인
                current_time_label = WebDriverWait(self._driver, 10).until(
                    EC.presence_of_element_located((By.ID, actual_id))
                )

                # 현재 선택된 시간이 원하는 값과 다른 경우만 설정
                if current_time_label.text != time_to_select:
                    current_time_label.click()

                    # start_hour 설정 시 press_time_diff 적용
                    if element_id == "start_hour":
                        displayed_start_hour = int(
                            current_time_label.text
                        )  # 현재 화면에 표시된 시간
                        target_hour = int(time_to_select)  # 설정하려는 목표 시간

                        # 시간 차이만큼 키보드 입력으로 조정
                        press_time_diff(displayed_start_hour, target_hour)
                        print(f"{element_id} 설정 완료: {time_to_select}")
                    elif element_id == "end_hour":
                        self.press_keyboard("down", 24, 0.0)
                        self.press_keyboard("up", time_to_select)
                    elif element_id == "end_min":
                        self.press_keyboard("up", 6, 0.0)
                        self.press_keyboard("down", time_to_select)
                    else:
                        # Tab 키를 눌러 포커스를 이동
                        self.press_keyboard("down", time_to_select)
                        print(f"{element_id} 설정 완료: {time_to_select}")
                    self.press_keyboard("enter")

                else:
                    print(f"현재 선택된 시간은 이미 {time_to_select}입니다.")

                # 기본 컨텐츠로 돌아오기
                self._driver.switch_to.default_content()
                print(f"{element_id} 설정 완료: {time_to_select}")

                return True

            except Exception as e:
                print(f"오류 발생: {e}")
                return False

        time_start = get_displayed_time(key="time_start")
        time_end = get_displayed_time(key="time_end")

        time_start_hour, index_start_minute = parse_time(time_start)
        time_end_hour, index_end_minute = parse_time(time_end)

        try:
            # start hour set
            self.press_keyboard("tab")
            press_time_diff(time_start_hour)
            self.press_keyboard("tab")

            set_time("start_min", index_start_minute + 1)
            set_time("end_hour", 23 - time_end_hour)
            set_time("end_min", index_end_minute + 1)
            return True

        except Exception:
            return False

    def try_enter_reason(self):
        reason = self._data_manager.get_default_data_with_key("reason")
        try:
            # iframe으로 전환
            WebDriverWait(self._driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "wframe4"))
            )

            # iframe
            element = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.ID, "cal_ZZ_WORK_DT_input"))
            )

            # inp_ZZ_REASON input 요소를 찾고 텍스트 입력
            input_element = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.ID, "inp_ZZ_REASON"))
            )
            input_element.clear()  # 기존 텍스트 삭제
            input_element.send_keys(reason)  # 새로운 텍스트 입력

            # 기본 컨텐츠로 돌아오기
            self._driver.switch_to.default_content()
            print(f"사유 입력 완료 : {reason}")

            return True
        except Exception:
            return False

    def try_press_save(self):
        try:
            # iframe으로 전환
            WebDriverWait(self._driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "wframe4"))
            )

            # btnSave 버튼이 존재하는지 확인
            save_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnSave"))
            )

            # 버튼이 존재할 경우 클릭
            save_button.click()
            print("저장 버튼 클릭 완료")

            # 저장용 alert 선택
            alert = WebDriverWait(self._driver, 1).until(EC.alert_is_present())
            print(alert.text)
            alert.accept()

            return not self.try_press_alert_confirm()

        except Exception:
            return False

    def try_press_alert_confirm(self, wait_time: int = 3):
        # alert가 떴을 때 확인 버튼을 누름
        try:
            alert = WebDriverWait(self._driver, wait_time).until(EC.alert_is_present())
            print(f"{alert.text}")
            return True
        except Exception:
            return False

    def register(self):
        if not self._data_manager._register_time:
            print("지금은 근태 생성 시간입니다.")
        else:
            if self._chrome_opend:
                self.quit_chrome()
            try:
                if not self.check_date():
                    raise Exception("등록된 날짜에는 비근 등록을 할 수 없습니다.")
                if not self.start_chrome():
                    raise Exception("Chrome을 시작하는 데 실패했습니다.")
                if not self.try_log_in():
                    raise Exception("로그인에 실패했습니다.")
                if not self.try_enter_register_page():
                    raise Exception("등록 페이지 진입에 실패했습니다.")
                if not self.try_enter_date():
                    raise Exception("날짜 입력에 실패했습니다.")
                if not self.try_select_category():
                    raise Exception("카테고리 선택에 실패했습니다.")
                if not self.try_enter_time():
                    raise Exception("시간 입력에 실패했습니다.")
                if not self.try_enter_reason():
                    raise Exception("사유 입력에 실패 했습니다.")
                if not self.try_press_save():
                    raise Exception("저장에 실패 했습니다.")
            except Exception as e:
                print(f"오류 발생: {e}")
                return False

    def send_mail(self):
        if self._data_manager._platform == "Windows":
            import win32com.client as win32

            name = self._data_manager.get_default_data_with_key("name")
            team = self._data_manager.get_default_data_with_key("team")
            position = self._data_manager.get_default_data_with_key("position")

            # Outlook Application 객체 생성
            outlook = win32.Dispatch("Outlook.Application")

            # Mail Item 생성
            mail_item = outlook.createItem(0)  # 0은 메일 아이템을 의미

            # Mail 내용 생성
            mail_item.Subject = "비근 등록 요청의 건"

            # 첨부 파일 절대 경로 지정
            attachment_path = self._data_manager.get_img_path()

            # 첨부 파일이 있는지 확인 후 추가
            if os.path.exists(attachment_path):
                attachment = mail_item.Attachments.Add(attachment_path)

                # Content-ID 속성 설정: 간단한 문자열 "image1"로 Content-ID 값을 지정
                attachment.PropertyAccessor.SetProperty(
                    "http://schemas.microsoft.com/mapi/proptag/0x3712001F", "image1"
                )
            else:
                print(f"파일을 찾을 수 없습니다: {attachment_path}")

            # HTML 형식으로 메시지 작성, fotmat 통일
            html_body = f"""
            <html>
                <body>
                    <p style="font-family: 'HD현대체  Light'; font-size: 16px">
                        안녕하십니까. {team} {name} {position}입니다. <br>
                        연일되는 격무에 노고 많으십니다. <br><br>
                        하기와 같이 비근등록 요청드립니다. <br>
                    </p>
                    <img src= "cid:image1" />
                    <p style="font-family: 'HD현대체  Light'; font-size: 16px">

                        감사합니다. <br>
                        {name} 드림.
                    <\p>
                </body>
            </html>
            """

            mail_item.HTMLBody = html_body

            # Mail 창 열기
            mail_item.Display()

            # 캡쳐 사진 삭제
            self._data_manager.delete_img()
        else:
            pass
