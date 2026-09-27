/**
 * Wedding Invitation Text & Event Configuration
 * 
 * Edit any text or details below to easily customize the wedding information.
 */

export const invitation = {
  /* ── Couple ──────────────────────────────────────────────── */
  groomName: 'ហ៊ឹម សំណាង',
  brideName: 'ឃន សារ៉េន',

  /** Two initials shown inside the golden monogram crest */
  initials: ['ស', 'រ'],

  /* ── Parents ─────────────────────────────────────────────── */
  groomFather: { role: 'លោក', name: 'ហ៊ឹម លាង' },
  groomMother: { role: 'លោកស្រី', name: 'អ៊ុំ ស្រ៊ឺ' },
  brideFather: { role: 'លោក', name: 'អ៊ុង សារ៉េត' },
  brideMother: { role: 'លោកស្រី', name: 'ធា ម៉ុំ' },

  /* ── Couple Roles ────────────────────────────────────────── */
  groomRole: 'កូនប្រុសនាម',
  brideRole: 'កូនស្រីនាម',

  /* ── Page Heading ────────────────────────────────────────── */
  pageTitle: 'សិរីមង្គលអាពាហ៍ពិពាហ៍',

  /* ── Honor Invite Subtitle ───────────────────────────────── */
  honorInviteText: 'មានកិត្តិយសសូមគោរពអញ្ជើញ',

  /* ── Formal Invitation Body ──────────────────────────────── */
  invitationLines: [
    'សម្តេច ទ្រង់ ឯកឧត្តម អ្នកឧកញ៉ា ឧកញ៉ា លោកជំទាវ លោក លោកស្រី អ្នកនាងកញ្ញា អញ្ជើញចូលរួមជាអធិបតី និងជាភ្ញៀវកិត្តិយស ដើម្បីប្រសិទ្ធពរជ័យ សិរីសួស្តី ជ័យមង្គល ក្នុងពិធីរៀបអាពាហ៍ពិពាហ៍ កូនប្រុស-កូនស្រី របស់យើងខ្ញុំ',
  ],

  /* ── Wedding Date ────────────────────────────────────────── */
  /**
   * ISO date-time string used by the countdown timer.
   * Format: 'YYYY-MM-DDTHH:mm:ss'
   */
  targetDate: '2027-03-13T08:00:00',

  /** Khmer lunar calendar date line */
  lunarDate: 'នៅថ្ងៃសៅរ៍ ៦កើត ខែផល្គុន ឆ្នាំមមី អដ្ឋស័ក ពុទ្ធសករាជ ២៥៧០',

  /** Solar (Gregorian) date shown prominently */
  solarDate: 'ត្រូវនឹងថ្ងៃទី ១៣ ខែមីនា ឆ្នាំ ២០២៧',

  /** Time of the reception */
  receptionTime: 'វេលាម៉ោង ០៥ : ០០ ល្ងាចនៅ គេហដ្ឋាននៃសិរីមង្គលអាពាហ៍ពិពាហ៍ ស្ថិតនៅ ភូមិអូរល្វា ឃុំជ្រៃសីម៉ា ស្រុកសំពៅលូន ខេត្តបាត់ដំបង',

/** Human-readable date shown on the invitation card */
  dateDisplay: 'ថ្ងៃសៅរ៍ ទី១៣ ខែមីនា ឆ្នាំ២០២៧',

  /* ── Venue & Location ────────────────────────────────────── */
  venueTitle: 'ទីតាំងប្រារព្ធពិធី',
  venueName: 'គេហដ្ឋាននៃសិរីមង្គលអាពាហ៍ពិពាហ៍',
  venueAddress: 'ភូមិអូរល្វា ឃុំជ្រៃសីម៉ា ស្រុកសំពៅលូន ខេត្តបាត់ដំបង',
  venueReceptionTime: 'វេលាម៉ោង ០៥:០០ ល្ងាច',
  venueButtonText: 'បើកមើលលើ Google Maps',
  venueClosingWish: 'សូមគោរពអញ្ជើញភ្ញៀវកិត្តិយសទាំងអស់ដោយមេត្រីភាព',
  venueMapsUrl: 'https://maps.app.goo.gl/TZE8CuT46X9Ze9r28',
  venueEmbedUrl: 'https://maps.google.com/maps?q=13.489456,102.368097&hl=km&z=16&output=embed',

  /* ── Photo Gallery (វិចិត្រសាល) ────────────────────────────── */
  galleryTitle: 'វិចិត្រសាល',
  gallerySubtitle: 'MEMORIES OF LOVE',
  galleryWishes: 'ស្នាមញញឹមនៃក្តីស្រឡាញ់ និងអនុស្សាវរីយ៍ដ៏ផ្អែមល្ហែម',

  /* ── Photo Album Grid (កម្រងរូបភាព) ────────────────────────── */
  albumTitle: 'កម្រងរូបភាពអនុស្សាវរីយ៍',
  albumSubtitle: 'SWEET MEMORIES',
  albumWishes: 'ស្នាមញញឹម និងអនុស្សាវរីយ៍ដ៏មានតម្លៃមិនអាចបំភ្លេចបាន',

  /* ── Words of Gratitude / សេចក្តីថ្លែងអំណរគុណ ─────────────── */
  thanksTitle: 'សេចក្តីថ្លែងអំណរគុណ',
  thanksPara1: 'យើងខ្ញុំជាមាតាបិតានៃ កូនប្រុស-កូនស្រី\nសូមគោរពថ្លែងអំណរគុណយ៉ាងជ្រាលជ្រៅបំផុតចំពោះ ឯកឧត្តម លោកជំទាវ លោកអ្នកឧកញ៉ា អ្នកឧកញ៉ា ឧកញ៉ា លោក លោកស្រី អ្នកនាង កញ្ញា ដែលបានអញ្ជើញចូលរួមជាអធិបតី និងជាភ្ញៀវកិត្តិយសក្នុង ពិធីមង្គលអាពាហ៍ពិពាហ៍ កូនប្រុស-កូនស្រី យើងខ្ញុំ។',
  thanksPara2: 'យើងខ្ញុំសូមគោរពសម្តែងនូវការរំភើបចិត្តខ្ពង់ខ្ពស់បំផុតជូន ឯកឧត្តម លោកជំទាវ លោកអ្នកឧកញ៉ា អ្នកឧកញ៉ា ឧកញ៉ា លោក លោកស្រី អ្នកនាង កញ្ញា និងភ្ញៀវកិត្តិយស សូមទទួលបាននូវពរទាំងបួនប្រការគឺ\nអាយុ វណ្ណៈ សុខៈ ពលៈ កុំបីឃ្លៀងឃ្លាតឡើយ។',
  thanksClosing: 'សូមអរគុណ !',

  scrollUpText: 'អូសឡើងទៅលើ',

  /* ── Wedding Agenda / Program Schedule ─────────────────────── */
  agendaTitle: 'កាលវិភាគកម្មវិធី',
  agendaDays: [
    {
      dayTitle: 'កម្មវិធីសិរីមង្គលអាពាហ៍ពិពាហ៍',
      schedule: [
        { time: '០៦:៣០ ព្រឹក', icon: 'welcome', title: 'ជួបជុំភ្ញៀវកិត្តិយសទាំងអស់' },
        { time: '០៦:៤៥ ព្រឹក', icon: 'fruit',   title: 'ពិធីហែជំនូន(ផ្លែឈើ)' },
        { time: '០៧:១៥ ព្រឹក', icon: 'hall',    title: 'កូនកំលោះចូលរោងជ័យ(សំពះ)' },
        { time: '០៨:៣០ ព្រឹក', icon: 'monks',   title: 'ពិធីសូត្រមន្តចម្រើនព្រះបរិត្ត' },
        { time: '០៩:៣០ ព្រឹក', icon: 'haircut', title: 'ពិធីកាត់សក់បង្កក់សិរី' },
        { time: '១០:១៥ ព្រឹក', icon: 'thread',  title: 'ពិធីសែនចងដៃកូនចៅ' },
        { time: '១១:១៥ ថ្ងៃត្រង់', icon: 'lunch',   title: 'អញ្ជើញភ្ញៀវកិត្តិយសពិសាអាហារថ្ងៃត្រង់' },
        { time: '០៥:០០ ល្ងាច', icon: 'banquet', title: 'អញ្ជើញភ្ញៀវកិត្តិយសពិសាភោជនាហារពេលល្ងាច ដោយមេត្រីភាព' },
      ],
      notice: '',
    },
  ],

  /* ── Khmer Text ──────────────────────────────────────────── */
  /** Main heading in Khmer (above logo) */
  khmerGreeting: 'សិរីមង្គលអាពាហ៍ពិពាហ៍',

  /** Subtitle lines in Khmer (below logo) */
  khmerSubtitle: [
    'សូមគោរពអញ្ជើញចូលរួម',
  ],

  /** "Save The Date" label above the date (in Khmer) */
  saveTheDateLabel: 'កាលបរិច្ឆេទថ្ងៃមង្គល',

  /* ── Honored Guest & Open Invitation ─────────────────────── */
  guestHonorLabel: 'ភ្ញៀវកិត្តិយស',
  btnOpenInvitation: 'សូមចុចបើកសំបុត្រ',
  openInvitationAlert: 'សូមស្វាគមន៍មកកាន់ពិធីមង្គលការរបស់យើងខ្ញុំ! 💍✨',


  /* ── Studio Branding ─────────────────────────────────────── */
  watermark: 'សំបុត្រអញ្ជើញឌីជីថល ដោយ SAMBOT ONLINE',

  /* ── Countdown Unit Labels ───────────────────────────────── */
  countdownLabels: {
    days: 'ថ្ងៃ',
    hours: 'ម៉ោង',
    mins: 'នាទី',
    secs: 'វិនាទី',
  },

  /* ── UI Strings & Alerts ─────────────────────────────────── */
  scrollHintText: 'អូសចុះក្រោម',
  rsvpAlertMessage: 'ទំព័រឆ្លើយតប (RSVP) នឹងមកដល់ឆាប់ៗនេះ! 💌',
  calendarDetails: 'សូមគោរពអញ្ជើញចូលរួមអបអរសាទរក្នុងថ្ងៃមង្គលការដ៏វិសេសវិសាលរបស់យើងខ្ញុំ!',

  /* ── RSVP Button ─────────────────────────────────────────── */
  /** Text labels for the action buttons */
  btnRsvpLabel:     '💌 ឆ្លើយតបការចូលរួម',
  btnCalendarLabel: '📅 កត់ត្រាប្រតិទិន',

  /**
   * Google Calendar event duration in hours (from targetDate).
   * Default: 6 hours.
   */
  eventDurationHours: 6,
}

export default invitation
