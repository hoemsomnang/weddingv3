<template>
  <div
    class="curtain-stage-container"
    :class="{ 'is-open': isOpen }"
    @click="$emit('toggle')"
  >
    <!-- 1. Background Palace Ballroom Layer -->
    <div class="ballroom-layer">
      <img
        :src="ballroomImg"
        alt="Grand Ballroom Hall"
        class="ballroom-img"
      />
    </div>

    <!-- 2. Ambient Radiant Chandelier Shimmer -->
    <div class="ambient-glow"></div>

    <!-- 3. Flickering Candlelights along Staircase -->
    <div class="candle-cluster">
      <div v-for="i in 10" :key="i" class="candle-spark"></div>
    </div>

    <!-- 4. Floating 3D SVG Butterflies -->
    <div class="butterflies-container">
      <div class="butterfly-agent butterfly-1">
        <img :src="butterflySvg" alt="Animated Butterfly" />
      </div>
      <div class="butterfly-agent butterfly-2">
        <img :src="butterflySvg" alt="Animated Butterfly" />
      </div>
      <img :src="sparkleSvg" class="sparkle-particle" alt="sparkle" />
      <img :src="sparkleSvg" class="sparkle-particle" alt="sparkle" />
      <img :src="sparkleSvg" class="sparkle-particle" alt="sparkle" />
    </div>

    <!-- 5. Split 2-Panel Stage Curtains (pic2-suitable-flush.jpg) -->
    <div class="curtains-wrapper">
      <!-- Left Curtain: Pulls diagonally up & outward in curved catenary arch -->
      <div class="curtain-panel-left">
        <img :src="curtainLeftImg" alt="Left Royal Curtain" />
        <div class="gather-shadow-overlay"></div>
      </div>

      <!-- Right Curtain: Pulls diagonally up & outward in curved catenary arch -->
      <div class="curtain-panel-right">
        <img :src="curtainRightImg" alt="Right Royal Curtain" />
        <div class="gather-shadow-overlay"></div>
      </div>
    </div>

    <!-- 6. Permanent Top Scalloped Valance (Lifts straight up out of frame) -->
    <div class="proscenium-valance">
      <img :src="valanceImg" alt="Top Scalloped Valance" />
    </div>

    <!-- Optional Slot for Invitation Card or Content -->
    <slot :isOpen="isOpen"></slot>
  </div>
</template>

<script setup>
import { ref, watch, onBeforeUnmount } from 'vue'
import ballroomImg from '@/assets/purple-ballroom-royal.jpg'
import curtainLeftImg from '@/assets/curtains/curtain-left.webp'
import curtainRightImg from '@/assets/curtains/curtain-right.webp'
import valanceImg from '@/assets/curtains/curtain-valance.webp'
import butterflySvg from '@/assets/svg/butterfly.svg'
import sparkleSvg from '@/assets/svg/sparkle.svg'

const props = defineProps({
  isOpen: {
    type: Boolean,
    default: false
  },
  autoLoop: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['toggle', 'update:isOpen'])

let loopInterval = null

watch(() => props.autoLoop, (looping) => {
  if (looping) {
    const runCycle = () => {
      emit('update:isOpen', false)
      setTimeout(() => {
        emit('update:isOpen', true)
      }, 2000)
      setTimeout(() => {
        emit('update:isOpen', false)
      }, 15500)
    }
    runCycle()
    loopInterval = setInterval(runCycle, 20000)
  } else {
    clearInterval(loopInterval)
    loopInterval = null
  }
}, { immediate: true })

onBeforeUnmount(() => {
  clearInterval(loopInterval)
})
</script>

<style scoped>
.curtain-stage-container {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #0d0414;
  user-select: none;
  perspective: 1200px;
}

/* 1. Background Ballroom */
.ballroom-layer {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  overflow: hidden;
}

.ballroom-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transform-origin: center 45%;
  transition: transform 1.5s cubic-bezier(0.2, 0.8, 0.25, 1);
}

.curtain-stage-container.is-open .ballroom-img {
  animation: kenBurnsZoom 16s infinite alternate ease-in-out;
}

