# CSPY Agencies Project

## Description
This is a role-based application for CSPY Agencies. It includes the following features:
- **Login System**: Role-based access for `Rank-User` and `Rank-Admin`.
- **Nuke Launch**: Submit, delete, and launch codes.
- **Directory**: View and edit user information based on role.
- **Terminal**: Execute commands like `ipconfig` and `$$Crash_System$$`.
- **User Creation Tool**: Admin-only feature to create new users.
- **Game Break**: A cookie clicker game for fun.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/cspy-agencies.git
   cd cspy-agencies
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Initialize the database:
   ```bash
   python app.py
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
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

## Features
### 1. Logon System
- Role-based login for `Rank-User` and `Rank-Admin`.

### 2. Nuke Launch
- Submit, delete, and launch nuke codes.

### 3. Directory
- View user directory.
- Edit user information based on role.

### 4. Terminal
- Execute `ipconfig` (fake IP address) and `$$Crash_System$$`.

### 5. User Creation Tool
- Admin-only feature to add new users.

### 6. Game Break
- A cookie clicker game for entertainment.

## License
This project is licensed under the MIT License.
