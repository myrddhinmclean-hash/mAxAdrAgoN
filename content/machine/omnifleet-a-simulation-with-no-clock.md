---
title: "A Fleet Simulation With No Clock In It"
date: "2026-09-03"
hoard: "machine"
branch: "Transportation"
branch_n: "6"
summary: "It served exactly one ride per vehicle out of two hundred submitted and then stopped. There was no clock, so no car ever finished a trip and came back for a second passenger, and the fleet sweep the project is named for was measuring the fleet against itself."
---

# A Fleet Simulation With No Clock In It

OmniFleet served exactly one ride per vehicle out of two hundred submitted and then stopped, which looks at first like a bug in the plotting.

The project asks how many robotaxis a city actually needs. An empty car driving to a pickup earns nothing and spends battery doing it, and the surge always arrives faster than a fleet repositions, so the question is worth answering with arithmetic instead of opinion.

It could not answer it. Dispatch was a single instant round. Every request was looked at once, each paired to the nearest idle vehicle, and then nothing happened, because nothing could. No time passed. A car that took a passenger never finished the trip, never came free, and never took a second. Twenty vehicles and two hundred requests gets you twenty rides and a hundred and eighty in the bin. The fleet sizing sweep the whole project is named for was measuring the fleet against itself.

There is a clock now. run_time_stepped carries a free_at time on every vehicle and moves the world forward, and wait is measured from the moment a rider asks to the moment a car pulls up, which is the number a rider actually feels rather than the number dispatch would like credit for.

The old instant round is still in there behind a flag with its tests untouched, because deleting it removes the only thing the new version can be checked against.

Three tests pass. Distance is straight line, there is no road network, there is no traffic. Calling it a teaching simulator is not modesty, it is the description.

The failure was never that the model was simple. Stated simplifications are honest and this one is full of them. The failure is that a simulation of a queue had no clock in it, and every number it produced had been read and believed anyway.
