<template>
  <div class="main-page">
    <div class="main-screen">
      <!-- 1. Fullscreen Base Backdrop -->
      <img
        :src="backdropImg"
        alt="Sage Wedding Backdrop"
        class="main-bg-img"
      />

      <!-- 2. Tiered Crystal Chandelier at Top Center -->
      <div class="chandelier-layer">
        <img
          :src="tieredChandelierImg"
          alt="Tiered Crystal Chandelier"
          class="layer-img chandelier-img"
        />
      </div>

      <!-- 3. Left Hanging Pendant Lamps (3 green, 2 warm) -->
      <div class="pendant-lamp lamp-left-green-1">
        <img
          :src="pendantGreenImg"
          alt="Green Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-left-warm-1">
        <img
          :src="pendantWarmImg"
          alt="Warm Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-left-green-2">
        <img
          :src="pendantGreenImg"
          alt="Green Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-left-warm-2">
        <img
          :src="pendantWarmImg"
          alt="Warm Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-left-green-3">
        <img
          :src="pendantGreenImg"
          alt="Green Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>

      <!-- 4. Right Hanging Pendant Lamps (3 green, 2 warm) -->
      <div class="pendant-lamp lamp-right-green-1">
        <img
          :src="pendantGreenImg"
          alt="Green Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-right-warm-1">
        <img
          :src="pendantWarmImg"
          alt="Warm Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-right-green-2">
        <img
          :src="pendantGreenImg"
          alt="Green Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-right-warm-2">
        <img
          :src="pendantWarmImg"
          alt="Warm Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>
      <div class="pendant-lamp lamp-right-green-3">
        <img
          :src="pendantGreenImg"
          alt="Green Pendant Lamp"
          class="layer-img"
        />
        <span class="lamp-flame"></span>
      </div>

      <!-- 5. Flying Butterflies Layer -->
      <div class="flying-butterflies-layer">
        <div class="butterfly-item b1">
          <div class="butterfly-flapper">
            <img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" />
          </div>
        </div>
        <div class="butterfly-item b2">
          <div class="butterfly-flapper">
            <img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" />
          </div>
        </div>
        <div class="butterfly-item b3">
          <div class="butterfly-flapper">
            <img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" />
          </div>
        </div>
        <div class="butterfly-item b4">
          <div class="butterfly-flapper">
            <img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" />
          </div>
        </div>
      </div>

      <!-- 6. Invitation Details Card -->
      <div class="invitation-overlay">
        <div class="invitation-card">
          <!-- Monogram Crest -->
          <div v-if="invitation.initials && invitation.initials.length" class="monogram-badge">
            <span class="monogram-char">{{ invitation.initials[0] }}</span>
            <span class="monogram-dot">✦</span>
            <span class="monogram-char">{{ invitation.initials[1] }}</span>
          </div>

          <!-- Page Heading: សិរីមង្គលអាពាហ៍ពិពាហ៍ -->
          <h1 class="invitation-heading">{{ invitation.pageTitle }}</h1>

          <!-- Parents Section -->
          <div class="parents-row">
            <div class="parents-group groom-parents">
              <div class="parent-entry">
                <span class="parent-role">{{ invitation.groomFather.role }}</span>
                <span class="parent-name">{{ invitation.groomFather.name }}</span>
              </div>
              <div class="parent-entry">
                <span class="parent-role">{{ invitation.groomMother.role }}</span>
                <span class="parent-name">{{ invitation.groomMother.name }}</span>
              </div>
            </div>
            <div class="parents-group bride-parents">
              <div class="parent-entry">
                <span class="parent-role">{{ invitation.brideFather.role }}</span>
                <span class="parent-name">{{ invitation.brideFather.name }}</span>
              </div>
              <div class="parent-entry">
                <span class="parent-role">{{ invitation.brideMother.role }}</span>
                <span class="parent-name">{{ invitation.brideMother.name }}</span>
              </div>
            </div>
          </div>

          <!-- Honor Invite Message -->
          <div class="honor-invite-section">
            <p class="honor-invite-title">{{ invitation.honorInviteText }}</p>
            <p
              v-for="(line, idx) in invitation.invitationLines"
              :key="idx"
              class="invitation-line"
            >
              {{ line }}
            </p>
          </div>

          <!-- Couple Section -->
          <div class="couple-section">
            <div class="couple-side groom-side">
              <span class="couple-role">{{ invitation.groomRole }}</span>
              <span class="couple-name">{{ invitation.groomName }}</span>
            </div>
            <div class="couple-ampersand">
              <img
                :src="monogramCrestImg"
                alt="Wedding Monogram Crest S&R"
                class="couple-crest-img"
              />
            </div>
            <div class="couple-side bride-side">
              <span class="couple-role">{{ invitation.brideRole }}</span>
              <span class="couple-name">{{ invitation.brideName }}</span>
            </div>
          </div>

          <!-- Wedding Date & Venue Section -->
          <div class="event-schedule-section">
            <p class="lunar-date">{{ invitation.lunarDate }}</p>
            <p class="solar-date">{{ invitation.solarDate }}</p>
            <div class="schedule-divider">
              <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
            </div>
            <p class="reception-time">{{ invitation.receptionTime }}</p>
          </div>
        </div>
      </div>


      <!-- Extra Flowers (Left and Right) -->
      <div class="extra-flower flower-5">
        <img :src="flower2Img" alt="Flower 2 Extra Left" class="roses-img" />
      </div>
      <div class="extra-flower flower-3">
        <img :src="flower2Img" alt="Flower 2 Left" class="roses-img" />
      </div>
      <div class="extra-flower flower-2">
        <img :src="flower2Img" alt="Flower 2 Right" class="roses-img" />
      </div>
      <div class="extra-flower flower-4">
        <img :src="flower2Img" alt="Flower 2 Extra Right" class="roses-img" />
      </div>
    </div>
  </div>
