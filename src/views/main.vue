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
          <!-- PAGE 1: Cover & Countdown -->
          <section class="snap-page section-cover" id="page-cover" :class="{ 'section-animate-in': isCoverInView }">
            <div class="page-content-wrapper">
              <!-- Page Heading: សិរីមង្គលអាពាហ៍ពិពាហ៍ -->
              <h1 class="invitation-heading anim-cover-item">{{ invitation.pageTitle }}</h1>

              <!-- Parents Section -->
              <div class="parents-row anim-cover-item">
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
              <div class="honor-invite-section anim-cover-item">
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
              <div class="couple-section anim-cover-item">
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
              <div class="event-schedule-section anim-cover-item">
                <p class="lunar-date">{{ invitation.lunarDate }}</p>
                <p class="solar-date">{{ invitation.solarDate }}</p>
                <div class="schedule-divider">
                  <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
                </div>
                <p class="reception-time">{{ invitation.receptionTime }}</p>
              </div>

              <!-- Countdown Section -->
              <div class="countdown-section">
                <div class="countdown-grid">
                  <div class="countdown-item anim-cover-item">
                    <span class="countdown-value">{{ toKhmerNumber(String(timeLeft.days).padStart(2, '0')) }}</span>
                    <span class="countdown-label">{{ invitation.countdownLabels.days }}</span>
                  </div>
                  <div class="countdown-item anim-cover-item">
                    <span class="countdown-value">{{ toKhmerNumber(String(timeLeft.hours).padStart(2, '0')) }}</span>
                    <span class="countdown-label">{{ invitation.countdownLabels.hours }}</span>
                  </div>
                  <div class="countdown-item anim-cover-item">
                    <span class="countdown-value">{{ toKhmerNumber(String(timeLeft.mins).padStart(2, '0')) }}</span>
                    <span class="countdown-label">{{ invitation.countdownLabels.mins }}</span>
                  </div>
                  <div class="countdown-item anim-cover-item">
                    <span class="countdown-value">{{ toKhmerNumber(String(timeLeft.secs).padStart(2, '0')) }}</span>
                    <span class="countdown-label">{{ invitation.countdownLabels.secs }}</span>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!-- PAGE 2: Agenda Section -->
          <section class="snap-page section-agenda" id="page-agenda" :class="{ 'section-animate-in': isAgendaInView }">
            <div class="page-content-wrapper agenda-page-content">
              <h2 class="section-title anim-item" style="transition-delay: 0.1s">{{ invitation.agendaTitle }}</h2>
              <div v-for="(day, dIdx) in invitation.agendaDays" :key="dIdx" class="agenda-day">
                <h3 class="agenda-day-title anim-item" style="transition-delay: 0.2s">{{ day.dayTitle }}</h3>
                <div class="agenda-timeline">
                  <div v-for="(item, iIdx) in day.schedule" :key="iIdx" class="agenda-item anim-item" :style="`transition-delay: ${0.3 + (iIdx * 0.15)}s`">
                    <div class="agenda-time">{{ item.time }}</div>
                    <div class="agenda-dot"></div>
                    <div class="agenda-content">
                      <img v-if="agendaIcons[item.icon]" :src="agendaIcons[item.icon]" class="agenda-icon-img" :alt="item.title" />
                      <span class="agenda-item-title">{{ item.title }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>

        <!-- Fixed Bottom Actions -->
        <div class="fixed-bottom-actions">
          <!-- Scroll Up Hint -->
          <div class="scroll-up-hint" @click="scrollToNextPage" style="cursor: pointer;">
            <div class="chevrons">
              <svg class="chevron" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
              <svg class="chevron" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>
            <span class="scroll-up-text">{{ invitation.scrollUpText }}</span>
          </div>

          <!-- Action Buttons -->
          <div class="action-buttons">
            <button class="action-btn">
              <img :src="btnCalendar" alt="Calendar" class="action-icon" />
            </button>
            <button class="action-btn">
              <img :src="btnLocation" alt="Location" class="action-icon" />
            </button>
            <button class="action-btn">
              <img :src="btnGallery" alt="Gallery" class="action-icon" />
            </button>
            <button class="action-btn">
              <img :src="btnWishes" alt="Wishes" class="action-icon" />
            </button>
          </div>
        </div>
      </div>


      <!-- Extra Flowers (Left and Right)
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
      
      // Lotus Flowers
      <div class="extra-flower lotus-tall-left">
        <img :src="lotusTallImg" alt="Lotus Tall Left" class="roses-img" />
      </div>
      <div class="extra-flower lotus-left">
        <img :src="lotusImg" alt="Lotus Left" class="roses-img" />
      </div>
      
      <div class="extra-flower lotus-tall-right">
        <img :src="lotusTallImg" alt="Lotus Tall Right" class="roses-img" />
      </div>
      <div class="extra-flower lotus-right">
        <img :src="lotusImg" alt="Lotus Right" class="roses-img" />
      </div>  
      
     
      
     New Lotus Next to Tall Right 
      <div class="extra-flower lotus-3-right">
        <img :src="lotus3Img" alt="Lotus 3 Right" class="roses-img" />
      </div>-->

       <!-- Wedding Couple -->
      <div class="wedding-couple-layer">
        <img :src="weddingCoupleImg" alt="Wedding Couple" class="wedding-couple-img" />
      </div>
    </div>
  </div>
</template>

<script setup>
import backdropImg from '@/assets/sage-wedding-backdrop.with-lamps.jpg'
import pendantGreenImg from '@/assets/items/pendant-lamp-green-transparent.png'
import pendantWarmImg from '@/assets/items/pendant-lamp-warm-transparent.png'
import tieredChandelierImg from '@/assets/items/tiered-crystal-chandelier-transparent.png'
import butterflyImg from '@/assets/items/wedding-butterfly.svg'
import monogramCrestImg from '@/assets/wedding_monogram_crest_sr_trans.webp'
import goldDividerImg from '@/assets/items/gold-wedding-divider.png'
import flower2Img from '@/assets/flower-2-transparent.png'
import lotusImg from '@/assets/lotus-transparent.png'
import lotusTallImg from '@/assets/lotus-tall-transparent.png'
import lotus3Img from '@/assets/lotus-3-transparent.png'
import weddingCoupleImg from '@/assets/wedding-couple-2-transparent.png'
import invitation from '@/config/invitation.js'
import btnCalendar from '@/assets/items/btn_calendar.svg'
import btnLocation from '@/assets/items/btn_location.svg'
import btnGallery from '@/assets/items/btn_gallery.svg'
import btnWishes from '@/assets/items/btn_wishes.svg'

import iconWelcome from '@/assets/items/agenda_01_welcome.webp'
import iconFruit from '@/assets/items/agenda_02_fruit.webp'
import iconHall from '@/assets/items/agenda_03_hall.webp'
import iconMonks from '@/assets/items/agenda_05_monks.webp'
import iconHaircut from '@/assets/items/agenda_06_haircut.webp'
import iconThread from '@/assets/items/agenda_07_thread.webp'
import iconLunch from '@/assets/items/agenda_08_lunch.webp'
import iconBanquet from '@/assets/items/agenda_09_banquet.webp'

import { ref, onMounted, onUnmounted } from 'vue'

const agendaIcons = {
  welcome: iconWelcome,
  fruit: iconFruit,
  hall: iconHall,
  monks: iconMonks,
  haircut: iconHaircut,
  thread: iconThread,
  lunch: iconLunch,
  banquet: iconBanquet
}

const timeLeft = ref({
  days: 0,
  hours: 0,
  mins: 0,
  secs: 0
});

const toKhmerNumber = (numStr) => {
  const khmerDigits = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩'];
  return String(numStr).replace(/\d/g, (d) => khmerDigits[d]);
};

let timerInterval = null;
let observer = null;
const isCoverInView = ref(true);
const isAgendaInView = ref(false);

const scrollToNextPage = () => {
  const container = document.querySelector('.invitation-card');
  if (container) {
    container.scrollBy({ top: window.innerHeight, behavior: 'smooth' });
  }
};

const updateCountdown = () => {
  if (!invitation.targetDate) return;
  const targetTime = new Date(invitation.targetDate).getTime();
  const now = new Date().getTime();
  const diff = targetTime - now;

  if (diff > 0) {
    timeLeft.value = {
      days: Math.floor(diff / (1000 * 60 * 60 * 24)),
      hours: Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
      mins: Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60)),
      secs: Math.floor((diff % (1000 * 60)) / 1000)
    };
  } else {
    timeLeft.value = { days: 0, hours: 0, mins: 0, secs: 0 };
    if (timerInterval) clearInterval(timerInterval);
  }
};

