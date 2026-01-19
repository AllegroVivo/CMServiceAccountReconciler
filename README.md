# CM Heating Service Account Reconciler

## Other Sections here

## Exporting the Executable
To export the application as a standalone executable, use the following `pyinstaller` command in this application's virtual environment terminal:

```bash
pyinstaller --clean -y --onefile --noconsole --icon=Assets/App.ico main.py
```

If the packaging fails, ensure that all dependencies are installed in the virtual environment and that the `pyinstaller` command is executed from within that environment.