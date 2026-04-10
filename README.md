# Brute Force Detection System

# Description
This project detects brute force login attacks by analyzing login logs using Python.

# Features
- Identifies failed login attempts
- Counts attempts per IP address
- Detects suspicious IPs based on threshold
- Generates alert reports
- Visualizes attack patterns using graphs

# Technologies Used
- Python
- Pandas
- Matplotlib

# How It Works
The system analyzes login logs and flags IP addresses with more than 5 failed login attempts as suspicious.

# How to Run
1. Install required libraries:
   pip install pandas matplotlib

2. Run the script:
   python main.py

# Project Structure
- main.py → main detection script  
- logs.csv → sample log data  