onMounted(() => {
  updateCountdown();
  timerInterval = setInterval(updateCountdown, 1000);

  const coverEl = document.getElementById('page-cover');
  const agendaEl = document.getElementById('page-agenda');
  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.target.id === 'page-cover') {
        isCoverInView.value = entry.isIntersecting;
      }
      if (entry.target.id === 'page-agenda') {
        isAgendaInView.value = entry.isIntersecting;
      }
    });
  }, { 
    root: document.querySelector('.invitation-card'),
    threshold: 0.25 
  });

  if (coverEl) observer.observe(coverEl);
  if (agendaEl) observer.observe(agendaEl);
});

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval);
  if (observer) observer.disconnect();
});
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
  width: 103%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

/* Layered Elements */
.layer-img {
  width: 96%;
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
  top: 0%;
  bottom: 0%;
  left: 4.5%;
  right: 4.5%;
  z-index: 8;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.invitation-card {
  width: 100%;
  background: transparent;
  box-sizing: border-box;
  text-align: center;
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
  -ms-overflow-style: none;
  
  /* Mask to fade out text slowly as it approaches the top (30px) */
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, transparent 10px, black 30px, black 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, transparent 10px, black 30px, black 100%);
}

.snap-page {
  position: relative;
  width: 100%;
  min-height: 100dvh;
  scroll-snap-align: start;
  scroll-snap-stop: always;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.page-content-wrapper {
  padding: 18vh 4px 150px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 7px;
}

.agenda-page-content {
  padding-top: 10vh; /* customized padding for agenda page to center it better */
}

.invitation-card::-webkit-scrollbar {
  display: none;
}

/* Luxury Staggered Scroll Entrance Transitions (V2 Style) */
.anim-item, .anim-cover-item, .countdown-item {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.35s ease, transform 0.35s ease;
  will-change: opacity, transform;
}

.section-animate-in .anim-item,
.section-animate-in .anim-cover-item,
.section-animate-in .countdown-item {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 1.1s cubic-bezier(0.16, 1, 0.3, 1), transform 1.1s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Parallel Cascading Delays for Cover Section */
.section-animate-in .invitation-heading { transition-delay: 0.1s; }
.section-animate-in .parents-row { transition-delay: 0.3s; }
.section-animate-in .honor-invite-section { transition-delay: 0.5s; }
.section-animate-in .couple-section { transition-delay: 0.7s; }
.section-animate-in .event-schedule-section { transition-delay: 0.9s; }

.section-animate-in .countdown-item:nth-child(1) { transition-delay: 1.1s; }
.section-animate-in .countdown-item:nth-child(2) { transition-delay: 1.25s; }
.section-animate-in .countdown-item:nth-child(3) { transition-delay: 1.4s; }
.section-animate-in .countdown-item:nth-child(4) { transition-delay: 1.55s; }

.agenda-section {
  width: 100%;
}

.anim-item {
  opacity: 0;
}
.section-animate-in .anim-item {
  animation: slideDownFade 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
.section-title {
  font-family: 'Moul', cursive;
  font-size: 18px;
  color: #835b12;
  margin-bottom: 20px;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1);
}
.agenda-day {
  margin-bottom: 20px;
  width: 100%;
  text-align: left;
  padding: 0 10px;
  box-sizing: border-box;
}
.agenda-day-title {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 14px;
  color: #435249;
  font-weight: 700;
  margin-bottom: 15px;
  text-align: center;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1);
}
.agenda-timeline {
  display: flex;
  flex-direction: column;
  gap: 12px;
  position: relative;
}
.agenda-timeline::before {
  content: '';
  position: absolute;
  left: 75px;
  top: 5px;
  bottom: 5px;
  width: 1px;
  background: rgba(131, 91, 18, 0.3);
}
.agenda-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  position: relative;
}
.agenda-time {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 12px;
  color: #835b12;
  font-weight: 700;
  width: 65px;
  text-align: right;
  flex-shrink: 0;
  padding-top: 2px;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1);
}
.agenda-dot {
  width: 7px;
  height: 7px;
  background: #835b12;
  border-radius: 50%;
  margin-top: 5px;
  z-index: 1;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.8);
  flex-shrink: 0;
}
.agenda-content {
  flex: 1;
  padding: 2px 0px 8px 12px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.agenda-icon-img {
  width: 32px;
  height: 32px;
  object-fit: contain;
  flex-shrink: 0;
}
.agenda-item-title {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 12px;
  color: #435249;
  line-height: 1.4;
  font-weight: 700;
  text-shadow: 0 0 4px #ffffff, 0 0 8px rgba(255, 255, 255, 0.95), 0 1px 3px rgba(255, 255, 255, 1);
}

.fixed-bottom-actions {
  position: absolute;
  bottom: 3%;
  left: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-bottom: 8px;
  z-index: 10;
  transform: translateY(20px);
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
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: start;
  width: 100%;
  gap: 16px;
  margin-top: 2px;
}

.parents-group {
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.groom-parents {
  text-align: left;
  justify-self: start;
}

.bride-parents {
  text-align: left;
  justify-self: end;
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

.countdown-section {
  margin-top: 8px;
  width: 100%;
}

.countdown-grid {
  display: flex;
  justify-content: center;
  gap: 12px;
}

.countdown-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(255, 255, 255, 0.4);
  border: 1px solid rgba(184, 135, 40, 0.4);
  border-radius: 8px;
  padding: 6px 10px;
  min-width: 45px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  backdrop-filter: blur(2px);
}

.countdown-value {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: #835b12;
  text-shadow: 0 0 2px #ffffff;
}

.countdown-label {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 10px;
  color: #435249;
  margin-top: 2px;
  font-weight: 600;
}

.scroll-up-hint {
  margin-top: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0px;
  color: #835b12;
  animation: bounceHint 2s infinite;
  text-shadow: 0 0 4px rgba(255, 255, 255, 0.8);
}

.chevrons {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 20px;
}

.chevron {
  height: 14px;
  margin-top: -6px;
}

.scroll-up-text {
  font-family: 'Kantumruy Pro', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
}

@keyframes bounceHint {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-8px);
  }
  60% {
    transform: translateY(-4px);
  }
}

