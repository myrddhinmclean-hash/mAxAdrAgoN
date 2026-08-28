# mAxAdrAgoN — Lair Governance

**Last updated:** on the date you post this
**Status of project:** Phase 0 and Phase 1 COMPLETE. Site live. First hoard entry published. No active phases — next work begins by the activation rule in §9.

**Primary reasoning agent:** Claude. Claude handles all high-reasoning tasks — drafting, excavation lens work, editorial second opinions, phase-transition analysis. Other agents serve mechanical or archival roles only. Claude's *reasoning* scope is never capped; only its *output* scope is (see §4).

---

## 1. THE BRAND IN ONE PARAGRAPH

mAxAdrAgoN is a dragon who hoards knowledge instead of gold. The premise: complex things that intimidate people are usually ordinary ideas behind heavy curtains, and Max's job is to pull the curtains and translate what's actually happening into plain speech. The lair is the site; the Hoards are the rooms:

- **Draega Hoard** — myths, geography, tales from the D&D world of Draega
- **Machine Hoard** — technical systems, software, architecture, teardowns
- **Odd Hoard** — curiosities, paradoxes, edge cases, fragments

Divergence between topics is a feature, not a problem. The character is the brand; the topics are rooms in the lair. (This is the Arlo/One-persona, many-rooms model. Do not narrow the brand to one topic. Do not scatter it across unnamed platforms.)

---

## 2. LOCKED DECISIONS (do not re-litigate — see §2.1)

1. **Voice conceit:** the owner IS the excavator-narrator. First person, uncovering and commenting on material with opinions and asides. NO in-character scribe/archivist persona.
2. **Face:** a dragon avatar represents Max visually. Voice = the owner, face = the avatar.
3. **AI stance:** anti-slop is FUNCTIONAL, not branded. The site reads like a human made it because the owner's ear filters everything. No summary or excerpt may reference AI at all. We never market on "no AI slop."
4. **Summaries are the owner's.** Agents draft bodies; the owner writes or approves every excerpt/summary. These are the highest-visibility words on the site.
5. **Publishing cadence:** none. No streaks, no schedules, no quotas of any kind. Gates only — progress is measured in finished entries, not calendar weeks.
6. **WotC content is always free** (Fan Content Policy constraint). Any future paid offering lives in the Machine Hoard or elsewhere, never gatekept D&D material.

7. **Place Rule:** Whenever a prompt raises a question of place (naming, geography, culture, or location detail), consult the Draega world on World Anvil for inspiration before inventing. Where Draega canon exists, use it; where it's silent, invent in its idiom and log the invention as an assumption.

### 2.1 How a locked decision gets reopened

Locked decisions are not changed in passing, mid-task, or at 2am. To reopen one, the owner opens a dedicated decision session and logs the old rule, the proposed change, and the reason via `decision savor`. Until that entry exists, the rule stands as written.

---

## 3. THE VETO GATE (the core quality control)

Nothing is published that the owner has not read and approved. Workflow:

1. Claude drafts from source material (fact-bounded: invent nothing, note gaps instead of filling them)
2. Draft lands as a file; the owner reads it
3. Owner: APPROVE / EDIT (own hand) / VETO
4. Owner writes the summary/excerpt
5. Publishing checklist (§7) — which includes confirming the gate was passed — pushes it live
6. Editor notes stay out of the reader copy (see §8)

A draft may be 90% agent or 90% owner. Both count. The gate is the constant.

### 3.1 The gate's overflow drain

The gate requires a decision. Decision paralysis is a real outcome and has its own protocol:

- A draft the owner has read but left unacted-on is **cold**. At every phase transition, all cold drafts are re-read and decided, or vetoed without guilt. Cold drafts are not failures; they are the drain that keeps the gate from flooding.
- A working limit: no more than **3 unreviewed drafts** may exist at once. When the third lands, the next session — however short — is a gate session. This is a capacity limit, not a deadline.

---

## 4. AGENT ROLES (one prompt, one agent, one deliverable)