</template>

<script setup>
import backdropImg from '@/assets/sage-wedding-backdrop-symmetric.jpg'
import pendantGreenImg from '@/assets/items/pendant-lamp-green-transparent.png'
import pendantWarmImg from '@/assets/items/pendant-lamp-warm-transparent.png'
import tieredChandelierImg from '@/assets/items/tiered-crystal-chandelier-transparent.png'
import butterflyImg from '@/assets/items/wedding-butterfly.svg'
import monogramCrestImg from '@/assets/wedding_monogram_crest_sr_trans.webp'
import goldDividerImg from '@/assets/items/gold-wedding-divider.png'
import flower2Img from '@/assets/flower-2-transparent.png'
import invitation from '@/config/invitation.js'
</script>

<style scoped>
.main-page {
  width: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #caa044;
  padding: 12px;
  box-sizing: border-box;
  overflow: hidden;
  user-select: none;
  position: relative;
}

.main-screen {
  width: min(calc(100vw - 24px), calc((100dvh - 24px) * 9 / 16));
  max-width: 440px;
  aspect-ratio: 9 / 16;
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.25);
  z-index: 2;
}

.main-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

/* Layered Elements */
.layer-img {
  width: 100%;
  height: auto;
  display: block;
  pointer-events: none;
}

/* Tiered Crystal Chandelier */
.chandelier-layer {
  position: absolute;
  top: -15%;
  left: 50%;
  transform: translateX(-50%);
  width: 55%;
  z-index: 6;
  pointer-events: none;
  transform-origin: 50% 0%;
  will-change: transform;
  animation: swayChandelier 7.5s ease-in-out infinite alternate -2.5s;
}

.chandelier-img {
  filter: drop-shadow(0 6px 16px rgba(0, 0, 0, 0.45));
}

/* Pendant Lamps Common */
.pendant-lamp {
  position: absolute;
  z-index: 5;
  pointer-events: none;
  filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.35));
  transform-origin: 50% 0%;
  will-change: transform;
}

/* Thin cord extending to ceiling for staggered lamps */
.pendant-lamp::before {
  content: '';
  position: absolute;
  top: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 1px;
  height: 200px;
  background: linear-gradient(to bottom, rgba(160, 130, 60, 0.7), rgba(212, 175, 55, 0.9));
}

/* Anti-culling extension: prevents mobile browsers from hiding lamps positioned with negative top */
.pendant-lamp::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  width: 1px;
  height: 250px;
  background: transparent;
  pointer-events: none;
}

