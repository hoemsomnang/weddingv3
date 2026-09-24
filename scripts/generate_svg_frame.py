import math
import os

def create_svg():
    width = 900
    height = 1600

    svg_parts = []
    svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #f5f4ef;">
  <defs>
    <!-- Paper background gradient with soft ambient light -->
    <radialGradient id="bg-ambient" cx="45%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#faf9f6" />
      <stop offset="55%" stop-color="#f4f2ec" />
      <stop offset="100%" stop-color="#ebe7df" />
    </radialGradient>

    <!-- Plaster relief drop shadows for realistic 3D depth -->
    <filter id="plaster-shadow-deep" x="-30%" y="-30%" width="170%" height="170%">
      <feDropShadow dx="-4" dy="6" stdDeviation="5" flood-color="#4d4436" flood-opacity="0.18" />
      <feDropShadow dx="-1" dy="2" stdDeviation="2" flood-color="#403628" flood-opacity="0.12" />
    </filter>

    <filter id="plaster-shadow-med" x="-25%" y="-25%" width="160%" height="160%">
      <feDropShadow dx="-3" dy="4.5" stdDeviation="3.5" flood-color="#544b3c" flood-opacity="0.16" />
    </filter>

    <filter id="plaster-shadow-soft" x="-20%" y="-20%" width="150%" height="150%">
      <feDropShadow dx="-2" dy="3" stdDeviation="2.5" flood-color="#615746" flood-opacity="0.13" />
    </filter>

    <!-- Pearl / Gold Metallic Bead Gradient -->
    <radialGradient id="gold-pearl-grad" cx="35%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="25%" stop-color="#fff4cc" />
      <stop offset="55%" stop-color="#eac266" />
      <stop offset="85%" stop-color="#b88426" />
      <stop offset="100%" stop-color="#7a4f0b" />
    </radialGradient>

    <!-- Pearl Bead Drop Shadow -->
    <filter id="pearl-shadow" x="-40%" y="-40%" width="200%" height="200%">
      <feDropShadow dx="-1" dy="1.5" stdDeviation="1" flood-color="#523910" flood-opacity="0.35" />
    </filter>

    <!-- Soft Golden Center Glow -->
    <radialGradient id="stamen-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f5e1a4" stop-opacity="0.5" />
      <stop offset="60%" stop-color="#e3c274" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#e3c274" stop-opacity="0" />
    </radialGradient>

    <!-- Petal surface sculpted gradients -->
    <linearGradient id="petal-grad-1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#f8f6f0" />
      <stop offset="85%" stop-color="#eee9dd" />
      <stop offset="100%" stop-color="#e1dbcc" />
    </linearGradient>

    <linearGradient id="petal-grad-2" x1="20%" y1="0%" x2="80%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="60%" stop-color="#f6f3eb" />
      <stop offset="100%" stop-color="#e5dfd2" />
    </linearGradient>

    <linearGradient id="petal-inner-crease" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9" />
      <stop offset="45%" stop-color="#e5dfd0" stop-opacity="0.6" />
      <stop offset="55%" stop-color="#cfc7b4" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.9" />
    </linearGradient>

    <!-- Leaf sculpted gradient -->
    <linearGradient id="leaf-grad-left" x1="0%" y1="30%" x2="100%" y2="70%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="45%" stop-color="#f5f3eb" />
      <stop offset="100%" stop-color="#ddd7c7" />
    </linearGradient>

    <linearGradient id="leaf-grad-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e3ddd0" />
      <stop offset="55%" stop-color="#f4f1e8" />
      <stop offset="100%" stop-color="#ffffff" />
    </linearGradient>

    <!-- Stem 3D tube gradient -->
    <linearGradient id="stem-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="35%" stop-color="#f8f7f2" />
      <stop offset="70%" stop-color="#e4ded1" />
      <stop offset="100%" stop-color="#cdc5b3" />
    </linearGradient>
  </defs>

  <!-- Card Background -->
  <rect width="{width}" height="{height}" fill="url(#bg-ambient)" />

  <!-- Subtle Outer Border/Margin Guideline (Very delicate, whisper tone) -->
  <rect x="25" y="25" width="{width-50}" height="{height-50}" fill="none" stroke="#e8e4da" stroke-width="1" stroke-dasharray="8 6" opacity="0.4" />
