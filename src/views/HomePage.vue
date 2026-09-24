<template>
  <div class="home-container">
    <!-- Ambient Golden Starlight / Sparkles -->
    <div class="ambient-sparks">
      <div v-for="n in 14" :key="n" :class="`spark spark-${n}`"></div>
    </div>

    <!-- 3D Envelope Viewport -->
    <div
      class="envelope-scene"
      :class="{ 'is-open': isOpen }"
      @click="toggleEnvelope"
    >
      <!-- 1. Envelope Back Wall with Warm Chamber Radiance -->
      <div class="envelope-back">
        <div class="inner-glow"></div>
        <div class="chamber-radial"></div>
      </div>

      <!-- 2. Inner Luxury Invitation Card (Slides Up on Open) -->
      <div class="inner-card">
        <div class="card-border-outer">
          <div class="card-border-inner">
            <!-- Monogram Crest -->
            <div class="card-crest">
              <span class="crest-letters">SR</span>
            </div>

            <!-- Khmer Main Title -->
            <h1 class="card-khmer-title">សិរីមង្គលអាពាហ៍ពិពាហ៍</h1>
            <p class="card-english-subtitle">WEDDING INVITATION</p>

            <div class="card-divider-line">
              <span class="line-wing left"></span>
              <span class="center-gem">✦</span>
              <span class="line-wing right"></span>
            </div>

            <!-- Couple Names -->
            <div class="card-couple">
              <span class="groom-name">Sonton</span>
              <span class="ampersand">&amp;</span>
              <span class="bride-name">Santini</span>
            </div>

            <p class="card-khmer-greeting">
              សូមគោរពអញ្ជើញ ឯកឧត្តម លោកជំទាវ លោក លោកស្រី អ្នកនាងកញ្ញា
            </p>

            <!-- Wedding Date Plaque -->
            <div class="card-date-plaque">
              <span class="date-month">FEBRUARY</span>
              <span class="date-day">14</span>
              <span class="date-year">2026</span>
            </div>

            <p class="card-venue">PHNOM PENH, CAMBODIA</p>

            <!-- Call to Action Button to Second Page -->
            <button
              class="card-action-btn"
              @click.stop="goToInvitation"
              title="View full wedding program and details"
            >
              <span>ចូលទស្សនាសំបុត្រ • View Invitation</span>
              <svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- 3. Front Envelope Pocket (Covers Card Lower Body) -->
      <div class="envelope-pocket">
        <img :src="pocketImg" alt="Envelope Pocket" />
      </div>

      <!-- 4. Top Folding Scalloped Flap (3D Hinge) -->
      <div class="envelope-flap-wrapper">
        <!-- Front: Pointing Down with Central Gold Monogram & Intact Scalloped Lace -->
        <div class="flap-front">
          <img :src="flapImg" alt="Luxury Scalloped Lace Flap" />
        </div>
        <!-- Back: Pointing Up with Golden Lining when Opened -->
        <div class="flap-back">
          <img :src="flapBackImg" alt="Opened Flap Lining" />
        </div>
      </div>

      <!-- 5. Interactive Tap Hint -->
      <div class="tap-hint" :class="{ 'hint-hidden': isOpen }">
        <span class="hint-khmer">សូមចុចដើម្បីបើកសំបុត្រ</span>
        <span class="hint-en">Tap Envelope to Open</span>
        <div class="hint-pulse-dot"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import flapImg from '@/assets/envelope/envelope-flap.png'
import flapBackImg from '@/assets/envelope/envelope-flap-back.png'
import pocketImg from '@/assets/envelope/envelope-pocket.png'

const router = useRouter()
const isOpen = ref(false)

const toggleEnvelope = () => {
  isOpen.value = !isOpen.value
}