/* Left Lamps Arrangement (Matches sage-wedding-backdrop.with-lamps.jpg: 3 green, 2 warm) */
.lamp-left-warm-1 {
  top: -15.5%;
  left: 4.5%;
  width: 10.5%;
  z-index: 4;
  animation: swayLeftToRight 5.8s ease-in-out infinite alternate -1.4s;
}

.lamp-left-green-1 {
  top: -11.5%;
  left: 3.5%;
  width: 10.5%;
  z-index: 5;
  animation: swayRightToLeft 6.4s ease-in-out infinite alternate -3.2s;
}

.lamp-left-warm-2 {
  top: -7.0%;
  left: 14.0%;
  width: 10.5%;
  z-index: 4;
  animation: swayLeftToRight 7.1s ease-in-out infinite alternate -4.5s;
}

.lamp-left-green-2 {
  top: -3.5%;
  left: 8.5%;
  width: 10.5%;
  z-index: 6;
  animation: swayRightToLeft 5.6s ease-in-out infinite alternate -2.1s;
}

.lamp-left-green-3 {
  top: 0%;
  left: 1.8%;
  width: 10.5%;
  z-index: 7;
  animation: swayLeftToRight 6.8s ease-in-out infinite alternate -0.9s;
}

/* Right Lamps Arrangement (Matches sage-wedding-backdrop.with-lamps.jpg: 3 green, 2 warm) */
.lamp-right-warm-1 {
  top: -15.5%;
  right: 4.5%;
  width: 10.5%;
  z-index: 4;
  animation: swayRightToLeft 6.0s ease-in-out infinite alternate -2.7s;
}

.lamp-right-green-1 {
  top: -11.5%;
  right: 3.5%;
  width: 10.5%;
  z-index: 5;
  animation: swayLeftToRight 6.6s ease-in-out infinite alternate -4.0s;
}

.lamp-right-warm-2 {
  top: -7.0%;
  right: 14.0%;
  width: 10.5%;
  z-index: 4;
  animation: swayRightToLeft 5.7s ease-in-out infinite alternate -1.8s;
}

.lamp-right-green-2 {
  top: -3.5%;
  right: 8.5%;
  width: 10.5%;
  z-index: 6;
  animation: swayLeftToRight 7.0s ease-in-out infinite alternate -3.5s;
}

.lamp-right-green-3 {
  top: 0%;
  right: 1.8%;
  width: 10.5%;
  z-index: 7;
  animation: swayRightToLeft 6.3s ease-in-out infinite alternate -5.1s;
}

/* Sway Animations: Left to Right & Right to Left */
@keyframes swayChandelier {
  0% {
    transform: translateX(-50%) rotate(-2.5deg);
  }
  100% {
    transform: translateX(-50%) rotate(2.5deg);
  }
}

@keyframes swayLeftToRight {
  0% {
    transform: rotate(-3deg);
  }
  100% {
    transform: rotate(3deg);
  }
}

@keyframes swayRightToLeft {
  0% {
    transform: rotate(3deg);
  }
  100% {
    transform: rotate(-3deg);
  }
}

/* Lamp Flame inside Bulb */
.lamp-flame {
  position: absolute;
  left: 50%;
  top: 83%;
  width: 14%;
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
    0 0 6px #fef08a,
    0 0 14px #f59e0b,
    0 0 22px rgba(245, 158, 11, 0.55),
    0 -1px 3px rgba(255, 255, 255, 0.9);
  transform: translate(-50%, -50%);
  transform-origin: 50% 85%;
  animation: flameFlicker 1.8s infinite ease-in-out;
  pointer-events: none;
  z-index: 2;
}

