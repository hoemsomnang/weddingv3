<template>
  <div class="home-container">

    <!-- ═══════════════════════════════════════════════
         ENVELOPE SCENE (unchanged)
    ════════════════════════════════════════════════ -->
    <div
      class="envelope-scene"
      :class="{ 'is-open': isOpen }"
      @click="toggleEnvelope"
    >
      <!-- 1. Envelope Back Wall -->
      <div class="envelope-back">
        <video 
          ref="previewVideoRef" 
          src="/video/preview_video_compressed.mp4" 
          playsinline 
          muted
          @ended="onVideoEnded"
          @timeupdate="onVideoTimeUpdate"
          @click.stop="skipVideo"
          :style="{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: showVideoScreen ? 1 : 0, transition: 'opacity 0.4s ease', cursor: 'pointer' }"
        ></video>
      </div>

      <!-- 2. Lower Envelope Body -->
      <div class="envelope-pocket-wrapper">
        <div class="envelope-pocket-base" :class="{ 'is-hidden': isOpen || isReturning }">
          <img :src="pocketImg" :alt="weddingText.accessibility.envelopePocketAlt" />
        </div>
        <div class="envelope-pocket-doors">
          <div class="pocket-door pocket-door-left">
            <img :src="pocketLeftImg" :alt="weddingText.accessibility.envelopePocketAlt + ' Left'" />
          </div>
          <div class="pocket-door pocket-door-right">
            <img :src="pocketRightImg" :alt="weddingText.accessibility.envelopePocketAlt + ' Right'" />
          </div>
        </div>
      </div>

      <!-- 3. Top Folding Flap -->
      <div class="envelope-flap-wrapper">
        <div class="flap-front">
          <img :src="flapImg" :alt="weddingText.accessibility.envelopeFlapAlt" />
        </div>
        <div class="flap-back"></div>
        <div ref="envelopeSealRef" class="gold-seal" :class="{ 'seal-hidden': isOpen || !isCoverOpen }">
          <img :src="goldSealCoverImg" :alt="weddingText.accessibility.envelopeSealAlt" />
        </div>
      </div>

      <!-- 4. Cover Overlay -->
      <Transition name="overlay-fade">
        <div
          v-if="!isCoverOpen"
          class="cover-overlay"
          :class="{ 'stage-disappear': isDisappearingOther }"
          @click.stop="openCover"
        >
          <div class="cover-content" @click.stop="openCover">
            <div class="cover-header">
              <h2 class="cover-title-khmer">{{ weddingText.cover.titleKhmer }}</h2>
            </div>
            <div
              ref="coverSealBoxRef"
              class="cover-seal-box"
              @click.stop="openCover"
              @keydown.enter.prevent="openCover"
              @keydown.space.prevent="openCover"
              role="button"
              tabindex="0"
              :title="weddingText.accessibility.sealButtonTitle"
            >
              <div class="seal-glow"></div>
              <img ref="coverSealImgRef" :src="goldSealCoverImg" :alt="weddingText.accessibility.coverSealAlt" class="cover-seal-img" />
            </div>
            <div class="cover-footer">
              <h2 class="cover-khmer-sub">{{ weddingText.cover.invitationKhmer }}</h2>
              <div class="tap-hint-pill">
                <span class="pulse-dot"></span>
                <span>{{ weddingText.cover.tapHint }}</span>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </div>

    <!-- Back to Cover Button -->
    <button
      v-if="isCoverOpen && !showInvitation"
      class="cover-return-btn"
      @click.stop="returnToCover"
      :title="weddingText.accessibility.backToCoverBtn"
    >
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
        <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z" />
      </svg>
    </button>

    <!-- ═══════════════════════════════════════════════
         MAIN INVITATION (emerges from palace door)
    ════════════════════════════════════════════════ -->
    <Transition name="door-emerge">
      <div v-if="showInvitation" class="main-on-top" :class="{ 'is-door-emerging': isEmergingFromDoor }">

        <div class="main-page">
          <!-- Golden radiance aura bursting from the palace doors -->
          <div v-if="isEmergingFromDoor" class="door-light-radiance"></div>

          <div class="main-screen">
            <!-- 1. Fullscreen Base Backdrop -->
            <img :src="backdropImg" alt="Sage Wedding Backdrop" class="main-bg-img" />

            <!-- 2. Tiered Crystal Chandelier -->
            <div class="chandelier-layer">
              <img :src="tieredChandelierImg" alt="Tiered Crystal Chandelier" class="layer-img chandelier-img" />
            </div>

            <!-- 3. Left Hanging Pendant Lamps -->
            <!--
            <div class="pendant-lamp lamp-left-green-1"><img :src="pendantGreenImg" alt="Green Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-left-warm-1"><img :src="pendantWarmImg" alt="Warm Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-left-green-2"><img :src="pendantGreenImg" alt="Green Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-left-warm-2"><img :src="pendantWarmImg" alt="Warm Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-left-green-3"><img :src="pendantGreenImg" alt="Green Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            -->

            <!-- 4. Right Hanging Pendant Lamps -->
            <!--
            <div class="pendant-lamp lamp-right-green-1"><img :src="pendantGreenImg" alt="Green Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-right-warm-1"><img :src="pendantWarmImg" alt="Warm Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-right-green-2"><img :src="pendantGreenImg" alt="Green Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-right-warm-2"><img :src="pendantWarmImg" alt="Warm Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            <div class="pendant-lamp lamp-right-green-3"><img :src="pendantGreenImg" alt="Green Pendant Lamp" class="layer-img" /><span class="lamp-flame"></span></div>
            -->

            <!-- 5. Flying Butterflies -->
            <div class="flying-butterflies-layer">
              <div class="butterfly-item b1"><div class="butterfly-flapper"><img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" /></div></div>
              <div class="butterfly-item b2"><div class="butterfly-flapper"><img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" /></div></div>
              <div class="butterfly-item b3"><div class="butterfly-flapper"><img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" /></div></div>
              <div class="butterfly-item b4"><div class="butterfly-flapper"><img :src="butterflyImg" alt="Wedding Butterfly" class="butterfly-graphic" /></div></div>
            </div>

            <!-- 6. Invitation Details Card -->
            <div class="invitation-overlay">
              <div class="invitation-card">
                <!-- PAGE 1: Cover & Countdown -->
                <section class="snap-page section-cover" id="page-cover" :class="{ 'section-animate-in': isCoverInView }">
                  <div class="page-content-wrapper">
                    <h1 class="invitation-heading anim-cover-item">{{ invitation.pageTitle }}</h1>
                    <div class="parents-row anim-cover-item">
                      <div class="parents-group groom-parents">
                        <div class="parent-entry"><span class="parent-role">{{ invitation.groomFather.role }}</span><span class="parent-name">{{ invitation.groomFather.name }}</span></div>
                        <div class="parent-entry"><span class="parent-role">{{ invitation.groomMother.role }}</span><span class="parent-name">{{ invitation.groomMother.name }}</span></div>
                      </div>
                      <div class="parents-group bride-parents">
                        <div class="parent-entry"><span class="parent-role">{{ invitation.brideFather.role }}</span><span class="parent-name">{{ invitation.brideFather.name }}</span></div>
                        <div class="parent-entry"><span class="parent-role">{{ invitation.brideMother.role }}</span><span class="parent-name">{{ invitation.brideMother.name }}</span></div>
                      </div>
                    </div>
                    <div class="honor-invite-section anim-cover-item">
                      <p class="honor-invite-title">{{ invitation.honorInviteText }}</p>
                      <p v-for="(line, idx) in invitation.invitationLines" :key="idx" class="invitation-line">{{ line }}</p>
                    </div>
                    <div class="couple-section anim-cover-item">
                      <div class="couple-side groom-side"><span class="couple-role">{{ invitation.groomRole }}</span><span class="couple-name">{{ invitation.groomName }}</span></div>
                      <div class="couple-ampersand"><img :src="monogramCrestImg" alt="Wedding Monogram Crest S&R" class="couple-crest-img" /></div>
                      <div class="couple-side bride-side"><span class="couple-role">{{ invitation.brideRole }}</span><span class="couple-name">{{ invitation.brideName }}</span></div>
                    </div>
                    <div class="event-schedule-section anim-cover-item">
                      <p class="lunar-date">{{ invitation.lunarDate }}</p>
                      <p class="solar-date">{{ invitation.solarDate }}</p>
                      <div class="schedule-divider"><img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" /></div>
                      <p class="reception-time">{{ invitation.receptionTime }}</p>
                    </div>
                    <div class="countdown-section">
                      <div class="countdown-grid">
                        <div class="countdown-item anim-cover-item"><span class="countdown-value">{{ toKhmerNumber(String(timeLeft.days).padStart(2, '0')) }}</span><span class="countdown-label">{{ invitation.countdownLabels.days }}</span></div>
                        <div class="countdown-item anim-cover-item"><span class="countdown-value">{{ toKhmerNumber(String(timeLeft.hours).padStart(2, '0')) }}</span><span class="countdown-label">{{ invitation.countdownLabels.hours }}</span></div>
                        <div class="countdown-item anim-cover-item"><span class="countdown-value">{{ toKhmerNumber(String(timeLeft.mins).padStart(2, '0')) }}</span><span class="countdown-label">{{ invitation.countdownLabels.mins }}</span></div>
                        <div class="countdown-item anim-cover-item"><span class="countdown-value">{{ toKhmerNumber(String(timeLeft.secs).padStart(2, '0')) }}</span><span class="countdown-label">{{ invitation.countdownLabels.secs }}</span></div>
                      </div>
                    </div>
                  </div>
                </section>



                <!-- PAGE 3: Agenda Section -->
                <section class="snap-page section-agenda" id="page-agenda" :class="{ 'section-animate-in': isAgendaInView }">
                  <div class="page-content-wrapper agenda-page-content">
                    <h2 class="section-title anim-item" style="transition-delay: 0.1s">{{ invitation.agendaTitle }}</h2>
                    <div v-for="(day, dIdx) in invitation.agendaDays" :key="dIdx" class="agenda-day">
                      <h3 class="agenda-day-title anim-item" style="transition-delay: 0.2s">{{ day.dayTitle }}</h3>
                      <div class="agenda-timeline">
                        <div v-for="(item, iIdx) in day.schedule" :key="iIdx" class="agenda-item anim-item" :style="`transition-delay: ${0.3 + (iIdx * 0.15)}s`">
                          <div class="agenda-icon-wrapper">
                            <img v-if="agendaIcons[item.icon]" :src="agendaIcons[item.icon]" class="agenda-icon-img" :alt="item.title" />
                          </div>
                          <div class="agenda-content">
                            <div class="agenda-time-row">
                              <span class="agenda-time">{{ item.time }}</span>
                              <span class="agenda-time-line"></span>
                            </div>
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
                <div class="scroll-up-hint" @click="scrollToNextPage" style="cursor: pointer;">
                  <div class="chevrons">
                    <svg class="chevron" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
                    <svg class="chevron" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
                  </div>
                  <span class="scroll-up-text">{{ invitation.scrollUpText }}</span>
                </div>
                <div class="action-buttons">
                  <button class="action-btn"><img :src="btnCalendar" alt="Calendar" class="action-icon" /></button>
                  <button class="action-btn"><img :src="btnLocation" alt="Location" class="action-icon" /></button>
                  <button class="action-btn"><img :src="btnGallery" alt="Gallery" class="action-icon" /></button>
                  <button class="action-btn"><img :src="btnWishes" alt="Wishes" class="action-icon" /></button>
                </div>
              </div>
            </div>

            <!-- Wedding Couple -->
            <div class="wedding-couple-layer">
              <img :src="weddingCoupleImg" alt="Wedding Couple" class="wedding-couple-img" />
            </div>
            </div>
          </div>
        </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// ── Envelope imports ──