const goToInvitation = () => {
  router.push('/second')
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
  background: radial-gradient(circle at 50% 40%, #201e1a 0%, #11100e 100%);
  padding: 24px 16px;
  box-sizing: border-box;
  overflow: hidden;
  user-select: none;
  position: relative;
}

/* Ambient Floating Particles */
.ambient-sparks {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.spark {
  position: absolute;
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: #fde68a;
  box-shadow: 0 0 8px #fbbf24;
  opacity: 0.3;
  animation: float-spark 6s infinite ease-in-out;
}

.spark-1 { top: 15%; left: 18%; animation-delay: 0s; animation-duration: 7s; }
.spark-2 { top: 30%; left: 82%; animation-delay: 1.5s; animation-duration: 5.5s; }
.spark-3 { top: 65%; left: 12%; animation-delay: 2.2s; animation-duration: 6.2s; }
.spark-4 { top: 80%; left: 75%; animation-delay: 3.1s; animation-duration: 7.8s; }
.spark-5 { top: 22%; left: 45%; animation-delay: 0.8s; animation-duration: 6.7s; }
.spark-6 { top: 50%; left: 88%; animation-delay: 2.8s; animation-duration: 5.8s; }
.spark-7 { top: 75%; left: 32%; animation-delay: 4s; animation-duration: 7.2s; }
.spark-8 { top: 10%; left: 70%; animation-delay: 1.2s; animation-duration: 8.5s; }
.spark-9 { top: 40%; left: 8%; animation-delay: 3.5s; animation-duration: 6s; }
.spark-10 { top: 85%; left: 55%; animation-delay: 2s; animation-duration: 7s; }
.spark-11 { top: 28%; left: 25%; animation-delay: 1.8s; animation-duration: 6.4s; }
.spark-12 { top: 60%; left: 68%; animation-delay: 3.8s; animation-duration: 5.2s; }
.spark-13 { top: 92%; left: 20%; animation-delay: 2.4s; animation-duration: 7.5s; }
.spark-14 { top: 5%; left: 38%; animation-delay: 0.4s; animation-duration: 8s; }

@keyframes float-spark {
  0%, 100% {
    transform: translateY(0) scale(0.8);
    opacity: 0.2;
  }
  50% {
    transform: translateY(-24px) scale(1.3);
    opacity: 0.75;
  }
}

/* 3D Scene Container */
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
  transition: transform 1.2s cubic-bezier(0.22, 1, 0.36, 1);
}

/* 1. Envelope Back Wall */
.envelope-back {
  position: absolute;
  inset: 0;
  background: #f5f3ec;
  border-radius: 20px;
  box-shadow:
    0 30px 70px rgba(0, 0, 0, 0.78),
    0 0 0 1px rgba(255, 255, 255, 0.1);
  overflow: hidden;
  z-index: 1;
}

/* Golden Inner Radiance when opened */
.inner-glow {
  position: absolute;
  top: 35%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 340px;
  height: 340px;
  background: radial-gradient(
    circle,
    rgba(253, 230, 138, 0.95) 0%,
    rgba(217, 169, 74, 0.45) 45%,
    transparent 75%
  );
  opacity: 0;
  transition: opacity 0.8s ease 0.2s;
  pointer-events: none;
  z-index: 2;
}

.chamber-radial {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, #ede7d8 0%, #f7f5ed 100%);
  opacity: 0.85;
}

/* ------------------------------------------------------------- */
/* 2. INNER INVITATION CARD                                      */
/* ------------------------------------------------------------- */
.inner-card {
  position: absolute;
  top: 14px;
  left: 14px;
  right: 14px;
  bottom: 14px;
  background: #fffdfa;
  border-radius: 14px;
  z-index: 4;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.22);
  transform: translateY(40px) scale(0.92);
  opacity: 0;
  transform-origin: center center;
  transition: transform 1.25s cubic-bezier(0.2, 0.9, 0.25, 1), opacity 0.7s ease 0.15s;
  pointer-events: none;
  overflow: hidden;
}

.card-border-outer {
  height: 100%;
  border: 1px solid #dfc488;
  border-radius: 12px;
  padding: 5px;
  box-sizing: border-box;
}