@keyframes kenBurnsZoom {
  0% { transform: scale(1.0) translateY(0); }
  100% { transform: scale(1.06) translateY(-10px); }
}

/* Ambient Warm Glow */
.ambient-glow {
  position: absolute;
  top: 15%;
  left: 50%;
  transform: translateX(-50%);
  width: 320px;
  height: 320px;
  background: radial-gradient(circle, rgba(254, 240, 138, 0.22) 0%, rgba(168, 85, 247, 0.15) 50%, transparent 75%);
  pointer-events: none;
  z-index: 2;
  opacity: 0;
  transition: opacity 1.5s ease 0.5s;
}

.curtain-stage-container.is-open .ambient-glow {
  opacity: 1;
  animation: warmPulse 4s infinite alternate ease-in-out;
}

@keyframes warmPulse {
  0% { opacity: 0.5; transform: translateX(-50%) scale(0.95); }
  100% { opacity: 0.9; transform: translateX(-50%) scale(1.1); }
}

/* 2. Flickering Candlelights */
.candle-cluster {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 3;
  opacity: 0;
  transition: opacity 1.2s ease 0.6s;
}

.curtain-stage-container.is-open .candle-cluster {
  opacity: 1;
}

.candle-spark {
  position: absolute;
  width: 4.5px;
  height: 4.5px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 0 0 6px #ffe082, 0 0 14px #ffb300, 0 0 22px rgba(255, 179, 0, 0.65);
  animation: candleFlicker 2s infinite ease-in-out;
}

.candle-spark:nth-child(1) { left: 24%; top: 58%; animation-delay: 0.1s; }
.candle-spark:nth-child(2) { left: 28%; top: 62%; animation-delay: 0.7s; }
.candle-spark:nth-child(3) { left: 32%; top: 66%; animation-delay: 0.3s; }
.candle-spark:nth-child(4) { left: 35%; top: 70%; animation-delay: 1.1s; }
.candle-spark:nth-child(5) { left: 20%; top: 72%; animation-delay: 0.5s; }
.candle-spark:nth-child(6) { right: 24%; top: 58%; animation-delay: 0.4s; }
.candle-spark:nth-child(7) { right: 28%; top: 62%; animation-delay: 0.9s; }
.candle-spark:nth-child(8) { right: 32%; top: 66%; animation-delay: 0.2s; }
.candle-spark:nth-child(9) { right: 35%; top: 70%; animation-delay: 0.8s; }
.candle-spark:nth-child(10) { right: 20%; top: 72%; animation-delay: 1.4s; }

@keyframes candleFlicker {
  0%, 100% { opacity: 0.7; transform: scale(0.9); }
  50% { opacity: 1; transform: scale(1.35); }
}

/* 3. 3D SVG Butterflies */
.butterflies-container {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 4;
  overflow: hidden;
  opacity: 0;
  transition: opacity 1.5s ease 0.6s;
}

.curtain-stage-container.is-open .butterflies-container {
  opacity: 1;
}

.butterfly-agent {
  position: absolute;
  width: 44px;
  height: 38px;
}

.butterfly-agent img {
  width: 100%;
  height: 100%;
}

.butterfly-1 {
  bottom: 27%;
  right: 28%;
  animation: flightPath1 8s infinite alternate ease-in-out;
}

.butterfly-2 {
  top: 34%;
  left: 28%;
  animation: flightPath2 9.5s infinite alternate ease-in-out 1s;
}

@keyframes flightPath1 {
  0% { transform: translate(0, 0) rotate(-15deg) scale(0.85); }
  50% { transform: translate(-30px, -45px) rotate(8deg) scale(0.95); }
  100% { transform: translate(20px, -75px) rotate(-10deg) scale(0.8); }
}

@keyframes flightPath2 {
  0% { transform: translate(0, 0) rotate(18deg) scale(0.68); }
  50% { transform: translate(40px, 20px) rotate(-8deg) scale(0.78); }
  100% { transform: translate(10px, -30px) rotate(12deg) scale(0.62); }
}

.sparkle-particle {
  position: absolute;
  width: 14px;
  height: 14px;
  pointer-events: none;
  opacity: 0;
  animation: sparkleFloat 5s infinite ease-in;
}

