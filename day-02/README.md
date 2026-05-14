# 📅 Day 02 – Set Up and Configure Jupyter Notebook Server

## 🗓️ Date: 14-05-2026

## 🎯 Today's Goal

Install, configure, and launch a **Jupyter Notebook Server** inside the Python virtual environment — a core tool for ML experimentation and data exploration in MLOps workflows.

---

## 📚 Concepts Learned

### What is Jupyter Notebook / JupyterLab?
**JupyterLab** is an interactive development environment for writing and running Python code in a browser-based interface. It is widely used in ML/Data Science for:

- Exploratory Data Analysis (EDA)
- Prototyping ML models
- Visualizing results inline
- Sharing reproducible experiments

### Why Run Jupyter as a Server?
In MLOps, Jupyter is often run as a **headless server** (without a browser on the server itself) so it can be:

- Accessed remotely via a browser
- Run on a cloud VM or WSL instance
- Started as a background process

### What is a Jupyter Config File?
A config file (`jupyter-config.py`) lets you pre-set options like:
- The port Jupyter listens on
- The notebook root directory
- Authentication settings
- Whether to auto-open a browser

---

## 💻 Commands Used

### 1. Activate Virtual Environment

```bash
source ml-env/bin/activate
```

> Always activate your environment first before running any Python/pip commands.

---

### 2. Install Jupyter Notebook

```bash
pip install notebook
```

> Installs JupyterLab and the classic Notebook interface inside the active virtual environment.

---

### 3. Update Jupyter Config File

```
Update jupyter-config.py with correct details such as port, file path, etc.
```

> The config file (`/root/code/jupyter-config.py`) is edited to set:
> - The port Jupyter runs on
> - The notebook directory (base directory for files)
> - `--allow-root` permission for running as root user
> - `--no-browser` to skip auto-launching a browser

---

### 4. Create Base Notebook Directory

```bash
mkdir -p /root/notebooks
```

> Creates the directory where all Jupyter notebooks will be stored.
> `-p` flag ensures no error if the directory already exists, and creates parent directories as needed.

---

### 5. Start Jupyter Lab Server in Background

```bash
jupyter lab --config=/root/code/jupyter-config.py --allow-root --no-browser &
```

> Launches JupyterLab as a **background process** (`&`) using the custom config.
>
> | Flag | Purpose |
> |------|---------|
> | `--config` | Path to your custom Jupyter config file |
> | `--allow-root` | Allows running as the root user (needed in WSL/Docker) |
> | `--no-browser` | Does not auto-open a browser on the server |
> | `&` | Runs the process in the background so the terminal stays free |

---

## 🔁 Workflow Summary

```
source ml-env/bin/activate              # Activate environment
        ↓
pip install notebook                    # Install Jupyter
        ↓
Edit jupyter-config.py                  # Set port, path, settings
        ↓
mkdir -p /root/notebooks                # Create notebooks directory
        ↓
jupyter lab --config=... --allow-root --no-browser &   # Start server
```

---

## ✅ Key Takeaways

- Always install Jupyter **inside your virtual environment**, not globally
- A config file makes the server setup **reproducible and consistent**
- `--allow-root` is required when running as root (common in WSL/Docker/Cloud VMs)
- The `&` at the end runs Jupyter as a **background process** — the terminal stays usable
- `mkdir -p` is safe to run multiple times — won't error if the folder already exists

---

## 📁 Files in This Directory

| File | Description |
|------|-------------|
| `README.md` | Day 02 notes and documentation |
| `commands.txt` | Raw commands used today |
| `screenshots/` | VS Code screenshots of the setup |

---

## 🔗 Resources

- [JupyterLab Docs](https://jupyterlab.readthedocs.io/en/stable/)
- [Jupyter Config Reference](https://jupyter-notebook.readthedocs.io/en/stable/config.html)
- [Running Jupyter as a background server](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)

---

> ✅ **Day 02 Complete!** — Jupyter Notebook Server is up and running. Ready for ML experiments! 🚀
>
> 🔥 #100DaysOfMLOps