<template>
  <div class="home-container">
    <!-- Video Preview Palace Scene as Fullscreen Background (replaces edge gold color) -->
    <div
      class="home-scene-background"
      :class="{ 'is-active': hasOpenedOnce }"
      :key="scenePlayKey"
    >
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
      <div class="curtain-overlay" :class="{ 'curtain-opening': isCurtainOpening }">
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

    <!-- Existing Envelope Scene (Kept 100% the same as requested) -->
    <div
      class="envelope-scene"
      :class="{ 'is-open': isOpen }"
      @click="toggleEnvelope"
    >
      <!-- 1. Envelope Back Wall with Palace Animation Scene -->
      <div class="envelope-back"></div>

      <!-- 2. Lower Envelope Body / Seamless Pocket Base & 3D Split Gatefold Doors -->
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

      <!-- 3. Top Folding Scalloped Flap (3D Hinge) -->
      <div class="envelope-flap-wrapper">
        <div class="flap-front">
          <img :src="flapImg" :alt="weddingText.accessibility.envelopeFlapAlt" />
        </div>
        <div class="flap-back"></div>

        <!-- Gold Seal Emblem on Flap Tip -->
        <div
          ref="envelopeSealRef"
          class="gold-seal"
          :class="{ 'seal-hidden': isOpen || !isCoverOpen }"
        >
          <img :src="goldSealCoverImg" :alt="weddingText.accessibility.envelopeSealAlt" />
        </div>
      </div>

      <!-- 4. Cover Overlay (Directly overlaid on envelope scene) -->
      <Transition name="overlay-fade">
        <div
          v-if="!isCoverOpen"
          class="cover-overlay"
          :class="{
            'stage-disappear': isDisappearingOther
          }"
          @click.stop="openCover"
        >
          <div class="cover-content" @click.stop="openCover">
            <!-- 1. Top Heading: សិរីមង្គល អាពាហ៍ពិពាហ៍ -->
            <div class="cover-header">
              <h2 class="cover-title-khmer">{{ weddingText.cover.titleKhmer }}</h2>
            </div>

            <!-- 2. Center Gold Seal: gold-seal-transparent.webp (click to reveal current page) -->
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
              <img
                ref="coverSealImgRef"
                :src="goldSealCoverImg"
                :alt="weddingText.accessibility.coverSealAlt"
                class="cover-seal-img"
              />
            </div>

            <!-- 3. Bottom Text: សូមយាង និងគោរពអញ្ជើញ / WEDDING INVITATION -->
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

    <!-- Back to Cover Button (discreet, accessible when envelope is shown) -->
    <button
      v-if="isCoverOpen"
      class="cover-return-btn"
      @click.stop="returnToCover"
      :title="weddingText.accessibility.backToCoverBtn"
    >
      <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
        <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z" />
      </svg>
    </button>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { weddingText } from '@/data/weddingText.js'
import goldSealCoverImg from '@/assets/envelope/gold-seal-transparent.webp'
import flapImg from '@/assets/envelope/envelope-flap.webp'
import pocketImg from '@/assets/envelope/envelope-pocket.webp'
import pocketLeftImg from '@/assets/envelope/envelope-pocket-left.webp'
import pocketRightImg from '@/assets/envelope/envelope-pocket-right.webp'

// Palace Scene Assets from video-preview
import purpleStaircaseImg from '@/assets/purple-staircase-clean.jpg'
import crystalChandelierImg from '@/assets/crystal-chandelier-transparent.png'
import weddingMonogramImg from '@/assets/items/wedding-monogram-seal.png'
import floralArchImg from '@/assets/items/royal-floral-wedding-arch.png'
import throneChairsImg from '@/assets/items/wedding-throne-chairs.png'
import purpleRoseBouquetImg from '@/assets/items/purple-rose-bouquet.png'
import curtainOverlayImg from '@/assets/curtain-open-step2-parting-transparent.png'

import './HomePage.css'

const isCoverOpen = ref(false)
const isOpen = ref(false)
const isReturning = ref(false)
const isDisappearingOther = ref(false)
const isAnimatingCover = ref(false)
let currentGlideAnim = null
let returnTimer = null

// Video Preview Palace Scene Controls
const hasOpenedOnce = ref(false)
const scenePlayKey = ref(0)
const isCurtainOpening = ref(false)

watch(isOpen, (newVal) => {
  if (newVal) {
    hasOpenedOnce.value = true
    scenePlayKey.value++
  }
})

const envelopeSealRef = ref(null)
const coverSealBoxRef = ref(null)
const coverSealImgRef = ref(null)

