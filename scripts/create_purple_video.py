import os
import math
from PIL import Image
import subprocess

WIDTH = 702
HEIGHT = 1300
FPS = 30
TOTAL_DURATION = 20.0
TOTAL_FRAMES = int(TOTAL_DURATION * FPS)

def load_and_fit(path, target_w=WIDTH, target_h=HEIGHT):
    img = Image.open(path).convert('RGB')
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    if img_ratio > target_ratio:
        new_h = target_h
        new_w = int(target_h * img_ratio)
    else:
        new_w = target_w
        new_h = int(target_w / img_ratio)
    img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img_resized.crop((left, top, left + target_w, top + target_h))

def ease_in_out(t):
    return 0.5 * (1 - math.cos(math.pi * t))

def main():
    assets_dir = r"D:\Learn\AI\02.Weeding\03_V3\src\assets"
    output_video = os.path.join(assets_dir, "video", "preview-video-purple.mp4")
    
    # Load all 5 sequential stages
    f0 = load_and_fit(os.path.join(assets_dir, "pic2-suitable-flush.jpg"))
    f1 = load_and_fit(os.path.join(assets_dir, "curtain-open-step1-crack.jpg"))
    f2 = load_and_fit(os.path.join(assets_dir, "curtain-open-step2-parting.jpg"))
    f3 = load_and_fit(os.path.join(assets_dir, "curtain-open-step3-wide.jpg"))
    f4 = load_and_fit(os.path.join(assets_dir, "purple-ballroom-royal.jpg"))

    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "medium",
        "-crf", "18",
        output_video
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    for frame_idx in range(TOTAL_FRAMES):
        t = frame_idx / FPS # seconds

        # Timeline (matching preview-video.mp4):
        # 0.0 - 1.8s: Stage 0 (Closed curtains)
        # 1.8 - 2.5s: Stage 0 -> Stage 1 (Golden Crack)
        # 2.5 - 3.4s: Stage 1 -> Stage 2 (Parting arch)
        # 3.4 - 4.4s: Stage 2 -> Stage 3 (Wide open)
        # 4.4 - 5.2s: Stage 3 -> Stage 4 (Full ballroom reveal)
        # 5.2 - 15.0s: Stage 4 with Ken Burns subtle zoom
        # 15.0 - 15.8s: Stage 4 -> Stage 3
        # 15.8 - 16.8s: Stage 3 -> Stage 2
        # 16.8 - 17.6s: Stage 2 -> Stage 1
        # 17.6 - 18.2s: Stage 1 -> Stage 0
        # 18.2 - 20.0s: Stage 0 (Closed)

        if t < 1.8:
            cur = f0
        elif t < 2.5:
            cur = Image.blend(f0, f1, ease_in_out((t - 1.8) / 0.7))
        elif t < 3.4:
            cur = Image.blend(f1, f2, ease_in_out((t - 2.5) / 0.9))
        elif t < 4.4:
            cur = Image.blend(f2, f3, ease_in_out((t - 3.4) / 1.0))
        elif t < 5.2:
            cur = Image.blend(f3, f4, ease_in_out((t - 4.4) / 0.8))
        elif t < 15.0:
            prog = (t - 5.2) / 9.8
            zoom = 1.0 + 0.05 * math.sin(prog * math.pi)
            w_crop = int(WIDTH / zoom)
            h_crop = int(HEIGHT / zoom)
            x_crop = (WIDTH - w_crop) // 2
            y_crop = int((HEIGHT - h_crop) * 0.35)
            cropped = f4.crop((x_crop, y_crop, x_crop + w_crop, y_crop + h_crop))
            cur = cropped.resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)
        elif t < 15.8:
            cur = Image.blend(f4, f3, ease_in_out((t - 15.0) / 0.8))
        elif t < 16.8:
            cur = Image.blend(f3, f2, ease_in_out((t - 15.8) / 1.0))
        elif t < 17.6:
            cur = Image.blend(f2, f1, ease_in_out((t - 16.8) / 0.8))
        elif t < 18.2:
            cur = Image.blend(f1, f0, ease_in_out((t - 17.6) / 0.6))
        else:
            cur = f0

        proc.stdin.write(cur.tobytes())

    proc.stdin.close()
    proc.wait()
    print("Multi-stage Video generation complete:", output_video)

if __name__ == "__main__":
    main()
