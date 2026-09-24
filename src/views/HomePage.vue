<template>
  <div class="home-container">
    <!-- Existing Envelope Scene (Kept 100% the same as requested) -->
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
        <img :src="pocketImg" :alt="weddingText.accessibility.envelopePocketAlt" />
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

    <!-- Cover Overlay (Pure transparent overlay for text & center seal) -->
    <Transition name="overlay-fade">
      <div
        v-if="!isCoverOpen"
        class="cover-overlay"
        :class="{
          'stage-disappear': isDisappearingOther
        }"
        @click="openCover"
      >
        <div class="cover-card" @click.stop="openCover">
          <div class="cover-content" @click.stop="openCover">
            <!-- 1. Top Heading: សិរីមង្គល អាពាហ៍ពិពាហ៍ -->
            <div class="cover-header">
              <h2 class="cover-title-khmer">{{ weddingText.cover.titleKhmer }}</h2>
            </div>

            <!-- 2. Center Gold Seal: gold-seal-transparent.png (click to reveal current page) -->
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
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { weddingText } from '@/data/weddingText.js'
import goldSealCoverImg from '@/assets/envelope/gold-seal-transparent.png'
import flapImg from '@/assets/envelope/envelope-flap.png'
import pocketImg from '@/assets/envelope/envelope-pocket.png'
import './HomePage.css'

const isCoverOpen = ref(false)
const isOpen = ref(false)
const isDisappearingOther = ref(false)
const isAnimatingCover = ref(false)
let currentGlideAnim = null

const envelopeSealRef = ref(null)
const coverSealBoxRef = ref(null)
const coverSealImgRef = ref(null)

const openCover = async () => {
  if (isCoverOpen.value || isAnimatingCover.value) return
  isAnimatingCover.value = true

  const coverSealEl = coverSealBoxRef.value
  const targetSealEl = envelopeSealRef.value

  if (!coverSealEl || !targetSealEl) {
    isCoverOpen.value = true
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
    await new Promise(resolve => setTimeout(resolve, 60))

    // -------------------------------------------------------------
    // 3. Final handoff to envelope flap seal
    // -------------------------------------------------------------
    isCoverOpen.value = true
  } catch (err) {
    isCoverOpen.value = true
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
  isCoverOpen.value = false
  isOpen.value = false
  isDisappearingOther.value = false
  isAnimatingCover.value = false
}

const toggleEnvelope = () => {
  isOpen.value = !isOpen.value
}
</script>