| Agent | Role | Scope |
|---|---|---|
| **Claude** | Chief Reasoner | Drafting (excavation/herald lenses), editorial analysis, phase-transition review. Reasoning scope uncapped; every brief still states exact files, exact deliverable, and "no other modifications." NEVER pushes. |
| **Antigravity** | Site Warden | All repo work: posting entries, layout fixes, pipeline changes. Works from the publishing checklist. The ONLY agent with push access. |
| **NotebookLM** | Archive | Source gathering, compendium maintenance, contradiction flagging. |
| **Codex** | Break-glass only | Only if Antigravity is blocked. Not a standing coder. |
| **Quorum / AmoebiX prism** | Gatekeepers | Consulted at PHASE TRANSITIONS only, not mid-phase. |

**Standing rule:** no agent receives a brief without an explicit file list and success criteria. If the prompt doesn't contain "no other modifications," it isn't ready to send. An agent's internal reasoning may be as deep as it needs; the delivered output must fit the brief exactly.

**Scope breach protocol:** a scope violation pauses that agent's write access immediately. It is restored after one clean, bounded task. A second violation restricts the agent permanently to read-only drafting or removes it. Breaches are logged in one line each.

---

## 5. AMOEBIX INTEGRATION

AmoebiX is the spine:

- `kernel dispatch / claim / complete` — the six-phase plan lives as task cards
- `sense tangent "..."` — stray ideas get parked here, NEVER acted on mid-task (this command IS the one-shelf-at-a-time protocol)
- `panel run --lens excavation` (or herald/quill) — draft generation
- `prism` / quorum lens — phase-transition second opinions only
- `decision savor` — log completed milestones and reopened locked decisions
- `backup` — auto-mirrors to Drive after panels/tasks/decisions; the publishing checklist includes confirming the mirror landed

**Custom lens:** `panel/lenses/excavation.md` — herald's fact-discipline + quill's voice rules + the excavation register (narrator uncovers and comments, never catalogs). Every draft includes an editor-only **source ledger**: primary sources, claims requiring verification, unresolved contradictions, and what is interpretation versus stated fact. Editor notes and source ledgers live in `<slug>.editor-notes.md` — NEVER in the entry body.

**Lens versioning:** prompts and lenses are treated as code. Any change to a lens requires a one-line entry in `panel/lenses/changelog.md` saying what changed and why, so quality drift can be rolled back.

**Degraded-mode rule:** without AmoebiX, a text editor and git are sufficient. The veto gate still applies.

---

## 6. TWO DOCUMENTS, ONE CONSTITUTION

This document governs principles. Tool-specific mechanics — git commands, URLs, `hoard.js` behavior, AmoebiX command syntax — live in **`OPERATIONS.md`** beside this file. Governance changes only at phase transitions or decision sessions; operations change whenever the tooling does. If this file contains a git command or a URL, it is out of date.

---

## 7. PUBLISHING CHECKLIST (works for humans and agents)

The full pipeline is in `OPERATIONS.md`. The governing steps, in order, are:

