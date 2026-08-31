# Editor notes: dungeon-cue-remote-control

**Editor-only. Never rendered. Never merged into the entry body.**

Drafted by Claude, 2026-08-31, for the owner's veto gate under governance section 3.
**Not registered in posts.json.** It stays unregistered until the gate passes and the owner writes the excerpt.

## SOURCE LEDGER

**PRIMARY SOURCES USED:**
- `DungeonCue_Project/README.md` (project root) — scope, status, Windows/Android split, the always-on listening analysis.
- `DungeonCue_Project/windows/README.md` — the implemented feature list, the two stated limitations, the remote-control architecture section, the Online Player requirement.

Both owner-authored. Every technical claim traces to one of them.

**REQUIRES VERIFICATION:** none from the sources. One thing worth the owner's eye: the Windows README states the live Tkinter window and microphone had not been run in the handoff environment. If that is still true, "the Windows version is finished" is stronger than the record supports. It is the one sentence in the entry I would want confirmed before publishing.

**UNRESOLVED CONTRADICTIONS:** none between the two READMEs.

**INTERPRETATION VS STATED FACT.** Stated: no audio produced locally, every trigger a REST call relayed by Syrinscape's servers; success returned even with no player listening; Online Player required, Fantasy/Sci-Fi/Board Game players not wired for remote triggers, confirmed on Syrinscape's developer forum; wake word approximated by chunking on speech pauses; arming deliberately decoupled from the app's name; per-mode delay, sensitivity, max triggers per minute, ambience; four configurable buttons with individual phrases, also clickable; "Roll for Initiative" arms combat and auto-switches; "Stand Down" disarms; Tabletop Audio has no public trigger API so its buttons open a link; Android is push-to-talk and always-on would need a foreground service, a self-restarting recognition loop, `FOREGROUND_SERVICE` and `FOREGROUND_SERVICE_MICROPHONE`, and a battery optimization exemption.

Interpreted: that "Roll for Initiative" is a good trigger because it is already said aloud at the right moment in every game. True and obvious once said, but it is my observation, not a line in the source.

**INVENTIONS — every element not in the source:**
1. The opening scene. Four people, thirty seconds of rain, a distant bell, a DM going quiet and clicking. Invented illustration.
2. "A button on a long wire." My image for the architecture.
3. "During a boss fight." Invented detail.
4. "A program that can fire sounds on speech will eventually hear a sentence it likes too much." My gloss on why a rate limit exists; the source states the limit, not the reason.
5. "Naming a thing after itself is the obvious choice and it is wrong." My conclusion. The source states the decoupling and its purpose but does not editorialize.

**COMPENDIUM MATERIAL USED:** none.

**PLACE RULE:** n/a.

**GAPS LEFT OPEN:**
- No setup instructions, no system requirements, no version number.
- No account of how the four buttons are configured in practice.
- Nothing about the electric-blue theme or the interface.
- Nothing on price, store page, or availability. Deliberate under section 11.

**PRESENCE CHECK:** the narrator is the author of the tool. "My program" is factually correct.

**MODE:** technical/explanatory, with a narrative opening.

**VETO SWEEP:**
- Em-dashes: zero. Hyphens in prose: zero. "Push to talk" and "one shot" written open rather than hyphenated to hold the rule.
- AI vocabulary: none.
- No lair lore used as analogy.
- No admiring adjectives on competence. The two places the tool is praised, it is praised for a refusal rather than a capability.

**COMMERCIAL CHECK (governance section 11):** no price, no store link, no purchase path, no launch language. **None of the launch material was used** — the project folder contains store pages, press outreach to named creators, a first-dollar pack and a testimonials file, and none of it went anywhere near this draft. Testimonials in particular should never appear on the lair.

**WEAKEST PASSAGE:** the four-buttons paragraph. It is the most specification-like stretch in the piece and carries the least insight.

**WORD COUNT:** roughly 700.
