from PyQt5 import QtCore, QtWidgets
from .qt5 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    on_register_clicked = QtCore.pyqtSignal()
    on_send_mail_clicked = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showEvent(self, event):
        super().showEvent(event)
        # 프로그램이 보일 때 기본 날짜를 클릭한 것처럼 설정
        self.calendarWidget.setSelectedDate(self.today)
        self.update_date_label(self.today)
        self.check_time_for_regist()

    def setup_default_id(self, id: str = "A525764"):
        """디폴트 사번 입력하기
        Args:
            id (str) - 사번

        Returns:
            None
        """
        super().setup_default_id()

    def setup_default_pw(self):
        """디폴트 비번 입력하기
        Args:
            pw (str) - 사번

        Returns:
            None
        """

        super().setup_default_pw()

    def setup_default_categories(self):
        """디폴트 항목리스트 입력하기
        default.json 의 CATEGORY 리스트를 읽어 화면 콤보 박스에 주입

        Returns:
            None
        """
        super().setup_default_categories()

    def setup_default_category(self):
        """디폴트 항목 입력하기

        Returns:
            None
        """
        super().setup_default_category()

    def setup_default_reason(self):
        """디폴트 사유 입력하기

        Returns:
            None
        """
        super().setup_default_reason()

    def setup_default_time(self):
        """디폴트 시간 입력하기

        Returns:
            None
        """
        super().setup_default_time()

    def on_register_click(self) -> dict:
        """비근 등록 버튼 눌렀을 때 동작"""
        super().on_register_click()
        self.on_register_clicked.emit()

    def on_send_mail_click(self):
        """비근 등록 정책에 따라 비근등록 매크로 불가시 메일 자동 생성
        Returns:
            png - 캡쳐 파일
        """
        super().on_send_mail_click()
        self.on_send_mail_clicked.emit()
