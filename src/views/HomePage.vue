<template>
  <div class="home-container">

    <!-- ═══════════════════════════════════════════════
         LUXURIOUS LIGHT LEAK & FLASH CROSSFADE OVERLAY
    ════════════════════════════════════════════════ -->
    <div
      class="light-leak-transition"
      :class="{
        'is-active': isLightLeakActive,
        'is-fading-out': isLightLeakFadingOut
      }"
      aria-hidden="true"
    ></div>

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
          ref="sealVideoRef" 
          src="/video/preview.mp4" 
          playsinline 
          class="seal-bg-video"
          :class="{ 'is-active': isVideoPlaying }"
          @timeupdate="onVideoTimeUpdate"
          @ended="onVideoEnded"
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
              <h2 class="cover-title-khmer">
                <img
                  :src="weddingTitleKhmerImg"
                  :alt="weddingText.cover.titleKhmer"
                  class="cover-title-khmer-img"
                />
              </h2>
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
              <h2 class="cover-khmer-sub">
                <img
                  :src="soamKouropAnjeyImg"
                  :alt="weddingText.cover.invitationKhmer"
                  class="cover-khmer-sub-img"
                />
              </h2>
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
      <div v-if="showInvitation" class="main-on-top">

        <div class="main-page">

          <div class="main-screen">
            <!-- 1. Fullscreen Base Backdrop -->
            <img :src="backdropImg" alt="Sage Wedding Backdrop" class="main-bg-img" />

            <!-- Ambient Magical Floating Particles & Sparkles Canvas -->
            <canvas ref="sparklesCanvasRef" class="ambient-particles-canvas" aria-hidden="true"></canvas>

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
              <div class="invitation-card" @scroll="onCardScroll">
                <!-- PAGE 1: Cover & Countdown -->
                <section class="snap-page section-cover" id="page-cover" :class="{ 'section-animate-in': isCoverInView }">
                  <div class="page-content-wrapper cover-page-content" :class="{ 'cinematic-camera-zoom': isCoverInView }">
                    <h1 class="invitation-heading anim-cover-item">
                      <img
                        :src="weddingTitleKhmerImg"
                        :alt="invitation.pageTitle"
                        class="invitation-heading-img"
                      />
                    </h1>

                    <!-- Dedicated Invitation Luxury Card Container with Background Frame -->
                    <div class="invitation-card-container anim-item" style="transition-delay: 0.25s">
                      <div class="invitation-gold-frame">
                        <!-- Gold Foil Shimmer Specular Light Sweep -->
                        <div class="gold-foil-shimmer-sweep" aria-hidden="true"></div>

                        <!-- 3D Gold Khmer Corner Ornaments -->
                        <img :src="corner3dTl" alt="3D Khmer Corner TL" class="invitation-kbach-corner corner-tl" />
                        <img :src="corner3dTr" alt="3D Khmer Corner TR" class="invitation-kbach-corner corner-tr" />
                        <img :src="corner3dBl" alt="3D Khmer Corner BL" class="invitation-kbach-corner corner-bl" />
                        <img :src="corner3dBr" alt="3D Khmer Corner BR" class="invitation-kbach-corner corner-br" />

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
                    </div>
                  </div>
                </section>



                <!-- PAGE 2: Agenda Section -->
                <section class="snap-page section-agenda" id="page-agenda" :class="{ 'section-animate-in': isAgendaInView }">
                  <div class="page-content-wrapper agenda-page-content">
                    <h2 class="section-title anim-item" style="transition-delay: 0.1s">
                      <img
                        :src="agendaTitleKhmerImg"
                        :alt="invitation.agendaTitle"
                        class="section-title-img"
                      />
                    </h2>
                    <div v-for="(day, dIdx) in invitation.agendaDays" :key="dIdx" class="agenda-day">
                     
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

                <!-- PAGE 3: Location Section (ទីតាំងប្រារព្ធពិធី) -->
                <section class="snap-page section-location" id="page-location" :class="{ 'section-animate-in': isLocationInView }">
                  <div class="page-content-wrapper location-page-content">
                    <!-- Title Header -->
                    <h2 class="section-title anim-item" style="transition-delay: 0.1s">
                      <img
                        :src="locationTitleKhmerImg"
                        :alt="invitation.venueTitle"
                        class="location-title-img"
                      />
                    </h2>

                    <!-- Venue Info Box with Luxury Background Frame & 3D Gold Corner Ornaments -->
                    <div class="location-card-box anim-item" style="transition-delay: 0.25s">
                      <!-- 3D Gold Khmer Corner Ornaments -->
                      <img :src="corner3dTl" alt="3D Khmer Corner TL" class="location-kbach-corner corner-tl" />
                      <img :src="corner3dTr" alt="3D Khmer Corner TR" class="location-kbach-corner corner-tr" />
                      <img :src="corner3dBl" alt="3D Khmer Corner BL" class="location-kbach-corner corner-bl" />
                      <img :src="corner3dBr" alt="3D Khmer Corner BR" class="location-kbach-corner corner-br" />

                      <!-- Venue Name -->
                      <div class="location-info-row venue-title-row">
                        <div class="location-icon-circle">
                          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                            <path d="M12 3L2 12h3v8h6v-5h2v5h6v-8h3L12 3z"/>
                          </svg>
                        </div>
                        <div class="location-text-col">
                          <span class="location-label">ទីកន្លែងទទួលភ្ញៀវ</span>
                          <span class="location-name-text">{{ invitation.venueName }}</span>
                        </div>
                      </div>

                      <div class="location-divider-line"></div>

                      <!-- Venue Address -->
                      <div class="location-info-row">
                        <div class="location-icon-circle">
                          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 0 1 0-5 2.5 2.5 0 0 1 0 5z"/>
                          </svg>
                        </div>
                        <div class="location-text-col">
                          <span class="location-label">អាសយដ្ឋាន</span>
                          <span class="location-address-text">{{ invitation.venueAddress }}</span>
                        </div>
                      </div>

                      <div class="location-divider-line"></div>

                      <!-- Reception Time -->
                      <div class="location-info-row">
                        <div class="location-icon-circle">
                          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                            <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/>
                          </svg>
                        </div>
                        <div class="location-text-col">
                          <span class="location-label">ពេលវេលាទទួលភ្ញៀវ</span>
                          <span class="location-time-text">{{ invitation.venueReceptionTime }}</span>
                        </div>
                      </div>
                    </div>

                    <!-- Google Map Interactive Frame -->
                    <div class="location-map-frame anim-item" style="transition-delay: 0.4s">
                      <iframe
                        :src="invitation.venueEmbedUrl"
                        width="100%"
                        height="100%"
                        style="border:0;"
                        allowfullscreen=""
                        loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade"
                        title="Google Maps Location"
                      ></iframe>
                      <div class="map-center-pin">
                        <img :src="goldMapImg" alt="Location Pin" class="map-center-pin-img" />
                      </div>
                    </div>

                    <!-- Open in Google Maps CTA Button -->
                    <a
                      :href="invitation.venueMapsUrl"
                      target="_blank"
                      rel="noopener noreferrer"
                      class="location-map-btn anim-item"
                      style="transition-delay: 0.5s"
                    >
                      <img :src="goldMapImg" alt="Location Map Pin" class="map-btn-icon" />
                      <span class="map-btn-text">{{ invitation.venueButtonText }}</span>
                      <svg class="map-btn-arrow" viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                        <path d="M14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3m-2 16H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7h-2v7z"/>
                      </svg>
                    </a>

                    <!-- Closing Courtesy Note & Gold Divider -->
                    <!-- Closing Courtesy Note & Gold Divider -->
                    <div class="location-footer-note anim-item" style="transition-delay: 0.6s">
                      <p class="location-closing-wish">{{ invitation.venueClosingWish }}</p>
                      <div class="schedule-divider">
                        <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
                      </div>
                    </div>
                  </div>
                </section>

                <!-- PAGE 4: Gallery Section (វិចិត្រសាល) -->
                <section class="snap-page section-gallery" id="page-gallery" :class="{ 'section-animate-in': isGalleryInView }">
                  <div class="page-content-wrapper gallery-page-content">
                    <!-- Title Header -->
                    <h2 class="section-title anim-item" style="transition-delay: 0.1s">
                      <img
                        :src="galleryTitleKhmerImg"
                        :alt="invitation.galleryTitle"
                        class="gallery-title-img"
                      />
                    </h2>

                    <!-- Subtitle & Love Quote -->
                    <div class="gallery-subtitle-wrapper anim-item" style="transition-delay: 0.2s">
                      
                      <p class="gallery-wishes-text">{{ invitation.galleryWishes }}</p>
                    </div>

                    <!-- Featured Hero Panoramic Banner -->
                    <div class="gallery-hero-card anim-item" style="transition-delay: 0.3s" @click="openLightbox(0)">
                      <div class="gallery-hero-frame">
                        <!-- Golden Shimmer Skeleton -->
                        <div class="gallery-img-skeleton" :class="{ 'is-hidden': loadedPhotos[0] }">
                          <div class="skeleton-shimmer"></div>
                          <div class="skeleton-spinner">
                            <div class="spinner-ring"></div>
                            <div class="spinner-sparkle">✦</div>
                          </div>
                        </div>

                        <img
                          :src="galleryPhotos[0].src"
                          :alt="galleryPhotos[0].alt"
                          class="gallery-hero-img"
                          :class="{ 'is-loaded': loadedPhotos[0] }"
                          @load="onPhotoLoad(0)"
                          loading="lazy"
                        />
                        <div class="gallery-hero-badge">
                          <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor">
                            <path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>
                          </svg>
                          <span>{{ galleryPhotos[0].caption }}</span>
                        </div>
                      </div>
                    </div>

                    <!-- 2-Column Photo Grid -->
                    <div class="gallery-grid anim-item" style="transition-delay: 0.4s">
                      <div
                        v-for="(photo, idx) in galleryPhotos.slice(1)"
                        :key="idx"
                        class="gallery-grid-item"
                        :class="{ 'gallery-grid-item-featured': idx === 4 }"
                        @click="openLightbox(idx + 1)"
                      >
                        <div class="gallery-item-inner">
                          <!-- Golden Shimmer Skeleton -->
                          <div class="gallery-img-skeleton" :class="{ 'is-hidden': loadedPhotos[idx + 1] }">
                            <div class="skeleton-shimmer"></div>
                            <div class="skeleton-spinner">
                              <div class="spinner-ring"></div>
                              <div class="spinner-sparkle">✦</div>
                            </div>
                          </div>

                          <img
                            :src="photo.src"
                            :alt="photo.alt"
                            class="gallery-grid-img"
                            :class="{ 'is-loaded': loadedPhotos[idx + 1] }"
                            @load="onPhotoLoad(idx + 1)"
                            loading="lazy"
                          />
                          <div class="gallery-item-overlay">
                            <span class="gallery-item-label">{{ photo.caption }}</span>
                          </div>
                        </div>
                      </div>
                    </div>

                    <!-- Closing Courtesy Note & Gold Divider -->
                    <div class="gallery-footer-note anim-item" style="transition-delay: 0.5s">
                      <p class="gallery-closing-wish">{{ invitation.albumWishes }}</p>
                      <div class="schedule-divider">
                        <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
                      </div>
                    </div>
                  </div>
                </section>

                <!-- PAGE 5: Wedding Gift & QR Code Section (ចំណងដៃអាពាហ៍ពិពាហ៍) -->
                <section class="snap-page section-gift" id="page-gift" :class="{ 'section-animate-in': isGiftInView }">
                  <div class="page-content-wrapper gift-page-content">

                    <!-- Title Header -->
                    <div class="gift-header-wrapper anim-item" style="transition-delay: 0.1s">
                      <div class="gift-title-row">
                        <span class="gift-ornament-wing ornament-left"></span>
                        <img src="/gift-title-khmer.png" alt="Wedding Gift" class="gift-title-khmer-img" />
                        <span class="gift-ornament-wing ornament-right"></span>
                      </div>
                    
                    </div>

                    <!-- Intro note -->
                    <p class="gift-intro-text reception-time anim-item" style="transition-delay: 0.15s">
                      {{ invitation.giftDesc }}
                    </p>

                    <!-- Groom / Bride Selector Tabs -->
                    <div class="gift-tabs-nav anim-item" style="transition-delay: 0.2s">
                      <button
                        class="gift-tab-btn"
                        :class="{ 'is-active': activeQrTab === 'groom' }"
                        @click="activeQrTab = 'groom'"
                      >
                        <span class="tab-emoji">🤵</span>
                        <span class="tab-label">{{ invitation.giftTabs.groom }}</span>
                      </button>
                      <button
                        class="gift-tab-btn"
                        :class="{ 'is-active': activeQrTab === 'bride' }"
                        @click="activeQrTab = 'bride'"
                      >
                        <span class="tab-emoji">👰</span>
                        <span class="tab-label">{{ invitation.giftTabs.bride }}</span>
                      </button>
                    </div>

                    <!-- KHQR Banking Card Container -->
                    <div class="gift-card-wrapper anim-item" style="transition-delay: 0.28s">
                      <div class="khqr-card-frame">
                        <!-- Corner Filigree Ornaments -->
                        <div class="thanks-corner corner-tl"></div>
                        <div class="thanks-corner corner-tr"></div>
                        <div class="thanks-corner corner-bl"></div>
                        <div class="thanks-corner corner-br"></div>

                        <!-- Red KHQR Header -->
                        <div class="khqr-header-bar">
                          <div class="khqr-header-left">
                            <span class="khqr-symbol">❖</span>
                            <span class="khqr-logo-text">KHQR</span>
                          </div>
                          <span class="khqr-bank-tag">{{ invitation.giftAccounts[activeQrTab].bank }}</span>
                        </div>

                        <!-- Account Owner Info -->
                        <div class="khqr-owner-box">
                          <span class="khqr-owner-role">{{ activeQrTab === 'groom' ? 'កូនកំលោះ' : 'កូនក្រមុំ' }}</span>
                          <span class="khqr-owner-name-kh">{{ invitation.giftAccounts[activeQrTab].nameKh }}</span>
                          <span class="khqr-owner-name-en">{{ invitation.giftAccounts[activeQrTab].nameEn }}</span>
                        </div>

                        <!-- QR Code Matrix Frame with Scan Glow -->
                        <div class="khqr-matrix-box" @click="zoomQr(activeQrTab === 'groom' ? cardGroomKhqr : cardBrideKhqr)" title="ចុចដើម្បីពង្រីក / Tap to Zoom">
                          <div class="khqr-qr-border">
                            <img
                              :src="activeQrTab === 'groom' ? qrGroomImg : qrBrideImg"
                              :alt="`QR Code ${activeQrTab}`"
                              class="khqr-code-img"
                            />
                          </div>
                          <div class="khqr-tap-hint">
                            <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
                            <span>ចុចដើម្បីពង្រីក</span>
                          </div>
                        </div>

                        <!-- Account Number with One-Click Copy -->
                        <div class="khqr-acc-strip">
                          <div class="khqr-acc-details">
                            <span class="khqr-acc-label">លេខគណនី (A/C No.)</span>
                            <span class="khqr-acc-number">{{ invitation.giftAccounts[activeQrTab].accountNumber }}</span>
                          </div>
                          <button
                            class="khqr-copy-btn"
                            @click="copyAccountNumber(invitation.giftAccounts[activeQrTab].accountNumber)"
                            title="ចម្លងលេខកុង"
                          >
                            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                              <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                            </svg>
                            <span>ចម្លង</span>
                          </button>
                        </div>

                        <!-- Currencies & Supported Banks Strip -->
                        <div class="khqr-footer-strip">
                          <div class="khqr-curr-pills">
                            <span class="curr-pill">USD ($)</span>
                            <span class="curr-pill">KHR (៛)</span>
                          </div>
                          <span class="khqr-compat-text">{{ invitation.giftAccounts[activeQrTab].note }}</span>
                        </div>

                      </div>
                    </div>

                    <!-- Download QR Action Button -->
                    <div class="gift-actions-row anim-item" style="transition-delay: 0.35s">
                      <a
                        :href="activeQrTab === 'groom' ? cardGroomKhqr : cardBrideKhqr"
                        :download="`KHQR_${activeQrTab === 'groom' ? 'Him_Somnang' : 'Khorn_Saren'}.png`"
                        class="gift-download-btn"
                      >
                        <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                          <polyline points="7 10 12 15 17 10"></polyline>
                          <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                        <span>រក្សាទុករូបភាព QR (Save QR)</span>
                      </a>
                    </div>

                    <!-- Subtle Gold Divider -->
                    <div class="gift-bottom-divider anim-item" style="transition-delay: 0.4s">
                      <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
                    </div>

                  </div>
                </section>

                <!-- PAGE 6: Words of Gratitude Section (សេចក្តីថ្លែងអំណរគុណ) -->
                <section class="snap-page section-thanks" id="page-thanks" :class="{ 'section-animate-in': isThanksInView }">
                  <div class="page-content-wrapper thanks-page-content">

                    <!-- Title Header -->
                    <div class="thanks-header-wrapper anim-item" style="transition-delay: 0.1s">
                      <div class="thanks-title-row">
                        <span class="thanks-ornament-wing ornament-left"></span>
                        <h2 class="section-title thanks-title-header">
                          <img
                            :src="thanksTitleKhmerImg"
                            :alt="invitation.thanksTitle"
                            class="thanks-title-img"
                          />
                        </h2>
                        <span class="thanks-ornament-wing ornament-right"></span>
                      </div>
                     
                    </div>

                    <!-- Luxury Gratitude Card -->
                    <div class="thanks-card-container anim-item" style="transition-delay: 0.25s">
                      <div class="thanks-gold-frame">
                        <!-- 3D Gold Khmer Corner Ornaments -->
                        <img :src="corner3dTl" alt="3D Khmer Corner TL" class="thanks-kbach-corner thanks-kbach-corner-tl" />
                        <img :src="corner3dTr" alt="3D Khmer Corner TR" class="thanks-kbach-corner thanks-kbach-corner-tr" />
                        <img :src="corner3dBl" alt="3D Khmer Corner BL" class="thanks-kbach-corner thanks-kbach-corner-bl" />
                        <img :src="corner3dBr" alt="3D Khmer Corner BR" class="thanks-kbach-corner thanks-kbach-corner-br" />

                        <!-- Monogram Crest -->
                        <div class="thanks-crest-box">
                          <img :src="monogramCrestImg" alt="Wedding Monogram Crest" class="thanks-crest-img" />
                        </div>

                        <!-- Couple Names Banner -->
                        <div class="thanks-couple-names">
                          <span class="thanks-groom">{{ invitation.groomName }}</span>
                          <span class="thanks-heart">❦</span>
                          <span class="thanks-bride">{{ invitation.brideName }}</span>
                        </div>

                        <div class="thanks-divider">
                          <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
                        </div>

                        <!-- Paragraph 1: Respectful Gratitude to Guests -->
                        <p class="thanks-text-para thanks-para-1">
                          {{ invitation.thanksPara1 }}
                        </p>

                        <!-- The 4 Traditional Buddhist Blessings (ពរទាំងបួនប្រការ) -->
                        <div class="thanks-blessings-card">
                          <div class="blessings-header-line">
                            <span class="blessings-tag">ពរទាំងបួនប្រការ</span>
                          </div>
                          <div class="thanks-blessings-grid">
                            <div class="blessing-pill">
                              <span class="blessing-kh">អាយុ</span>
                              <span class="blessing-en">Longevity</span>
                            </div>
                            <div class="blessing-pill">
                              <span class="blessing-kh">វណ្ណៈ</span>
                              <span class="blessing-en">Beauty</span>
                            </div>
                            <div class="blessing-pill">
                              <span class="blessing-kh">សុខៈ</span>
                              <span class="blessing-en">Happiness</span>
                            </div>
                            <div class="blessing-pill">
                              <span class="blessing-kh">ពលៈ</span>
                              <span class="blessing-en">Strength</span>
                            </div>
                          </div>
                        </div>

                        <!-- Paragraph 2: Best Wishes & Blessings -->
                        <p class="thanks-text-para thanks-para-2">
                          {{ invitation.thanksPara2 }}
                        </p>

                        <div class="thanks-divider">
                          <img :src="goldDividerImg" alt="Gold Wedding Divider" class="divider-graphic" />
                        </div>

                        <!-- Respectful Closing -->
                        <div class="thanks-closing-wrapper">
                          <span class="thanks-closing-text">{{ invitation.thanksClosing }}</span>
                
                        </div>

                        <!-- Signatures of Parents -->
                        <div class="thanks-parents-row">
                          <div class="thanks-parent-col">
                            <span class="thanks-parent-title">មាតាបិតាខាងកូនប្រុស</span>
                            <span class="thanks-parent-names">{{ invitation.groomFather.role }} {{ invitation.groomFather.name }}</span>
                            <span class="thanks-parent-names">{{ invitation.groomMother.role }} {{ invitation.groomMother.name }}</span>
                          </div>
                          <div class="thanks-parent-col">
                            <span class="thanks-parent-title">មាតាបិតាខាងកូនស្រី</span>
                            <span class="thanks-parent-names">{{ invitation.brideFather.role }} {{ invitation.brideFather.name }}</span>
                            <span class="thanks-parent-names">{{ invitation.brideMother.role }} {{ invitation.brideMother.name }}</span>
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
                  <div class="chevrons" :class="{ 'is-flipped': isThanksInView }">
                    <svg class="chevron" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
                    <svg class="chevron" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
                  </div>
                  <span class="scroll-up-text">{{ isThanksInView ? 'ត្រឡប់ទៅលើ' : invitation.scrollUpText }}</span>
                </div>
                <div class="action-buttons">
                  <button class="action-btn" :class="{ 'is-active': isCoverInView }" @click="scrollToPage('cover')" title="Calendar / Date"><img :src="btnCalendar" alt="Calendar" class="action-icon" /></button>
                  <button class="action-btn" :class="{ 'is-active': isAgendaInView }" @click="scrollToPage('agenda')" title="Agenda"><img :src="agendaIcons.hall" alt="Agenda" class="action-icon" /></button>
                  <button class="action-btn" :class="{ 'is-active': isLocationInView }" @click="scrollToPage('location')" title="Location"><img :src="goldMapImg" alt="Location" class="action-icon" /></button>
                  <button class="action-btn" :class="{ 'is-active': isGalleryInView }" @click="scrollToPage('gallery')" title="Gallery"><img :src="btnGallery" alt="Gallery" class="action-icon" /></button>
                  <button class="action-btn" :class="{ 'is-active': isGiftInView }" @click="scrollToPage('gift')" title="QR Gift"><img :src="btnQR" alt="QR Gift" class="action-icon" /></button>
                  <button class="action-btn" :class="{ 'is-active': isThanksInView }" @click="scrollToPage('thanks')" title="Gratitude"><img :src="btnWishes" alt="Gratitude" class="action-icon" /></button>
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

    <!-- Fullscreen Gallery Lightbox Modal -->
    <Transition name="lightbox-fade">
      <div
        v-if="activeLightboxIndex !== null"
        class="gallery-lightbox-modal"
        @click.self="closeLightbox"
      >
        <button class="lightbox-close-btn" @click="closeLightbox" title="Close">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
          </svg>
        </button>

        <div class="lightbox-content-box">
          <button class="lightbox-nav-btn btn-prev" @click.stop="prevPhoto" title="Previous Photo">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
              <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
            </svg>
          </button>

          <div class="lightbox-img-wrapper">
            <!-- Lightbox Golden Loading Indicator -->
            <div v-if="isLightboxLoading" class="lightbox-loading-overlay">
              <div class="lightbox-spinner-ring"></div>
              <span class="lightbox-loading-text">កំពុងផ្ទុករូបភាព...</span>
            </div>

            <img
              :src="galleryPhotos[activeLightboxIndex].src"
              :alt="galleryPhotos[activeLightboxIndex].alt"
              class="lightbox-main-img"
              :class="{ 'is-loaded': !isLightboxLoading }"
              @load="onLightboxImgLoad"
            />
            <div class="lightbox-caption-bar">
              <span class="lightbox-counter">{{ toKhmerNumber(String(activeLightboxIndex + 1)) }} / {{ toKhmerNumber(String(galleryPhotos.length)) }}</span>
              <span class="lightbox-caption-text">{{ galleryPhotos[activeLightboxIndex].caption }}</span>
            </div>
          </div>

          <button class="lightbox-nav-btn btn-next" @click.stop="nextPhoto" title="Next Photo">
            <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
              <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
            </svg>
          </button>
        </div>
      </div>
    </Transition>

    <!-- Zoomed QR Code Modal -->
    <Transition name="lightbox-fade">
      <div v-if="zoomedQr" class="qr-zoom-modal" @click="closeZoomQr">
        <button class="lightbox-close-btn" @click="closeZoomQr" title="Close">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
          </svg>
        </button>
        <div class="qr-zoom-box" @click.stop>
          <img :src="zoomedQr" class="qr-zoom-img" alt="Zoomed KHQR" />
          <div class="qr-zoom-footer">
            <span class="qr-zoom-text">{{ activeQrTab === 'groom' ? invitation.giftAccounts.groom.nameKh : invitation.giftAccounts.bride.nameKh }}</span>
            <span class="qr-zoom-sub">{{ activeQrTab === 'groom' ? invitation.giftAccounts.groom.accountNumber : invitation.giftAccounts.bride.accountNumber }}</span>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Copied Toast Notification -->
    <Transition name="toast-fade">
      <div v-if="copiedNotice" class="copied-toast">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
        <span>{{ copiedNotice }}</span>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

