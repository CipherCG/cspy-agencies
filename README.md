# CSPY Agencies Project

## Description
This is a role-based application for CSPY Agencies, designed for **offline use** as a standalone Windows executable. It includes:

- **Login System**: Role-based access for `Rank-User` and `Rank-Admin`.
- **Nuke Launch**: Submit, delete, and launch codes.
- **Directory**: View and edit user information based on role.
- **Terminal**: Execute commands like `ipconfig` and `$$Crash_System$$`.
- **User Creation Tool**: Admin-only feature to create new users.
- **Game Break**: A cookie clicker game for fun.

All HTML interface files and the initial SQL database schema are bundled within the EXE for full offline operation.

## Building a Standalone Windows Executable

### 1. Clone this repository
```bash
git clone https://github.com/CipherCG/cspy-agencies.git
cd cspy-agencies
```

### 2. Install Python dependencies
```bash
pip install flask
pip install pyinstaller
```

### 3. Initialize the database (first run only)
The app uses a local SQLite database. You can initialize the database by running:
```bash
python app.py
```
This will create the SQLite database using `schema.sql`.

### 4. Bundle as a Windows Executable
Use PyInstaller to create a single EXE that includes all necessary files:

```bash
pyinstaller --onefile --add-data "templates;templates" --add-data "schema.sql;." app.py
```
- The `--onefile` flag bundles everything into a single EXE.
- The `--add-data` flag ensures HTML templates and the SQL schema are included.

> **Note:** On Windows, use `;` to separate source and destination. On Linux/Mac, use `:`.

### 5. Running the EXE
- After building, you’ll find your standalone EXE in the `dist` folder.
- Double-click the EXE or run from the command line:
  ```bash
  dist\app.exe
  ```
- The app runs locally; open your browser to:
  ```
  http://127.0.0.1:5000
  ```

## File Structure
```
/cspy-agencies
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   ├── login.html
    │   ├── role_menu.html
    │   ├── nuke_launch.html
    │   ├── directory.html
    │   ├── terminal.html
    │   ├── user_creation_tool.html
    │   ├── game_break.html
    └── schema.sql
```

## Offline Usage
The EXE bundles all HTML and SQL files internally. No need for an internet connection. All data remains local to your computer.

## License
This project is licensed under the MIT License.
