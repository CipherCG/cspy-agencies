## Building a Standalone Desktop Application (No Browser Required)

This project uses [PyWebview](https://pywebview.flowrl.com/) to create a native desktop app, bundling all HTML/CSS/JS and the SQLite database for offline use.

### 1. Install requirements

```bash
pip install pywebview
```

### 2. (Optional) Initialize your SQLite database

If your app expects an existing database, run a setup script or let the app create it automatically on first start.

### 3. Build with auto-py-to-exe

Install and run auto-py-to-exe:

```bash
pip install auto-py-to-exe
auto-py-to-exe
```

- **Script Location:** `app.py`
- **Onefile:** checked
- **Add Folders:** add the `templates` folder (Destination: `templates`)
- **Add File:** add `schema.sql` (Destination: `.`) if needed
- **Console Window:** Window Based

Click "Convert .py to .exe". Your EXE will appear in the output directory.

### 4. Run Your App

Double-click the EXE—your app will open in its own window, with no browser or server required.

---

**All HTML/CSS/JS and the database are bundled inside the app for true offline, self-contained use.**

---

## Need sample code or help converting your Flask routes to PyWebview app logic?  
Let me know which features you need help porting!
