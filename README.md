# Alphabetical Authentication

## Requirements
This project uses the following standard library modules:
- random
- string
- threading
- os
- signal

Ensure Python 3.x (>=3.8) is installed, as these versions of the standard library modules are included.

To convert the source code to a .exe or equivalent executable file run the following:
```powershell
pip install pyinstaller
```

If this **doesn't** work:

```powershell
python -m pip install pyinstaller
```

To package the source code to a `.exe file` use the following command:

```powershell
pyinstaller --onefile --console alpha_auth.py