# jupyter-config.py
# Jupyter Lab / Notebook Server Configuration File

# ─────────────────────────────────────────
# 🌐 Network Settings
# ─────────────────────────────────────────

# Host IP — 0.0.0.0 means accessible from all network interfaces
c.ServerApp.ip = '0.0.0.0'

# Port the Jupyter server will listen on
c.ServerApp.port = 8888

# Do not open browser automatically on server start
c.ServerApp.open_browser = False

# ─────────────────────────────────────────
# 📁 Notebook Directory
# ─────────────────────────────────────────

# Root directory where notebooks are stored
c.ServerApp.root_dir = '/root/notebooks'

# ─────────────────────────────────────────
# 🔐 Authentication Settings
# ─────────────────────────────────────────

# Token-based authentication
# Use this token in the browser URL: http://<ip>:8888/?token=your_secret_token
c.ServerApp.token = 'your_secret_token_here'

# Password-based authentication (hashed)
# To generate a hashed password, run:
#   python -c "from jupyter_server.auth import passwd; print(passwd('yourpassword'))"
# Then paste the output below:
c.ServerApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$your_hashed_password_here'

# ─────────────────────────────────────────
# 🛡️ Security Settings
# ─────────────────────────────────────────

# Disable XSRF (Cross-Site Request Forgery) protection
# Set to True to ENABLE protection (recommended for production)
# Set to False only for local/dev/trusted environments
c.ServerApp.disable_check_xsrf = False

# Allow requests from any origin (useful for remote access / WSL)
c.ServerApp.allow_origin = '*'

# Allow remote access
c.ServerApp.allow_remote_access = True

# ─────────────────────────────────────────
# 🔒 Root Access
# ─────────────────────────────────────────

# Allow Jupyter to run as root user (required in WSL / Docker)
c.ServerApp.allow_root = True