\# mAxAdrAgoN — Lair Governance



\*\*Last updated:\*\* on the date you post this

\*\*Status of project:\*\* Phase 0 and Phase 1 COMPLETE. Site live. First hoard

entry published. No active phases — next work begins when the owner decides.



\---



\## 1. THE BRAND IN ONE PARAGRAPH



mAxAdrAgoN is a dragon who hoards knowledge instead of gold. The premise:

complex things that intimidate people are usually ordinary ideas behind heavy

curtains, and Max's job is to pull the curtains and translate what's actually

happening into plain speech. The lair is the site; the Hoards are the rooms:



\- \*\*Draega Hoard\*\* — myths, geography, tales from the D\&D world of Draega

\- \*\*Machine Hoard\*\* — technical systems, software, architecture, teardowns

\- \*\*Odd Hoard\*\* — curiosities, paradoxes, edge cases, fragments



Divergence between topics is a feature, not a problem. The character is the

brand; the topics are rooms in the lair. (This is the Arlo/One-persona,

many-rooms model. Do not narrow the brand to one topic. Do not scatter it

across unnamed platforms.)



\## 2. LOCKED DECISIONS (do not re-litigate without the owner)



1\. \*\*Voice conceit:\*\* the owner IS the excavator-narrator. First person,

&#x20;  uncovering and commenting on material with opinions and asides. NO

&#x20;  in-character scribe/archivist persona.

2\. \*\*Face:\*\* a dragon avatar represents Max visually. Voice = the owner,

&#x20;  face = the avatar.

3\. \*\*AI stance:\*\* anti-slop is FUNCTIONAL, not branded. The site reads like

&#x20;  a human made it because the owner's ear filters everything. We never

&#x20;  market on "no AI slop."

4\. \*\*Summaries are the owner's.\*\* Agents draft bodies; the owner writes or

&#x20;  approves every excerpt/summary. These are the highest-visibility words on

&#x20;  the site.

5\. \*\*Publishing cadence:\*\* none. No streaks, no schedules. Gates only —

&#x20;  progress is measured in finished entries, not calendar weeks.

6\. \*\*WotC content is always free\*\* (Fan Content Policy constraint). Any

&#x20;  future paid offering lives in the Machine Hoard or elsewhere, never

&#x20;  gatekept D\&D material.



\## 3. THE VETO GATE (the core quality control)



Nothing is published that the owner has not read and approved. Workflow:



1\. Agent/lens drafts from source material (fact-bounded: invent nothing,

&#x20;  note gaps instead of filling them)

2\. Draft lands as a file; the owner reads it

3\. Owner: APPROVE / EDIT (own hand) / VETO

4\. Owner writes the summary/excerpt

5\. Publishing checklist (Section 6) pushes it live

6\. Editor notes stay out of the reader copy (see Section 7)



A draft may be 90% agent or 90% owner. Both count. The gate is the constant.



\## 4. AGENT ROLES (one prompt, one agent, one deliverable)



| Agent | Role | Scope |

|---|---|---|

| \*\*Antigravity\*\* | Site Warden | All repo work: posting entries, layout fixes, pipeline changes. Works from the publishing checklist. |

| \*\*Workshop agent\*\* (Hermes / AmoebiX panel) | Drafting | Runs excavation/herald lenses on source material. Writes draft files. NEVER pushes. |

| \*\*NotebookLM\*\* | Archive | Source gathering, compendium maintenance, contradiction flagging. |

| \*\*Codex\*\* | Break-glass only | Only if Antigravity is blocked. Not a standing coder. |

| \*\*Quorum / AmoebiX prism\*\* | Gatekeepers | Consulted at PHASE TRANSITIONS only, not mid-phase. |



\*\*Standing rule:\*\* no agent receives an open-ended brief like "improve the

site." Every prompt states the exact files, the exact change, and the words

"no other modifications." Any agent that exceeds scope is demoted same day.



\## 5. AMOEBIX INTEGRATION



AmoebiX (not DeleGate — deprecated) is the spine:



\- `kernel dispatch / claim / complete` — the six-phase plan lives as task cards

\- `sense tangent "..."` — stray ideas get parked here, NEVER acted on mid-task

&#x20; (this command IS the one-shelf-at-a-time protocol)

\- `panel run --lens excavation` (or herald/quill) — draft generation

\- `prism` / quorum lens — phase-transition second opinions only

\- `decision savor` — log completed milestones

\- `backup` — auto-mirrors to Drive after panels/tasks/decisions



\*\*Custom lens:\*\* `panel/lenses/excavation.md` — herald's fact-discipline +

quill's voice rules + the excavation register (narrator uncovers and

comments, never catalogs). Editor notes go to `<slug>.editor-notes.md`,

