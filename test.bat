@echo off

cd /d %~dp0
python tts.py

PowerShell -command [Console]::Beep(349, 800)
PowerShell -command (New-Object Media.SoundPlayer 'C:\Users\leafe\workspace\calmtech_python\output.wav').PlaySync();