.action-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-top: 15px;
  width: 100%;
}

.action-btn {
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  background: linear-gradient(145deg, #43524938 0%, #43524947 100%);
  border: 1.5px solid #835b128c;
  border-radius: clamp(14px, 3.8vw, 18px);
  outline: none;
  flex: none;
  justify-content: center;
  align-items: center;
  width: clamp(52px, 15.5vw, 68px);
  height: clamp(44px, 13vw, 56px);
  margin: 0;
  padding: 0;
  transition: transform .22s cubic-bezier(.34, 1.56, .64, 1), box-shadow .22s, background-color .22s;
  display: flex;
  box-shadow: 0 4px 12px #4352492e, inset 0 1px 1.5px #fff6;
}

.action-btn:active {
  transform: scale(0.9);
}

.action-icon {
  width: 24px;
  height: 24px;
  object-fit: contain;
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
  filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.28)) sepia(0.35) saturate(0.7) brightness(0.9) contrast(0.85);
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

.lotus-tall-left {
    left: 28%;
    bottom: -2%;
    width: 20%;
    z-index: 4;
    animation: swayFlowerLeft 6.5s ease-in-out infinite alternate -0.5s;
}

.lotus-tall-left .roses-img {
    transform: scaleX(-1) rotate(5deg);
}

