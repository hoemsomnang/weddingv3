<template>
  <div class="video-preview-container">
    <div class="preview-viewport">
      <!-- Camera Zoom Stage: Zooms in to wedding-throne-chairs then zooms out slowly back -->
      <div class="camera-zoom-stage">
        <!-- 1. Background Image -->
        <img
          :src="purpleStaircaseImg"
          alt="Purple Staircase"
          class="preview-bg-image"
        />

        <!-- 2. Royal Wedding Palace Items Layer -->
        <div class="palace-items-layer">
          <!-- 2a. Royal Golden Wedding Monogram / Seal (In Upper Cathedral Arch) -->
          <div class="item-monogram">
            <img
              :src="weddingMonogramImg"
              alt="Royal Wedding Monogram Seal"
            />
          </div>

          <!-- 2b. Royal Floral Wedding Arch (Top Landing Doorway) -->
          <div class="item-floral-arch">
            <img
              :src="floralArchImg"
              alt="Royal Floral Wedding Arch"
            />
          </div>

          <!-- 2c. Twin Royal Throne Chairs (Inside Arch on Top Landing) -->
          <div class="item-throne-chairs">
            <img
              :src="throneChairsImg"
              alt="Twin Royal Wedding Thrones"
            />
          </div>
        </div>

        <!-- 3. 3 Crystal Chandeliers on Top: Left, Center, Right -->
        <div class="chandeliers-container">
          <!-- Left Chandelier -->
          <div class="chandelier-item chandelier-left">
            <img
              :src="crystalChandelierImg"
              alt="Crystal Chandelier Left"
              class="chandelier-img"
            />
            <div class="flames-group">
              <span class="candle-flame f-top"></span>
              <span class="candle-flame f-mid-l"></span>
              <span class="candle-flame f-mid-r"></span>
              <span class="candle-flame f-inner-l"></span>
              <span class="candle-flame f-inner-r"></span>
              <span class="candle-flame f-outer-l"></span>
              <span class="candle-flame f-outer-r"></span>
              <span class="candle-flame f-edge-l"></span>
              <span class="candle-flame f-edge-r"></span>
            </div>
          </div>

          <!-- Center Chandelier -->
          <div class="chandelier-item chandelier-center">
            <img
              :src="crystalChandelierImg"
              alt="Crystal Chandelier Center"
              class="chandelier-img"
            />
            <div class="flames-group">
              <span class="candle-flame f-top"></span>
              <span class="candle-flame f-mid-l"></span>
              <span class="candle-flame f-mid-r"></span>
              <span class="candle-flame f-inner-l"></span>
              <span class="candle-flame f-inner-r"></span>
              <span class="candle-flame f-outer-l"></span>
              <span class="candle-flame f-outer-r"></span>
              <span class="candle-flame f-edge-l"></span>
              <span class="candle-flame f-edge-r"></span>
            </div>
          </div>

          <!-- Right Chandelier -->
          <div class="chandelier-item chandelier-right">
            <img
              :src="crystalChandelierImg"
              alt="Crystal Chandelier Right"
              class="chandelier-img"
            />
            <div class="flames-group">
              <span class="candle-flame f-top"></span>
              <span class="candle-flame f-mid-l"></span>
              <span class="candle-flame f-mid-r"></span>
              <span class="candle-flame f-inner-l"></span>
              <span class="candle-flame f-inner-r"></span>
              <span class="candle-flame f-outer-l"></span>
              <span class="candle-flame f-outer-r"></span>
              <span class="candle-flame f-edge-l"></span>
              <span class="candle-flame f-edge-r"></span>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. Overlay Background (Disappears slowly to reveal background and palace items) -->
      <div class="curtain-overlay">
        <img
          :src="curtainOverlayImg"
          alt="Curtain Overlay"
          class="curtain-overlay-img"
        />
      </div>

      <!-- 5. Edge Purple Rose Bouquets on Left & Right (Animate when zoom nears the end) -->
      <div class="zoom-edge-bouquet bouquet-left">
        <div class="bouquet-float float-left">
          <img
            :src="purpleRoseBouquetImg"
            alt="Purple Rose Bouquet Left"
          />
        </div>
      </div>
      <div class="zoom-edge-bouquet bouquet-right">
        <div class="bouquet-float float-right">
          <img
            :src="purpleRoseBouquetImg"
            alt="Purple Rose Bouquet Right"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import purpleStaircaseImg from '@/assets/purple-staircase-clean.jpg'