// ── Envelope imports ──
import { weddingText } from '@/data/weddingText.js'
import weddingTitleKhmerImg from '@/assets/wedding_title_khmer_transparent.png'
import soamKouropAnjeyImg from '@/assets/soam_kourop_anjey_transparent.png'
import agendaTitleKhmerImg from '@/assets/agenda_title_khmer_transparent.png'
import locationTitleKhmerImg from '@/assets/location_title_khmer_transparent.png'
import galleryTitleKhmerImg from '@/assets/gallery_title_khmer_transparent.png'
import thanksTitleKhmerImg from '@/assets/thanks_title_khmer_transparent.png'
import galleryBannerImg from '@/assets/gallery/album_01_banner.webp'
import gallery01Img from '@/assets/gallery/gallery_01_royal.webp'
import gallery02Img from '@/assets/gallery/gallery_02_traditional.webp'
import gallery03Img from '@/assets/gallery/gallery_03_modern.webp'
import gallery04Img from '@/assets/gallery/gallery_04_sunset.webp'
import gallery05Img from '@/assets/gallery/gallery_05_intimate.webp'
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
import goldMapImg from '@/assets/gold_map.webp'
import btnGallery from '@/assets/items/btn_gallery.svg'
import btnQR from '@/assets/items/btn_qr.svg'
import btnWishes from '@/assets/items/btn_wishes.svg'
import qrGroomImg from '@/assets/qr/qr_groom_khqr.png'
import qrBrideImg from '@/assets/qr/qr_bride_khqr.png'
import cardGroomKhqr from '@/assets/qr/card_groom_khqr.png'
import cardBrideKhqr from '@/assets/qr/card_bride_khqr.png'
import corner3dTl from '@/assets/items/khmer_corner_gold_3d_tl.png'
import corner3dTr from '@/assets/items/khmer_corner_gold_3d_tr.png'
import corner3dBl from '@/assets/items/khmer_corner_gold_3d_bl.png'
import corner3dBr from '@/assets/items/khmer_corner_gold_3d_br.png'
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
const isDisappearingOther = ref(false)
const isAnimatingCover = ref(false)
const showInvitation = ref(false)
const sealVideoRef = ref(null)
const isVideoPlaying = ref(false)
let currentGlideAnim = null
let returnTimer = null
let videoFallbackTimer = null
let videoTimeCheckInterval = null

