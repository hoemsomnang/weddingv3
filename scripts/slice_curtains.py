import os
from PIL import Image

def slice_suitable_curtains(source_filename="pic2-suitable-flush.jpg"):
    assets_dir = r"D:\Learn\AI\02.Weeding\03_V3\src\assets"
    curtains_dir = os.path.join(assets_dir, "curtains")
    public_curtains_dir = r"D:\Learn\AI\02.Weeding\03_V3\public\curtains"
    os.makedirs(curtains_dir, exist_ok=True)
    os.makedirs(public_curtains_dir, exist_ok=True)

    img_path = os.path.join(assets_dir, source_filename)
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size # 768, 1376
    mid_x = w // 2 # 384
    overlap = 12 # 12px overlap for seamless center seam

    # 1. Left curtain panel (0 to mid_x + overlap)
    left_img = img.crop((0, 0, mid_x + overlap, h))
    left_img.save(os.path.join(curtains_dir, "curtain-left.webp"), "WEBP", quality=95)
    left_img.save(os.path.join(public_curtains_dir, "curtain-left.webp"), "WEBP", quality=95)
    print(f"Saved curtain-left.webp: {left_img.size}")

    # 2. Right curtain panel (mid_x - overlap to w)
    right_img = img.crop((mid_x - overlap, 0, w, h))
    right_img.save(os.path.join(curtains_dir, "curtain-right.webp"), "WEBP", quality=95)
    right_img.save(os.path.join(public_curtains_dir, "curtain-right.webp"), "WEBP", quality=95)
    print(f"Saved curtain-right.webp: {right_img.size}")

    # 3. Top Valance (y: 0 to 365 with soft bottom alpha gradient)
    valance_h = 365
    valance_img = img.crop((0, 0, w, valance_h)).copy()
    valance_alpha = valance_img.split()[-1]
    alpha_pixels = bytearray(valance_alpha.tobytes())
    fade_start = 315
    for y in range(valance_h):
        if y >= fade_start:
            factor = 1.0 - ((y - fade_start) / (valance_h - fade_start))
            for x in range(w):
                idx = y * w + x
                alpha_pixels[idx] = int(alpha_pixels[idx] * factor)
    valance_alpha_faded = Image.frombytes("L", (w, valance_h), bytes(alpha_pixels))
    valance_img.putalpha(valance_alpha_faded)
    valance_img.save(os.path.join(curtains_dir, "curtain-valance.webp"), "WEBP", quality=95)
    valance_img.save(os.path.join(public_curtains_dir, "curtain-valance.webp"), "WEBP", quality=95)
    print(f"Saved curtain-valance.webp: {valance_img.size}")

if __name__ == "__main__":
    slice_suitable_curtains("pic2-suitable-flush.jpg")
