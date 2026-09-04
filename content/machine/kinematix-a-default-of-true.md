---
title: "A Robot Balance Model That Called Every Fall a Recovery"
date: "2026-09-03"
hoard: "machine"
branch: "Robotics and physical automation"
branch_n: "5"
summary: "The physics checks out against Pratt 2006, Hof 2008 and Kajita 2003, which was the whole credibility of the project. The verdict function did not: it returned success whenever it could not read the shape of a result, and reported recovery at every force it was given."
---

# A Robot Balance Model That Called Every Fall a Recovery

A verdict function in Kinematix returned True whenever it could not read the shape of a result, so it reported successful recovery at every push force it was given.

The project models a two legged robot staying upright when something shoves it. A biped that falls breaks the expensive parts, and the recovery has to be chosen in the moment before the fall commits, so the body becomes a weight on a stick. Track whether the pressure under the foot is still inside the foot. Work out where the next step has to land to cancel the momentum.

That is textbook, and the entire credibility of the project rested on whether the textbook had been implemented or only cited. On 2026-09-03 the physics was checked against Pratt 2006, Hof 2008 and Kajita 2003, and all three match. That was the outstanding item on this one and it is closed.

9 tests pass. Stability margin falls linearly with push force, 0.092 metres at 40 newtons down to 0.026 metres at 360, and it does not reach zero anywhere inside 400 newtons. So the knee sits above the range that was swept rather than being missing from the model, and knowing which of those two it is was worth the sweep.

Then the verdict function. Unable to read a result shape, it returned success. Every force came back as a recovery. A default of True in a safety check is a false pass, and a false pass is the one output worse than no output at all, because no output sends you to look. It raises now.

It is a teaching simulator and not a robot controller. The distance between those two is the three papers it was finally checked against.
