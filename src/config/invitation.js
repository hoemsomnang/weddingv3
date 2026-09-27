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
}

export default invitation
