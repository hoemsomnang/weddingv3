<template>
  <div class="home-container">
    <div
      class="envelope-scene"
      :class="{ 'is-open': isOpen }"
      @click="toggleEnvelope"
    >
      <!-- 1. Envelope Back Wall with Warm Golden Radiance -->
      <div class="envelope-back">
        <div class="inner-glow"></div>
      </div>

      <!-- 2. Lower Envelope Body / Pocket -->
      <div class="envelope-pocket">
        <img src="/envelope-pocket.png" alt="Envelope Pocket" />
      </div>

      <!-- 3. Top Folding Scalloped Flap (3D Hinge) -->
      <div class="envelope-flap-wrapper">
        <div class="flap-front">
          <img src="/envelope-flap.png" alt="Scalloped Flap" />
        </div>
        <div class="flap-back"></div>

        <!-- Gold Seal Emblem on Flap Tip -->
        <div class="gold-seal" :class="{ 'seal-hidden': isOpen }">
          <img src="/gold-seal-sr.png" alt="Gold Seal SR" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isOpen = ref(false)

const toggleEnvelope = () => {
  isOpen.value = !isOpen.value
}
</script>

<style scoped>
/* Fullscreen Canvas */
.home-container {
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #141311;
  padding: 16px;
  box-sizing: border-box;
  overflow: hidden;
  user-select: none;
}

/* 3D Scene Viewport */
.envelope-scene {
  perspective: 1400px;
  width: 100%;
  max-width: 410px;
  aspect-ratio: 9 / 16;
  position: relative;
  cursor: pointer;
  transform-style: preserve-3d;
  border-radius: 20px;
  transform-origin: center center;
  transition: transform 1.2s cubic-bezier(0.25, 1, 0.35, 1);
}

/* 1. Envelope Back Wall */
.envelope-back {
  position: absolute;
  inset: 0;
  background: #f4f2ec;
  border-radius: 20px;
  box-shadow:
    0 25px 65px rgba(0, 0, 0, 0.75),
    0 0 0 1px rgba(255, 255, 255, 0.08);
  overflow: hidden;
  z-index: 1;
}

/* Warm Golden Glow Inside Chamber */
.inner-glow {
  position: absolute;
  top: 32%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 320px;
  height: 320px;
  background: radial-gradient(
    circle,
    rgba(253, 224, 138, 0.85) 0%,
    rgba(202, 160, 68, 0.35) 45%,
    transparent 75%
  );
  opacity: 0;
  transition: opacity 0.8s ease 0.25s;
  pointer-events: none;
  z-index: 2;
}

/* 2. Lower Envelope Body */
.envelope-pocket {
  position: absolute;
  inset: 0;
  z-index: 5;
  pointer-events: none;
  border-radius: 20px;
  overflow: hidden;
}

.envelope-pocket img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* 3. Top Folding Scalloped Flap (3D Hinge) */
.envelope-flap-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 52%;
  transform-origin: top center;
  transform-style: preserve-3d;
  transition: transform 1.15s cubic-bezier(0.35, 0, 0.2, 1);
  z-index: 10;
}

.flap-front {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  overflow: hidden;
  filter: drop-shadow(0 14px 18px rgba(45, 35, 22, 0.42));
  transition: filter 1.1s ease;
}

.flap-front img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  display: block;
}

.flap-back {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, #dfd8c8 0%, #eee8db 60%, #fff7e4 100%);
  transform: rotateY(180deg) rotateZ(180deg);
  backface-visibility: hidden;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  border-bottom: 2px solid #caa452;
  box-shadow: inset 0 -15px 30px rgba(184, 142, 48, 0.25);
}

/* Center Gold Seal Emblem */
.gold-seal {
  position: absolute;
  bottom: 4%;
  left: 50%;
  transform: translateX(-50%);
  width: 98px;
  height: 98px;
  z-index: 15;
  transition: transform 0.35s ease, opacity 0.4s ease;
  animation: seal-pulse 3s infinite ease-in-out;
}

.gold-seal img {
  width: 100%;
  height: 100%;
  display: block;
  filter: drop-shadow(0 6px 12px rgba(60, 42, 10, 0.45));
}

.gold-seal.seal-hidden {
  opacity: 0;
  pointer-events: none;
}

@keyframes seal-pulse {
  0%, 100% {
    transform: translateX(-50%) scale(1);
  }
  50% {
    transform: translateX(-50%) scale(1.06);
  }
}

/* ------------------------------------------------------------- */
/* ANIMATE OPEN & ZOOM IN (ACTIVE STATE)                         */
/* ------------------------------------------------------------- */
/* When clicked: the entire envelope ZOOMS IN */
.envelope-scene.is-open {
  transform: scale(1.22);
}

/* Flap folds 178 degrees backward */
.envelope-scene.is-open .envelope-flap-wrapper {
  transform: rotateX(178deg);
  z-index: 2;
}

.envelope-scene.is-open .flap-front {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.15));
}

/* Chamber golden radiance illuminates */
.envelope-scene.is-open .inner-glow {
  opacity: 1;
}

/* Mobile full-height optimization */
@media (max-width: 440px) {
  .home-container {
    padding: 0;
  }
  .envelope-scene {
    max-width: 100vw;
    height: 100dvh;
    border-radius: 0;
  }
  .envelope-back {
    border-radius: 0;
  }
  .flap-front,
  .flap-back {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
  .envelope-pocket {
    border-radius: 0;
  }
  .envelope-scene.is-open {
    transform: scale(1.15);
  }
}
</style>
