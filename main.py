from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from Database import init_db
from UI.MainWindow import MainWindow
from UI.Controller import ReconciliationController
################################################################################
def main() -> int:

    init_db()

    app = QApplication(sys.argv)
    app.setApplicationName("Service Account Reconciler")
    app.setOrganizationName("Frogge Tech Solutions")
    app.setStyle("Fusion")

    icon_path = Path(__file__).with_name("Assets").joinpath("App.ico")
    app.setWindowIcon(QIcon(str(icon_path)))

    win = MainWindow()
    # Reference the controller here to keep it from being garbage collected
    c = ReconciliationController(win)
    win.show()

    return app.exec()

################################################################################
if __name__ == '__main__':
    raise SystemExit(main())
