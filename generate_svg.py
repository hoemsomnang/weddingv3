import math

def generate_html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animated Peacock Artwork</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="artwork-container">
        <svg viewBox="0 0 1000 1200" class="artwork-svg" preserveAspectRatio="xMidYMid slice">
            <defs>
                <!-- Filters for Embossed 3D Look -->
                <filter id="emboss" x="-30%" y="-30%" width="160%" height="160%">
                    <!-- Soft drop shadow -->
                    <feDropShadow dx="3" dy="6" stdDeviation="5" flood-color="#c4a5a5" flood-opacity="0.4"/>
                    <!-- Second tighter shadow for depth -->
                    <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#a88d8d" flood-opacity="0.2"/>
                </filter>
                
                <filter id="light-emboss" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="1" dy="3" stdDeviation="2" flood-color="#d6b8b8" flood-opacity="0.4"/>
                </filter>

                <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur stdDeviation="8" result="blur"/>
                    <feComposite in="SourceGraphic" in2="blur" operator="over"/>
                </filter>

                <!-- Gradients -->
                <linearGradient id="ivory-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="50%" stop-color="#fdfafa"/>
                    <stop offset="100%" stop-color="#efe3e3"/>
                </linearGradient>

                <linearGradient id="pink-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="100%" stop-color="#f7d5dc"/>
                </linearGradient>
                
                <linearGradient id="blue-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ffffff"/>
                    <stop offset="100%" stop-color="#c3d1f0"/>
                </linearGradient>

                <!-- SVG Symbols / Reusable Parts -->
                
                <!-- A single peacock tail feather -->
                <g id="feather">
                    <!-- The stem -->
                    <path d="M 0,0 Q 5,60 0,150" fill="none" stroke="#e8d5d5" stroke-width="2"/>
                    <!-- The eye/fan -->
                    <path d="M 0,-10 C -20,30 -30,70 0,110 C 30,70 20,30 0,-10 Z" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <circle cx="0" cy="30" r="12" fill="url(#blue-grad)" filter="url(#light-emboss)"/>
                    <circle cx="0" cy="32" r="5" fill="#ffffff"/>
                </g>

                <!-- A flower -->
                <g id="flower">
                    <circle cx="0" cy="0" r="8" fill="#f7d5dc" filter="url(#light-emboss)"/>
                    <!-- 5 petals -->
                    <path d="M 0,-8 C -15,-30 15,-30 0,-8 Z" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <path d="M 0,-8 C -15,-30 15,-30 0,-8 Z" transform="rotate(72)" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <path d="M 0,-8 C -15,-30 15,-30 0,-8 Z" transform="rotate(144)" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <path d="M 0,-8 C -15,-30 15,-30 0,-8 Z" transform="rotate(216)" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <path d="M 0,-8 C -15,-30 15,-30 0,-8 Z" transform="rotate(288)" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                </g>
                
                <!-- A leaf -->
                <g id="leaf">
                    <path d="M 0,0 C -15,-20 0,-40 0,-50 C 0,-40 15,-20 0,0 Z" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                </g>
                
                <!-- A small bud -->
                <g id="bud">
                    <circle cx="0" cy="0" r="10" fill="url(#pink-grad)" filter="url(#light-emboss)"/>
                    <circle cx="-2" cy="-2" r="3" fill="#fff" opacity="0.6"/>
                </g>

                <!-- A single wing feather -->
                <g id="wing-feather">
                    <path d="M 0,0 C -10,20 -15,40 0,60 C 15,40 10,20 0,0 Z" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                </g>

                <!-- Full Wing -->
                <g id="full-wing">
                    <path d="M -30,-40 C 40,-80 80,0 20,80 C -40,120 -80,50 -30,-40 Z" fill="url(#ivory-grad)" filter="url(#emboss)"/>
                    <!-- Overlapping wing feathers -->
"""
    # Generate wing feathers
    for i in range(5):
        html += f'                    <use href="#wing-feather" x="{-20 + i*10}" y="{-20 + i*5}" transform="rotate({-20 + i*10})" />\n'
    for i in range(4):
        html += f'                    <use href="#wing-feather" x="{-10 + i*10}" y="{10 + i*5}" transform="rotate({-10 + i*10})" />\n'
    
    html += """                </g>
            </defs>

            <!-- Background Base -->
            <rect width="100%" height="100%" fill="#fdf7f5" />

            <!-- Floral Border Generation -->
            <g class="border-layer">
