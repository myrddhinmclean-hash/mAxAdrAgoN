---
title: "The Grid Scheduler That Only Ran on Its Own Demo"
date: "2026-09-03"
hoard: "machine"
branch: "Energy"
branch_n: "3"
summary: "The dispatcher looked jobs up by hardcoded name and raised KeyError on anything else, so the only workload it could ever schedule was the one in the demo. It takes real price curves and real job files now."
---

# The Grid Scheduler That Only Ran on Its Own Demo

GridPulse looked its jobs up by hardcoded name and raised KeyError on anything else, so the only workload it could schedule was the one that came with it.

The idea holds up. A training cluster pulls hardest whenever it is asked, which is how congestion and a large bill turn up together, and most of that work does not care what hour it runs in. So read the price curve, hold back what can wait, stand down what is running when power turns dear, and never touch the cooling.

The dispatcher matched job names against a table written into the source. Feed it a workload that was not in the example and it raised KeyError and stopped. Every number the project had ever produced was therefore a description of the example, which is a fine thing for a demo to be and a poor thing for a result to be.

It takes real price curves and real job files now, and 4 tests pass.

The saving figure was illustrative until the price curve stopped being synthetic, and the register called it illustrative the whole way through. That is the difference between a placeholder and a claim, and it is the reason this one needed a fix rather than a retraction.

A program that only runs on its own demo data is not a short distance from working. It is the whole distance, wearing the clothes of almost.
