# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\theca\Desktop\Hackerton\Resistration_of_non_working.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from data import DataManager
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt, QDate, QLocale

import os
import json


class Ui_MainWindow(object):
    _data_manager = DataManager.instance()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 450)
        self.set_window_icon(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Case 2
        # 흰배경
        self.centralwidget.setStyleSheet("""
            QWidget#centralwidget {
                background-color: #ffffff /* White */
                color: #000000
            };
        """)

        # 그룹박스 및 주요 UI 설정
        self.setup_radio_buttons()
        self.setup_labels()
        self.setup_text_browsers()
        self.setup_buttons()
        self.setup_comboboxes()
        self.setup_calendar()
        self.setup_font()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.on_register_click)
        self.pushButton_2.clicked.connect(self.on_send_mail_click)

    def set_window_icon(self, MainWindow):
        icon = QtGui.QIcon()
        icon_path = self._data_manager.resource_path(
            os.path.join("ui", "img", "logo.png")
        )
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def setup_labels(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 56, 21))
        self.label.setObjectName("label")
        self.label.setStyleSheet("""
            QLabel {
                font-size: 10pt; /* 폰트 크기를 10포인트로 설정 */
                /*color: black; 진한 남색 (#2c3e50)으로 설정 */
            }
        """)

        # 날짜 설정
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(70, 40, 300, 21))
        self.label_date.setObjectName("label_date")

        # 소속 설정
        self.label_team = QtWidgets.QLabel(self.centralwidget)
        self.label_team.setGeometry(QtCore.QRect(380, 30, 56, 31))
        self.label_team.setObjectName("label_team")

        # 직위 설정
        self.label_position = QtWidgets.QLabel(self.centralwidget)
        self.label_position.setGeometry(QtCore.QRect(380, 70, 56, 31))
        self.label_position.setObjectName("label_position")

        # 사번 설정
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(380, 110, 56, 31))
        self.label_id.setObjectName("label_id")

        # 비번 설정
        self.label_pw = QtWidgets.QLabel(self.centralwidget)
        self.label_pw.setGeometry(QtCore.QRect(380, 150, 56, 31))
        self.label_pw.setObjectName("label_pw")

        # 이름 설정
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(380, 190, 56, 31))
        self.label_name.setObjectName("label_name")

        # 비근 항목 설정
        self.label_category = QtWidgets.QLabel(self.centralwidget)
        self.label_category.setGeometry(QtCore.QRect(380, 230, 71, 31))
        self.label_category.setObjectName("label_category")

        # 시간 설정
        self.label_time_start = QtWidgets.QLabel(self.centralwidget)
        self.label_time_start.setGeometry(QtCore.QRect(380, 270, 71, 31))
        self.label_time_start.setObjectName("label_time_start")
        self.label_time_end = QtWidgets.QLabel(self.centralwidget)
        self.label_time_end.setGeometry(QtCore.QRect(380, 310, 71, 31))
        self.label_time_end.setObjectName("label_time_end")
        self.setup_small_labels()

        self.label_reason = QtWidgets.QLabel(self.centralwidget)
        self.label_reason.setGeometry(QtCore.QRect(380, 350, 71, 21))
        self.label_reason.setObjectName("label_reason")

    def setup_radio_buttons(self):
        # 위치 조정을 위한 container 위젯 생성
        container_widget = QtWidgets.QWidget(self.centralwidget)
        container_widget.setGeometry(
            QtCore.QRect(8, 10, 200, 35)
        )  # container의 위치와 크기 설정

        h_layout = QtWidgets.QHBoxLayout(container_widget)
        label = QtWidgets.QLabel("네트워크: ")
        label.setGeometry(QtCore.QRect(22, 10, 200, 35))

        # QButtonGroup으로 라디오 버튼 그룹 설정
        self.network_group = QtWidgets.QButtonGroup(container_widget)

        # 라디오 버튼 생성
        self.internal_network_button = QtWidgets.QRadioButton("사내망")
        self.external_network_button = QtWidgets.QRadioButton("외부망")

        # 기본값 설정 (예: 사내망 기본 선택)
        self.setup_default_network()

        # 버튼 그룹에 라디오 버튼 추가
        self.network_group.addButton(self.internal_network_button)
        self.network_group.addButton(self.external_network_button)

        # 수평 레이아웃에 라벨과 버튼 추가
        h_layout.addWidget(label)
        h_layout.addWidget(self.internal_network_button)
        h_layout.addWidget(self.external_network_button)

        # 신호 연결
        self.network_group.buttonClicked.connect(self.on_network_selection)

    def on_network_selection(self):
        """라디오 버튼 선택 결과 확인"""
        if self.internal_network_button.isChecked():
            self._data_manager.set_default_data_with_key("network", "in")
            print("사내망이 선택되었습니다.")
            # 사내망에 대한 처리 로직
        elif self.external_network_button.isChecked():
            self._data_manager.set_default_data_with_key("network", "out")
            print("외부망이 선택되었습니다.")

    def setup_small_labels(self):
        self.label_time_start_hour = QtWidgets.QLabel(self.centralwidget)
        self.label_time_start_hour.setGeometry(QtCore.QRect(520, 270, 21, 31))
        self.label_time_start_hour.setObjectName("label_time_start_hour")

        self.label_time_start_min = QtWidgets.QLabel(self.centralwidget)
        self.label_time_start_min.setGeometry(QtCore.QRect(600, 270, 21, 31))
        self.label_time_start_min.setObjectName("label_time_start_min")

        self.label_time_end_min = QtWidgets.QLabel(self.centralwidget)
        self.label_time_end_min.setGeometry(QtCore.QRect(600, 310, 21, 31))
        self.label_time_end_min.setObjectName("label_time_end_min")

        self.label_time_end_hour = QtWidgets.QLabel(self.centralwidget)
        self.label_time_end_hour.setGeometry(QtCore.QRect(520, 310, 21, 31))
        self.label_time_end_hour.setObjectName("label_time_end_hour")

    def setup_text_browsers(self):
        self.input_team = QtWidgets.QLineEdit(self.centralwidget)
        self.input_team.setGeometry(QtCore.QRect(460, 30, 161, 31))
        self.input_team.setObjectName("input_team")
        self.setup_default_team()

        self.input_position = QtWidgets.QLineEdit(self.centralwidget)
        self.input_position.setGeometry(QtCore.QRect(460, 70, 161, 31))
        self.input_position.setObjectName("input_position")
        self.setup_default_position()

        self.input_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(460, 110, 161, 31))
        self.input_id.setObjectName("input_id")
        self.setup_default_id()

        self.input_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pw.setGeometry(QtCore.QRect(460, 150, 161, 31))
        self.input_pw.setObjectName("input_pw")
        self.input_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.setup_default_pw()

        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(460, 190, 161, 31))
        self.input_name.setObjectName("input_name")
        self.setup_default_name()

        self.input_reason = QtWidgets.QLineEdit(self.centralwidget)
        self.input_reason.setGeometry(QtCore.QRect(380, 370, 241, 62))
        self.input_reason.setObjectName("input_reason")
        self.input_reason.setAlignment(Qt.AlignCenter)
        self.setup_default_reason()

    def setup_buttons(self):
        def check_date_for_regist():
            if not self.pushButton.isEnabled():
                print("비근 등록이 불가능한 날짜 입니다.")
            else:
                print("비근 등록 작업을 진행합니다.")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 150, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 380, 150, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        # Case 1

        # 버튼 스타일 (파란색 톤, 둥근 모서리, 마우스 오버 시 진한 색상)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background: #007ACC;
                color: white;
                border-radius: 6px;
                padding: 5px;
            }
            QPushButton:disabled {
                background: #444444;  /* 진한 회색 */
                color: #666666;       /* 연한 회색 텍스트 */
            }m
        """)

        self.pushButton_2.setStyleSheet("""
        QPushButton {
            background: #007ACC;
            color: white;
            border-radius: 6px;
            padding: 5px;
        }
        QPushButton:disabled {
            background: #444444;  /* 진한 회색 */
            color: #666666;       /* 연한 회색 텍스트 */
        }
        """)

        self.set_pushButton_2_enable(True)
        self.pushButton.clicked.connect(check_date_for_regist)

    def setup_comboboxes(self):
        # 카테고리 콤보박스
        self.comboBox_category = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_category.setGeometry(QtCore.QRect(460, 230, 161, 31))
        self.comboBox_category.setObjectName("comboBox_category")
        self.setup_default_categories()
        self.setup_default_category()

        # 시작 시간(시)
        self.comboBox_time_start_hour = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time_start_hour.setGeometry(QtCore.QRect(460, 270, 50, 31))
        self.comboBox_time_start_hour.setObjectName("comboBox_time_start_hour")
        for hour in range(24):
            self.comboBox_time_start_hour.addItem(f"{hour:02}")

        # 시작 시간(분)
        self.comboBox_time_start_minute = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time_start_minute.setGeometry(QtCore.QRect(540, 270, 50, 31))
        self.comboBox_time_start_minute.setObjectName("comboBox_time_start_minute")
        for minute in range(0, 51, 10):
            self.comboBox_time_start_minute.addItem(f"{minute:02}")

        # 종료 시간(시)
        self.comboBox_time_end_hour = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time_end_hour.setGeometry(QtCore.QRect(460, 310, 50, 31))
        self.comboBox_time_end_hour.setObjectName("comboBox_time_end_hour")
        for hour in range(24):
            self.comboBox_time_end_hour.addItem(f"{hour:02}")

        # 종료 시간(분)
        self.comboBox_time_end_minute = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_time_end_minute.setGeometry(QtCore.QRect(540, 310, 50, 31))
        self.comboBox_time_end_minute.setObjectName("comboBox_time_end_minute")
        for minute in range(0, 51, 10):
            self.comboBox_time_end_minute.addItem(f"{minute:02}")
        self.setup_default_time()

    def setup_calendar(self):
        def return_to_today():
            # 오늘 날짜로 돌아가기
            today = QtCore.QDate.currentDate()
            self.calendarWidget.setSelectedDate(today)
            self.update_date_label(today)
            self.set_pushButton_2_enable(True)
            self.pushButton.setEnabled(True)  # pushButton 활성화

        def adjust_month_dropdown():
            """캘린더 위젯의 월 선택 드롭박스 크기를 조정"""
            # 'qt_calendar_monthbutton' 이름으로 드롭다운 버튼 찾기
            month_dropdown = self.findChild(
                QtWidgets.QToolButton, "qt_calendar_monthbutton"
            )
            if month_dropdown:
                month_dropdown.setFixedWidth(60)  # 원하는 너비로 설정
                month_dropdown.setStyleSheet("""
                    QCalendarWidget QToolButton::menu-indicator { 
                        width: 0px;  /* 드롭다운 버튼 화살표 너비 조정 */
                    }
                    QCalendarWidget QAbstractItemView {
                        min-width: 0px; /* 드롭다운 목록의 최소 너비 설정 */
                    }
                    QComboBox {
                        background: transparent;  /* 배경 투명 */
                        border: none;             /* 테두리 없음 */
                        color: black;             /* 텍스트 색상 */
                        padding: 2px;
                        font-size: 9px;
                    }
                    QComboBox::drop-down {
                        border: none;             /* 드롭다운 버튼 테두리 없음 */
                        background: transparent;  /* 드롭다운 버튼 배경 투명 */
                    }
                    QComboBox QAbstractItemView {
                        selection-background-color: lightgray;  /* 선택 항목 배경 */
                        background: transparent;
                    }
                """)
            year_dropdown = self.findChild(
                QtWidgets.QToolButton, "qt_calendar_yearbutton"
            )
            if year_dropdown:
                year_dropdown.setFixedWidth(60)  # 원하는 너비로 설정
                year_dropdown.setStyleSheet("""
                    QComboBox {
                        background: transparent;
                        border: none;
                        color: black;
                        padding: 2px;
                        font-size: 9px;
                    }
                    QComboBox::drop-down {
                        border: none;
                        background: transparent;
                    }
                    QComboBox QAbstractItemView {
                        background: transparent;
                        selection-background-color: lightgray;
                        background: transparent;
                    }
                """)

        # Calendar Widget 추가
        korean_locale = QLocale(QLocale.Korean, QLocale.SouthKorea)
        QLocale.setDefault(korean_locale)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setVerticalHeaderFormat(
            QtWidgets.QCalendarWidget.NoVerticalHeader
        )
        self.calendarWidget.setGeometry(QtCore.QRect(20, 70, 320, 300))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setLocale(korean_locale)

        # 오늘 돌아가기 버튼 생성
        today_button = QtWidgets.QPushButton("오늘", self)
        today_button.setGeometry(QtCore.QRect(80, 75, 320, 300))
        today_button.setStyleSheet(
            """
            background: #007ACC;
            color: white;
            border-radius: 3px;
            max-width: 20px;
            max-height: 14px;
            """
        )
        today_button.clicked.connect(return_to_today)

        adjust_month_dropdown()

        # case 2
        self.calendarWidget.setStyleSheet("""
        QHeaderView::section {
        background-color : #008233;
        color : #ffffff;
        }
        QTableView::item:selected {
        background-color: #008233;  
        color: white;  
        }
        QCalendarWidget QTableView QHeaderView::section {
        width: 0;  /* 주차(week number) 부분 숨기기 */
        }
        """)

        # 오늘 날짜와 전일을 활성화하고 나머지 날짜는 비활성화
        self.today = QDate.currentDate()
        self.previous_day = self.today.addDays(-1)

        # 초기 날짜 라벨 업데이트
        self.calendarWidget.setSelectedDate(self.today)
        self.update_date_label(self.today)

        # 날짜 클릭 이벤트에 check_date 함수 연결
        self.calendarWidget.clicked.connect(self.check_date)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "HD현대로보틱스 비근 자동 등록 프로그램")
        )

        # Labels and button text
        label_width = 8  # 각 라벨 문자열의 고정 길이 (필요에 맞게 조절 가능)

        self.label.setText(_translate("MainWindow", "날짜 : "))
        self.label_date.setText("날짜를 선택하세요.")
        self.label_id.setText(
            _translate("MainWindow", f"{'사':<{label_width + 1}}번 : ")
        )
        self.label_name.setText(
            _translate("MainWindow", f"{'이':<{label_width + 1}}름 : ")
        )
        self.label_position.setText(
            _translate("MainWindow", f"{'직':<{label_width + 1}}위 : ")
        )
        self.label_team.setText(
            _translate("MainWindow", f"{'소':<{label_width + 1}}속 : ")
        )
        self.label_category.setText(
            _translate("MainWindow", f"{'비근 항목':<{label_width}}: ")
        )
        self.label_reason.setText(_translate("MainWindow", "사유"))
        self.pushButton.setText(_translate("MainWindow", "비근 등록"))
        self.pushButton_2.setText(_translate("MainWindow", "비근 등록 메일 생성"))
        self.label_pw.setText(
            _translate("MainWindow", f"{'비밀 번호':<{label_width}}: ")
        )
        self.label_time_start.setText(
            _translate("MainWindow", f"{'시작 시간':<{label_width}}: ")
        )
        self.label_time_end.setText(
            _translate("MainWindow", f"{'종료 시간':<{label_width}}: ")
        )
        self.label_time_start_hour.setText(_translate("MainWindow", "시"))
        self.label_time_start_min.setText(_translate("MainWindow", "분"))
        self.label_time_end_hour.setText(_translate("MainWindow", "시"))
        self.label_time_end_min.setText(_translate("MainWindow", "분"))

    def setup_default_network(self) -> None:
        """기본 네트워크 설정"""
        network = self._data_manager.get_default_data_with_key("network")

        if network == "in":
            self.internal_network_button.setChecked(True)
            self.external_network_button.setChecked(False)
        else:
            self.internal_network_button.setChecked(False)
            self.external_network_button.setChecked(True)

    def setup_default_team(self) -> None:
        """이름 입력 시 기본 설정값 지정"""
        default_team = self._data_manager.get_default_data()["team"]
        self.input_team.setText(default_team)

    def setup_default_position(self) -> None:
        """이름 입력 시 기본 설정값 지정"""
        default_position = self._data_manager.get_default_data()["position"]
        self.input_position.setText(default_position)

    def setup_default_id(self) -> None:
        """이름 입력 시 기본 설정값 지정"""
        default_id = self._data_manager.get_default_data()["id"]
        self.input_id.setText(default_id)

    def setup_default_pw(self) -> None:
        default_pw = self._data_manager.get_default_data()["pw"]
        self.input_pw.setText(default_pw)

    def setup_default_name(self) -> None:
        default_name = self._data_manager.get_default_data()["name"]
        self.input_name.setText(default_name)

    def setup_default_categories(self):
        for c in self._data_manager.get_total_data()["CATEGORIES"]:
            self.comboBox_category.addItem(f"{c}")

    def setup_default_category(self):
        default_category = self._data_manager.get_default_data()["category"]
        self.comboBox_category.setCurrentText(default_category)

    def setup_default_time(self):
        """시간 입력 시 기본 설정값 지정"""

        def parse_time(time_str):
            hour_str, minute_str = time_str.split(":")
            hour = int(hour_str)
            minute = int(minute_str)

            # 10분 단위로 분의 인덱스를 계산 (0: 00, 1: 10, ..., 6: 60)
            minute_index = minute // 10
            return hour, minute_index

        # default 시간 로드
        time_start = self._data_manager.get_default_data()["time_start"]
        time_end = self._data_manager.get_default_data()["time_end"]

        # 시작 시간 설정
        start_hour, start_minute_index = parse_time(time_start)
        self.comboBox_time_start_hour.setCurrentIndex(start_hour)
        self.comboBox_time_start_minute.setCurrentIndex(start_minute_index)

        # 종료 시간 설정
        end_hour, end_minute_index = parse_time(time_end)
        self.comboBox_time_end_hour.setCurrentIndex(end_hour)
        self.comboBox_time_end_minute.setCurrentIndex(end_minute_index)

    def setup_default_reason(self):
        """사유 입력 시 기본 설정값 지정"""
        reason = self._data_manager.get_default_data()["reason"]
        self.input_reason.setText(reason)

    def set_pushButton_2_enable(self, state: bool = True):
        if self._data_manager._platform == "Windows":
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)

    def check_time_for_regist(self) -> bool:
        """근태 생성시간 확인
        자정 ~ 새벽 2시 30분 근태 생성 불가"""

        # 현재 시간을 24시간 형식으로 가져오기
        current_time = QtCore.QTime.currentTime()

        # 비교할 시간 범위 설정 (자정 00:00 ~ 새벽 2:30)
        start_time = QtCore.QTime(0, 0)  # 00:00
        end_time = QtCore.QTime(2, 30)  # 02:30

        # 현재 시간이 자정에서 새벽 2:30 사이인 경우
        if start_time <= current_time < end_time:
            self.label_date.setText(
                "지금은 근태 생성 시간이 아닙니다. '<span style=\"background-color: #660000; color: white; padding: 2px;\">매일 00:00~2:30</span>' 클릭."
            )
            self._data_manager._register_time = False
            self.set_pushButton_2_enable(True)
            self.pushButton.setEnabled(False)  # pushButton 활성화
            return False

        # 생성 가능한 시간대일 경우
        self._data_manager._register_time = True
        return True

    def check_date(self, date: QDate):
        if self.check_time_for_regist():
            if date == self.today or date == self.previous_day:
                self.update_date_label(date)
                self.set_pushButton_2_enable(True)
                self.pushButton.setEnabled(True)  # pushButton 활성화
            else:
                # 비활성화된 날짜를 클릭한 경우 메시지 표시 및 선택 취소
                self.label_date.setText(
                    "비근등록 생성일이 아닙니다. '<span style=\"background-color: #007ACC; color: white; padding: 2px;\">비근 등록 메일 생성</span>' 클릭."
                )
                self.set_pushButton_2_enable(True)
                self.pushButton.setEnabled(False)  # pushButton 활성화

    def update_date_label(self, date: QDate):
        korean_locale = QLocale(QLocale.Korean, QLocale.SouthKorea)
        formatted_date = korean_locale.toString(date, "yyyy년 MM월 dd일 dddd")
        self.label_date.setText(formatted_date)

    def get_displayed_network(self) -> str:
        network = self.network_group.checkedButton().text()
        print(network)
        network = "in" if network == "사내망" else "out"
        return network

    def get_displayed_id(self) -> str:
        return self.input_id.text()

    def get_displayed_date(self) -> str:
        displayed_date = self.calendarWidget.selectedDate()
        return displayed_date.year(), displayed_date.month(), displayed_date.day()

    def get_displayed_team(self) -> str:
        return self.input_team.text()

    def get_displayed_position(self) -> str:
        return self.input_position.text()

    def get_displayed_name(self) -> str:
        return self.input_name.text()

    def get_displayed_pw(self) -> str:
        return self.input_pw.text()

    def get_displayed_reason(self) -> str:
        return self.input_reason.text()

    def get_register_date(self) -> str:
        selected_qdate = self.calendarWidget.selectedDate()
        return selected_qdate.year(), selected_qdate.month(), selected_qdate.day()

    def get_displayed_category(self) -> str:
        return self.comboBox_category.currentText()

    def get_displayed_time_start(self) -> str:
        displayed_hour = self.comboBox_time_start_hour.currentText()
        displayed_minute = self.comboBox_time_start_minute.currentIndex() * 10
        return f"{displayed_hour}:{displayed_minute}"

    def get_displayed_time_end(self) -> str:
        displayed_hour = self.comboBox_time_end_hour.currentText()
        displayed_minute = self.comboBox_time_end_minute.currentIndex() * 10
        return f"{displayed_hour}:{displayed_minute}"

    def get_displayed_data(self) -> dict:
        displayed_date = self.get_displayed_date()
        displayed_network = self.get_displayed_network()
        displayed_id = self.get_displayed_id()
        displayed_pw = self.get_displayed_pw()
        displayed_reason = self.get_displayed_reason()
        displayed_year = int(displayed_date[0])
        displayed_month = int(displayed_date[1])
        displayed_day = int(displayed_date[2])
        displayed_time_start = self.get_displayed_time_start()
        displayed_time_end = self.get_displayed_time_end()
        displayed_category = self.get_displayed_category()
        displayed_name = self.get_displayed_name()
        displayed_position = self.get_displayed_position()
        displayed_team = self.get_displayed_team()

        return {
            "network": displayed_network,
            "id": displayed_id,
            "pw": displayed_pw,
            "year": displayed_year,
            "month": displayed_month,
            "day": displayed_day,
            "time_start": displayed_time_start,
            "time_end": displayed_time_end,
            "reason": displayed_reason,
            "category": displayed_category,
            "name": displayed_name,
            "position": displayed_position,
            "team": displayed_team,
        }

    def setup_font(self):
        # # 폰트 경로 설정 디버깅 시
        # font_path_bold = os.path.join(os.getcwd(), "ui", "font", "HDHyundai-Bold.ttf")
        # font_path_light = os.path.join(os.getcwd(), "ui", "font", "HDHyundai-light.ttf")
        # font_path_medium = os.path.join(
        #     os.getcwd(), "ui", "font", "HDHyundai-Medium.ttf"
        # )

        # # 폰트 경로 확인 및 로드
        # self.load_font(font_path_bold)
        # self.load_font(font_path_light)
        # self.load_font(font_path_medium)

        # 빌드 시 적용되는 경로
        font_path_bold = os.path.join("ui", "font", "HDHyundai-Bold.ttf")
        font_path_light = os.path.join("ui", "font", "HDHyundai-light.ttf")
        font_path_medium = os.path.join("ui", "font", "HDHyundai-Medium.ttf")

        # 폰트 경로 확인 및 로드
        self.load_font(self._data_manager.resource_path(font_path_bold))
        self.load_font(self._data_manager.resource_path(font_path_light))
        self.load_font(self._data_manager.resource_path(font_path_medium))

        # 기본 폰트 설정
        self.set_font("HDHyundai Medium")

    def load_font(self, font_path):
        if os.path.isfile(font_path):
            QFontDatabase().addApplicationFont(font_path)
            print(f"폰트 로드됨: {font_path}")
        else:
            print(f"경고: 폰트 파일을 찾을 수 없음 - {font_path}")

    def set_font(self, font_name):
        # 폰트를 설정하여 UI 전체에 적용
        font = QFont(font_name)
        font.setPointSize(9)  # 폰트 크기를 적절히 설정
        QtWidgets.QApplication.setFont(font)

        # 현재 날짜 텍스트 스타일 설정
        self.label_date.setStyleSheet("""
        QLabel {
            font-size: 10pt; /* 폰트 크기를 10포인트로 설정 */
            /*color: black; 진한 남색 (#2c3e50)으로 설정 */
        }
        """)

    def save_to_default(self, reg_data):
        # 현재 작업 경로 기준으로 default.json 파일 경로 설정
        json_path = self._data_manager.resource_path(os.getcwd(), "default.json")

        # 파일이 존재하면 JSON 파일 로드, 아니면 빈 딕셔너리로 초기화
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {"CATEGORY": [], "DEFAULT": {}}

        # DEFAULT 항목만 갱신
        data["DEFAULT"] = {
            "network": reg_data["network"],
            "id": reg_data["id"],
            "pw": reg_data["pw"],
            "year": reg_data["year"],
            "month": reg_data["month"],
            "day": reg_data["day"],
            "category": reg_data["category"],
            "reason": reg_data["reason"],
            "name": reg_data["name"],
            "position": reg_data["position"],
            "team": reg_data["team"],
        }

        # 업데이트된 데이터를 다시 default.json 파일에 저장
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("DEFAULT 설정이 업데이트되었습니다.")

    def on_register_click(self) -> dict:
        displayed_data = self.get_displayed_data()
        self._data_manager.set_total_data(
            data=None, key="DEFAULT", values=displayed_data
        )
        self._data_manager.save_default_json()
        return

    def on_send_mail_click(self):
        displayed_data = self.get_displayed_data()
        self._data_manager.set_total_data(
            data=None, key="DEFAULT", values=displayed_data
        )
        self._data_manager.save_default_json()

        # gui 캡처
        pixmap = self.grab()

        # 캡처한 이미지를 파일로 저장
        pixmap.save(self._data_manager.get_img_path(), "png")