// ── 5-Second Transition, Light Leak & Ambient Particles State ──
const isLightLeakActive = ref(false)
const isLightLeakFadingOut = ref(false)
const hasTriggeredCoverTransition = ref(false)
const sparklesCanvasRef = ref(null)
let particlesAnimId = null

const envelopeSealRef = ref(null)
const coverSealBoxRef = ref(null)
const coverSealImgRef = ref(null)

// ── Main invitation state ──
const agendaIcons = { welcome: iconWelcome, fruit: iconFruit, hall: iconHall, monks: iconMonks, haircut: iconHaircut, thread: iconThread, lunch: iconLunch, banquet: iconBanquet }
const timeLeft = ref({ days: 0, hours: 0, mins: 0, secs: 0 })
const isCoverInView = ref(false)
const isAgendaInView = ref(false)
const isLocationInView = ref(false)
const isGalleryInView = ref(false)
const isGiftInView = ref(false)
const isThanksInView = ref(false)
const activeQrTab = ref('groom')
const copiedNotice = ref('')
const zoomedQr = ref(null)

const galleryPhotos = [
  {
    src: galleryBannerImg,
    alt: 'Angkor Wat Royal Blessing',
    caption: 'ពិធីហែជំនូនមុខប្រាសាទអង្គរវត្តដ៏ពិសិដ្ឋ'
  },
  {
    src: gallery01Img,
    alt: 'Royal Attire Portrait',
    caption: 'សម្លៀកបំពាក់ប្រពៃណីព្រះរាជទ្រព្យ'
  },
  {
    src: gallery02Img,
    alt: 'Traditional Purple Splendor',
    caption: 'សម្រស់ផ្កាពណ៌ស្វាយនៃក្តីស្រឡាញ់'
  },
  {
    src: gallery03Img,
    alt: 'Modern Wedding Elegance',
    caption: 'រ៉ូបកូនក្រមុំពណ៌សដ៏ប្រណិត'
  },
  {
    src: gallery04Img,
    alt: 'Sunset Romance',
    caption: 'ស្នាមញញឹមក្រោមពន្លឺថ្ងៃរៀបលិច'
  },
  {
    src: gallery05Img,
    alt: 'Intimate Royal Moment',
    caption: 'អនុស្សាវរីយ៍ដ៏ផ្អែមល្ហែមរវាងគូស្នេហ៍'
  }
]

