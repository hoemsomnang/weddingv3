from PIL import Image, ImageFilter
import numpy as np

src_path = "C:/Users/lemon/.gemini/antigravity-ide/brain/6a06214e-b73a-42d6-9f13-b51801eb643c/gold_seal_sr_1790176285339.jpg"
im = Image.open(src_path).convert("RGBA")

# Save direct copy to public and assets
im.convert("RGB").save("public/gold-seal-sr.jpg")
im.convert("RGB").save("src/assets/envelope/gold-seal-sr.jpg")

# Now create transparent PNG
# Background is solid black (RGB < 15)
data = np.array(im)
# Calculate brightness
rgb = data[:, :, :3].astype(np.float32)
# Max channel or luminance
brightness = np.max(rgb, axis=2)

# Create smooth alpha mask:
# Fully transparent where brightness < 12
# Smooth transition between 12 and 45
alpha = np.clip((brightness - 12) / 33.0, 0.0, 1.0) * 255.0
data[:, :, 3] = alpha.astype(np.uint8)

seal_png = Image.fromarray(data)
seal_png.save("public/gold-seal-sr.png")
seal_png.save("src/assets/envelope/gold-seal-sr.png")
print("Saved gold-seal-sr.jpg and transparent gold-seal-sr.png successfully!")