import crystalChandelierImg from '@/assets/crystal-chandelier-transparent.png'

// Newly generated items
import weddingMonogramImg from '@/assets/items/wedding-monogram-seal.png'
import floralArchImg from '@/assets/items/royal-floral-wedding-arch.png'
import throneChairsImg from '@/assets/items/wedding-throne-chairs.png'
import purpleRoseBouquetImg from '@/assets/items/purple-rose-bouquet.png'

// Curtain overlay
import curtainOverlayImg from '@/assets/curtain-open-step2-parting-transparent.png'
// import curtainOverlayImg from '@/assets/pic2-suitable-flush.jpg'
</script>

<style scoped>
/* Fullscreen Canvas following HomePage.css */
.video-preview-container {
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #c59828 0%, #e0bc66 35%, #f5dc94 50%, #c59828 70%, #a8791c 100%);
  padding: 12px;
  box-sizing: border-box;
  overflow: hidden;
  user-select: none;
  position: relative;
}

/* Smartphone Viewport strictly following HomePage.css */
.preview-viewport {
  width: min(calc(100vw - 24px), calc((100dvh - 24px) * 9 / 16));
  max-width: 440px;
  aspect-ratio: 9 / 16;
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(50, 35, 5, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.6);
  background-color: #0d0414;
}

/* Camera Zoom Stage: Zooms in till wedding-throne-chairs then zooms out slowly back */
.camera-zoom-stage {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  transform-origin: 50% 43%;
  animation: throneCameraZoom 32s infinite;
  will-change: transform;
}

@keyframes throneCameraZoom {
  0% {
    transform: scale(1);
    animation-timing-function: ease-in-out;
  }
  9.4% {
    transform: scale(1);
    animation-timing-function: cubic-bezier(0.35, 0, 0.25, 1);
  }
  43.8% {
    transform: scale(2.0);
    animation-timing-function: ease-in-out;
  }
  56.2% {
    transform: scale(2.0);
    animation-timing-function: cubic-bezier(0.25, 1, 0.35, 1);
  }
  87.5% {
    transform: scale(1);
    animation-timing-function: ease-in-out;
  }
  100% {
    transform: scale(1);
  }
}

.preview-bg-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
  image-rendering: -webkit-optimize-contrast;
  image-rendering: high-quality;
}

/* 2. Palace Items Layer */
.palace-items-layer {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

/* 2a. Royal Monogram Seal */
.item-monogram {
  position: absolute;
  top: 18%;
  left: 50%;
  transform: translateX(-50%);
  width: 19%;
  z-index: 6;
  pointer-events: none;
  animation: monogramFloat 6.5s ease-in-out infinite alternate;
}

.item-monogram img {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 0 12px rgba(254, 240, 138, 0.5)) drop-shadow(0 4px 10px rgba(0, 0, 0, 0.8));
}

@keyframes monogramFloat {
  0% {
    transform: translateX(-50%) translateY(0) scale(1);
  }
  100% {
    transform: translateX(-50%) translateY(-5px) scale(1.04);
  }
}

/* 2b. Royal Floral Wedding Arch */
.item-floral-arch {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translateX(-50%);
  width: 50%;
  z-index: 7;
  pointer-events: none;
}

.item-floral-arch img {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 6px 16px rgba(0, 0, 0, 0.75));
}

/* 2c. Twin Throne Chairs */
.item-throne-chairs {
  position: absolute;
  top: 41%;
  left: 50%;
  transform: translateX(-50%);
  width: 23%;
  z-index: 8;
  pointer-events: none;
}

.item-throne-chairs img {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.85));
}


/* 3. Chandeliers Proscenium Layer at the Top */
.chandeliers-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 40%;
  pointer-events: none;
  z-index: 10;
  overflow: visible;
  animation: chandelierDropIn 4.2s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

@keyframes chandelierDropIn {
  0% {
    transform: translateY(-115%);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

.chandelier-item {
  position: absolute;
  transform-origin: 50% 0%;
  will-change: transform;
}

.chandelier-img {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.65));
}

