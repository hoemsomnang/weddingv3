from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Base image
im = Image.open("public/wedding-envelope-scallop.jpg").convert("RGBA")
w, h = im.size

# In wedding-envelope-scallop.jpg (768 x 1376):
# The flap starts on the left at y ~ 490, dips down to center tip at y ~ 670, and goes up to right at y ~ 460.
# Let's create high-precision masks:

# FLAP MASK: 
# Everything from y=0 down to the scalloped edge.
# We give it a generous cut that includes the shadow edge under the flap so when it folds, the shadow folds with it!
mask_flap = Image.new("L", (w, h), 0)
draw_f = ImageDraw.Draw(mask_flap)

# Exact V-scallop points for the flap
pts_f = [
    (0, 0),
    (w, 0),
    (w, 475),
    (int(w * 0.85), 525),
    (int(w * 0.70), 585),
    (int(w * 0.50), 685), # tip of flap including shadow
    (int(w * 0.30), 585),
    (int(w * 0.15), 525),
    (0, 495)
]
draw_f.polygon(pts_f, fill=255)
# Very subtle blur for anti-aliased edge
mask_flap = mask_flap.filter(ImageFilter.GaussianBlur(0.8))

flap = im.copy()
flap.putalpha(mask_flap)
# Crop flap to height of 700
flap_cropped = flap.crop((0, 0, w, 700))
flap_cropped.save("public/envelope-flap.png")
flap_cropped.save("src/assets/envelope/envelope-flap.png")
print("Saved perfect envelope-flap.png")

# POCKET MASK:
# The pocket covers the entire lower half of the envelope.
# To ensure ZERO gaps, the pocket goes all the way up to y=450 behind the flap!
# That way, behind the scalloped edge of the flap, the pocket is solid paper!
mask_pocket = Image.new("L", (w, h), 0)
draw_p = ImageDraw.Draw(mask_pocket)

pts_p = [
    (0, 470),
    (int(w * 0.15), 500),
    (int(w * 0.30), 560),
    (int(w * 0.50), 660),
    (int(w * 0.70), 560),
    (int(w * 0.85), 500),
    (w, 450),
    (w, h),
    (0, h)
]
draw_p.polygon(pts_p, fill=255)
mask_pocket = mask_pocket.filter(ImageFilter.GaussianBlur(0.8))

pocket = im.copy()
pocket.putalpha(mask_pocket)
pocket.save("public/envelope-pocket.png")
pocket.save("src/assets/envelope/envelope-pocket.png")
print("Saved perfect envelope-pocket.png")