import { weddingText } from '@/data/weddingText.js'
import goldSealCoverImg from '@/assets/envelope/gold-seal-transparent.webp'
import flapImg from '@/assets/envelope/envelope-flap.webp'
import pocketImg from '@/assets/envelope/envelope-pocket.webp'
import pocketLeftImg from '@/assets/envelope/envelope-pocket-left.webp'
import pocketRightImg from '@/assets/envelope/envelope-pocket-right.webp'

// ── Main invitation imports ──
import backdropImg from '@/assets/invitation_floral_frame.jpg'
import pendantGreenImg from '@/assets/items/pendant-lamp-green-transparent.png'
import pendantWarmImg from '@/assets/items/pendant-lamp-warm-transparent.png'
import tieredChandelierImg from '@/assets/items/tiered-crystal-chandelier-transparent.png'
import butterflyImg from '@/assets/items/wedding-butterfly.svg'
import monogramCrestImg from '@/assets/wedding_monogram_crest_sr_trans.webp'
import goldDividerImg from '@/assets/items/gold-wedding-divider.png'
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

import './HomePage.css'

// ── Envelope state ──
const isCoverOpen = ref(false)
const isOpen = ref(false)
const isReturning = ref(false)
const hasPlayedVideo = ref(false)
const videoFailed = ref(false)
const isDisappearingOther = ref(false)
const isAnimatingCover = ref(false)
const showInvitation = ref(false)
const showVideoScreen = ref(false)
let currentGlideAnim = null
let returnTimer = null