const loadedPhotos = ref({})
const isLightboxLoading = ref(false)

const onPhotoLoad = (idx) => {
  loadedPhotos.value[idx] = true
}

const onLightboxImgLoad = () => {
  isLightboxLoading.value = false
}

const activeLightboxIndex = ref(null)

const openLightbox = (index) => {
  isLightboxLoading.value = true
  activeLightboxIndex.value = index
}

const closeLightbox = () => {
  activeLightboxIndex.value = null
  isLightboxLoading.value = false
}

const prevPhoto = () => {
  if (activeLightboxIndex.value !== null) {
    isLightboxLoading.value = true
    activeLightboxIndex.value = (activeLightboxIndex.value - 1 + galleryPhotos.length) % galleryPhotos.length
  }
}

const nextPhoto = () => {
  if (activeLightboxIndex.value !== null) {
    isLightboxLoading.value = true
    activeLightboxIndex.value = (activeLightboxIndex.value + 1) % galleryPhotos.length
  }
}

const onKeyDown = (e) => {
  if (activeLightboxIndex.value === null) return
  if (e.key === 'Escape') closeLightbox()
  if (e.key === 'ArrowLeft') prevPhoto()
  if (e.key === 'ArrowRight') nextPhoto()
}
let timerInterval = null
let observer = null

