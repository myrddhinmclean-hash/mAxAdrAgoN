---
title: "Forty References, Counted Instead of Guessed"
date: "2026-09-03"
hoard: "machine"
branch: "Verification, trust, epistemics"
branch_n: "2"
summary: "It was written up as overcounting, and the reference counts it was being scored against had been invented rather than counted. The check now asserts the indices form the complete run from one to N, which a wrong number in a fixture cannot defeat."
---

# Forty References, Counted Instead of Guessed

SynapseGraph was written up as overcounting on 2026-09-03, and the reference counts it was being scored against had been invented rather than counted.

A paper is built to be printed, not searched, and the thing tying one claim to the last is a number inside a bracket. This pulls out the sections, the references and the named quantities, then links every citation to the entry it points at. The question underneath all of it is where a claim actually came from.

Measured against five real arXiv papers, it pulls 1 through 40 out of the Attention paper complete, no gaps and no duplicates, against the 40 references the paper has.

The check has changed shape, and that is the part worth keeping. It used to compare a count against a number somebody had written into a fixture. It now asserts that the extracted indices form the complete run from one to N. A program that invents an extra entry cannot satisfy that, a program that drops one in the middle cannot satisfy it, and a wrong number in a fixture cannot defeat it.

Underneath that sat a quieter fault. The test file imported functions that do not exist, so collection broke and the project's other tests never ran at all. A test file that cannot be imported does not fail loudly. It removes itself from the count and leaves a smaller green number behind.

18 tests pass now. The entity vocabulary is still a fixed list of patterns rather than anything trained, so it finds what it was told to look for and nothing else.

Two of the day's three retractions came from the same shape of mistake. A number nobody had checked, sitting in a fixture, deciding whether working code was broken.
