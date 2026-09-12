@echo off
title LeetCode to GitHub Sync
color 0B
echo =================================================================
echo             LeetCode to GitHub Automatic Sync
echo =================================================================
echo.
cd /d "V:\Projects\leetcode_exp"
python leetcode_exp.py
echo.
echo =================================================================
echo Press any key to close this window...
pause >nul