.card-border-inner {
  height: 100%;
  border: 1px solid rgba(212, 175, 98, 0.4);
  border-radius: 8px;
  padding: 20px 16px 28px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  text-align: center;
  background: radial-gradient(circle at 50% 25%, #fffdfa 0%, #faf6eb 100%);
}

.card-crest {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: 1.5px solid #c9a34e;
  background: rgba(254, 243, 199, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(184, 134, 40, 0.2);
}

.crest-letters {
  font-family: 'Cinzel', serif;
  font-weight: 700;
  font-size: 18px;
  letter-spacing: 2px;
  color: #997327;
}

.card-khmer-title {
  font-family: 'Moul', cursive;
  font-size: 14.5px;
  line-height: 1.5;
  color: #8f6c24;
  margin: 0;
  font-weight: 400;
  text-shadow: 0 1px 1px rgba(255, 255, 255, 0.9);
}

.card-english-subtitle {
  font-family: 'Cinzel', serif;
  font-size: 8.5px;
  letter-spacing: 3.5px;
  color: #9c8e78;
  margin: 0;
  text-transform: uppercase;
}

.card-divider-line {
  display: flex;
  align-items: center;
  width: 70%;
  gap: 8px;
}

.line-wing {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #caa456, transparent);
}

.center-gem {
  color: #c9a34e;
  font-size: 10px;
}

.card-couple {
  display: flex;
  flex-direction: column;
  align-items: center;
  line-height: 1.05;
}

.groom-name,
.bride-name {
  font-family: 'Great Vibes', cursive;
  font-size: 36px;
  color: #8c671b;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.85);
}

.ampersand {
  font-family: 'Cinzel', serif;
  font-size: 15px;
  color: #c4a04d;
  margin: -4px 0;
}

.card-khmer-greeting {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 10.5px;
  line-height: 1.5;
  color: #6a6152;
  margin: 0;
  max-width: 92%;
}

.card-date-plaque {
  border-top: 1px solid #e5d2a7;
  border-bottom: 1px solid #e5d2a7;
  padding: 4px 16px;
  display: flex;
  align-items: baseline;
  gap: 8px;
  background: rgba(255, 255, 255, 0.6);
}

.date-month {
  font-family: 'Cinzel', serif;
  font-size: 10.5px;
  letter-spacing: 2px;
  color: #8a7b66;
}

.date-day {
  font-family: 'Cinzel', serif;
  font-size: 19px;
  font-weight: 700;
  color: #8a6417;
}

.date-year {
  font-family: 'Cinzel', serif;
  font-size: 10.5px;
  letter-spacing: 2px;
  color: #8a7b66;
}

.card-location {
  font-family: 'Montserrat', sans-serif;
  font-size: 8.5px;
  letter-spacing: 2px;
  color: #9c8e78;
  margin: 0;
}

.card-action-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 9px 18px;
  border-radius: 25px;
  background: linear-gradient(135deg, #d3ab55 0%, #aa802e 100%);
  color: #fffdf8;
  border: none;
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(162, 120, 40, 0.38);
  transition: all 0.3s ease;
  pointer-events: auto;
}

.card-action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 7px 20px rgba(162, 120, 40, 0.5);
  background: linear-gradient(135deg, #dfb963 0%, #b88d37 100%);
}

.btn-arrow {
  transition: transform 0.25s ease;
}

.card-action-btn:hover .btn-arrow {
  transform: translateX(3px);
}

/* ------------------------------------------------------------- */
/* 3. FRONT ENVELOPE POCKET                                      */
/* ------------------------------------------------------------- */
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

/* ------------------------------------------------------------- */
/* 4. TOP FOLDING SCALLOPED FLAP (3D HINGE)                      */
/* ------------------------------------------------------------- */
.envelope-flap-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 48%;
  transform-origin: top center;
  transform-style: preserve-3d;
  transition: transform 1.25s cubic-bezier(0.35, 0, 0.2, 1);
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
  filter: drop-shadow(0 12px 20px rgba(45, 33, 16, 0.45));
  transition: filter 1.2s ease;
}

.flap-front img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  display: block;
}

.flap-back {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  transform: rotateY(180deg) rotateZ(180deg);
  backface-visibility: hidden;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  filter: drop-shadow(0 6px 14px rgba(0, 0, 0, 0.25));
}

.flap-back img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: bottom center;
  display: block;
}

/* ------------------------------------------------------------- */
/* 5. INTERACTIVE TAP HINT                                       */
/* ------------------------------------------------------------- */
.tap-hint {
  position: absolute;
  bottom: -46px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(32, 30, 26, 0.8);
  border: 1px solid rgba(202, 164, 82, 0.35);
  border-radius: 20px;
  padding: 6px 16px;
  backdrop-filter: blur(8px);
  transition: opacity 0.4s ease, transform 0.4s ease;
  pointer-events: none;
  white-space: nowrap;
}

.hint-khmer {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11.5px;
  color: #fde68a;
}

.hint-en {
  font-family: 'Montserrat', sans-serif;
  font-size: 10.5px;
  color: #d1c7b8;
  letter-spacing: 0.5px;
}

.hint-pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #caa452;
  box-shadow: 0 0 6px #fbbf24;
  animation: pulse-dot 1.8s infinite ease-in-out;
}

@keyframes pulse-dot {
  0%, 100% { transform: scale(1); opacity: 0.6; }
  50% { transform: scale(1.6); opacity: 1; }
}

.tap-hint.hint-hidden {
  opacity: 0;
  transform: translate(-50%, 10px);
}

/* ------------------------------------------------------------- */
/* ANIMATE OPEN (ACTIVE STATE)                                   */
/* ------------------------------------------------------------- */
.envelope-scene.is-open {
  transform: scale(1.08) translateY(60px);
}

/* Flap folds 178 degrees upward */
.envelope-scene.is-open .envelope-flap-wrapper {
  transform: rotateX(178deg);
  z-index: 2;
}

.envelope-scene.is-open .flap-front {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.15));
}

/* Inner gold radiance shines */
.envelope-scene.is-open .inner-glow {
  opacity: 1;
}

/* Inner invitation card slides up, comes to front & reveals */
.envelope-scene.is-open .inner-card {
  transform: translateY(-20px) translateZ(50px) scale(1.03);
  z-index: 8;
  opacity: 1;
  pointer-events: auto;
  box-shadow: 0 30px 65px rgba(0, 0, 0, 0.55);
}

/* Responsive optimization */
@media (max-width: 440px) {
  .home-container {
    padding: 12px;
  }
  .envelope-scene.is-open {
    transform: scale(1.04) translateY(65px);
  }
  .envelope-scene.is-open .inner-card {
    transform: translateY(-170px) scale(0.98);
  }
}
</style>