/* Left Chandelier */
.chandelier-left {
  top: -8px;
  left: -2%;
  width: calc(34% - 10px);
  z-index: 11;
  animation: swayLeftToRight 6.8s ease-in-out infinite alternate;
}

/* Center Chandelier */
.chandelier-center {
  top: -12px;
  left: 50%;
  width: 46%;
  z-index: 12;
  animation: swayCenterLeftRight 7.6s ease-in-out infinite alternate;
}

/* Right Chandelier */
.chandelier-right {
  top: -8px;
  right: -2%;
  width: calc(34% - 10px);
  z-index: 11;
  animation: swayRightToLeft 7.0s ease-in-out infinite alternate;
}

/* Sway Animations */
@keyframes swayLeftToRight {
  0% {
    transform: rotate(-3.5deg) translateX(-4px);
  }
  100% {
    transform: rotate(3.5deg) translateX(4px);
  }
}

@keyframes swayCenterLeftRight {
  0% {
    transform: translateX(-50%) rotate(-2.8deg);
  }
  100% {
    transform: translateX(-50%) rotate(2.8deg);
  }
}

@keyframes swayRightToLeft {
  0% {
    transform: rotate(3.5deg) translateX(4px);
  }
  100% {
    transform: rotate(-3.5deg) translateX(-4px);
  }
}

