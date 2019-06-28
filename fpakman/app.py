import argparse
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from fpakman import __version__
from fpakman.core import resource
from fpakman.core import util
from fpakman.core.controller import FlatpakManager
from fpakman.view.qt.systray import TrayIcon

parser = argparse.ArgumentParser(prog='fpakman', description="GUI for Flatpak applications management")
parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(__version__))
args = parser.parse_args()

locale_keys = util.get_locale_keys(os.getenv('FPAKMAN_LOCALE', None))

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(resource.get_path('img/flathub_45.svg')))

manager = FlatpakManager(cache_expire=int(os.getenv('FPAKMAN_CACHE_EXPIRATION', 60 * 60)))

trayIcon = TrayIcon(locale_keys=locale_keys,
                    manager=manager,
                    check_interval=int(os.getenv('FPAKMAN_CHECK_INTERVAL', 60)))
trayIcon.load_database()
trayIcon.show()

sys.exit(app.exec_())
