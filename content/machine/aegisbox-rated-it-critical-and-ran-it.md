---
title: "The Sandbox That Rated the Code CRITICAL and Then Ran It"
date: "2026-09-03"
hoard: "machine"
branch: "AI agents and automation"
branch_n: "1"
summary: "Four guarantees, ten tests, and not one of the tests ever tried to break out. The watchdog holds. The floor did not, that morning. And the threat scanner reads the code, rates it CRITICAL_THREAT, and then runs it, because detection shipped on and blocking shipped off."
---

# The Sandbox That Rated the Code CRITICAL and Then Ran It

AegisBox was attacked properly for the first time on 2026-09-03, and the first thing the attacks found was the front door standing open.

The idea is a room. An agent that writes and runs its own code is one bad line away from deleting your files, and reading every line is not an answer at the speed these things generate. So give the code a floor it cannot write through, no network unless you opened one, a ceiling on memory, and a clock that kills whatever overruns.

Four guarantees, all claimed, none ever tested against somebody trying to break them. Ten tests existed and not one of them attempted an escape. They confirmed the room had walls by asking the room.

The watchdog holds. The airgap holds. Filesystem confinement did not hold that morning and holds now. The threat scanner is the one worth sitting with. It reads the code, rates it CRITICAL_THREAT, and then runs it, because detection ships on and blocking ships off. That is not a security control. That is a smoke alarm wired to a notebook.

Two faults are still standing, written down rather than smoothed over. The memory cap does not hold on Windows, where the fix is a job object through ctypes that nobody has written, so a two gigabyte allocation sails straight past a 256 megabyte limit. And the shims patch names inside one interpreter, so a child process gets a clean socket module and prints SHIM_BYPASSED, which is the sandbox telling on itself.

Thirty one tests now, two of them skipped with the reason sitting next to them. Telemetry reports which memory guarantee the caller actually has rather than the one the description implies.

The fixes are not the useful part of the day. The useful part is learning that four guarantees had been believed on the strength of a test suite that never once tried the handle.