''')

    # Helper functions to draw relief elements
    def render_leaf(cx, cy, length, angle_deg, curve=0.2, scale=1.0):
        # Generates a sculpted 3D leaf with center rib vein
        rad = math.radians(angle_deg)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        
        # Leaf contour points relative to base (0,0)
        w = length * 0.42 * scale
        l = length * scale
        
        # Rotate & translate helper
        def transform(x, y):
            tx = cx + (x * cos_a - y * sin_a)
            ty = cy + (x * sin_a + y * cos_a)
            return f"{tx:.1f},{ty:.1f}"
        
        # Left half of leaf
        d_left = f"M {transform(0, 0)} " \
                 f"C {transform(l*0.25, -w*0.8)} {transform(l*0.7, -w*0.9)} {transform(l, 0)} " \
                 f"C {transform(l*0.6, -w*0.1)} {transform(l*0.3, 0)} {transform(0, 0)} Z"
        
        # Right half of leaf
        d_right = f"M {transform(0, 0)} " \
                  f"C {transform(l*0.3, 0)} {transform(l*0.6, w*0.1)} {transform(l, 0)} " \
                  f"C {transform(l*0.7, w*0.9)} {transform(l*0.25, w*0.8)} {transform(0, 0)} Z"
        
        # Center vein
        d_vein = f"M {transform(0, 0)} Q {transform(l*0.5, l*curve*0.1)} {transform(l*0.95, 0)}"

        return f'''
    <g filter="url(#plaster-shadow-soft)">
      <path d="{d_left}" fill="url(#leaf-grad-left)" />
      <path d="{d_right}" fill="url(#leaf-grad-right)" />
      <path d="{d_vein}" fill="none" stroke="#cfc7b5" stroke-width="{1.5*scale}" stroke-linecap="round" opacity="0.75" />
    </g>'''

    def render_vine(d_path, width_stroke=3.5):
        return f'''
    <g filter="url(#plaster-shadow-soft)">
      <path d="{d_path}" fill="none" stroke="#ded8c9" stroke-width="{width_stroke + 1.2}" stroke-linecap="round" />
      <path d="{d_path}" fill="none" stroke="url(#stem-grad)" stroke-width="{width_stroke}" stroke-linecap="round" />
      <path d="{d_path}" fill="none" stroke="#ffffff" stroke-width="{width_stroke * 0.35}" stroke-linecap="round" opacity="0.8" />
    </g>'''

    def render_flower(cx, cy, size, rotation=0, petal_count=5, open_ratio=1.0, bead_count=5):
        elements = []
        elements.append(f'  <!-- Flower at ({cx},{cy}) -->')
        elements.append(f'  <g transform="translate({cx}, {cy}) rotate({rotation})">')
        
        # Background ambient shadow for whole flower cluster
        elements.append(f'    <circle cx="0" cy="0" r="{size * 0.9}" fill="url(#stamen-glow)" opacity="0.7" />')

        # Layer 1: Outer Petals
        angle_step = 360 / petal_count
        p_len = size
        p_w = size * 0.65 * (0.8 + 0.2 * open_ratio)

        for i in range(petal_count):
            p_ang = i * angle_step
            rad = math.radians(p_ang)
            ca = math.cos(rad)
            sa = math.sin(rad)

            # A sculpted curved petal path
            # starts at (0,0), curves outward to tip at (0, -p_len), curves back to (0,0)
            d_petal = f"M 0,0 " \
                      f"C {-p_w*0.8:.1f},{-p_len*0.3:.1f} {-p_w:.1f},{-p_len*0.75:.1f} 0,{-p_len:.1f} " \
                      f"C {p_w:.1f},{-p_len*0.75:.1f} {p_w*0.8:.1f},{-p_len*0.3:.1f} 0,0 Z"

            elements.append(f'''
      <!-- Petal {i+1} -->
      <g transform="rotate({p_ang:.1f})" filter="url(#plaster-shadow-med)">
        <path d="{d_petal}" fill="url(#petal-grad-1)" />
        <!-- Petal center ridge / embossed fold line -->
        <path d="M 0,0 C 0,{-p_len*0.3:.1f} 0,{-p_len*0.7:.1f} 0,{-p_len*0.95:.1f}" 
              fill="none" stroke="#ffffff" stroke-width="1.8" opacity="0.85" stroke-linecap="round" />
        <path d="M {-p_w*0.1:.1f},{-p_len*0.2:.1f} C {-p_w*0.15:.1f},{-p_len*0.5:.1f} {-p_w*0.1:.1f},{-p_len*0.75:.1f} 0,{-p_len*0.9:.1f}" 
              fill="none" stroke="#dcd6c5" stroke-width="1" opacity="0.45" />
      </g>''')

        # Layer 2: Inner Petal Ruffle / Core Cup (if large flower)
        if size > 45:
            inner_count = petal_count
            inner_len = size * 0.55
            inner_w = inner_len * 0.7
            inner_offset = angle_step / 2
            for j in range(inner_count):
                i_ang = j * angle_step + inner_offset
                d_inner = f"M 0,0 " \
                          f"C {-inner_w*0.7:.1f},{-inner_len*0.3:.1f} {-inner_w:.1f},{-inner_len*0.8:.1f} 0,{-inner_len:.1f} " \
                          f"C {inner_w:.1f},{-inner_len*0.8:.1f} {inner_w*0.7:.1f},{-inner_len*0.3:.1f} 0,0 Z"
                elements.append(f'''
      <g transform="rotate({i_ang:.1f})" filter="url(#plaster-shadow-deep)">
        <path d="{d_inner}" fill="url(#petal-grad-2)" />
        <path d="M 0,0 L 0,{-inner_len*0.85:.1f}" fill="none" stroke="#ffffff" stroke-width="1.2" opacity="0.9" />
      </g>''')

        # Pistil Golden Pearl Beads Cluster
        elements.append('      <!-- Center Pearl Stamen Cluster -->')
        elements.append('      <g filter="url(#pearl-shadow)">')
        
        # Center bead
        c_r = max(2.8, size * 0.075)
        elements.append(f'        <circle cx="0" cy="0" r="{c_r:.1f}" fill="url(#gold-pearl-grad)" />')
        elements.append(f'        <circle cx="{-c_r*0.3:.1f}" cy="{-c_r*0.3:.1f}" r="{c_r*0.3:.1f}" fill="#ffffff" opacity="0.9" />')

        # Surrounding ring of pearl beads
        surround_r = c_r * 1.55
        bead_r = c_r * 0.82
        for b in range(bead_count):
            b_ang = b * (360 / bead_count) + 15
            b_rad = math.radians(b_ang)
            bx = surround_r * math.cos(b_rad)
            by = surround_r * math.sin(b_rad)
            elements.append(f'        <circle cx="{bx:.1f}" cy="{by:.1f}" r="{bead_r:.1f}" fill="url(#gold-pearl-grad)" />')
            elements.append(f'        <circle cx="{bx - bead_r*0.25:.1f}" cy="{by - bead_r*0.25:.1f}" r="{bead_r*0.28:.1f}" fill="#ffffff" opacity="0.85" />')

        elements.append('      </g>')
        elements.append('  </g>')
        return "\n".join(elements)

    def render_bud(cx, cy, size, angle_deg):
        # A delicate unopened flower bud
        elements = []
        elements.append(f'  <g transform="translate({cx}, {cy}) rotate({angle_deg})" filter="url(#plaster-shadow-soft)">')
        elements.append(f'''
    <!-- Bud Sepals and Petals -->
    <path d="M 0,0 C -{size*0.4:.1f},-{size*0.4:.1f} -{size*0.5:.1f},-{size*0.9:.1f} 0,-{size*1.2:.1f} C {size*0.5:.1f},-{size*0.9:.1f} {size*0.4:.1f},-{size*0.4:.1f} 0,0 Z" fill="url(#petal-grad-1)" />
    <path d="M 0,0 C -{size*0.2:.1f},-{size*0.5:.1f} 0,-{size:.1f} 0,-{size*1.18:.1f}" stroke="#ffffff" stroke-width="1.2" fill="none" opacity="0.8" />
    <!-- Sepal clasp -->
    <path d="M -{size*0.35:.1f},0 C -{size*0.2:.1f},-{size*0.5:.1f} 0,-{size*0.3:.1f} 0,0 C 0,-{size*0.3:.1f} {size*0.2:.1f},-{size*0.5:.1f} {size*0.35:.1f},0 Z" fill="url(#leaf-grad-left)" />