"""
    # Border elements
    border_elements = []
    # Corners
    corners = [(100, 100), (900, 100), (100, 1100), (900, 1100)]
    for cx, cy in corners:
        html += f'                <!-- Corner at {cx},{cy} -->\n'
        for j in range(8):
            ang = j * 45
            rad = 80
            lx, ly = cx + rad*math.cos(math.radians(ang)), cy + rad*math.sin(math.radians(ang))
            html += f'                <use href="#leaf" x="{lx}" y="{ly}" transform="rotate({ang + 90} {lx} {ly}) scale(1.5)" />\n'
        for j in range(3):
            rad = 40
            ang = j * 120
            fx, fy = cx + rad*math.cos(math.radians(ang)), cy + rad*math.sin(math.radians(ang))
            html += f'                <use href="#flower" x="{fx}" y="{fy}" transform="rotate({ang} {fx} {fy}) scale(2)" />\n'
        html += f'                <use href="#flower" x="{cx}" y="{cy}" transform="scale(3)" style="transform-origin: {cx}px {cy}px;" />\n'

    # Vines along edges
    for y in range(250, 1000, 150):
        html += f'                <use href="#flower" x="80" y="{y}" transform="scale(1.5)" style="transform-origin: 80px {y}px;" />\n'
        html += f'                <use href="#bud" x="120" y="{y+50}" />\n'
        html += f'                <use href="#leaf" x="50" y="{y-40}" transform="rotate(45 50 {y-40})" />\n'

        html += f'                <use href="#flower" x="920" y="{y}" transform="scale(1.5)" style="transform-origin: 920px {y}px;" />\n'
        html += f'                <use href="#bud" x="880" y="{y+50}" />\n'
        html += f'                <use href="#leaf" x="950" y="{y-40}" transform="rotate(-45 950 {y-40})" />\n'

    for x in range(300, 800, 150):
        html += f'                <use href="#flower" x="{x}" y="80" transform="scale(1.5)" style="transform-origin: {x}px 80px;" />\n'
        html += f'                <use href="#leaf" x="{x+40}" y="50" transform="rotate(135 {x+40} 50)" />\n'

        html += f'                <use href="#flower" x="{x}" y="1120" transform="scale(1.5)" style="transform-origin: {x}px 1120px;" />\n'
        html += f'                <use href="#leaf" x="{x+40}" y="1150" transform="rotate(-45 {x+40} 1150)" />\n'

    html += """            </g>

            <!-- Heart in Center -->
            <g class="anim-heart" transform="translate(500, 600)">
                <!-- Heart shadow & glow -->
                <path d="M 0,30 C -120,-70 -250,40 0,180 C 250,40 120,-70 0,30 Z" fill="url(#pink-grad)" filter="url(#emboss)"/>
                <!-- Inner heart -->
                <path d="M 0,50 C -80,-30 -180,50 0,150 C 180,50 80,-30 0,50 Z" fill="none" stroke="#ffffff" stroke-width="8" filter="url(#light-emboss)"/>
                <!-- Bow on heart -->
                <path d="M 0,50 Q -40,10 -60,40 Q -80,70 -40,80 Q -10,90 0,50 Z" fill="url(#ivory-grad)" filter="url(#emboss)"/>
                <path d="M 0,50 Q 40,10 60,40 Q 80,70 40,80 Q 10,90 0,50 Z" fill="url(#ivory-grad)" filter="url(#emboss)"/>
                <circle cx="0" cy="50" r="10" fill="url(#pink-grad)" filter="url(#emboss)"/>
                <path d="M 0,50 Q -20,100 -40,120" fill="none" stroke="#f7d5dc" stroke-width="12" stroke-linecap="round" filter="url(#emboss)"/>
                <path d="M 0,50 Q 20,100 40,120" fill="none" stroke="#f7d5dc" stroke-width="12" stroke-linecap="round" filter="url(#emboss)"/>
            </g>

            <!-- LEFT PEACOCK -->
            <g id="left-peacock" class="peacock anim-peacock-left" transform="translate(300, 750)">
                <!-- Tail Fan -->
                <g class="tail anim-tail-left">
"""
    # Generate tail feathers
    for i in range(25):
        angle = -140 + i * 5
        scale = 1.0 + (math.sin(math.radians(i/25 * 180)) * 0.5)  # Longer in the middle
        html += f'                    <use href="#feather" transform="rotate({angle}) scale({scale})" />\n'
    
    html += """                </g>

                <!-- Body -->
                <g class="body" filter="url(#emboss)">
                    <!-- Elegant neck & body -->
                    <path d="M -30,-50 C -80,-250 60,-350 40,-400 C 20,-450 -50,-400 -60,-330 C -70,-220 -150,-150 -100,50 C 50,80 100,-20 -30,-50 Z" fill="url(#ivory-grad)"/>
                    
                    <!-- Eye & Beak -->
                    <path d="M 40,-400 L 70,-380 L 45,-375 Z" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <path d="M 40,-400 L 70,-380 L 45,-375 Z" fill="none" stroke="#c4a5a5" stroke-width="1"/>
                    
                    <!-- Closed Eye (romantic) -->
                    <path d="M 25,-390 Q 35,-385 45,-390" fill="none" stroke="#888" stroke-width="2" stroke-linecap="round"/>
                    <path d="M 30,-387 L 28,-383 M 35,-387 L 35,-383 M 40,-387 L 42,-383" fill="none" stroke="#888" stroke-width="1.5" stroke-linecap="round"/>

                    <!-- Crown / Crest -->
                    <g stroke="#d6b8b8" stroke-width="2">
                        <path d="M 10,-405 Q 0,-440 -10,-460" fill="none"/>
                        <circle cx="-10" cy="-460" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                        
                        <path d="M 0,-400 Q -15,-440 -30,-450" fill="none"/>
                        <circle cx="-30" cy="-450" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                        
                        <path d="M -10,-395 Q -30,-430 -50,-430" fill="none"/>
                        <circle cx="-50" cy="-430" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                        
                        <path d="M 20,-405 Q 25,-440 30,-465" fill="none"/>
                        <circle cx="30" cy="-465" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                    </g>
                    
                    <!-- Subtle scales on chest -->