const envelopeSealRef = ref(null)
const coverSealBoxRef = ref(null)
const coverSealImgRef = ref(null)

// ── Main invitation state ──
const agendaIcons = { welcome: iconWelcome, fruit: iconFruit, hall: iconHall, monks: iconMonks, haircut: iconHaircut, thread: iconThread, lunch: iconLunch, banquet: iconBanquet }
const timeLeft = ref({ days: 0, hours: 0, mins: 0, secs: 0 })
const isCoverInView = ref(true)
const isAgendaInView = ref(false)
const previewVideoRef = ref(null)
const isEmergingFromDoor = ref(false)
let doorTransitionTimer = null
let timerInterval = null
let observer = null

const toKhmerNumber = (numStr) => {
  const khmerDigits = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩']
  return String(numStr).replace(/\d/g, (d) => khmerDigits[d])
}

const scrollToNextPage = () => {
  const container = document.querySelector('.invitation-card')
  if (container) container.scrollBy({ top: window.innerHeight, behavior: 'smooth' })
}

const setupScrollObserver = () => {
  setTimeout(() => {
    const agendaEl = document.getElementById('page-agenda')
    const coverEl = document.getElementById('page-cover')
    
    if (observer) observer.disconnect()
    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.target.id === 'page-cover') isCoverInView.value = entry.isIntersecting
        if (entry.target.id === 'page-agenda') isAgendaInView.value = entry.isIntersecting
      })
    }, { root: document.querySelector('.invitation-card'), threshold: 0.25 })
    if (coverEl) observer.observe(coverEl)
    if (agendaEl) observer.observe(agendaEl)
  }, 150)
}