@keyframes flameFlicker {
  0%, 100% {
    transform: translate(-50%, -50%) scale(1) rotate(-1deg);
    opacity: 0.92;
  }
  25% {
    transform: translate(-50%, -52%) scale(1.12, 0.95) rotate(1.5deg);
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

/* Staggered flame flickering delays (negative delays for immediate smooth rendering) */
.lamp-left-warm-1 .lamp-flame { animation-delay: -0.2s; }
.lamp-left-green-1 .lamp-flame { animation-delay: -0.7s; }
.lamp-left-warm-2 .lamp-flame { animation-delay: -1.3s; }
.lamp-left-green-2 .lamp-flame { animation-delay: -0.4s; }
.lamp-left-green-3 .lamp-flame { animation-delay: -1.0s; }

.lamp-right-warm-1 .lamp-flame { animation-delay: -0.5s; }
.lamp-right-green-1 .lamp-flame { animation-delay: -1.1s; }
.lamp-right-warm-2 .lamp-flame { animation-delay: -0.8s; }
.lamp-right-green-2 .lamp-flame { animation-delay: -1.5s; }
.lamp-right-green-3 .lamp-flame { animation-delay: -0.3s; }

/* 5. Flying Butterflies Layer */
.flying-butterflies-layer {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 12;
}

.butterfly-item {
  position: absolute;
  pointer-events: none;
  will-change: transform, opacity;
  filter: drop-shadow(0 0 8px rgba(254, 240, 138, 0.7)) drop-shadow(0 3px 6px rgba(0, 0, 0, 0.35));
}

.butterfly-flapper {
  width: 100%;
  height: 100%;
  transform-origin: 50% 50%;
  animation: wingFlap 0.22s ease-in-out infinite alternate;
  will-change: transform;
}

.butterfly-graphic {
  width: 100%;
  height: auto;
  display: block;
}

@keyframes wingFlap {
  0% {
    transform: scaleX(1) scaleY(1);
  }
  100% {
    transform: scaleX(0.22) scaleY(0.92);
  }
}

/* Butterfly Sizes & Flight Assignments */
.b1 {
  width: 32px;
  animation: flyButterfly1 16s ease-in-out infinite -2s;
}

.b2 {
  width: 28px;
  animation: flyButterfly2 18s ease-in-out infinite -7s;
}

.b3 {
  width: 36px;
  animation: flyButterfly3 15s ease-in-out infinite -11s;
}

.b4 {
  width: 24px;
  animation: flyButterfly4 21s ease-in-out infinite -4s;
}

/* Flight Path 1: Dances around left floral pillar and swoops up to arch */
@keyframes flyButterfly1 {
  0% {
    left: 8%;
    top: 75%;
    transform: rotate(20deg) scale(0.9);
    opacity: 0;
  }
  8% {
    opacity: 1;
  }
  25% {
    left: 22%;
    top: 55%;
    transform: rotate(-15deg) scale(1);
  }
  45% {
    left: 12%;
    top: 35%;
    transform: rotate(35deg) scale(1.05);
  }
  65% {
    left: 32%;
    top: 25%;
    transform: rotate(-25deg) scale(0.95);
  }
  85% {
    left: 15%;
    top: 50%;
    transform: rotate(18deg) scale(1);
    opacity: 0.95;
  }
  100% {
    left: 8%;
    top: 75%;
    transform: rotate(20deg) scale(0.9);
    opacity: 0;
  }
}

/* Flight Path 2: Swoops from upper right across center arch to left */
@keyframes flyButterfly2 {
  0% {
    right: 5%;
    top: 25%;
    transform: scaleX(-1) rotate(15deg) scale(0.85);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  30% {
    right: 30%;
    top: 40%;
    transform: scaleX(-1) rotate(-20deg) scale(1);
  }
  50% {
    right: 55%;
    top: 30%;
    transform: scaleX(-1) rotate(10deg) scale(1.05);
  }
  70% {
    right: 75%;
    top: 48%;
    transform: scaleX(-1) rotate(-30deg) scale(0.95);
  }
  90% {
    right: 25%;
    top: 35%;
    transform: scaleX(-1) rotate(20deg) scale(0.9);
    opacity: 0.9;
  }
  100% {
    right: 5%;
    top: 25%;
    transform: scaleX(-1) rotate(15deg) scale(0.85);
    opacity: 0;
  }
}

/* Flight Path 3: Elegant figure-eight flutter in the lower center zone */
@keyframes flyButterfly3 {
  0% {
    left: 45%;
    top: 80%;
    transform: rotate(-10deg) scale(0.9);
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  25% {
    left: 65%;
    top: 68%;
    transform: rotate(30deg) scale(1.05);
  }
  50% {
    left: 48%;
    top: 52%;
    transform: rotate(-25deg) scale(1);
  }
  75% {
    left: 28%;
    top: 65%;
    transform: rotate(20deg) scale(1.05);
  }
  90% {
    left: 40%;
    top: 75%;
    transform: rotate(-15deg) scale(0.95);
    opacity: 0.9;
  }
  100% {
    left: 45%;
    top: 80%;
    transform: rotate(-10deg) scale(0.9);
    opacity: 0;
  }
}

/* Flight Path 4: Playfully flutters around right floral column */
@keyframes flyButterfly4 {
  0% {
    right: 10%;
    top: 82%;
    transform: rotate(-25deg) scale(0.85);
    opacity: 0;
  }
  12% {
    opacity: 0.95;
  }
  35% {
    right: 25%;
    top: 62%;
    transform: rotate(25deg) scale(1);
  }
  60% {
    right: 12%;
    top: 45%;
    transform: rotate(-20deg) scale(0.95);
  }
  80% {
    right: 28%;
    top: 70%;
    transform: rotate(15deg) scale(0.9);
    opacity: 0.9;
  }
  100% {
    right: 10%;
    top: 82%;
    transform: rotate(-25deg) scale(0.85);
    opacity: 0;
  }
}

/* 6. Wedding Invitation Card Overlay & Typography */
.invitation-overlay {
  position: absolute;
  top: 18%;
  bottom: 3%;
  left: 4.5%;
  right: 4.5%;
  z-index: 8;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.invitation-overlay::-webkit-scrollbar {
  display: none;
}

.invitation-card {
  width: 100%;
  background: transparent;
  padding: 8px 4px;
  box-sizing: border-box;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 7px;
}

.monogram-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 3px 14px;
  border-radius: 999px;
  background: transparent;
  border: 1px solid rgba(184, 135, 40, 0.5);
}

.monogram-char {
  font-family: 'Moul', cursive;
  font-size: 14px;
  color: #8a6417;
  line-height: 1.2;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1);
}

.monogram-dot {
  font-size: 10px;
  color: #c49733;
}

.invitation-heading {
  font-family: 'Moul', 'Kantumruy Pro', cursive;
  font-size: 17px;
  color: #835b12;
  margin: 0;
  line-height: 1.4;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1), 0 2px 4px rgba(90, 60, 10, 0.2);
  letter-spacing: 0.3px;
}

.parents-row {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 8px;
  margin-top: 2px;
}

.parents-group {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.groom-parents {
  text-align: left;
}

.bride-parents {
  text-align: right;
}

.parent-entry {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 13.5px;
  color: #1a241e;
  line-height: 1.5;
  text-shadow: 0 0 3px #ffffff, 0 0 7px rgba(255, 255, 255, 0.95), 0 1px 2px rgba(255, 255, 255, 1);
}

.parent-role {
  color: #435249;
  margin-right: 3px;
  font-weight: 600;
  font-size: 13px;
}

.parent-name {
  font-weight: 700;
  color: #141c17;
  font-size: 14px;
}

.honor-invite-section {
  margin-top: 2px;
  padding: 4px 2px;
}

.honor-invite-title {
  font-family: 'Moul', 'Kantumruy Pro', cursive;
  font-size: 13px;
  color: #8f671b;
  margin: 0 0 4px 0;
  line-height: 1.35;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1), 0 2px 4px rgba(90, 60, 10, 0.2);
}

.invitation-line {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11.5px;
  font-weight: 700;
  line-height: 1.65;
  color: #1c2620;
  margin: 0;
  text-align: center;
  text-shadow: 0 0 3px #ffffff, 0 0 8px rgba(255, 255, 255, 0.98), 0 1px 2px rgba(255, 255, 255, 1);
}

.couple-section {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 10px;
  margin-top: 3px;
  padding: 7px 4px;
}

.couple-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
  flex: 1;
}

.couple-role {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11.5px;
  color: #1c2620;
  font-weight: 700;
  text-shadow: 0 0 3px #ffffff, 0 0 7px rgba(255, 255, 255, 0.95), 0 1px 2px rgba(255, 255, 255, 1);
}

.couple-name {
  font-family: 'Moul', 'Kantumruy Pro', cursive;
  font-size: 16px;
  color: #835b12;
  letter-spacing: 0.3px;
  line-height: 1.35;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1), 0 2px 4px rgba(90, 60, 10, 0.2);
}

