# Khmer Wedding Invitation Envelope Transformation Analysis

> **Source Analysis**: Mobile digital wedding invitation interface from `e.sambot.co`.  
> **Sequence Flow**: Analyzed **from Right to Left** (Right image is the initial closed state, progressing to the open state on the far left).

---

## 1. Overview & Conceptual Architecture

The digital invitation represents a traditional Khmer wedding envelope (*សំបុត្រអាពាហ៍ពិពាហ៍*) undergoing a 4-step progressive 3D unfolding animation:

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│   Step 1        │  ──►  │   Step 2        │  ──►  │   Step 3        │  ──►  │   Step 4        │
│   (Far Right)   │       │ (2nd from Right)│       │ (2nd from Left) │       │   (Far Left)    │
│   Closed Flap   │       │  Initial Lift   │       │ Radiance Reveal │       │   Fully Open    │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```

---

## 2. Step-by-Step Visual Analysis (Right to Left)

### Step 1: Closed Envelope Flap (Far Right — Starting State)
* **Status**: Resting / Unopened.
* **Flap Geometry**:
  * Scalloped lace triangular flap pointing downward toward the center of the card.
  * Flap angle: `rotateX(0deg)`.
  * Position: Covers the top 50% of the envelope cavity.
* **Emblem / Seal**:
  * Circular gold filigree mandala medallion resting in the center of the scalloped flap.
  * Contains the couple's intertwined gold monogram initials (**`ល-វ`**).
* **Card Texture & Borders**:
  * Ivory / pearlescent cream paper texture (`#faf7f0`).
  * Double gold hairline border (`#c59828`) with beveled corner accents.
* **User Interaction**:
  * Waiting for guest tap or trigger.

---

### Step 2: Unsealing & Initial Lift (Second from Right)
* **Status**: Transition from 0% to ~30%.
* **Flap Geometry**:
  * The flap unseals and begins folding upward along the top fold line (`rotateX(0deg → 55deg)`).
  * **3D Perspective**: As the flap tilts backward, its vertical height visually compresses via CSS `perspective(1000px)`.
* **Shadows & Depth**:
  * A warm golden/amber drop shadow emerges beneath the lifted scalloped flap (`rgba(160, 110, 20, 0.45)`).
  * The bottom pocket rim becomes visible beneath the lifted edge.
* **Emblem**:
  * Monogram crest moves upward and tilts back with the flap.

---

### Step 3: Flipping & Golden Radiance Reveal (Second from Left)
* **Status**: Transition from 30% to ~70%.
* **Flap Geometry**:
  * The flap passes the vertical threshold (`rotateX(90deg → 145deg)`).
  * Moves towards the top of the smartphone screen.
* **Chamber Illumination**:
  * The interior lining of the envelope is exposed, emitting an intense golden burst (`#f59e0b` to `#fef08a`).
  * Floating golden sparkles and light particles emerge from within the envelope cavity.
* **Pocket Geometry**:
  * The front envelope pocket remains fixed at the bottom half with a downward V-neckline.

---

### Step 4: Fully Opened Envelope & Card Presentation (Far Left — Final State)
* **Status**: 100% Complete.
* **Flap Geometry**:
  * The top flap is completely opened and resting flat at the top (`rotateX(180deg)` or translated to top edge).
  * The golden monogram seal is now prominently displayed at the top center.
* **Inner Glow**:
  * Warm, uniform golden halo illuminating the center.
* **Invitation Presentation**:
  * The inner invitation letter/card is now fully accessible and begins its upward slide animation out of the envelope pocket to present the ceremony details, groom & bride names, schedule, and RSVP.

---

## 3. Visual Specifications & Design Tokens

### Color Palette
| Token Name | Hex Value | Usage |
| :--- | :--- | :--- |
| `--envelope-cream` | `#faf7f0` | Main paper texture for pocket and flap |
| `--envelope-border` | `#c59828` | Outer frame and filigree outline |
| `--gold-glow-core` | `#fffbeb` | Center light burst inside envelope |
| `--gold-glow-mid` | `#fbbf24` | Warm golden chamber radiance |
| `--gold-glow-outer` | `#d97706` | Deep amber shadow inside pocket |
| `--shadow-fold` | `rgba(146, 94, 11, 0.35)` | 3D shadow cast under opening flap |

### Typography
- **Khmer Heading**: `Moul`, cursive (`សិរីមង្គលអាពាហ៍ពិពាហ៍`)
- **Khmer Body**: `Kantumruy Pro`, sans-serif (`សូមគោរពអញ្ជើញ`)
- **English Subtitle**: `Cinzel`, serif (`WEDDING INVITATION`)

---

## 4. Multi-Layer Component Structure

```
[Layer 4]  Flap Element (.envelope-flap)
           ├── Scalloped lace border
           └── Gold Monogram Emblem (.monogram-seal)
           (Animates: transform-origin: top; rotateX: 0deg -> 180deg)
               │
[Layer 3]  Front Pocket (.envelope-pocket)
           ├── Fixed lower half with V-neckline
           └── Double gold border + corner cuts
               │
[Layer 2]  Inner Letter (.wedding-letter-card)
           └── Slides up (translateY: 0% -> -80%)
               │
[Layer 1]  Back Wall & Inner Glow (.envelope-back)
           └── Radial golden burst + floating sparkles
```

---

## 5. CSS 3D Transformation Math

```css
/* Container Perspective */
.envelope-container {
  perspective: 1200px;
  position: relative;
  width: 100%;
  max-width: 390px;
  height: 720px;
}

/* 3D Folding Flap */
.envelope-flap {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  transform-origin: top center;
  transform-style: preserve-3d;
  transition: transform 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Step States */
.envelope-container[data-step="1"] .envelope-flap {
  transform: rotateX(0deg);
  z-index: 10;
}

.envelope-container[data-step="2"] .envelope-flap {
  transform: rotateX(55deg);
  z-index: 10;
}

.envelope-container[data-step="3"] .envelope-flap {
  transform: rotateX(145deg);
  z-index: 2;
}

.envelope-container[data-step="4"] .envelope-flap {
  transform: rotateX(180deg);
  z-index: 1;
}
```
