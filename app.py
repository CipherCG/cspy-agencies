from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from datetime import datetime, timedelta
import random
import time

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Replace with a strong secret key for production

# Database Initialization
DATABASE = "users.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            dob DATE NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            alt_email TEXT,
            alt_phone TEXT,
            ssn TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT CHECK(role IN ('Rank-Admin', 'Rank-User')) NOT NULL
        )
    """)

    # Create Launch Codes Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS launch_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            created_by INTEGER NOT NULL,
            FOREIGN KEY (created_by) REFERENCES users(id)
        )
    """)

    # Create Account Locks Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS account_locks (
            user_id INTEGER PRIMARY KEY,
            locked_until DATETIME,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()

# Utility Functions
def get_db_connection():
    return sqlite3.connect(DATABASE)

def create_fake_ip():
    ip_parts = [str(random.randint(10, 99)) if i == 2 else str(random.randint(1, 9)) for i in range(6)]
    fake_ip = ".".join(ip_parts)
    return fake_ip

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            session["username"] = user[10]
            session["role"] = user[12]
            return redirect(url_for("role_menu"))
        else:
            flash("Invalid username or password.", "error")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/role_menu")
def role_menu():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("role_menu.html", role=session["role"])

@app.route("/nuke_launch", methods=["GET", "POST"])
def nuke_launch():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        action = request.form["action"]

        if action == "submit":
            code = request.form["code"]
            if 4 <= len(code) <= 10:
                cursor.execute("INSERT INTO launch_codes (code, created_by) VALUES (?, ?)", (code, session["user_id"]))
                conn.commit()
                flash("Launch code submitted successfully!", "success")
            else:
                flash("Invalid code. It must be 4-10 digits.", "error")

        elif action == "delete":
            code_id = request.form["code_id"]
            cursor.execute("DELETE FROM launch_codes WHERE id = ? AND created_by = ?", (code_id, session["user_id"]))
            conn.commit()
            flash("Launch code deleted successfully!", "success")

        elif action == "launch":
            nuke_type = request.form["nuke_type"]
            location = request.form["location"]
            forcefield = request.form["forcefield"]
            if forcefield == "yes":
                flash(f"{nuke_type} launched to {location}. You are a good person!", "success")
            else:
                flash(f"{nuke_type} launched to {location}. You monster!", "error")

    cursor.execute("SELECT * FROM launch_codes WHERE created_by = ?", (session["user_id"],))
    codes = cursor.fetchall()
    conn.close()

    return render_template("nuke_launch.html", codes=codes)

@app.route("/directory")
def directory():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    return render_template("directory.html", users=users, role=session["role"], username=session["username"])

@app.route("/terminal", methods=["GET", "POST"])
def terminal():
    if "user_id" not in session:
        return redirect(url_for("login"))

    output = ""
    if request.method == "POST":
        command = request.form["command"]

        if command.lower() == "ipconfig":
            output = create_fake_ip()
        elif command == "$$Crash_System$$":
            output = "Redirecting to crash system..."
            # Implement crash system logic
        else:
            output = "Unknown command."

    return render_template("terminal.html", output=output)

@app.route("/user_creation_tool", methods=["GET", "POST"])
def user_creation_tool():
    if "user_id" not in session or session["role"] != "Rank-Admin":
        return redirect(url_for("login"))

    if request.method == "POST":
        user_data = {
            "first_name": request.form["first_name"],
            "middle_name": request.form["middle_name"],
            "last_name": request.form["last_name"],
            "dob": request.form["dob"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "alt_email": request.form["alt_email"],
            "alt_phone": request.form["alt_phone"],
            "ssn": request.form["ssn"],
            "username": request.form["username"],
            "password": request.form["password"],
            "role": "Rank-User"
        }

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (first_name, middle_name, last_name, dob, email, phone, alt_email, alt_phone, ssn, username, password, role)
            VALUES (:first_name, :middle_name, :last_name, :dob, :email, :phone, :alt_email, :alt_phone, :ssn, :username, :password, :role)
        """, user_data)
        conn.commit()
        conn.close()

        flash("User created successfully!", "success")
        return redirect(url_for("user_creation_tool"))

    return render_template("user_creation_tool.html")

@app.route("/game_break")
def game_break():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("game_break.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)