.couple-ampersand {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 76px;
  height: 76px;
}

.couple-crest-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
  filter: drop-shadow(0 2px 5px rgba(0, 0, 0, 0.18));
}

.event-schedule-section {
  margin-top: 3px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  width: 100%;
}

.lunar-date {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11px;
  font-weight: 700;
  color: #2b3931;
  margin: 0;
  line-height: 1.45;
  text-shadow: 0 0 3px #ffffff, 0 0 7px rgba(255, 255, 255, 0.95), 0 1px 2px rgba(255, 255, 255, 1);
}

.solar-date {
  font-family: 'Moul', 'Kantumruy Pro', cursive;
  font-size: 13px;
  color: #835b12;
  margin: 0;
  line-height: 1.4;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1), 0 2px 4px rgba(90, 60, 10, 0.2);
}

.schedule-divider {
  width: 180px;
  max-width: 65%;
  margin: 3px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.divider-graphic {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 1px 2px rgba(255, 255, 255, 0.95));
}

.reception-time {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11px;
  font-weight: 700;
  line-height: 1.55;
  color: #1c2620;
  margin: 0;
  text-align: center;
  max-width: 96%;
  text-shadow: 0 0 3px #ffffff, 0 0 8px rgba(255, 255, 255, 0.98), 0 1px 2px rgba(255, 255, 255, 1);
}

