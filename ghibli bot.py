import pyautogui
import time
import os
import cv2
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline
import torch

# Screenshot save path
savepath = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
os.makedirs(savepath, exist_ok=True)

def tshot():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(savepath, f"screenshot_{timestamp}.png")
    shot = pyautogui.screenshot()
    shot.save(filepath)
    print(f"Saved: {filepath}")

# Take screenshots every 5s for 30s
timer = time.time() + 30
while time.time() < timer:
    tshot()
    time.sleep(5)

print("Screenshots captured.")

# Ask for Ghibli stylization
choice = input("Do you want a Ghibli-style timelapse? (yes/no): ").strip().lower()

if choice == "yes":
    stylized_path = os.path.join(savepath, "Ghibli_Timelapse")
    os.makedirs(stylized_path, exist_ok=True)

    model_id = "nitrosocke/Ghibli-Diffusion"
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
       ).to("cuda")

    images = sorted([f for f in os.listdir(savepath) if f.endswith(".png")])
    for img_name in images:
        img_path = os.path.join(savepath, img_name)
        init_image = Image.open(img_path).convert("RGB").resize((512, 512))
        prompt = "ghibli style magical town at sunset"
        stylized = pipe(prompt=prompt, image=init_image, strength=0.6, guidance_scale=7.5).images[0]
        stylized.save(os.path.join(stylized_path, img_name))

    frames_dir = stylized_path
else:
    normal_path = os.path.join(savepath, "Normal_Timelapse")
    os.makedirs(normal_path, exist_ok=True)
    frames_dir = savepath

# Create timelapse
video_path = os.path.join(frames_dir, "timelapse.avi")
images = sorted([img for img in os.listdir(frames_dir) if img.endswith(".png")])
if not images:
    print("No images found!")
    exit()

first_frame = cv2.imread(os.path.join(frames_dir, images[0]))
height, width, _ = first_frame.shape
video_writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"XVID"), 2, (width, height))

for img in images:
    frame = cv2.imread(os.path.join(frames_dir, img))
    video_writer.write(frame)

video_writer.release()
cv2.destroyAllWindows()

print(f"Timelapse video saved at: {video_path}")
