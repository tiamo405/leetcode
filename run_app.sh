#!/bin/bash

# LeetCode Solutions Flask App Runner
echo "🚀 Starting LeetCode Solutions Flask App..."

# Activate virtual environment and run the app
cd /home/namtp/Desktop/code/leetcode
source .venv/bin/activate
export FLASK_ENV=development
python app.py