.left-roses-bouquet {
  position: absolute;
  left: -10px;
  bottom: -20px;
  width: 60px;
  z-index: 9;
  pointer-events: none;
  transform: rotate(6deg);
  transform-origin: bottom center;
}

.right-roses-bouquet {
  position: absolute;
  right: -10px;
  bottom: -20px;
  width: 60px;
  z-index: 9;
  pointer-events: none;
  transform: rotate(-6deg);
  transform-origin: bottom center;
}

.right-roses-bouquet .roses-img {
  transform: scaleX(-1);
}

.extra-flower {
  position: absolute;
  pointer-events: none;
}

.extra-flower .roses-img {
  filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.28)) sepia(0.15) saturate(0.55) brightness(0.95) contrast(0.9);
}

.flower-1 {
  right: 15%;
  transform: rotate(-10deg);
}

.flower-3 {
  left: -5%;
  bottom: -2%;
  width: 25%;
  z-index: 10;
  animation: swayFlowerLeft 5s ease-in-out infinite alternate -1s;
}

@keyframes swayFlowerLeft {
  0% { transform: rotate(26deg); }
  100% { transform: rotate(31deg); }
}

.flower-3 .roses-img {
  transform: scaleX(-1);
}

.flower-5 {
    left: 3%;
    bottom: -5%;
    width: 25%;
    z-index: 10;
    animation: swayFlowerLeft2 6s ease-in-out infinite alternate -0.5s;
}

.flower-5 .roses-img {
    transform: scaleX(-1) rotate(310deg);
}

@keyframes swayFlowerLeft2 {
  0% { transform: rotate(1deg); }
  100% { transform: rotate(5deg); }
}

.flower-2 {
    right: -5%;
    bottom: -2%;
    width: 25%;
    z-index: 10;
    animation: swayFlowerRight 5.5s ease-in-out infinite alternate -2s;
}

@keyframes swayFlowerRight {
  0% { transform: rotate(330deg); }
  100% { transform: rotate(335deg); }
}

.flower-4 {
    right: 3%;
    bottom: -5%;
    width: 25%;
    z-index: 10;
    animation: swayFlowerRight2 6s ease-in-out infinite alternate -0.5s;
}

.flower-4 .roses-img {
    transform: rotate(310deg);
}

@keyframes swayFlowerRight2 {
  0% { transform: rotate(-5deg); }
  100% { transform: rotate(-1deg); }
}

.roses-img,
.left-roses-img,
.right-roses-img {
  width: 100%;
  height: auto;
  display: block;
  filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.28));
}
</style>