const toKhmerNumber = (numStr) => {
  const khmerDigits = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩']
  return String(numStr).replace(/\d/g, (d) => khmerDigits[d])
}

const scrollToNextPage = () => {
  const container = document.querySelector('.invitation-card')
  if (!container) return
  if (isThanksInView.value || (container.scrollTop + container.clientHeight >= container.scrollHeight - 60)) {
    const coverEl = document.getElementById('page-cover')
    if (coverEl) {
      coverEl.scrollIntoView({ behavior: 'smooth' })
    } else {
      container.scrollTo({ top: 0, behavior: 'smooth' })
    }
  } else {
    container.scrollBy({ top: window.innerHeight * 0.85, behavior: 'smooth' })
  }
}

const scrollToPage = (pageId) => {
  const el = document.getElementById(`page-${pageId}`)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
  }
}

const onCardScroll = (e) => {
  if (e.target && e.target.scrollLeft !== 0) {
    e.target.scrollLeft = 0
  }
}

const setupScrollObserver = () => {
  setTimeout(() => {
    const cardEl = document.querySelector('.invitation-card')
    if (cardEl && cardEl.scrollLeft !== 0) cardEl.scrollLeft = 0

    const coverEl = document.getElementById('page-cover')
    const agendaEl = document.getElementById('page-agenda')
    const locationEl = document.getElementById('page-location')
    const galleryEl = document.getElementById('page-gallery')
    const giftEl = document.getElementById('page-gift')
    const thanksEl = document.getElementById('page-thanks')
    
    if (observer) observer.disconnect()
    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.target.id === 'page-cover') isCoverInView.value = entry.isIntersecting
        if (entry.target.id === 'page-agenda') isAgendaInView.value = entry.isIntersecting
        if (entry.target.id === 'page-location') isLocationInView.value = entry.isIntersecting
        if (entry.target.id === 'page-gallery') isGalleryInView.value = entry.isIntersecting
        if (entry.target.id === 'page-gift') isGiftInView.value = entry.isIntersecting
        if (entry.target.id === 'page-thanks') isThanksInView.value = entry.isIntersecting
      })
    }, { root: document.querySelector('.invitation-card'), threshold: 0.25 })
    if (coverEl) observer.observe(coverEl)
    if (agendaEl) observer.observe(agendaEl)
    if (locationEl) observer.observe(locationEl)
    if (galleryEl) observer.observe(galleryEl)
    if (giftEl) observer.observe(giftEl)
    if (thanksEl) observer.observe(thanksEl)
  }, 150)
}