const onVideoTimeUpdate = () => {
  if (!previewVideoRef.value) return

  // Trigger door emergence when video reaches 10.00s
  if (previewVideoRef.value.currentTime >= 10.00 && showVideoScreen.value && !showInvitation.value) {
    showInvitation.value = true
    isEmergingFromDoor.value = true

    updateCountdown()
    if (timerInterval) clearInterval(timerInterval)
    timerInterval = setInterval(updateCountdown, 1000)
    setupScrollObserver()

    // Video plays as doors open and card emerges from door
    if (doorTransitionTimer) clearTimeout(doorTransitionTimer)
    doorTransitionTimer = setTimeout(() => {
      if (previewVideoRef.value) {
        previewVideoRef.value.pause()
      }
      showVideoScreen.value = false
      isEmergingFromDoor.value = false
    }, 1400)
  }
}

const onVideoEnded = () => {
  if (!showVideoScreen.value && showInvitation.value) return
  if (doorTransitionTimer) clearTimeout(doorTransitionTimer)
  if (previewVideoRef.value) {
    previewVideoRef.value.pause()
  }
  showVideoScreen.value = false
  showInvitation.value = true
  isEmergingFromDoor.value = false
  
  updateCountdown()
  if (timerInterval) clearInterval(timerInterval)
  timerInterval = setInterval(updateCountdown, 1000)
  setupScrollObserver()
}

const skipVideo = () => {
  onVideoEnded()
}

const updateCountdown = () => {
  if (!invitation.targetDate) return
  const diff = new Date(invitation.targetDate).getTime() - Date.now()
  if (diff > 0) {
    timeLeft.value = {
      days: Math.floor(diff / 86400000),
      hours: Math.floor((diff % 86400000) / 3600000),
      mins: Math.floor((diff % 3600000) / 60000),
      secs: Math.floor((diff % 60000) / 1000)
    }
  } else {
    timeLeft.value = { days: 0, hours: 0, mins: 0, secs: 0 }
    if (timerInterval) clearInterval(timerInterval)
  }
}

