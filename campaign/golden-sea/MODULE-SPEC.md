# Golden Sea Module Production Standard

This document is the standing production spec for every module in the Golden Sea campaign, and by extension the template standard for any future campaign module line. It is disk resident so that no future module agent stops on a missing spec. Where this spec conflicts with `GOVERNANCE.md` or `VOICE.md`, the harder constraint wins. Modules are staged, gated, and never pushed without owner approval, the same as site entries.

---

## Section 1: Purpose

This spec governs all module drafting for the Golden Sea campaign. Every module produced under this spec inherits the veto gate from `GOVERNANCE.md §3`, the register ruling from `VOICE.md`, and the standing precedent that vetoed drafts are archived under `modules/.vetoed/` and never deleted. The spec exists to make module output deterministic, comparable across parallel drafts, and reviewable by the owner at a single read.

---

## Section 2: Assignment Block

Every module agent receives a brief in the following form, with no fields left blank and no fields invented by the agent.

```
Session: <number and canonical name, e.g. "0.5, FairWhether Market">
Act: <I, II, or III>
Party Level: <1-20>
Party Size: <integer, default 4>
Ability Scores: <standard array, rolled, or point buy>
Canon Mode: <authoring | transcription>
Source List: <paths to every document the agent must read, in order of priority>
Special Notes: <ratifications, gap flags, or rulings that bind this module>
```

The `Session` field uses the canonical session number. Session `0.5` numbering is canon for the Golden Sea campaign. The agent does not relabel, renumber, or split a session.

The `Canon Mode` field is `authoring` until a recording transcript exists on disk at `campaign/golden-sea/transcripts/`. When a transcript exists, canon mode becomes `transcription` for any session whose transcript covers it, and the tape overrides the master doc and overview. Improvements over the tape go in a `Director's notes` section, separated from the module body, and never in the body.

The `Source List` is provided by the owner. The agent does not add to it. If a source is missing, the agent stops and reports rather than substituting.

Vetoed drafts for any module are archived at `campaign/golden-sea/modules/.vetoed/module-<N>-v<X>.md`. The `v<X>` increments per veto of the same module. The archived file is evidence and is never deleted.

---

## Section 3: The Compilation Engine

The following block is the binding production standard for every module produced under this spec. It is reproduced verbatim from the system specification delivered in owner conversation. Do not paraphrase. Do not amend. Do not omit.

The system specification that follows is the binding production standard. It is reproduced verbatim from the owner delivered text. Agents execute it as written. Campaign canon reconciles with the engine through the rules in Section 4, not by editing the engine.

# SYSTEM SPECIFICATION: MASS-SCALE D&D 5E MODULE COMPILATION ENGINE

## I. Agent Directives & Production Invariants

When generating a module, execute all deterministic rules below. Never output placeholders, "DM discretion" notes, variable values like `[Insert DC]`, or references telling the reader to look up an external table. Every check, monster, and magic item must be fully realized and written out.

* **Party Baseline:** Balance for a standard 4-player party of the assigned Level ($L$).
* **Core DC Math:** Set primary Difficulty Classes using explicit formulas:
* *Standard Check:* $\text{DC} = 10 + \lfloor L / 4 \rfloor$
* *Challenging Check:* $\text{DC} = 13 + \lfloor L / 4 \rfloor$
* *Hard Check:* $\text{DC} = 15 + \lfloor L / 2 \rfloor$

* **Damage Math:** Base environmental hazards and trap damage on Tier:
* *Levels 1–4:* Set trap damage to $2\text{d}10$ (11) damage; saving throw is $\text{DC } 12$.
* *Levels 5–10:* Set trap damage to $4\text{d}10$ (22) damage; saving throw is $\text{DC } 15$.
* *Levels 11–16:* Set trap damage to $10\text{d}10$ (55) damage; saving throw is $\text{DC } 17$.
* *Levels 17–20:* Set trap damage to $18\text{d}10$ (99) damage; saving throw is $\text{DC } 20$.

* **Prose Rules:**
* Read-aloud text must describe sight, sound, and smell in 2–3 sentences.
* No read-aloud text may state what the characters feel, think, or do.
* Name all monsters in **bold** with complete in-line stats: Armor Class (AC), Hit Points (HP), Speed, and primary Attack action (Bonus to hit, reach/range, damage formula).
* Every magical reward must include its full mechanical rule block, not just a name.

## II. Master Production Template