.lotus-left {
    left: 30%;
    bottom: -2%;
    width: 15%;
    z-index: 5;
}

.lotus-left .roses-img {
    transform: scaleX(-1) rotate(15deg);
}

.lotus-tall-right {
    right: 28%;
    bottom: -2%;
    width: 20%;
    z-index: 4;
    animation: swayFlowerRight 6.5s ease-in-out infinite alternate -1s;
}

.lotus-tall-right .roses-img {
    transform: rotate(-5deg);
}

.lotus-right {
    right: 30%;
    bottom: -2%;
    width: 15%;
    z-index: 5;
}

.lotus-right .roses-img {
    transform: rotate(355deg);
}

.lotus-3-right {
    right: 42%;
    bottom: -2%;
    width: 18%;
    z-index: 6;
    animation: swayFlowerRight 6s ease-in-out infinite alternate -1s;
}

.lotus-3-right .roses-img {
    transform: rotate(350deg);
}

.wedding-couple-layer {
    position: absolute;
    left: 20%;
    right: 20%;
    bottom: 1%;
    width: 60%;
    z-index: 0;
    pointer-events: none;
    display: flex;
    justify-content: center;
}

.wedding-couple-img {
    width: 100%;
    height: auto;
    filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.28)) sepia(0.1) saturate(0.8) brightness(0.95) blur(0.8px);
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
