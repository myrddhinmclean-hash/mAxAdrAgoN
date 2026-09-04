---
title: "A Hub That Could Only Find What Was Already Inside It"
date: "2026-09-03"
hoard: "machine"
branch: "AI agents and automation"
branch_n: "1"
summary: "It exists so one agent can find another's tools without anyone wiring the pair together first, and until 2026-09-03 every agent had to be running inside the same Python process. Discovery crosses that line now. Invocation does not."
---

# A Hub That Could Only Find What Was Already Inside It

AgentMesh exists so that one agent can find and borrow another's tools without anybody wiring that exact pair together first. Until 2026-09-03 every agent had to be running inside the same Python process.

The problem it is aimed at is real. Connecting two agents means writing an integration for that specific pair by hand, and pairs multiply faster than anyone keeps up with. The way out is to stop naming providers. An agent advertises what it can do, a caller asks for a capability rather than for a name, and every call lands in a ledger that only ever grows.

The hub was in process only. Which is to say the thing built to remove a wiring problem between separate programs required all of them to be one program. That is not a small bug. It is the opposite of the situation the project describes, sitting inside the project.

Discovery crosses that line now, verified with real subprocesses rather than with threads dressed as processes. 12 tests pass.

Invocation does not cross it. A separate program can advertise a capability and be found by a caller that never heard of it, and actually calling the thing still needs a transport that has not been built. Each entry carries an invoke hint, and an invoke hint is a string rather than a promise.

Half the problem is solved and the register says half. A capability you can discover and cannot call is a phone book. The phone book was worth building. It is not the phone.
