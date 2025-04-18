-- Create Users Table
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
);

-- Insert Default Admin User
INSERT INTO users (first_name, middle_name, last_name, dob, email, phone, alt_email, alt_phone, ssn, username, password, role)
VALUES (
    'Default', 
    'Admin', 
    'User', 
    '2000-01-01', 
    'admin@cspy-agencies.com', 
    '1234567890', 
    'admin-alt@cspy-agencies.com', 
    '0987654321', 
    '000-00-0000', 
    'admin', 
    '1234', 
    'Rank-Admin'
);

-- Create Launch Codes Table
CREATE TABLE IF NOT EXISTS launch_codes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER NOT NULL,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Create Account Locks Table
CREATE TABLE IF NOT EXISTS account_locks (
    user_id INTEGER PRIMARY KEY,
    locked_until DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);