.sparkle-particle:nth-child(1) { left: 45%; top: 40%; animation-delay: 0.5s; }
.sparkle-particle:nth-child(2) { left: 35%; top: 60%; animation-delay: 2s; }
.sparkle-particle:nth-child(3) { left: 62%; top: 50%; animation-delay: 3.2s; }

@keyframes sparkleFloat {
  0% { opacity: 0; transform: translateY(20px) scale(0.5); }
  40% { opacity: 0.85; transform: translateY(-15px) scale(1.1); }
  80% { opacity: 0.5; transform: translateY(-40px) scale(0.8); }
  100% { opacity: 0.9; transform: translateY(-60px) scale(0.3); }
}

/* 4. Split 2-Panel Stage Curtains (pic2-suitable-flush.jpg) */
.curtains-wrapper {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 10;
  pointer-events: none;
  transform-style: preserve-3d;
}

.curtain-panel-left {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 51.5%;
  height: 100%;
  overflow: hidden;
  transform-origin: 0% 0%;
  clip-path: polygon(0% 0%, 100% 0%, 100% 40%, 100% 100%, 0% 100%);
  transform: translate3d(0, 0, 0) scale(1) rotate(0deg);
  transition: clip-path 2.4s cubic-bezier(0.25, 1, 0.35, 1),
              transform 2.4s cubic-bezier(0.25, 1, 0.35, 1),
              filter 2.4s ease;
  will-change: transform, clip-path, filter;
  filter: drop-shadow(6px 0 15px rgba(0, 0, 0, 0.7));
}

.curtain-panel-left img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: left top;
}

.curtain-panel-right {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 51.5%;
  height: 100%;
  overflow: hidden;
  transform-origin: 100% 0%;
  clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 40%);
  transform: translate3d(0, 0, 0) scale(1) rotate(0deg);
  transition: clip-path 2.4s cubic-bezier(0.25, 1, 0.35, 1),
              transform 2.4s cubic-bezier(0.25, 1, 0.35, 1),
              filter 2.4s ease;
  will-change: transform, clip-path, filter;
  filter: drop-shadow(-6px 0 15px rgba(0, 0, 0, 0.7));
}

.curtain-panel-right img {
  position: absolute;
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: right top;
}

.gather-shadow-overlay {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    90deg,
    rgba(0, 0, 0, 0.55) 0px,
    transparent 15px,
    rgba(0, 0, 0, 0.6) 30px
  );
  opacity: 0;
  transition: opacity 2.0s ease;
  pointer-events: none;
}

/* Opera / Tableau Drape Active State: Diagonal Sweep + Curved Arch (Exact preview-video.mp4 match) */
.curtain-stage-container.is-open .curtain-panel-left {
  clip-path: polygon(0% 0%, 65% 0%, 12% 45%, 4% 85%, 0% 100%);
  transform: translate3d(-30%, -8%, 0) scale(0.72, 0.92) skewY(-8deg);
  filter: drop-shadow(15px 0 25px rgba(0, 0, 0, 0.9));
}

.curtain-stage-container.is-open .curtain-panel-right {
  clip-path: polygon(35% 0%, 100% 0%, 100% 100%, 96% 85%, 88% 45%);
  transform: translate3d(30%, -8%, 0) scale(0.72, 0.92) skewY(8deg);
  filter: drop-shadow(-15px 0 25px rgba(0, 0, 0, 0.9));
}

.curtain-stage-container.is-open .gather-shadow-overlay {
  opacity: 0.75;
}

/* 5. Permanent Top Scalloped Valance (Lifts vertically upward like video) */
.proscenium-valance {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 26.5%;
  z-index: 20;
  pointer-events: none;
  transform: translateY(0);
  transition: transform 2.0s cubic-bezier(0.25, 1, 0.5, 1),
              opacity 1.8s ease;
  filter: drop-shadow(0 14px 22px rgba(10, 2, 16, 0.9));
}

.curtain-stage-container.is-open .proscenium-valance {
  transform: translateY(-112%);
  opacity: 0;
}

.proscenium-valance img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
}
</style>