''')
        elements.append('  </g>')
        return "\n".join(elements)

    # -------------------------------------------------------------
    # TOP-LEFT CORNER COMPOSITION
    # -------------------------------------------------------------
    svg_parts.append('  <!-- ============================================== -->')
    svg_parts.append('  <!-- TOP-LEFT EMBOSSED PLASTER FLORAL CORNER        -->')
    svg_parts.append('  <!-- ============================================== -->')
    svg_parts.append('  <g id="top-left-corner">')

    # Main cascading vine stems
    svg_parts.append(render_vine("M -20,40 C 60,60 120,90 190,75 C 240,65 290,110 320,130", 4.2))
    svg_parts.append(render_vine("M 20,-20 C 40,80 70,160 85,260 C 95,350 45,430 30,510 C 15,570 35,620 40,650", 4.0))
    svg_parts.append(render_vine("M 85,250 C 130,280 180,260 215,225 C 240,200 250,160 230,120", 3.2))
    svg_parts.append(render_vine("M 70,360 C 110,390 140,430 135,480 C 130,520 100,560 70,580", 2.8))
    svg_parts.append(render_vine("M 180,75 C 195,30 230,20 270,35 C 310,50 330,25 350,15", 2.5))
    svg_parts.append(render_vine("M 30,510 C 65,530 80,570 75,610", 2.4))

    # Curling filigree flourishes / tendrils
    svg_parts.append(render_vine("M 190,75 C 220,105 205,145 175,140 C 155,135 158,110 178,112", 2.0))
    svg_parts.append(render_vine("M 35,420 C 65,425 75,455 60,475 C 45,485 30,465 42,450", 1.8))
    svg_parts.append(render_vine("M 270,35 C 300,30 320,55 305,75 C 290,85 275,70 288,60", 1.8))

    # Sculpted Leaves along top-left
    leaves_tl = [
        # (cx, cy, length, angle, curve, scale)
        (75, 45, 60, 35, 0.2, 1.0),
        (130, 65, 55, 15, -0.2, 0.9),
        (225, 60, 50, 40, 0.3, 0.85),
        (275, 115, 65, 65, 0.2, 1.0),
        (315, 135, 45, 30, -0.2, 0.75),
        (35, 140, 65, 80, 0.2, 1.0),
        (50, 195, 55, 105, -0.2, 0.9),
        (100, 190, 48, 15, 0.3, 0.8),
        (145, 230, 55, 35, -0.2, 0.85),
        (190, 245, 60, 20, 0.2, 0.95),
        (65, 320, 60, 120, -0.3, 0.9),
        (100, 360, 50, 75, 0.2, 0.8),
        (120, 420, 58, 60, -0.2, 0.95),
        (130, 490, 52, 95, 0.2, 0.85),
        (95, 550, 55, 115, -0.2, 0.9),
        (55, 590, 45, 130, 0.2, 0.75),
        (40, 645, 40, 110, -0.2, 0.7),
        (35, 270, 45, 145, 0.2, 0.75),
        (20, 380, 45, 160, -0.2, 0.75),
    ]
    for lx, ly, l_len, l_ang, l_crv, l_sc in leaves_tl:
        svg_parts.append(render_leaf(lx, ly, l_len, l_ang, l_crv, l_sc))

    # Buds along top-left
    svg_parts.append(render_bud(330, 140, 28, 55))
    svg_parts.append(render_bud(355, 18, 24, 75))
    svg_parts.append(render_bud(42, 655, 26, 125))
    svg_parts.append(render_bud(78, 615, 22, 140))
    svg_parts.append(render_bud(245, 175, 25, 40))

    # Flowers in Top-Left (Layered in perspective from small to focal)
    # Small accent florets
    svg_parts.append(render_flower(215, 115, 36, rotation=22, petal_count=5, open_ratio=0.85, bead_count=4))
    svg_parts.append(render_flower(140, 440, 38, rotation=45, petal_count=5, open_ratio=0.85, bead_count=4))
    svg_parts.append(render_flower(75, 505, 34, rotation=10, petal_count=5, open_ratio=0.8, bead_count=3))

    # Medium flowers
    svg_parts.append(render_flower(170, 70, 58, rotation=12, petal_count=5, open_ratio=1.0, bead_count=5))
    svg_parts.append(render_flower(125, 275, 48, rotation=68, petal_count=5, open_ratio=0.9, bead_count=5))
    svg_parts.append(render_flower(38, 380, 44, rotation=35, petal_count=5, open_ratio=0.9, bead_count=4))

    # Main Showcase Flower 1: Top-Left Hero Blossom (Grand Camellia / Plumeria)
    svg_parts.append(render_flower(65, 215, 76, rotation=52, petal_count=5, open_ratio=1.1, bead_count=7))
    
    # Secondary Showcase Flower: Top Upper Center
    svg_parts.append(render_flower(180, 180, 52, rotation=85, petal_count=5, open_ratio=0.95, bead_count=5))

    svg_parts.append('  </g>')

    # -------------------------------------------------------------
    # BOTTOM-RIGHT CORNER COMPOSITION
    # -------------------------------------------------------------
    svg_parts.append('  <!-- ============================================== -->')
    svg_parts.append('  <!-- BOTTOM-RIGHT EMBOSSED PLASTER FLORAL CORNER    -->')
    svg_parts.append('  <!-- ============================================== -->')
    svg_parts.append('  <g id="bottom-right-corner">')

    # Main cascading vine stems for bottom-right
    svg_parts.append(render_vine("M 920,1540 C 840,1520 780,1490 700,1505 C 650,1515 600,1470 560,1450", 4.2))
    svg_parts.append(render_vine("M 880,1620 C 860,1520 830,1440 815,1340 C 805,1240 855,1160 870,1080 C 885,1020 865,970 860,940", 4.0))
    svg_parts.append(render_vine("M 815,1340 C 770,1310 720,1330 685,1365 C 660,1390 650,1430 670,1470", 3.2))
    svg_parts.append(render_vine("M 830,1230 C 790,1200 760,1160 765,1110 C 770,1070 800,1030 830,1010", 2.8))
    svg_parts.append(render_vine("M 710,1515 C 695,1560 660,1570 620,1555 C 580,1540 560,1565 540,1575", 2.5))
    svg_parts.append(render_vine("M 870,1080 C 835,1060 820,1020 825,980", 2.4))

    # Delicate tendrils
    svg_parts.append(render_vine("M 700,1515 C 670,1485 685,1445 715,1450 C 735,1455 732,1480 712,1478", 2.0))
    svg_parts.append(render_vine("M 865,1170 C 835,1165 825,1135 840,1115 C 855,1105 870,1125 858,1140", 1.8))
    svg_parts.append(render_vine("M 620,1555 C 590,1560 570,1535 585,1515 C 600,1505 615,1520 602,1530", 1.8))

    # Sculpted Leaves along bottom-right
    leaves_br = [
        # (cx, cy, length, angle, curve, scale)
        (825, 1545, 60, 215, 0.2, 1.0),
        (770, 1525, 55, 195, -0.2, 0.9),
        (665, 1530, 50, 220, 0.3, 0.85),
        (615, 1475, 65, 245, 0.2, 1.0),
        (575, 1455, 45, 210, -0.2, 0.75),
        (865, 1450, 65, 260, 0.2, 1.0),
        (850, 1395, 55, 285, -0.2, 0.9),
        (800, 1400, 48, 195, 0.3, 0.8),
        (745, 1360, 55, 215, -0.2, 0.85),
        (700, 1345, 60, 200, 0.2, 0.95),
        (835, 1270, 60, 300, -0.3, 0.9),
        (800, 1230, 50, 255, 0.2, 0.8),
        (770, 1170, 58, 240, -0.2, 0.95),
        (760, 1100, 52, 275, 0.2, 0.85),
        (795, 1040, 55, 295, -0.2, 0.9),
        (835, 1000, 45, 310, 0.2, 0.75),
        (850, 945, 40, 290, -0.2, 0.7),
        (865, 1320, 45, 325, 0.2, 0.75),
        (875, 1210, 45, 340, -0.2, 0.75),
    ]
    for lx, ly, l_len, l_ang, l_crv, l_sc in leaves_br:
        svg_parts.append(render_leaf(lx, ly, l_len, l_ang, l_crv, l_sc))

    # Buds along bottom-right
    svg_parts.append(render_bud(560, 1450, 28, 235))
    svg_parts.append(render_bud(535, 1570, 24, 255))
    svg_parts.append(render_bud(848, 935, 26, 305))
    svg_parts.append(render_bud(812, 975, 22, 320))
    svg_parts.append(render_bud(645, 1415, 25, 220))

    # Flowers in Bottom-Right
    # Small accent florets
    svg_parts.append(render_flower(675, 1475, 36, rotation=202, petal_count=5, open_ratio=0.85, bead_count=4))
    svg_parts.append(render_flower(750, 1150, 38, rotation=225, petal_count=5, open_ratio=0.85, bead_count=4))
    svg_parts.append(render_flower(815, 1085, 34, rotation=190, petal_count=5, open_ratio=0.8, bead_count=3))

    # Medium flowers
    svg_parts.append(render_flower(720, 1520, 58, rotation=192, petal_count=5, open_ratio=1.0, bead_count=5))
    svg_parts.append(render_flower(765, 1315, 48, rotation=248, petal_count=5, open_ratio=0.9, bead_count=5))
    svg_parts.append(render_flower(852, 1210, 44, rotation=215, petal_count=5, open_ratio=0.9, bead_count=4))

    # Main Showcase Flower 2: Bottom-Right Hero Blossom
    svg_parts.append(render_flower(825, 1375, 78, rotation=232, petal_count=5, open_ratio=1.1, bead_count=7))
    
    # Secondary Showcase Flower: Bottom-Right Inner companion
    svg_parts.append(render_flower(710, 1410, 54, rotation=265, petal_count=5, open_ratio=0.95, bead_count=5))

    svg_parts.append('  </g>')

    # Finish SVG
    svg_parts.append('</svg>')
    return "\n".join(svg_parts)

if __name__ == "__main__":
    content = create_svg()
    
    # Write to public/
    os.makedirs("public", exist_ok=True)
    pub_path = os.path.join("public", "wedding-floral-frame.svg")
    with open(pub_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {pub_path} ({len(content)} bytes)")

    # Write to src/assets/
    os.makedirs(os.path.join("src", "assets"), exist_ok=True)
    asset_path = os.path.join("src", "assets", "wedding-floral-frame.svg")
    with open(asset_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved: {asset_path} ({len(content)} bytes)")
