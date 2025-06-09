from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from werkzeug.security import check_password_hash, generate_password_hash
import os
import json

app = Flask(__name__)
app.secret_key = "very_secret_key"

BASE_FOLDER = "shared_files"
USER_FILE = "users.json"
LOG_FILE = "activity.log"

os.makedirs(BASE_FOLDER, exist_ok=True)

# Log function
def log_activity(user, action):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{user}] {action}\n")

# Load users
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Get per-user folder
def user_folder():
    return os.path.join(BASE_FOLDER, session["username"])

# Login Route
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        users = load_users()
        if username in users and check_password_hash(users[username], password):
            session["username"] = username
            os.makedirs(user_folder(), exist_ok=True)
            log_activity(username, "logged in")
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# Registration Route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        users = load_users()

        if username in users:
            return render_template("register.html", error="Username already exists!")

        hashed_password = generate_password_hash(password)
        users[username] = hashed_password

        with open(USER_FILE, "w") as f:
            json.dump(users, f)

        os.makedirs(os.path.join(BASE_FOLDER, username), exist_ok=True)
        log_activity(username, "registered account")

        return redirect(url_for("login"))
    
    return render_template("register.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["username"])

# View Files
@app.route("/view_shares")
def view_shares():
    if "username" not in session:
        return redirect(url_for("login"))
    files = os.listdir(user_folder())
    return render_template("view_shares.html", shared_files=files)

# Upload Files
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if "username" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file:
            file_path = os.path.join(user_folder(), file.filename)
            file.save(file_path)
            log_activity(session["username"], f"uploaded file: {file.filename}")
            return redirect(url_for("view_shares"))
    return render_template("upload.html")

# Download Files
@app.route("/download/<filename>")
def download_file(filename):
    if "username" not in session:
        return redirect(url_for("login"))
    log_activity(session["username"], f"downloaded file: {filename}")
    return send_from_directory(user_folder(), filename, as_attachment=True)

# Delete Files
@app.route("/delete/<filename>")
def delete_file(filename):
    if "username" not in session:
        return redirect(url_for("login"))
    try:
        os.remove(os.path.join(user_folder(), filename))
        log_activity(session["username"], f"deleted file: {filename}")
    except FileNotFoundError:
        pass
    return redirect(url_for("view_shares"))

# Change Password
@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        old_password = request.form["old_password"]
        new_password = request.form["new_password"]

        users = load_users()
        username = session["username"]

        if check_password_hash(users[username], old_password):
            users[username] = generate_password_hash(new_password)
            with open(USER_FILE, "w") as f:
                json.dump(users, f)
            log_activity(username, "changed password")
            return render_template("change_password.html", message="Password changed successfully!")
        else:
            return render_template("change_password.html", error="Old password incorrect!")

    return render_template("change_password.html")

# Admin Panel
@app.route("/admin")
def admin_panel():
    if "username" not in session:
        return redirect(url_for("login"))
    if session["username"] != "admin":
        return redirect(url_for("dashboard"))

    users = load_users()
    user_stats = {}

    for user in users:
        folder = os.path.join(BASE_FOLDER, user)
        file_count = len(os.listdir(folder)) if os.path.exists(folder) else 0
        user_stats[user] = file_count

    return render_template("admin.html", user_stats=user_stats)

# Logout
@app.route("/logout")
def logout():
    log_activity(session["username"], "logged out")
    session.pop("username", None)
    return redirect(url_for("login"))

# Start Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