const copyAccountNumber = async (accNum) => {
  try {
    await navigator.clipboard.writeText(accNum.replace(/\s+/g, ''))
    copiedNotice.value = 'បានចម្លងលេខគណនីរួចរាល់!'
    setTimeout(() => { copiedNotice.value = '' }, 2500)
  } catch (e) {
    copiedNotice.value = 'លេខគណនី: ' + accNum
    setTimeout(() => { copiedNotice.value = '' }, 3000)
  }
}

const zoomQr = (src) => { zoomedQr.value = src }
const closeZoomQr = () => { zoomedQr.value = null }


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

// ── Ambient Floating Particles & Sparkles Simulation ──
const initAmbientParticles = () => {
  const canvas = sparklesCanvasRef.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  const dpr = Math.min(window.devicePixelRatio || 1, 2)
  const rect = canvas.getBoundingClientRect()
  const w = (rect.width || 420) * dpr
  const h = (rect.height || 750) * dpr
  canvas.width = w
  canvas.height = h

  const numParticles = 42
  const particles = []

  for (let i = 0; i < numParticles; i++) {
    const isSparkle = Math.random() < 0.28
    particles.push({
      x: Math.random() * w,
      y: Math.random() * h,
      radius: (Math.random() * 1.6 + 1.2) * dpr,
      vx: (Math.random() - 0.5) * 0.22 * dpr,
      vy: -(Math.random() * 0.32 + 0.14) * dpr, // gentle upward floating dust
      baseAlpha: Math.random() * 0.45 + 0.25,
      pulseSpeed: Math.random() * 0.025 + 0.015,
      pulseOffset: Math.random() * Math.PI * 2,
      isSparkle,
      sparkleAngle: Math.random() * Math.PI,
      rotSpeed: (Math.random() - 0.5) * 0.015
    })
  }

  const drawDiamondSparkle = (cx, cy, size, alpha, angle) => {
    ctx.save()
    ctx.translate(cx, cy)
    ctx.rotate(angle)
    ctx.beginPath()
    const rOuter = size * 1.9
    const rInner = size * 0.35
    for (let i = 0; i < 4; i++) {
      const a = (i * Math.PI) / 2
      ctx.lineTo(Math.cos(a) * rOuter, Math.sin(a) * rOuter)
      ctx.lineTo(Math.cos(a + Math.PI / 4) * rInner, Math.sin(a + Math.PI / 4) * rInner)
    }
    ctx.closePath()
    ctx.fillStyle = `rgba(255, 250, 220, ${alpha})`
    ctx.shadowColor = 'rgba(255, 225, 120, 0.75)'
    ctx.shadowBlur = 6 * dpr
    ctx.fill()
    ctx.restore()
  }

  const render = (time) => {
    if (!showInvitation.value) return
    ctx.clearRect(0, 0, w, h)

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i]
      p.x += p.vx
      p.y += p.vy
      p.sparkleAngle += p.rotSpeed

      if (p.y < -15) p.y = h + 15
      if (p.x < -15) p.x = w + 15
      if (p.x > w + 15) p.x = -15

      const currentAlpha = Math.max(0.1, Math.min(0.85, p.baseAlpha + Math.sin(time * 0.002 * p.pulseSpeed * 60 + p.pulseOffset) * 0.3))

      if (p.isSparkle) {
        drawDiamondSparkle(p.x, p.y, p.radius * 1.5, currentAlpha, p.sparkleAngle)
      } else {
        const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius * 2.2)
        grad.addColorStop(0, `rgba(255, 252, 230, ${currentAlpha})`)
        grad.addColorStop(0.5, `rgba(254, 230, 140, ${currentAlpha * 0.6})`)
        grad.addColorStop(1, 'rgba(212, 175, 55, 0)')

        ctx.beginPath()
        ctx.arc(p.x, p.y, p.radius * 2.2, 0, Math.PI * 2)
        ctx.fillStyle = grad
        ctx.fill()
      }
    }

    particlesAnimId = requestAnimationFrame(render)
  }

  if (particlesAnimId) cancelAnimationFrame(particlesAnimId)
  particlesAnimId = requestAnimationFrame(render)
}

