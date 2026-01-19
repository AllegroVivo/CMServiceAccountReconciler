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

    # while True:
    #     print(
    #         "Service Membership Reconciler v1.0\n"
    #         "By Frogge Tech Solutions\n"
    #         "=============================\n"
    #         "1. Parse Master Google Spreadsheet Data\n"
    #         "2. Load QuickBooks Export CSV\n"
    #         "3. Configure Interpretation Thresholds\n"
    #         "4. Perform Reconciliation\n"
    #         "5. Write Results\n"
    #         "0. Exit\n"
    #         "=============================\n"
    #     )
    #     choice = input("Enter choice (1-4, 0 to exit): ")
    #
    #     if choice == "1":
    #         # sheet_id = input("Enter sheet ID: ")
    #         sheet_id = "1OX8YHKCEq1R1pJd0lhOdK_gMAKpv1ZANllTaF7bWwJY"
    #         reconciler.load_data(sheet_id)
    #         # reconciler.parse_spreadsheet()
    #     elif choice == "2":
    #         # csv_addr = input("Enter path to reconciliation export CSV: ")
    #         csv_addr = "C:/Dev/Frogge Tech Solutions/CM Heating/ServiceMembershipsReconciliation/Reconcilerv2/QB Export CSV Deferred Revenue.CSV"
    #         # csv_addr = r"/Users/steph/PycharmProjects/ReconcilerV2/QB Export CSV Deferred Revenue.CSV"
    #         csv_addr = Path(csv_addr)
    #         if not csv_addr.exists():
    #             raise FileNotFoundError("File does not exist.")
    #         reconciler.load_qb_export(csv_addr)
    #     elif choice == "3":
    #         reconciler.thresholds_menu()
    #     elif choice == "4":
    #         reconciler.reconcile_all()
    #     elif choice == "5":
    #         reconciler.write_to_destination()
    #     elif choice == "0":
    #         break

    return app.exec()

################################################################################
if __name__ == '__main__':
    raise SystemExit(main())
