---
title: "Dungeon Cue Is a Remote Control, Not an Audio Engine"
date: "2026-08-31"
hoard: "machine"
summary: "The mouse is on the wrong side of the table. Say the phrase and the rain starts, without breaking the scene to go clicking. It produces no sound of its own, which turns out to be the most important thing about it."
---

# Dungeon Cue Is a Remote Control, Not an Audio Engine

The problem is that the mouse is on the wrong side of the table. You are running a scene, four people are looking at you, and the thing you need is thirty seconds of rain and a distant bell. Reaching for the laptop breaks the scene worse than silence does. Everyone at that table has watched a DM go quiet and start clicking.

Dungeon Cue listens instead. You say the phrase, it fires the sound, you keep talking. Under the hood it is doing something much less clever than it appears, and the less clever version is the one worth understanding.

It produces no audio at all. Every trigger is a web request to Syrinscape's API, which tells Syrinscape's servers to relay a play command to whichever player is logged into your account and listening. The sound comes out of that player. Dungeon Cue never touches an audio device, never holds a file, never mixes anything. It is a button on a long wire.

That architecture has one consequence you will meet on your first evening. If no player is open, the API accepts the command and returns success, and nothing plays anywhere. The request worked. The relay worked. There was nobody at the other end. A silent trigger with no error is almost always this, and almost never a bug in my program.

It also has to be the Online Player specifically. The Fantasy, Sci-Fi and Board Game players are standalone applications and are not wired to receive remote triggers at all, which is confirmed on Syrinscape's own developer forum rather than guessed at. Keep the Online Player or the web player open and logged into the same account for the whole session. No amount of cleverness on my end gets around that, because the thing I would need to change lives on their servers.

The other honest limit is the wake word, which is not really a wake word. Dedicated keyword engines listen continuously with very low latency. This one listens in chunks split on pauses in speech and checks whether your phrase turned up in the chunk. At a table, where people breathe and stop and let each other talk, that works well. Buried mid sentence with no pause around it, it will miss. Calling it a wake word is an approximation and I would rather say so than let you discover it during a boss fight.

The design decision I like most is a small one. Arming the listener is deliberately not tied to the app's own name. You say "Ambiance Mode On" to arm it and "Ambiance Mode Off" to disarm, and both phrases are yours to change. If the trigger were the words "Dungeon Cue", then every time somebody at the table mentioned the program by name it would wake up and start matching. Naming a thing after itself is the obvious choice and it is wrong.

Combat gets its own everything. Its own delay, sensitivity, trigger ceiling and ambience behaviour, and its own pair of phrases. Saying "Roll for Initiative" arms combat mode and switches you into it from wherever you were, which is convenient in a way that took me a while to notice: that sentence is already said out loud, at exactly the right moment, in every game that has ever been run. The best trigger phrase is one nobody has to remember.

Four buttons, each pointing at a mood, an element, a one shot, or a saved link, each with its own phrase, each still clickable by hand when your voice is doing something else. There is a rate limit per minute, because a program that can fire sounds on speech will eventually hear a sentence it likes too much.

Tabletop Audio is supported and is the weaker half. It is a browser based mixer with no public way to fire a sound remotely, so its buttons open your saved link rather than triggering silently. That is not a feature I am proud of. It is what the platform allows.

The Windows version is finished and the Android version is not, and the gap between them is not a setting. Android kills background microphone access aggressively, so listening through a whole session there needs a foreground service, a permanent notification, a different recognition pattern that restarts itself for hours, extra permissions, and a battery exemption the user has to grant. Push to talk is what exists today. Saying so is cheaper than letting somebody find out at their table.
