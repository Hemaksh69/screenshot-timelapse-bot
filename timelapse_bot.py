import pyautogui
import time
import os
import cv2

savepaths = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")

if not os.path.exists(savepaths):
    print(f"Creating directory: {savepaths}")
    os.makedirs(savepaths, exist_ok=True)

video = os.path.join(savepaths, "timelapse.avi")

def tshot():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(savepaths, f"screenshot_{timestamp}.png")

    try:
        shot = pyautogui.screenshot()
        if shot is None:
            print("Failed to capture screenshot!")
        else:
            shot.save(filepath)
            print(f"Screenshot saved: {filepath}")
    except Exception as e:
        print(f"Error saving screenshot: {e}")

timer = time.time() + 30

while time.time() < timer:
    tshot()
    time.sleep(5)

print("Screenshot capturing completed!")
print("Creating Timelapse...")

images = [img for img in os.listdir(savepaths) if img.endswith(".png")]
images.sort()

if not images:
    print("NO SCREENSHOTS FOUND!")
    exit()

first_image_path = os.path.join(savepaths, images[0])
frame = cv2.imread(first_image_path)

if frame is None:
    print("Error reading the first image!")
    exit()

height, width, layers = frame.shape

video_writer = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*"XVID"), 2, (width, height))

for image in images:
    img_path = os.path.join(savepaths, image)
    frame = cv2.imread(img_path)
    
    if frame is None:
        print(f"Error reading image: {img_path}")
        continue

    video_writer.write(frame)

video_writer.release()
cv2.destroyAllWindows()

print(f"Timelapse video saved as {video}")