// ── Envelope logic ──
const openCover = async () => {
  if (isCoverOpen.value || isAnimatingCover.value) return
  isReturning.value = false
  clearTimeout(returnTimer)
  isAnimatingCover.value = true

  // Ensure video can play by starting it synchronously with the click
  if (previewVideoRef.value && !hasPlayedVideo.value) {
    previewVideoRef.value.currentTime = 0;
    const playPromise = previewVideoRef.value.play();
    if (playPromise !== undefined) {
      playPromise.catch(e => {
        console.log('Autoplay prevented initially:', e);
        videoFailed.value = true;
      });
    }
  }

  const coverSealEl = coverSealBoxRef.value
  const targetSealEl = envelopeSealRef.value

  if (!coverSealEl || !targetSealEl) {
    isCoverOpen.value = true
    isOpen.value = true
    isAnimatingCover.value = false
    return
  }

  const sourceRect = coverSealEl.getBoundingClientRect()
  const targetRect = targetSealEl.getBoundingClientRect()
  const deltaX = (targetRect.left + targetRect.width / 2) - (sourceRect.left + sourceRect.width / 2)
  const deltaY = (targetRect.top + targetRect.height / 2) - (sourceRect.top + sourceRect.height / 2)
  const targetScale = targetRect.width / sourceRect.width

  isDisappearingOther.value = true
  await new Promise(resolve => setTimeout(resolve, 850))

  try {
    currentGlideAnim = coverSealEl.animate(
      [
        { transform: 'translate(0px, 0px) scale(1)', filter: 'drop-shadow(0 14px 28px rgba(60, 42, 10, 0.5))', offset: 0 },
        { transform: `translate(${deltaX * 0.38}px, ${deltaY * 0.42}px) scale(${1 - (1 - targetScale) * 0.68})`, filter: 'drop-shadow(0 10px 20px rgba(60, 42, 10, 0.48))', offset: 0.45 },
        { transform: `translate(${deltaX}px, ${deltaY}px) scale(${targetScale})`, filter: 'drop-shadow(0 6px 12px rgba(60, 42, 10, 0.45))', offset: 1 }
      ],
      { duration: 1100, easing: 'cubic-bezier(0.22, 1, 0.36, 1)', fill: 'forwards' }
    )
    await currentGlideAnim.finished
    await new Promise(resolve => setTimeout(resolve, 80))

    isCoverOpen.value = true
    await new Promise(resolve => setTimeout(resolve, 450))
    isOpen.value = true

    if (!hasPlayedVideo.value) {
      hasPlayedVideo.value = true
      
      if (videoFailed.value) {
        // If it failed to play initially, skip it completely so we don't get stuck
        onVideoEnded()
      } else {
        // Show video shortly after envelope starts opening
        await new Promise(resolve => setTimeout(resolve, 800))
        showVideoScreen.value = true
        
        // Video is already playing in the background, we just fade it in!
        // In case it somehow paused, try playing again, but gracefully fallback if it fails.
        if (previewVideoRef.value && previewVideoRef.value.paused) {
          previewVideoRef.value.play().catch(e => {
            console.log('Autoplay prevented at fade-in', e)
            onVideoEnded()
          })
        }
      }
    } else {
      // Skip video entirely on subsequent opens
      showInvitation.value = true
      updateCountdown()
      setupScrollObserver()
    }

  } catch (err) {
    isCoverOpen.value = true
    isOpen.value = true
  } finally {
    isDisappearingOther.value = false
    isAnimatingCover.value = false
    currentGlideAnim = null
  }
}

const returnToCover = () => {
  if (currentGlideAnim) {
    try { currentGlideAnim.cancel() } catch (e) {}
    currentGlideAnim = null
  }
  isReturning.value = true
  isCoverOpen.value = false
  isOpen.value = false
  isDisappearingOther.value = false
  isAnimatingCover.value = false
  clearTimeout(returnTimer)
  returnTimer = setTimeout(() => { isReturning.value = false }, 3500)
}

const toggleEnvelope = () => {
  if (showVideoScreen.value || showInvitation.value) return
  if (isOpen.value) {
    isReturning.value = true
    isOpen.value = false
    clearTimeout(returnTimer)
    returnTimer = setTimeout(() => { isReturning.value = false }, 3500)
  } else {
    isReturning.value = false
    clearTimeout(returnTimer)
    isOpen.value = true
  }
}

onUnmounted(() => {
  if (timerInterval) clearInterval(timerInterval)
  if (doorTransitionTimer) clearTimeout(doorTransitionTimer)
  if (observer) observer.disconnect()
})
</script>