1. **VETO GATE PASSED** — owner has read and approved the draft body (approve/edit/veto)
2. Owner has written the summary/excerpt
3. Entry file created with correct frontmatter (real current date, correct hoard, owner's summary) and registered in `posts.json`, newest first
4. Antigravity validates before commit: `posts.json` parses, every registered slug resolves to a file, no editor notes in the body, footer disclaimer intact
5. Committed and pushed to live
6. Verified live: entry renders correctly, index updated, no editor notes visible
7. Confirm Drive mirror received the change

If anything is wrong after push: unlist or revert first, debug second. Nothing broken stays public while it's being diagnosed.

---

## 8. PIPELINE RULES (permanent)

- Editor notes and source ledgers live ONLY in `<slug>.editor-notes.md`. Source files never contain them. The renderer (`hoard.js`) strips stray note blocks at render time as defense-in-depth — but the primary rule is that they are never written into entry files at all.
- WotC Fan Content Policy disclaimer is in every page footer. It must stay.
- Date field: `date` is always the publish date. If lore-time matters for an entry, add an optional `lore_date` field — never bend `date` to mean both.

---

## 9. THE SIX-PHASE PLAN (gates, not dates)

- **Phase 0 — Lair Opens:** site live, disclaimered, handles claimed. ✅ DONE
- **Phase 1 — First Real Entry:** first Draega entry published, voice gate proven. ✅ DONE
- **Phase 2 — The Shelf Fills:** Draega entries only, this phase. Conversion jobs from the compendium (pulling existing lore into the voice), never creation jobs. **Activation rule:** the phase activates with one small act — pick one compendium item, issue one excavation brief. No schedule, no other ceremony. **DONE WHEN:** at least 3 Draega entries are live AND the owner has completed the full publish sequence twice from memory of the pipeline alone (no doc-consulting, no redesign). "Posting stops feeling like an event" is the felt confirmation of the gate, not the gate itself.
- **Phase 3 — First Contact:** share the URL in 2–3 existing communities. Not before Phase 2's gate clears — a shelf with three things reads as "a site with three posts," and strangers' silence would be misread as a verdict on the voice when it's a verdict on thinness. Watch what people click and quote. **DONE WHEN:** one stranger engages unprompted. If nobody does, the fix is better entries, not more platforms.
- **Phase 4 — The Voice Gets a Body:** one video (read an entry aloud, static avatar, one-take with silence-cuts). No editing beyond silence-cuts, no channel page work, no thumbnails before the decision. **DONE WHEN:** the video exists and the owner answers exactly one question in a `decision savor` entry: does the voice translate to audio, and is it worth doing again?
- **Phase 5 — Review, Don't Pivot:** what was enjoyed, what dropped, what engaged. Adjust Hoard weights. Parked items (AI training, avatar build, domain, any commercial question) are reconsidered HERE and only here.

**Phase transition protocol:** a phase ends when its gate is met, confirmed by a `decision savor` entry and (for phases 3+) a quorum pass. The AmoebiX log is the canonical state — not the owner's memory of it.

**Backlog:** lives in AmoebiX task cards, not in this document. If a specific task name appears here, this document is out of date.

---

## 10. EXECUTIVE-DYSFUNCTION PROTOCOLS (the part that keeps this alive)

1. Stray ideas → `sense tangent`, never a context switch
2. The veto gate replaces motivation — never "feel like writing"
3. One shelf at a time — including during phases: Phase 2 is Draega-only until its gate clears; obsessions in other rooms get parked like any other tangent
4. No streaks, no calendars, no quotas — gates only; silent weeks mean nothing
5. Cold drafts drain at phase transitions — paralysis has a protocol, not a guilt spiral
6. Quorum at phase transitions only
7. Agents get two sentences of scope — and if "no other modifications" isn't in the prompt, the prompt isn't ready
8. If multiple shelves appeal anyway, pick the one already densest in the compendium — momentum over novelty

---

## 11. WHAT THIS PROJECT IS NOT

- Not a content farm. No posting quota exists anywhere in this document — including quotas disguised as distribution rules.
- Not a rebrand-in-waiting. Platform migrations are explicitly rejected unless the current site fails a real need.
- Not the agent's site. Every agent here serves the gate; the owner decides what's treasure.
- Not a business — yet. Economic questions are parked to Phase 5 like everything else, and this document deliberately contains no monetization gates, KPIs, or "asset formation" rules. If that layer is ever added, it is added at Phase 5, by decision session, as its own document.













# mAxAdrAgoN — Lair Governance ADDENDUM v2.1

**Status:** Append this document after §11 of the Governance v2. Where an addendum item conflicts with the main document, **this addendum wins**. Logged by decision session per §2.1.

---

## A1. AUTHORSHIP AMENDMENT (supersedes the "conversion jobs, never creation jobs" rule in §9, Phase 2)

The owner does not author the world of Draega personally. The owner is **editor-in-chief**; agents are the **writers' room**.

- Creation jobs are now permitted alongside conversion jobs.
- The veto gate (§3) is the safeguard that replaces sole authorship: nothing is canon, and nothing is published, that has not passed the owner's gate. Agent-generated lore that passes the gate IS owner-approved by definition.
- The owner's current active goal is **building voice and standards through modules** — a small set of finished, published pieces that demonstrate what the voice sounds like, so that all future generation has a target to hit.

## A2. THE QUESTION-DRIVEN MODULE METHOD (new standing workflow)

New Draega modules are created through **structured interviews**: the reasoning agent (Claude) asks the owner questions; the owner answers; the agent shapes the answers into material.

**The loop:**

1. **Seed** — agent proposes a topic or asks an opening question (e.g., "What's the last thing a traveler sees before reaching the valley?")
2. **Answer** — the owner answers in any form: complete sentences, fragments, "I don't know, figure it out." All three are valid material.
3. **Shape & follow up** — the agent shapes what it heard, then asks the next question, prioritizing gaps in the material
4. **Draft** — when the interview has enough, the agent assembles a draft in the excavation register and delivers it to the gate with editor notes
5. **Gate** — standard §3 flow. Owner approves, edits, or vetoes.

**Rules of the method:**

- The agent asks; the owner answers; the agent never fills a silence with invention *during the interview*. "You decide" from the owner is the one exception — a delegated invention is then owner-sanctioned and marked as such in editor notes.
- Answers are canon. If a later draft contradicts something the owner said in an interview, the draft is wrong, not the answer.
- Interviews are themselves sources. A module built this way has a traceable provenance chain: *interview → draft → gate*. This satisfies §A4.

## A3. VOICE-FIRST SEQUENCING (order of operations)

1. **Now:** module track. Two or three published modules establish the demonstrated standard.
2. **Then:** open worldbuilding generation scales off that standard — every brief points at published entries as the voice target ("like that, not like that").
3. Worldbuilding agents **propose; the owner disposes.** Generated material arrives as a menu, never as canon-by-default.

## A4. PROVENANCE & CONTAMINATION RULES (permanent — arises from the compendium contamination event)

The master worldbuilding compendium (`draega-worldbuilding-compilation-v2.md`) was partially AI-filled during campaignOS/dmtoolbox generation. Its contents are **untrusted** until verified.

- **Contamination flag stands** on the compendium: nothing converts from it without source confirmation.
- **A source is only a source if it traces to something the owner wrote or can personally point at.** AI-filled summaries of the owner's materials are leads, not sources.
- **Recognition pass:** the owner skims the compendium and marks items real / unknown / false. The owner's memory outranks any agent's confidence. Unrecognized material is guilty until proven innocent.
- **Verification task** (NotebookLM): item-by-item pass, marking each claim VERIFIED / UNVERIFIED / FABRICATED-SUSPECT, report only, no other modifications. Runs after the owner's recognition pass narrows the list.
- **Generated lore is marked as generated until it passes the gate.** After the gate, it's canon — the gate is the provenance.
- The owner does not need to personally author lore for it to be trustworthy; the owner needs to have *approved* it. Approval is the provenance.

## A5. THE DRAEGA PODCAST (parked project card, recorded here so it isn't re-litigated)

- A recorded Draega campaign podcast exists, never published. It is a **separate pet project** with its own lifecycle (interest-building, scoping, planning, hardware) living **beside** the six phases, not inside them.
- It will tie into the site at **Phase 4 or later**. It does not affect current phases.
- **Verbal blessing from players exists, contingent on the podcast's release.** Honor it by not publishing other players' characters before the podcast is real. When release approaches, refresh the verbal yes once, cheaply.
- **Characters belonging to other players (e.g., Anjax Proudmane) are OFF the site backlog** until the podcast is released. They are podcast-project material, not lair material.
- Needs its own scoping session someday. Not scheduled. Parked.

## A6. CORRECTED BACKLOG (supersedes backlog items in prior conversation)

**Lair backlog — owner's material, convertible freely:**
- The Puzzle Wall (19 letters, copper ring, "Come, human, die by sword or spear")
- The Seasons Room
- The Boot Room
- The LIES puzzle
- Gladigow and the other Mysterious Monuments (source: Mysterious Monuments.pdf — verify provenance per §A4 before converting)
- The TerTah naming mystery
- Astrina's assassination, the six-year siege of Braaken, Session-material entries (all pending §A4 verification)

**Blocked pending podcast release (§A5):** Anjax and any other player-owned characters.

**Parked:** homepage/about framing, YouTube/Phase 4 decisions, podcast scoping, all commercial questions.

## A7. CURRENT STATE

- **Phase 2: active. Gate progress: 1 of 3 entries live** (The Druid's Temple in Shell Valley). Publish-sequence runs: 1 of 2.
- Next module(s) created via the §A2 interview method.
- Editorial posture: the owner curates; the gate decides; the voice accumulates one module at a time.

---

*End of addendum. Main governance (§1–§11) remains in force except as amended above.*