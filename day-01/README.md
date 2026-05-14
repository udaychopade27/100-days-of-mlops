# 📅 Day 01 – Python Virtual Environment Setup

## 🗓️ Date: 13-05-2026

## 🎯 Today's Goal

Set up a clean Python virtual environment for ML development — the foundation of any reproducible MLOps workflow.

---

## 📚 Concepts Learned

### What is a Virtual Environment?
A **virtual environment** is an isolated Python environment that keeps project dependencies separate from the system Python. This is critical in MLOps to:

- Avoid **dependency conflicts** between projects
- Ensure **reproducibility** across machines and team members
- Keep the global Python installation clean
- Make it easy to export and share exact package versions

### Why `requirements.txt`?
A `requirements.txt` file captures the exact versions of all installed packages. This allows anyone (or any CI/CD pipeline) to recreate the same environment with a single command.

---

## 💻 Commands Used

### 1. Create a Virtual Environment

```bash
python -m venv ml-env
```

> Creates a new virtual environment named `ml-env` in the current directory.

---

### 2. Activate the Virtual Environment

```bash
source ml-env/bin/activate
```

> Activates the environment. Your terminal prompt will change to show `(ml-env)`, confirming it's active.

---

### 3. Install Packages Inside the Virtual Environment

```bash
pip install <package-name>
```

> Installs any Python package into the isolated environment only (not system-wide).

---

### 4. List All Installed Packages

```bash
pip freeze
```

> Displays all installed packages and their exact versions in the active environment.

---

### 5. Save All Packages to a File

```bash
pip freeze > requirements.txt
```

> Exports the full list of installed packages into `requirements.txt` for reproducibility.

---

## 🔁 Workflow Summary

```
python -m venv ml-env          # Create environment
    ↓
source ml-env/bin/activate     # Activate environment
    ↓
pip install <packages>         # Install dependencies
    ↓
pip freeze > requirements.txt  # Save dependencies
```

---

## ✅ Key Takeaways

- Always use a virtual environment for ML projects — never install directly to system Python
- `pip freeze` captures the **exact state** of your environment
- `requirements.txt` is the standard way to share and reproduce environments
- Anyone can recreate your environment using `pip install -r requirements.txt`

---

## 📁 Files in This Directory

| File | Description |
|------|-------------|
| `README.md` | Day 01 notes and documentation |
| `commands.txt` | Raw commands used today |
| `screenshots/` | VS Code screenshots of the setup |

---

## 🔗 Resources

- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [pip freeze documentation](https://pip.pypa.io/en/stable/cli/pip_freeze/)

---

> ✅ **Day 01 Complete!** — Environment setup done. Ready to install ML tools tomorrow. 🚀
>
> 🔥 #100DaysOfMLOps