NEVER into the entry body.



\## 6. PUBLISHING CHECKLIST (works for humans and agents)



1\. Choose the Hoard: `content/draega/`, `content/machine/`, or `content/odd/`

2\. Create `<slug>.md` with frontmatter:

&#x20;  ---

&#x20;  title: "Title"

&#x20;  date: "YYYY-MM-DD"      ← real current date, not future

&#x20;  hoard: "draega"          ← draega | machine | odd

&#x20;  summary: "Owner-written excerpt"

&#x20;  ---

3\. Register at TOP of `content/posts.json` (newest first)

4\. Commit and push:

&#x20;  git add content/

&#x20;  git commit -m "Publish new entry: <Title>"

&#x20;  git push origin main

5\. Live in \~60 seconds at:

&#x20;  https://myrddhinmclean-hash.github.io/mAxAdrAgoN/hoards/<hoard>.html

&#x20;  https://myrddhinmclean-hash.github.io/mAxAdrAgoN/hoards/entry.html?post=<slug>



\## 7. PIPELINE RULES (permanent, in code)



\- `assets/js/hoard.js` strips any trailing "Tempted to invent but didn't:"

&#x20; block (plus preceding `---`) at render time. Editor notes are workshop-

&#x20; only and must never reach the reader copy. Source md files MAY retain

&#x20; them; the renderer is the safety net.

\- WotC Fan Content Policy disclaimer is in every page footer. It must stay.



\## 8. THE SIX-PHASE PLAN (gates, not dates)



\- \*\*Phase 0 — Lair Opens:\*\* site live, disclaimered, handles claimed. ✅ DONE

\- \*\*Phase 1 — First Real Entry:\*\* first Draega entry published, voice gate

&#x20; proven. ✅ DONE

\- \*\*Phase 2 — The Shelf Fills:\*\* 3–5 more Draega entries (conversion jobs

&#x20; from the compendium, not creation jobs), Odd Hoard entries when obsessions

&#x20; strike, Machine Hoard only when natural. DONE WHEN: posting stops feeling

&#x20; like an event.

\- \*\*Phase 3 — First Contact:\*\* share the URL in 2–3 existing communities.

&#x20; Watch what people click and quote. DONE WHEN: one stranger engages

&#x20; unprompted. If nobody does, the fix is better entries, not more platforms.

\- \*\*Phase 4 — The Voice Gets a Body:\*\* one video (read an entry aloud, static

&#x20; avatar, one-take with silence-cuts). One video, then decide. YouTube rooms

&#x20; get named as places in the world when a topic outgrows one channel.

\- \*\*Phase 5 — Review, Don't Pivot:\*\* what was enjoyed, what dropped, what

&#x20; engaged. Adjust Hoard weights. Parked items (AI training, avatar build,

&#x20; domain) reconsidered here.



\*\*Known backlog (no commitment, do not start unprompted):\*\* monuments entry

(Puzzle Wall, LIES, Seasons Room, Boot Room), Anjax character piece, expand

Alistair/Erik/Kooms/Gelda, fix nav duplication, verify "Read the Lore"

placement, correct entry date field.



\## 9. EXECUTIVE-DYSFUNCTION PROTOCOLS (the part that keeps this alive)



1\. Stray ideas → `sense tangent`, never a context switch

2\. The veto gate replaces motivation — never "feel like writing"

3\. One shelf at a time

4\. No streaks, no calendars — gates only; silent weeks mean nothing

5\. Quorum at phase transitions only

6\. Agents get two sentences of scope, always



\## 10. WHAT THIS PROJECT IS NOT



\- Not a content farm. No posting quota exists anywhere in this document.

\- Not a rebrand-in-waiting. VitePress/Actions migrations are explicitly

&#x20; rejected unless the current site fails a real need.

\- Not the agent's site. Every agent here serves the gate; the owner decides

&#x20; what's treasure.



