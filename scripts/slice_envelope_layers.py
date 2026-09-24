import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import os

# Load the base scallop image
img_path = "d:/Learn/AI/02.Weeding/03_V3/public/wedding-envelope-scallop.jpg"
im = Image.open(img_path).convert("RGBA")
w, h = im.size

# Let's inspect where the flap edge is:
# In wedding-envelope-scallop.jpg:
# The flap starts from left at ~y = 480, slopes down to center tip at ~y = 675, and slopes up to right at ~y = 450.
# Let's create an alpha mask for the flap
mask_flap = Image.new("L", (w, h), 0)
draw_flap = ImageDraw.Draw(mask_flap)

# Define the scalloped contour polygon for the flap
# Top rectangle (0,0) to (w, y_hinge)
# And the scalloped/lace V-shape
pts_flap = [
    (0, 0),
    (w, 0),
    (w, 460),
    (int(w * 0.85), 515),
    (int(w * 0.70), 570),
    (int(w * 0.50), 680),  # tip
    (int(w * 0.30), 570),
    (int(w * 0.15), 515),
    (0, 480)
]
draw_flap.polygon(pts_flap, fill=255)

# Soften the edge slightly for natural anti-aliasing
mask_flap_soft = mask_flap.filter(ImageFilter.GaussianBlur(1.2))

# Save Flap PNG
flap_im = im.copy()
flap_im.putalpha(mask_flap_soft)
# Crop to flap height with extra margin
flap_cropped = flap_im.crop((0, 0, w, 700))
flap_cropped.save("d:/Learn/AI/02.Weeding/03_V3/public/envelope-flap.png")
print("Saved envelope-flap.png")

# Now create the Pocket mask (everything below the flap)
mask_pocket = Image.new("L", (w, h), 0)
draw_pocket = ImageDraw.Draw(mask_pocket)
pts_pocket = [
    (0, 480),
    (int(w * 0.15), 515),
    (int(w * 0.30), 570),
    (int(w * 0.50), 680),
    (int(w * 0.70), 570),
    (int(w * 0.85), 515),
    (w, 460),
    (w, h),
    (0, h)
]
draw_pocket.polygon(pts_pocket, fill=255)
mask_pocket_soft = mask_pocket.filter(ImageFilter.GaussianBlur(1.2))

pocket_im = im.copy()
pocket_im.putalpha(mask_pocket_soft)
pocket_im.save("d:/Learn/AI/02.Weeding/03_V3/public/envelope-pocket.png")
print("Saved envelope-pocket.png")