/* Candle Flames Layer */
.flames-group {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.candle-flame {
  position: absolute;
  width: 4.5%;
  aspect-ratio: 1 / 1.7;
  border-radius: 50% 50% 35% 35% / 60% 60% 40% 40%;
  background: radial-gradient(
    circle at 50% 75%,
    #ffffff 0%,
    #fff7a1 25%,
    #f59e0b 60%,
    rgba(220, 38, 38, 0.85) 100%
  );
  box-shadow:
    0 0 5px #fef08a,
    0 0 10px #f59e0b,
    0 -1px 4px rgba(255, 255, 255, 0.8);
  transform: translate(-50%, -50%);
  transform-origin: 50% 85%;
  animation: flameFlicker 1.8s infinite ease-in-out;
}

/* Candle Flame Coordinates */
.f-top { left: 50%; top: 35.5%; animation-delay: 0.1s; }
.f-mid-l { left: 29.3%; top: 38%; animation-delay: 0.4s; }
.f-mid-r { left: 70.7%; top: 38%; animation-delay: 0.9s; }
.f-inner-l { left: 34.5%; top: 44%; animation-delay: 0.2s; }
.f-inner-r { left: 65.5%; top: 44%; animation-delay: 0.7s; }
.f-outer-l { left: 19.5%; top: 46.5%; animation-delay: 1.1s; }
.f-outer-r { left: 80.5%; top: 46.5%; animation-delay: 0.5s; }
.f-edge-l { left: 14%; top: 50%; animation-delay: 0.8s; }
.f-edge-r { left: 86%; top: 50%; animation-delay: 0.3s; }

@keyframes flameFlicker {
  0%, 100% {
    transform: translate(-50%, -50%) scale(1) rotate(-1deg);
    opacity: 0.9;
  }
  25% {
    transform: translate(-50%, -52%) scale(1.15, 0.95) rotate(1.5deg);
    opacity: 1;
  }
  50% {
    transform: translate(-50%, -49%) scale(0.92, 1.1) rotate(-2deg);
    opacity: 0.82;
  }
  75% {
    transform: translate(-50%, -51%) scale(1.08, 1.02) rotate(1deg);
    opacity: 0.96;
  }
}

/* 4. Curtain Overlay Layer: Displays at wide shot, fades out on zoom, and fades back in after zoom out */
.curtain-overlay {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 20;
  pointer-events: none;
  transform-origin: center center;
  animation: curtainLoopFade 32s infinite;
  will-change: transform, opacity;
}

.curtain-overlay-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

@keyframes curtainLoopFade {
  0% {
    opacity: 1;
    transform: scale(1);
    animation-timing-function: ease-in-out;
  }
  2% {
    opacity: 1;
    transform: scale(1);
    animation-timing-function: cubic-bezier(0.35, 0, 0.25, 1);
  }
  11% {
    opacity: 0;
    transform: scale(1.15);
    animation-timing-function: ease-in-out;
  }
  76% {
    opacity: 0;
    transform: scale(1.1);
    animation-timing-function: cubic-bezier(0.25, 1, 0.35, 1);
  }
  87% {
    opacity: 1;
    transform: scale(1);
    animation-timing-function: ease-in-out;
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

/* 5. Edge Purple Rose Bouquets (Animate in when zoom nears the end) */
.zoom-edge-bouquet {
  position: absolute;
  bottom: 20%;
  width: 34%;
  z-index: 15;
  pointer-events: none;
  filter: drop-shadow(0 8px 18px rgba(0, 0, 0, 0.85));
}

.bouquet-float {
  width: 100%;
  animation: bouquetFloatUpDown 3.2s ease-in-out infinite alternate;
  will-change: transform;
}

.float-left {
  animation-delay: 0s;
}

.float-right {
  animation-delay: 0.6s;
}

@keyframes bouquetFloatUpDown {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-22px);
  }
}

.zoom-edge-bouquet img {
  width: 100%;
  height: auto;
  display: block;
}

.bouquet-left {
  left: -20%;
  animation: bouquetLeftAnim 32s infinite;
  transform-origin: left bottom;
  will-change: transform, opacity;
}

.bouquet-right {
  right: -20%;
  animation: bouquetRightAnim 32s infinite;
  transform-origin: right bottom;
  will-change: transform, opacity;
}

.bouquet-right img {
  transform: scaleX(-1);
}

@keyframes bouquetLeftAnim {
  0%, 20% {
    opacity: 0;
    transform: translateX(-120%) translateY(30px) rotate(-15deg) scale(0.7);
    animation-timing-function: cubic-bezier(0.34, 1.3, 0.64, 1);
  }
  33.8% {
    opacity: 1;
    transform: translateX(0) translateY(0) rotate(0deg) scale(1);
    animation-timing-function: ease-in-out;
  }
  50% {
    opacity: 1;
    transform: translateX(3px) translateY(-6px) rotate(2deg) scale(1.04);
    animation-timing-function: ease-in-out;
  }
  56.2% {
    opacity: 1;
    transform: translateX(0) translateY(0) rotate(0deg) scale(1);
    animation-timing-function: cubic-bezier(0.25, 1, 0.5, 1);
  }
  68%, 100% {
    opacity: 0;
    transform: translateX(-120%) translateY(30px) rotate(-15deg) scale(0.7);
  }
}

@keyframes bouquetRightAnim {
  0%, 20% {
    opacity: 0;
    transform: translateX(120%) translateY(30px) rotate(15deg) scale(0.7);
    animation-timing-function: cubic-bezier(0.34, 1.3, 0.64, 1);
  }
  33.8% {
    opacity: 1;
    transform: translateX(0) translateY(0) rotate(0deg) scale(1);
    animation-timing-function: ease-in-out;
  }
  50% {
    opacity: 1;
    transform: translateX(-3px) translateY(-6px) rotate(-2deg) scale(1.04);
    animation-timing-function: ease-in-out;
  }
  56.2% {
    opacity: 1;
    transform: translateX(0) translateY(0) rotate(0deg) scale(1);
    animation-timing-function: cubic-bezier(0.25, 1, 0.5, 1);
  }
  68%, 100% {
    opacity: 0;
    transform: translateX(120%) translateY(30px) rotate(15deg) scale(0.7);
  }
}

/* Smartphone Media Query strictly following HomePage.css */
@media (max-width: 480px) {
  .video-preview-container {
    padding: 12px;
    margin: 0;
    width: 100vw;
    height: 100dvh;
    box-sizing: border-box;
    background: linear-gradient(135deg, #c59828 0%, #e0bc66 35%, #f5dc94 50%, #c59828 70%, #a8791c 100%);
  }

  .preview-viewport {
    width: min(calc(100vw - 24px), calc((100dvh - 24px) * 9 / 16));
    max-width: 440px;
    height: auto;
    aspect-ratio: 9 / 16;
    border-radius: 24px;
    box-shadow: 0 10px 30px rgba(50, 35, 5, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.6);
    margin: 0 auto;
  }
}
</style>
