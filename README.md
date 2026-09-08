# CLI Task Tracker

A lightweight, zero-dependency Python command-line tool designed to manage daily tasks directly from your terminal with maximum speed and custom validation.

## Project Links

* **Repository URL:** [THE REPOSITORY](https://github.com/benm07amed48-netizen/CV-page.git)
* **Challenge Page:** [roadmap.sh - Task Tracker Project](https://roadmap.sh/projects/task-tracker)

## Tech Stack

* **Python 3.13.14** (Standard Library only: `json`, `sys`, `datetime`)
* **Git & GitHub** (Version Control & Repository)

## Features

* **Zero External Dependencies:** Built purely with Python's built-in modules.
* **Direct Terminal Execution:** Pass commands and parameters instantly as CLI arguments.
* **Data Persistence:** JSON-based storage using robust standard formatting.
* **Comprehensive Task Schema:** Stores `id`, `description`, `status`, `createdAt`, `updatedAt`, `dueDate`, `priority`, and `estimatedTime`.

---

## Setup & Alias Configuration (`_`)

Clone the repository to your local machine using the following steps:

```bash
git clone https://github.com/benm07amed48-netizen/CV-page.git
cd YOUR_REPO_NAME
```

To run commands effortlessly using _ instead of typing python structure.py every time, add a global shortcut to your terminal:

### Linux / macOS (Bash & Zsh):
```bash
alias _="python3 structure.py"
source ~/.bashrc
```

### Windows (Git Bash / Cmder):
```bash
alias _=python "structure.py" $*
```

### Windows (PowerShell):
```powershell
function _ { python "structure.py" $args }
```

## How to Run Commands Directly:
#### exmples: [the example only work when the alias is applied]
* Adding task: ```_ a "Complete backend API design"```
* Listing tasks: ```_ l all```
* Editing tasks: ```_ e stat 1    # Update task status (todo / in-progress / done)```
* Inspecting tasks: ```_ i 1         # Inspect details for task ID 1```
* deleting a task: ```_ d 1```