const openCover = async () => {
  if (isCoverOpen.value || isAnimatingCover.value) return
  isReturning.value = false
  clearTimeout(returnTimer)
  isAnimatingCover.value = true

  const coverSealEl = coverSealBoxRef.value
  const targetSealEl = envelopeSealRef.value

  if (!coverSealEl || !targetSealEl) {
    isCoverOpen.value = true
    isOpen.value = true
    setTimeout(() => {
      if (isOpen.value && isCoverOpen.value) {
        isCurtainOpening.value = true
      }
    }, 2200)
    isAnimatingCover.value = false
    return
  }

  // Pre-calculate coordinates & target scale
  const sourceRect = coverSealEl.getBoundingClientRect()
  const targetRect = targetSealEl.getBoundingClientRect()

  const deltaX = (targetRect.left + targetRect.width / 2) - (sourceRect.left + sourceRect.width / 2)
  const deltaY = (targetRect.top + targetRect.height / 2) - (sourceRect.top + sourceRect.height / 2)
  const targetScale = targetRect.width / sourceRect.width

  // -------------------------------------------------------------
  // 1. "just slow disapear text":
  // Slowly fade out cover text (header, footer, hint, seal glow)
  // -------------------------------------------------------------
  isDisappearingOther.value = true

  // Wait for text to fade away smoothly (~750ms + 100ms pause)
  await new Promise(resolve => setTimeout(resolve, 850))

  // -------------------------------------------------------------
  // 2. "and slowly animate like current":
  // Gold seal slowly glides and scales into its flap dock position
  // -------------------------------------------------------------
  try {
    currentGlideAnim = coverSealEl.animate(
      [
        {
          transform: 'translate(0px, 0px) scale(1)',
          filter: 'drop-shadow(0 14px 28px rgba(60, 42, 10, 0.5))',
          offset: 0
        },
        {
          transform: `translate(${deltaX * 0.38}px, ${deltaY * 0.42}px) scale(${1 - (1 - targetScale) * 0.68})`,
          filter: 'drop-shadow(0 10px 20px rgba(60, 42, 10, 0.48))',
          offset: 0.45
        },
        {
          transform: `translate(${deltaX}px, ${deltaY}px) scale(${targetScale})`,
          filter: 'drop-shadow(0 6px 12px rgba(60, 42, 10, 0.45))',
          offset: 1
        }
      ],
      {
        duration: 1100,
        easing: 'cubic-bezier(0.22, 1, 0.36, 1)',
        fill: 'forwards'
      }
    )

    await currentGlideAnim.finished
    // Small settle delay for visual perfection
    await new Promise(resolve => setTimeout(resolve, 80))

    // -------------------------------------------------------------
    // 3. Final handoff to envelope flap seal & automatically open flap
    // -------------------------------------------------------------
    isCoverOpen.value = true

    // Smoothly and gracefully open the envelope flap (slow and majestic like seal-glow)
    await new Promise(resolve => setTimeout(resolve, 450))
    isOpen.value = true

    // Wait until the envelope is DONE opening (~2.2s) so the background curtain is clearly displayed first
    await new Promise(resolve => setTimeout(resolve, 2200))
    if (isOpen.value && isCoverOpen.value) {
      isCurtainOpening.value = true
    }
  } catch (err) {
    isCoverOpen.value = true
    isOpen.value = true
    setTimeout(() => {
      if (isOpen.value && isCoverOpen.value) {
        isCurtainOpening.value = true
      }
    }, 2200)
  } finally {
    isDisappearingOther.value = false
    isAnimatingCover.value = false
    currentGlideAnim = null
  }
}

const returnToCover = () => {
  if (currentGlideAnim) {
    try {
      currentGlideAnim.cancel()
    } catch (e) {}
    currentGlideAnim = null
  }
  isReturning.value = true
  isCoverOpen.value = false
  isOpen.value = false
  isCurtainOpening.value = false
  isDisappearingOther.value = false
  isAnimatingCover.value = false

  clearTimeout(returnTimer)
  returnTimer = setTimeout(() => {
    isReturning.value = false
  }, 3500)
}

const toggleEnvelope = () => {
  if (isOpen.value) {
    // Closing / returning back: keep envelope-pocket.png hidden during return animation
    isReturning.value = true
    isOpen.value = false
    clearTimeout(returnTimer)
    returnTimer = setTimeout(() => {
      isReturning.value = false
    }, 3500)
  } else {
    isReturning.value = false
    clearTimeout(returnTimer)
    isOpen.value = true
  }
}
</script>