"""
    # Chest scales
    for row in range(5):
        for col in range(3):
            cx = -60 + col*20 + (row%2)*10
            cy = -250 + row*25
            html += f'                    <path d="M {cx},{cy} Q {cx+10},{cy+15} {cx+20},{cy}" fill="none" stroke="#fff" stroke-width="2" filter="url(#light-emboss)"/>\n'
    
    html += """                </g>

                <!-- Wing -->
                <use href="#full-wing" class="wing anim-wing-left" x="0" y="0" />
            </g>

            <!-- RIGHT PEACOCK (Mirrored) -->
            <g id="right-peacock" class="peacock anim-peacock-right" transform="translate(700, 750) scale(-1, 1)">
                <!-- Tail Fan -->
                <g class="tail anim-tail-right">
"""
    # Generate tail feathers
    for i in range(25):
        angle = -140 + i * 5
        scale = 1.0 + (math.sin(math.radians(i/25 * 180)) * 0.5)
        html += f'                    <use href="#feather" transform="rotate({angle}) scale({scale})" />\n'
    
    html += """                </g>

                <!-- Body -->
                <g class="body" filter="url(#emboss)">
                    <!-- Elegant neck & body -->
                    <path d="M -30,-50 C -80,-250 60,-350 40,-400 C 20,-450 -50,-400 -60,-330 C -70,-220 -150,-150 -100,50 C 50,80 100,-20 -30,-50 Z" fill="url(#ivory-grad)"/>
                    
                    <path d="M 40,-400 L 70,-380 L 45,-375 Z" fill="url(#ivory-grad)" filter="url(#light-emboss)"/>
                    <path d="M 40,-400 L 70,-380 L 45,-375 Z" fill="none" stroke="#c4a5a5" stroke-width="1"/>
                    
                    <path d="M 25,-390 Q 35,-385 45,-390" fill="none" stroke="#888" stroke-width="2" stroke-linecap="round"/>
                    <path d="M 30,-387 L 28,-383 M 35,-387 L 35,-383 M 40,-387 L 42,-383" fill="none" stroke="#888" stroke-width="1.5" stroke-linecap="round"/>

                    <g stroke="#d6b8b8" stroke-width="2">
                        <path d="M 10,-405 Q 0,-440 -10,-460" fill="none"/>
                        <circle cx="-10" cy="-460" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                        
                        <path d="M 0,-400 Q -15,-440 -30,-450" fill="none"/>
                        <circle cx="-30" cy="-450" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                        
                        <path d="M -10,-395 Q -30,-430 -50,-430" fill="none"/>
                        <circle cx="-50" cy="-430" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                        
                        <path d="M 20,-405 Q 25,-440 30,-465" fill="none"/>
                        <circle cx="30" cy="-465" r="6" fill="url(#pink-grad)" stroke="none" filter="url(#light-emboss)"/>
                    </g>
"""
    # Chest scales
    for row in range(5):
        for col in range(3):
            cx = -60 + col*20 + (row%2)*10
            cy = -250 + row*25
            html += f'                    <path d="M {cx},{cy} Q {cx+10},{cy+15} {cx+20},{cy}" fill="none" stroke="#fff" stroke-width="2" filter="url(#light-emboss)"/>\n'
    
    html += """                </g>

                <!-- Wing -->
                <use href="#full-wing" class="wing anim-wing-right" x="0" y="0" />
            </g>
            
            <!-- Foreground Decorative Flowers overlapping the birds -->
            <use href="#flower" x="500" y="850" transform="scale(3) rotate(15)" style="transform-origin: 500px 850px;"/>
            <use href="#leaf" x="430" y="860" transform="rotate(-60 430 860) scale(1.5)" />
            <use href="#leaf" x="570" y="860" transform="rotate(60 570 860) scale(1.5)" />
            
            <use href="#flower" x="350" y="800" transform="scale(2) rotate(-20)" style="transform-origin: 350px 800px;"/>
            <use href="#flower" x="650" y="800" transform="scale(2) rotate(20)" style="transform-origin: 650px 800px;"/>

        </svg>
    </div>
    <script src="script.js"></script>
</body>
</html>
"""
    with open('peacock-animation/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated index.html successfully.")

if __name__ == "__main__":
    generate_html()
