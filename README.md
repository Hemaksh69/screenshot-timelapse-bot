<div align="center">

# ❄️ Screenshot Timelapse Bot

### 📸 Automated Screen Capture & Timelapse Video Generator

![Python](https://img.shields.io/badge/Python-3.7+-E92063?style=flat-square&logo=python&logoColor=white)
![pyautogui](https://img.shields.io/badge/PyAutoGUI-Latest-E92063?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-E92063?style=flat-square&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-E92063?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-E92063?style=flat-square)

*A lightweight Python bot that captures periodic screenshots and stitches them into smooth timelapse videos*

[🚀 Quick Start](#-installation--setup) • [✨ Features](#-features) • [📖 Usage](#-usage) • [🔧 Configuration](#-configuration)

</div>

---

## 📋 Table of Contents

<details>
<summary>🔍 Click to expand</summary>

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Configuration](#-configuration)
- [File Structure](#-file-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

</details>

---

## 🌈 Overview

**Screenshot Timelapse Bot** is a Python automation tool that effortlessly captures your screen at regular intervals and compiles the screenshots into a professional timelapse video. Perfect for tracking productivity, creating tutorials, documenting design workflows, or monitoring system activities!

---

## 🎯 Features

<details open>
<summary>✨ Core Capabilities</summary>

<br>

| Feature | Description |
|---------|-------------|
| ⏱️ **Auto-Capture** | Takes screenshots every 5 seconds automatically |
| 🏷️ **Smart Naming** | Timestamps each screenshot (YYYY-MM-DD_HH-MM-SS) |
| 🎬 **Video Generation** | Creates timelapse video using OpenCV |
| 📁 **Auto-Organization** | Creates and manages screenshot directories |
| 💾 **High Quality** | PNG format screenshots with full resolution |
| 🔄 **Error Handling** | Robust error checking and logging |
| 🎥 **XVID Codec** | Compressed, compatible video output |
| 🖥️ **Cross-Platform** | Works on Windows, macOS, and Linux |

</details>

---

## 🛠 Tech Stack

<details>
<summary>🔧 Technologies Used</summary>

<br>
┌─────────────────────────────────────────┐
│ │
│ 🐍 Python 3.7+ Core Language │
│ 📸 pyautogui Screenshot Capture │
│ 🎥 OpenCV (cv2) Video Processing │
│ 📁 os File Management │
│ ⏰ time Scheduling & Timing │
│ 🖼️ Pillow Image Processing │
│ │
└─────────────────────────────────────────┘

text


</details>

---

## 🚀 Installation & Setup

<details>
<summary>📦 Step-by-Step Guide</summary>

<br>

### **Prerequisites**

![Python](https://img.shields.io/badge/Python-3.7%2B%20Required-E92063?style=flat-square&logo=python&logoColor=white)

- Install [Python 3.7+](https://www.python.org/downloads/)
- Ensure `pip` is installed and updated

### **1️⃣ Clone Repository**

```bash
git clone https://github.com/Hemaksh69/screenshot-timelapse-bot.git
cd screenshot-timelapse-bot
2️⃣ Install Dependencies
Bash

pip install pyautogui opencv-python pillow
Or use requirements.txt:

Bash

pip install -r requirements.txt
3️⃣ Run the Bot
Bash

python timelapse.py
4️⃣ Check Output
Screenshots and video will be saved to:

text

📁 ~/Pictures/Screenshots/
   ├── screenshot_2024-01-15_14-30-00.png
   ├── screenshot_2024-01-15_14-30-05.png
   ├── ...
   └── timelapse.avi
</details>
🎮 Usage
<details> <summary>🏃 Quick Start Guide</summary><br>
Basic Execution
Bash

python timelapse.py
What Happens:
🎬 Initialization - Creates ~/Pictures/Screenshots/ directory
📸 Capture Phase - Takes 6 screenshots over 30 seconds (every 5s)
🎥 Compilation - Processes all PNG files into video
💾 Output - Saves timelapse.avi at 2 FPS
✅ Completion - Displays success message
Expected Output:
text

Creating directory: /home/user/Pictures/Screenshots
Screenshot saved: /home/user/Pictures/Screenshots/screenshot_2024-01-15_14-30-00.png
Screenshot saved: /home/user/Pictures/Screenshots/screenshot_2024-01-15_14-30-05.png
...
Screenshot capturing completed!
Creating Timelapse...
Timelapse video saved as /home/user/Pictures/Screenshots/timelapse.avi
</details>
🔧 Configuration
<details> <summary>⚙️ Customization Options</summary><br>
🕒 Change Capture Duration
Python

# Default: 30 seconds
timer = time.time() + 30  # ← Change this value
Example: 2 minutes of capture

Python

timer = time.time() + 120
⏱️ Change Capture Interval
Python

# Default: 5 seconds between screenshots
time.sleep(5)  # ← Change this value
Example: Screenshot every 2 seconds

Python

time.sleep(2)
🎬 Change Video Frame Rate
Python

# Default: 2 FPS
cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"XVID"), 2, (width, height))
#                                                        ↑
#                                                    Change FPS
Example: Smoother 10 FPS video

Python

cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"XVID"), 10, (width, height))
📁 Change Save Location
Python

# Default: ~/Pictures/Screenshots
savepaths = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
Example: Custom directory

Python

savepaths = os.path.join(os.path.expanduser("~"), "Desktop", "MyTimelapse")
🎨 Configuration Examples
Use Case	Duration	Interval	FPS
🎨 Design Work	3600s (1hr)	30s	5
📚 Study Session	7200s (2hr)	60s	10
🎮 Gaming	1800s (30m)	10s	15
💼 Work Day	28800s (8hr)	300s (5m)	5
</details>
📂 File Structure
<details> <summary>🗂️ Project Organization</summary><br>
text

screenshot-timelapse-bot/
│
├── 📄 timelapse.py           # Main script
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Documentation
├── 📄 LICENSE               # MIT License
├── 📄 .gitignore            # Git ignore rules
│
└── 📁 ~/Pictures/Screenshots/  (Output directory)
    ├── 🖼️ screenshot_2024-01-15_14-30-00.png
    ├── 🖼️ screenshot_2024-01-15_14-30-05.png
    ├── 🖼️ screenshot_2024-01-15_14-30-10.png
    └── 🎥 timelapse.avi
</details>
🔍 How It Works
<details> <summary>⚙️ Technical Breakdown</summary><br>
Phase 1: Setup
Python

# Creates screenshot directory if it doesn't exist
savepaths = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
os.makedirs(savepaths, exist_ok=True)
Phase 2: Screenshot Capture
Python

# Captures screen with timestamp
def tshot():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    shot = pyautogui.screenshot()
    shot.save(filepath)
Phase 3: Capture Loop
Python

# Runs for 30 seconds, capturing every 5 seconds
timer = time.time() + 30
while time.time() < timer:
    tshot()
    time.sleep(5)
Phase 4: Video Compilation
Python

# Reads all PNG files and creates video
video_writer = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"XVID"), 2, (width, height))
for image in images:
    frame = cv2.imread(img_path)
    video_writer.write(frame)
</details>
🐛 Troubleshooting
<details> <summary>❓ Common Issues & Solutions</summary><br>
❌ "Failed to capture screenshot!"
Cause: Screen access permissions
Solution:

Bash

# macOS: Grant Terminal/Python screen recording permission in:
# System Preferences → Security & Privacy → Screen Recording

# Linux: Install scrot if using Wayland
sudo apt-get install scrot
❌ "NO SCREENSHOTS FOUND!"
Cause: No PNG files in directory
Solution: Check write permissions and disk space

Bash

ls -la ~/Pictures/Screenshots/
❌ "Error reading image"
Cause: Corrupted or incomplete file
Solution: Delete corrupted files and re-run

Bash

cd ~/Pictures/Screenshots/
rm screenshot_*.png
❌ Video won't play
Cause: Missing XVID codec
Solution:

Install VLC Media Player
Or install codec: sudo apt-get install libxvidcore-dev
❌ ModuleNotFoundError
Cause: Missing dependencies
Solution:

Bash

pip install --upgrade pyautogui opencv-python pillow
</details>
🤝 Contributing
<details> <summary>💡 How to Contribute</summary><br>
Contributions are welcome! 🎉

Steps:
🍴 Fork the repository
🌿 Create feature branch
Bash

git checkout -b feature/AmazingFeature
💾 Commit your changes
Bash

git commit -m 'Add some AmazingFeature'
📤 Push to the branch
Bash

git push origin feature/AmazingFeature
🔃 Open a Pull Request
Ideas for Contributions:
🎨 Add GUI interface
⚙️ Config file support
🔔 Desktop notifications
📊 Progress bar
🎞️ Multiple video formats
🌐 Web dashboard
</details>
👤 Author
<div align="center">
Hemaksh69 ❄️
GitHub
Profile

Made with 💖 and Python

</div>
📄 License
<details> <summary>⚖️ MIT License</summary><br>
text

MIT License

Copyright (c) 2024 Hemaksh69

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</details>
<div align="center">
⭐ Star this repo if you found it helpful!
Stars
Forks
Issues

Happy Coding! 🚀❄️

</div> ```
