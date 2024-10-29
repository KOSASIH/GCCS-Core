# Step-by-Step Setup Instructions

## Introduction
This tutorial guides you through the process of setting up the Global Climate Control System (GCCS-Core) on your local machine.

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git

## Step 1: Clone the Repository
```bash
1 git clone https://github.com/KOSASIH/GCCS-Core.git
2 cd GCCS-Core
```

## Step 2: Install Dependencies
```bash
1 pip install -r requirements.txt
```

## Step 3: Configure the System

Create a new file named config.json in the root directory.
Add the following configuration settings:

```json
1 {
2   "database": {
3     "host": "localhost",
4     "port": 5432,
5     "username": "your_username",
6     "password": "your_password"
7   }
7 }
```

## Step 4: Start the System

```bash
1 python src/main/climate_monitor.py
```

# Conclusion
You have successfully set up the GCCS-Core system on your local machine. You can now access the dashboard at http://localhost:5000.
