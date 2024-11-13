# data_manager.py
import os
import sys
import json
import platform
from typing import Dict, Optional


class DataManager:
    _instance: Optional["DataManager"] = None

    def __init__(self) -> None:
        if DataManager._instance is not None:
            raise Exception("이 클래스는 싱글톤입니다. instance() 메서드를 사용하세요.")
        self._data: Dict = {"DEFAULT": {}}  # DEFAULT 키를 기본으로 초기화
        self._default_json_path: str = self.resource_path("default.json")
        self._driver = None
        self._register_time = True
        self._img_path = self.resource_path(
            os.path.join("ui", "img", "gui_screen_capture.png")
        )
        self._platform = self.check_platform()
        self._chrome_path = self.get_chrome_path()
        self._chromedriver_path = self.get_chromedriver_path()

    def check_platform(self) -> str:
        p = platform.system()
        if p == "Windows":
            print("This is Windows.")
        elif p == "Darwin":
            print("This is macOS.")
        elif p == "Linux":
            print("This is Linux")
        else:
            print(f"This os is {self._platform}")
        return p

    def get_chromedriver_path(self) -> str:
        p = self.check_platform()
        if p == "Windows":
            return self.resource_path(
                os.path.join("chrome", "chromedriver-win64", "chromedriver.exe")
            )
        elif p == "Darwin":
            return self.resource_path(
                os.path.join("chrome", "chromedriver-mac-arm64", "chromedriver")
            )
        elif p == "Linux":
            return self.resource_path(
                os.path.join("chrome", "chromedriver-linux64", "chromedriver")
            )
        else:
            raise ("Current OS is not supported.")

    def get_chrome_path(self) -> str:
        p = self.check_platform()
        if p == "Windows":
            return self.resource_path(
                os.path.join("chrome", "chrome-win64", "chrome.exe")
            )
        elif p == "Darwin":
            return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        elif p == "Linux":
            return "/usr/bin/google-chrome"
        else:
            raise ("Current OS is not supported.")

    def resource_path(self, relative_path):
        """PyInstaller 빌드 후 파일 경로 설정"""
        base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
        return os.path.join(base_path, relative_path)

    def get_img_path(self) -> str:
        return self._img_path

    def delete_img(self) -> str:
        os.system(f"rm {self.get_img_path()}")

    @staticmethod
    def instance() -> "DataManager":
        """싱글톤 인스턴스를 반환하는 static 메서드"""
        if DataManager._instance is None:
            DataManager._instance = DataManager()
        return DataManager._instance

    def get_total_data(self) -> dict:
        return self._data

    def set_total_data(self, data: dict, key: str = None, values=None) -> None:
        if data is None:
            self._data[key] = values
        else:
            self._data = data

    def get_categories(self) -> dict:
        return self._data["CATEGORIES"]

    def set_default_data_with_key(self, key: str, value: str) -> None:
        self._data["DEFAULT"][key] = value

    def get_default_data_with_key(self, key: str):
        return self._data["DEFAULT"][key]

    def get_default_data(self) -> dict:
        return self._data["DEFAULT"]

    def load_temp_info(self) -> dict:
        return {
            "CATEGORIES": {
                "--선택--": "0",
                "지각(무급)": "1",
                "외출(무급)": "2",
                "조퇴(무급)": "3",
                "사내개인용무(무급)": "4",
                "안전교육(유급)": "5",
                "예비군훈련(유급)": "6",
                "민방위훈련(유급)": "7",
                "건강검진(유급)": "8",
                "공무외출(유급)": "9",
                "사내교육(유급)": "10",
                "휴게시간(무급)": "11",
                "법정의무교육(유급)": "12",
                "임산부건강진단(유급)": "13",
                "임신초기/말기단축(유급)": "14",
            },
            "DEFAULT": {
                "network": "in",
                "id": "A999999",
                "pw": "123",
                "year": 2024,
                "month": 11,
                "day": 8,
                "time_start": "16:50",
                "time_end": "17:20",
                "reason": "석식",
                "category": "휴게시간(무급)",
                "name": "차은우",
                "position": "연구원",
                "team": "로봇소프트웨어개발팀",
            },
        }

    def load_default_json(self) -> None:
        """JSON 파일에서 data를 읽어와서 self._data에 저장합니다."""
        try:
            with open(self._default_json_path, "r", encoding="utf-8") as file:
                self._data = json.load(file)
        except FileNotFoundError:
            print(
                f"'{self._default_json_path}' 파일이 없습니다. default 데이터를 불러옵니다."
            )
            self._data = self.load_temp_info()
        except json.JSONDecodeError:
            print("Error: JSON 파일을 해석할 수 없습니다.")

    def save_default_json(self, file_path) -> None:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self._data, file, ensure_ascii=False, indent=4)
        except TypeError:
            print("Error: 데이터를 JSON 형식으로 저장할 수 없습니다.")