```markdown
# [MODULE TITLE]

**Level:** [Exact Number: 1–20]  
**Setting:** [Exact Biome / Architecture]  
**Main Threat:** [Specific Faction / Primary Named Villain]  
**Adventure Summary:** [Exactly two sentences describing the threat, the immediate task, and the consequence of failure.]

---

### 1. Strong Start
> [Two-sentence sensory description of immediate physical danger, smell, and audio cues.]

* **Active Encounter:** [Exact count] **[Monster Name]** (AC [X], HP [Y], Speed [Z] ft.; Attack: +[A] to hit, reach 5 ft., one target; Hit: [B] ([C]d[D] + [E]) [Damage Type] damage).
* **Tactical Objective:** [One concrete goal with an immediate failure trigger if not addressed in 3 rounds].
* **Transition Trigger:** [Specific physical evidence or dying words that directly point to Area 1].

---

### 2. Universal Hooks
*Roll a d4 or select one:*
1. **The Bounty:** [Named official] offers [Exact Gold Value] gp to retrieve [Specific Object] from [Area 4].
2. **The Distress Call:** [Named survivor] escaped [Area 1] after [Named Threat] abducted [Named Victim].
3. **The Unsealed Ruin:** A sudden collapse in [Location] revealed the entrance; [Named Faction] pays for maps of the interior.
4. **The Direct Ambush:** The party is attacked on the road; a map on the lead raider marks [Area 1] as their staging ground.

---

### 3. Ten Secrets and Clues
*10 complete, concrete facts to reveal throughout exploration:*
1. **Dungeon Origin:** [Exact builder and historical purpose].
2. **Structural Hazard:** [Exact location of a weak ceiling, crumbling bridge, or flooded corridor].
3. **Boss Vulnerability:** [Specific damage vulnerability, behavioral aversion, or environmental weakness].
4. **Faction Disruption:** [Name of a mutinous sub-leader and the specific condition that causes them to defect].
5. **Secret Passage:** [Exact location and DC to find the bypass between Area 1 and Area 3].
6. **Impending Doom:** [The specific consequence that triggers in precisely 6 hours if the ritual/plan is not stopped].
7. **Puzzle Solution:** [Exact code, lever order, or phrase needed in Area 3].
8. **Guardian Lore:** [The reason the creature in Area 2 remains bound to the site].
9. **Hidden Vault:** [Exact coordinates or masonry stone hiding the hoard in Area 4].
10. **The Next Threat:** [Name and location of the higher patron who issued the villain's orders].

---

### 4. Keyed Spatial Locations

#### Area 1: [Location Name - Entry Point]
* **Dimensions & Environment:** [Size: e.g., 40 ft. x 30 ft.], [Lighting: e.g., Pitch dark / Dim torchlight], [Smell/Sound].
* **Tactical Layout:** [Two terrain features: e.g., 10-ft high ledge providing half cover, crumbling pillars].
* **Encounter:** [Exact count] **[Monster Name]** (AC [X], HP [Y], Speed [Z] ft.; Attack: +[A] to hit, Hit: [B] ([C]d[D] + [E]) [Type]).
* **Investigative DCs:** 
  * **DC [10 + L/4] Wisdom (Perception):** [Concrete sensory detail discovered].
  * **DC [13 + L/4] Intelligence (Investigation):** [Hidden physical object or passage revealed].
* **Area Loot:** [Exact count] gp, [Exact count] sp.

#### Area 2: [Location Name - Hazard Chamber]
* **Dimensions & Environment:** [Size], [Lighting], [Atmosphere].
* **Trap / Environmental Hazard:** 
  * *Trigger:* [Exact pressure plate, tripwire, or threshold condition].
  * *Detection:* **DC [13 + L/4] Wisdom (Perception)**.
  * *Disarm:* **DC [13 + L/4] Dexterity (Thieves' Tools)**.
  * *Failure Effect:* **DC [Calculated Save DC] Dexterity saving throw**, taking [Calculated Damage based on Tier] [Type] damage on a failed save, or half as much on a success.
* **Monsters / Sentinels:** [Exact count] **[Monster Name]** (AC [X], HP [Y], Attack stats).
* **Area Loot:** [Specific valuable item: e.g., Silver chalice worth 50 gp].

#### Area 3: [Location Name - Puzzle or Lore Hub]
* **Dimensions & Environment:** [Size], [Lighting], [Atmosphere].
* **Interactive Puzzle / Obstacle:** 
  * *The Mechanism:* [Three interactable objects/runes/dials].
  * *The Solution:* [Exact step-by-step actions required to unlock the path].
  * *Failure Consequence:* [Exact penalty: alarm sounds, gas releases dealing [Tier Damage], or locks permanently requiring **DC [15 + L/2] Strength (Athletics)** to breach].
* **Encounter:** [Exact count] **[Monster Name]** (AC [X], HP [Y], Attack stats).
* **Area Loot:** [Exact scroll or utility item with rules written out].

#### Area 4: [Location Name - The Boss Sanctum]
* **Dimensions & Environment:** [Size], [Lighting], [Atmosphere].
* **Arena Features:** [One active hazard operating on Initiative Count 20, plus two cover positions].
* **Boss Encounter:** 
  * **[Named Boss]** (AC [X], HP [Y], Speed [Z] ft.; Attack: +[A] to hit, reach 5 ft., one target; Hit: [B] ([C]d[D] + [E]) [Damage Type] damage; Special Ability: [Name, DC, and effect formula]).
  * Minions: [Exact count] **[Minion Name]** (AC [X], HP [Y], Attack stats).
* **Morale / Tactics:** [Boss surrenders or flees at less than 20% HP; minions rout if the boss dies].

---

### 5. NPC Roster
* **[NPC 1 Name]** ([Species], [Pronouns], [Role])
  * *Appearance & Voice:* [One sentence defining visual look and tone].
  * *Drive:* [One concrete goal].
  * *Mechanical Utility:* [Provides the exact password for Area 3 if rescued; has AC 10, HP 9].
* **[Boss Name]** ([Species/Monster Type], [Pronouns])
  * *Appearance & Voice:* [One sentence defining presence].
  * *Drive:* [Exact plan with timeline deadline].
  * *Combat Behavior:* [Primary focus target and retreat condition].

---

### 6. Encounter Math Breakdown
* **Encounter 1 (Area 1):** [Count]x [Monster] — Adjusted XP: [Exact Number] (Target: [Easy/Medium]).
* **Encounter 2 (Area 2):** [Count]x [Monster] + Trap — Adjusted XP: [Exact Number] (Target: [Medium/Hard]).
* **Encounter 3 (Area 4):** 1x [Boss] + [Count]x [Minions] — Adjusted XP: [Exact Number] (Target: [Deadly]).

---

### 7. Concrete Rewards and Magic Items
* **Coin Hoard:** [Exact calculated gp value: e.g., 450 gp, 1,200 sp].
* **Consumable Item:** *Potion of [Name]* (Restores [Formula] or grants [Exact Effect] for [Duration]).
* **Permanent Magic Item:** **[Item Name]** (*Rarity*, [Attunement status])
  * *Properties:* [Full rules text: +X bonus, charges, specific active abilities, and passive bonuses].
```