// ── 5-Second Transition & Light Leak Crossfade Logic ──
const triggerCoverTransition = () => {
  if (hasTriggeredCoverTransition.value || showInvitation.value) return
  hasTriggeredCoverTransition.value = true

  // Step 1: Soft glowing light leak & warm white/gold flash blooms across the screen
  isLightLeakActive.value = true
  isLightLeakFadingOut.value = false

  // Step 2: At the light bloom crest (~250ms), dissolve & crossfade the cover page into view
  setTimeout(() => {
    showInvitation.value = true
    isCoverInView.value = true

    updateCountdown()
    if (timerInterval) clearInterval(timerInterval)
    timerInterval = setInterval(updateCountdown, 1000)

    nextTick(() => {
      const cardContainer = document.querySelector('.invitation-card')
      if (cardContainer) cardContainer.scrollTop = 0
      const coverEl = document.getElementById('page-cover')
      if (coverEl) coverEl.scrollIntoView({ behavior: 'auto' })
      setupScrollObserver()
      initAmbientParticles()
    })
  }, 250)

  // Step 3: Gently fade out the light leak, seamlessly revealing the cover page
  setTimeout(() => {
    isLightLeakFadingOut.value = true
    if (sealVideoRef.value) {
      try { sealVideoRef.value.pause() } catch (e) {}
    }
  }, 750)

  // Step 4: Finalize transition
  setTimeout(() => {
    isLightLeakActive.value = false
    isLightLeakFadingOut.value = false
    isVideoPlaying.value = false
    if (videoTimeCheckInterval) {
      clearInterval(videoTimeCheckInterval)
      videoTimeCheckInterval = null
    }
  }, 1600)
}

