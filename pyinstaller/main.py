from PyQt5 import QtWidgets
from ui.module import MainWindow
from bot import Bot
from data import DataManager

import sys


if __name__ == "__main__":
    # 싱글톤 인스턴스 가져온다음에, data_manager 로 메서드 사용.
    data_manager = DataManager.instance()
    data_manager.load_default_json()

    # QT 모듈 실행
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    bot = Bot()

    # 신호 연결
    window.on_register_clicked.connect(bot.register)
    if data_manager._platform == "Windows":
        window.on_send_mail_clicked.connect(bot.send_mail)
    window.show()

    sys.exit(app.exec_())

# build 시
# pyinstaller --onefile --add-data "ui;ui" ---add-data "C:\Users\A525764.HHIROB\.cache\selenium\chromedriver\win64\130.0.6723.116\chromedriver.exe;." --log-level DEBUG --name "HRBot" --icon ui/img/icon.ico main.py