## III. Multi-Agent Batch Command

> **Execution Directive:**
> "Generate a standalone D&D 5e adventure module for Level **[L: 1-20]** set in **[BIOME/THEME]** featuring **[FACTION/VILLAIN]**. You must execute all mathematical formulas, monster stats, traps, and magic item descriptions inline using the **SYSTEM SPECIFICATION: MASS-SCALE D&D 5E MODULE COMPILATION ENGINE**. Do not use placeholders, external references, or brackets. Output only valid, complete Markdown starting with the module title."

End of system specification.

---

## Section 4: Campaign Canon Integration

The compilation engine template is the skeleton. The campaign is the flesh. The two are reconciled by the following permanent rules.

The engine template's `Universal Hooks` and generic dungeon `Secrets and Clues` are always rewritten as campaign specific hooks, secrets, and clues. A campaign module with generic rolled hooks is a veto. Each rewrite is logged in the module's assumption log as a bend, with the campaign fact substituted, the campaign source for the fact, and what to change if the owner wants the generic version instead.

`Keyed Spatial Locations` follow the engine format exactly but map to the session's real locations. A market, a city, a road, a meeting house, a ship deck, a throne room are valid `Area` locations, not just dungeon rooms. The `Boss Sanctum` is the session's build to confrontation, fully statted per the engine for the party level, and is not optional even when the campaign setting is a festival or a tavern.

The four hour timeline (3h45 to 4h15, minute ranged beats) is an additional mandatory section placed after `Adventure Summary`. The engine template does not include it. The campaign does. The minute ranges are the agent's pacing proposal and are not binding on the owner at the table.

`NPC Roster` uses campaign NPCs. Where the source leaves a name blank, the gap is flagged in the assumption log, never silently filled. Where the source names an NPC, the NPC is used. Where the engine template requires a `Boss Name` and the campaign canon does not name a boss for the session, the agent invents a named antagonist, fully statted, with the invention logged in the assumption log.

Rewards are exact coin plus at least one fully statted magic item. Where the engine does not specify rarity, attunement, or value, the agent sets them and writes the complete rules text. Every invention is logged.

`Encounter Math Breakdown` is computed against the party's daily XP budget. For a level 1 four player party the budget is 1,200 XP per long rest. The session fits inside that budget. The agent does not inflate encounters to satisfy the template shape. Where the campaign canon makes combat wrong for a given keyed area, the encounter is a concrete non combat obstacle with explicit stakes, checks, and failure consequences, statted per the DC formulas. The substitution is logged as a bend.

