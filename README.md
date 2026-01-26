# CM Heating Service Account Reconciler

This project is a tool that performs the following tasks related to Service Account balance reconciliation:
1. Reads in current service account record and balance data from a Google Sheets workbook.
2. Reads in recent transaction data from a QuickBooks CSV export file.
3. Adds, modifies, or removes service account entries in the Google Sheets workbook to reflect the transactions recorded in QuickBooks.
4. Identifies and flags any discrepancies between the expected and actual service account balances for further review.
5. Writes the updated service account data back to the Google Sheets workbook.

## Download

The latest release of the CM Heating Service Account Reconciler can be downloaded from the Releases section of this repository 
[by clicking here!](https://github.com/AllegroVivo/CMServiceAccountReconciler/releases)

## Usage & Operation

Detailed usage instructions and operational guidelines for the CM Heating Service Account Reconciler can be found in this repository's documentation [located here](https://allegrovivo.github.io/CMServiceAccountReconciler/). Please refer to this page for step-by-step instructions on how to set up and use the application.

## Archive Contents

The downloaded release archive contains the following files:
- `ServiceAccountReconciler.exe` - The main executable file for the application.
- `service_account.json` - A JSON file containing Google API service account credentials.
- `service-reconciler.sqlite3` - A SQLite database file used for local data storage.
- `.env` - An environment configuration file that stores application settings and credentials.

All of these files should be kept together in the same directory for the application to function correctly.

## Dependencies

The CM Heating Service Account Reconciler relies on the following libraries and frameworks:
- `PySide6` - For creating the graphical user interface (GUI).
- `google-auth` - For handling Google API authentication.
- `SQLAlchemy` - For database management and operations.
- `requests` - For handling HTTP requests.
- `python-dotenv` - For managing environment variables.
- `pyinstaller` - For packaging the application into a standalone executable.

## System Requirements

- **OS:** Windows 10 or later
- **Disk Space:** Minimum 60 MB free space for application and associated files

## Google Sheets API Setup

This application requires access to Google Sheets via the Google Sheets API. It will require read and write permissions for the master service account source workbook. These can be granted by sharing the document with the `client_email` address specified in the developer-provided `service_account.json` credentials file.

## Exporting the Executable

To export the application as a standalone executable, use the following `pyinstaller` command in this application's virtual environment terminal:

```bash
pyinstaller --clean -y --onefile --noconsole --icon=Assets/App.ico main.py
```

If the packaging fails, ensure that all dependencies are installed in the virtual environment and that the `pyinstaller` command is executed from within that environment.