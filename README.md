# PyClass-FashionProjects
This isn't spaghetti code, just some thoughts in progress that need a bit of structure.

Please consider that in this repo, all the projects will be different and for each case you will need to download and install the needed packages. 

## 🛠️ Dependency Management
To ensure consistency and avoid the "it works on my machine" problem, we use a `requirements.txt` file to manage these dependencies.

### Why use `requirements.txt`?
* **Consistency:** It locks down the exact versions of the libraries used during development, preventing breaking changes when newer versions are released.
* **Portability:** Anyone cloning this repository can set up the identical environment in seconds.
* **Cleanliness:** It keeps the repository lightweight; we only track the *names* of the dependencies, not the source code of the libraries themselves

# To install all pakages from requirements.txt run    
    pip install -r requirements.txt 

# If you install more packages in the project, you can update the list using
    pip freeze > requirements.txt
    

## 🔒 Virtual Environment Setup

Before installing any dependencies, it is highly recommended to set up a **Virtual Environment (`venv`)**. 

### Why is this necessary?
* **Isolation:** Python installs packages globally by default. A virtual environment creates an isolated sandbox for this project, preventing library version conflicts with other projects on your computer.
* **Clean Deployments:** It ensures that when we generate the `requirements.txt` file using `pip freeze`, it only includes the packages explicitly needed for this script, rather than every Python library installed on your machine.


* **1. Create and Activate a Virtual Environment (Recommended)**
An isolated virtual environment prevents conflicts with other Python projects on your system.

# Create the virtual environment
  python -m venv venv

# Activate it:
# On Windows (Command Prompt)**:
  .\venv\Scripts\activate
  
# On Windows (PowerShell)**:
  .\venv\Scripts\Activate.ps1
  
# On macOS/Linux:**
  source venv/bin/activate