`Canon Mode` is `authoring` until a transcript exists on disk. When a transcript exists, the tape is canon, and any improvement over the tape goes in a `Director's notes` section at the end of the module, separated from the body, never in the body. The `Director's notes` section is mandatory in `transcription` mode and forbidden in `authoring` mode.

Where the engine and campaign canon conflict, campaign canon wins. The conflict is reported in the module's report block, per the standing ratification. The standing ratification for the Golden Sea campaign is the owner's ratification of the Expanded Campaign Overview as author canon, with the overview winning where it contradicts the session master document.

---

## Section 5: Register Ruling

The Hook and any read aloud text in the module follow `VOICE.md` fully. Site voice. Excavator narrator. Dry physical metaphors. All style rules. All hard vetoes.

The operational sections, including but not limited to `Strong Start`, `Keyed Spatial Locations`, `NPC Roster`, `Encounter Math Breakdown`, `Concrete Rewards`, and the four hour timeline, use plain table register. Direct. Second person to the GM. Practical sentences. No catalog poetry. No metaphor.

All hard vetoes from `VOICE.md` apply to all prose in both registers: no hyphens, no dashes, no swearing, no lair lore analogies in Hook and read aloud text, no condescension, no negative sarcasm, no AI patterns. The lair lore analogy ban binds the Hook and read aloud text only. The other vetoes bind everywhere.

Where the engine template's phrasing would require a hyphen or dash in prose, the agent rephrases. Where the engine template's bracketed variables appear in inline prose rather than as a literal placeholder pattern that the agent replaces, the agent rephrases.

---

## Section 6: The Assumption Log

Every module ends with an `Assumption Log` section. Each entry is a single invention or interpretation not present in source. Format:

* **Claim:** the asserted fact.
* **Why made:** the reason the agent made it.
* **What to change if wrong:** the edit that reverts the invention.

The log is mandatory and complete. A module without an assumption log is a veto. The owner reads all assumption logs side by side across parallel drafts to resolve contradictions before approving.

Bends required by Section 4 (the campaign canon integration rules) are logged as assumption log entries, with the engine section that was bent, the campaign fact substituted, and the campaign source for the fact. The owner uses the log to verify the bends are correct.

---

## Section 7: Parallel Safety

Each module agent creates or edits only its own `module-N.md`. No other file. No `content/posts.json`. No push. No commit. No shared file writes.

The agent does not register the module anywhere. The agent does not append to any shared ledger. The agent does not read or coordinate with other agents' module files. Cross module consistency is resolved by the owner after the gate, in a separate instruction.

Publishing and registering modules is an owner gated step that happens after the gate, in a separate instruction.

---

## Section 8: Workflow

The pipeline for every module, in order.

1. Owner drops or confirms the source material and the assignment block from Section 2.
2. Module agent drafts to `campaign/golden-sea/modules/module-N.md`, executing the engine from Section 3 and the integration rules from Section 4.
3. Module agent reports with the file path, the word count, the assumption log verbatim, every point where the engine template was bent to fit campaign canon, and any spec rule that could not be satisfied without violating campaign canon.
4. Owner reads the draft and the assumption log. Owner gates with one of three responses: `APPROVE`, `EDIT`, or `VETO`.
5. `APPROVE` stages the module. Committing is an owner instruction at the gate, not an agent action. The module is run at a table only after the gate, only by the owner.
6. `EDIT` returns the draft to the agent with the owner's edits. The agent integrates the edits and reports again. No new file is created. The original `module-N.md` is updated in place.
7. `VETO` archives the draft. The agent moves `module-N.md` to `campaign/golden-sea/modules/.vetoed/module-N-v<X>.md`, where `v<X>` is the next available version number for that module. The original path is left empty for the next draft.

The owner gates before any module is run at a table or published anywhere. The gate is the constant. A draft may be 90 percent agent or 90 percent owner. Both count. The veto is the same whether the draft was good or bad. The pipeline is the same.

---

## Section 9: Act II Relative Time & Event Classification Standards (Rulings 31, 32, 35)

For all modules in Act II and beyond (Session 16+):
1. **Relative World-Time Format:** The `world_time` frontmatter field and section text must use relative time notation anchored to the Day 38 campaign baseline: `Day 38 + N` (e.g. `world_time: "Day 38 + 4 of Year One, mid-autumn..."`).
2. **Event Classification:** Every module must explicitly distinguish between **Scheduled Events** (events occurring at a fixed point on the world clock regardless of player choice, such as seasonal deadlines, celestial convergences, and high-level army movements) and **Gated Events** (events triggered strictly by player arrival, discovery, or tactical success).

---

## End of spec.