const onVideoTimeUpdate = () => {
  if (sealVideoRef.value && !hasTriggeredCoverTransition.value && isVideoPlaying.value) {
    // Exactly at the 5-second mark (5.0s) of the peacock video
    if (sealVideoRef.value.currentTime >= 5.0) {
      triggerCoverTransition()
    }
  }
}

const onVideoEnded = () => {
  if (showInvitation.value) return
  if (videoFallbackTimer) clearTimeout(videoFallbackTimer)
  triggerCoverTransition()
}

const openCover = async () => {
  if (isCoverOpen.value || isAnimatingCover.value) return
  isReturning.value = false
  clearTimeout(returnTimer)
  isAnimatingCover.value = true

  // Start video synchronously on user tap
  if (sealVideoRef.value) {
    sealVideoRef.value.currentTime = 0
    sealVideoRef.value.muted = false
    const playPromise = sealVideoRef.value.play()
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        // Fallback to muted playback if audio is restricted
        if (sealVideoRef.value) {
          sealVideoRef.value.muted = true
          sealVideoRef.value.play().catch(e => console.log('Autoplay error:', e))
        }
      })
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
  await new Promise(resolve => setTimeout(resolve, 350))

  try {
    currentGlideAnim = coverSealEl.animate(
      [
        { transform: 'translate(0px, 0px) scale(1)', filter: 'drop-shadow(0 14px 28px rgba(60, 42, 10, 0.5))', offset: 0 },
        { transform: `translate(${deltaX * 0.38}px, ${deltaY * 0.42}px) scale(${1 - (1 - targetScale) * 0.68})`, filter: 'drop-shadow(0 10px 20px rgba(60, 42, 10, 0.48))', offset: 0.45 },
        { transform: `translate(${deltaX}px, ${deltaY}px) scale(${targetScale})`, filter: 'drop-shadow(0 6px 12px rgba(60, 42, 10, 0.45))', offset: 1 }
      ],
      { duration: 850, easing: 'cubic-bezier(0.22, 1, 0.36, 1)', fill: 'forwards' }
    )
    await currentGlideAnim.finished
    await new Promise(resolve => setTimeout(resolve, 60))

    isCoverOpen.value = true
    await new Promise(resolve => setTimeout(resolve, 350))
    isOpen.value = true
    isVideoPlaying.value = true
    hasTriggeredCoverTransition.value = false

    // Restart from beginning so peacock video plays smoothly while envelope is open
    if (sealVideoRef.value) {
      sealVideoRef.value.currentTime = 0
      sealVideoRef.value.play().catch(e => console.log('Video play error:', e))
    }

    // High-resolution interval check for exactly the 5.0s transition mark
    if (videoTimeCheckInterval) clearInterval(videoTimeCheckInterval)
    videoTimeCheckInterval = setInterval(() => {
      if (sealVideoRef.value && !hasTriggeredCoverTransition.value && isVideoPlaying.value) {
        if (sealVideoRef.value.currentTime >= 5.0) {
          triggerCoverTransition()
        }
      }
    }, 40)

    // Safety fallback timer
    clearTimeout(videoFallbackTimer)
    videoFallbackTimer = setTimeout(() => {
      if (isVideoPlaying.value && !showInvitation.value) {
        triggerCoverTransition()
      }
    }, 6000)

  } catch (err) {
    isCoverOpen.value = true
    isOpen.value = true
    triggerCoverTransition()
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
  if (videoFallbackTimer) clearTimeout(videoFallbackTimer)
  if (videoTimeCheckInterval) {
    clearInterval(videoTimeCheckInterval)
    videoTimeCheckInterval = null
  }
  if (particlesAnimId) {
    cancelAnimationFrame(particlesAnimId)
    particlesAnimId = null
  }
  if (sealVideoRef.value) {
    try {
      sealVideoRef.value.pause()
      sealVideoRef.value.currentTime = 0
    } catch (e) {}
  }
  hasTriggeredCoverTransition.value = false
  isLightLeakActive.value = false
  isLightLeakFadingOut.value = false
  isVideoPlaying.value = false
  isCoverInView.value = false
  showInvitation.value = false
  isReturning.value = true
  isCoverOpen.value = false
  isOpen.value = false
  isDisappearingOther.value = false
  isAnimatingCover.value = false
  clearTimeout(returnTimer)
  returnTimer = setTimeout(() => { isReturning.value = false }, 3500)
}

const toggleEnvelope = () => {
  if (isVideoPlaying.value || showInvitation.value) return
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

onMounted(() => {
  window.addEventListener('keydown', onKeyDown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', onKeyDown)
  if (timerInterval) clearInterval(timerInterval)
  if (videoFallbackTimer) clearTimeout(videoFallbackTimer)
  if (videoTimeCheckInterval) clearInterval(videoTimeCheckInterval)
  if (particlesAnimId) cancelAnimationFrame(particlesAnimId)
  if (observer) observer.disconnect()
})
</script>
