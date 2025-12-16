import os
import subprocess
from datetime import datetime

for i in range(7):
  # 1. Get the current directory where this script is located
  repo_path = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(repo_path, "daily_log.txt")

  # 2. Update the file so Git sees a change
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  content = f"Last run: {current_time}\n"

  try:
      # Append the date to the file
      with open(file_path, "a") as file:
          file.write(content)
      
      # 3. Git Commands using subprocess
      # Change directory to the repo
      os.chdir(repo_path)
      
      # Add, Commit, Push
      subprocess.run(["git", "add", "daily_log.txt"], check=True)
      subprocess.run(["git", "commit", "-m", f"Daily update: {current_time}"], check=True)
      
      # Make sure you have set up SSH keys or cached credentials!
      subprocess.run(["git", "push"], check=True)
      
      print(f"✅ Success! Contribution made for {current_time}")

  except Exception as e:
      print(f"❌ Aare yaar, error hoyeche: {e}")