---
title: "Negative Zero for Table Salt"
date: "2026-09-03"
hoard: "machine"
branch: "Materials and nanotech"
branch_n: "8"
summary: "It returned a formation energy of negative zero for sodium chloride, because neither element was in its thirteen entry table and anything unrecognised was skipped without a word. Fixing that exposed the larger fault underneath: the valence field was in the data the whole time and was never read."
---

# Negative Zero for Table Salt

CrystalGen returned a formation energy of negative zero for table salt, which is the most confident way a program can tell you it has never heard of sodium.

The tool estimates whether a proposed crystal would survive being made. Lab time is the expensive part of materials work, so the screen belongs in front of it. Give it a formula, get back stable, worth trying, or no.

The element table held thirteen entries. Sodium was not one of them. Chlorine was not one of them. Anything the table did not recognise was skipped in silence, and the sum of nothing is zero. No warning, no refusal, just a number with a minus sign in front of it and enough decimal places to look considered.

The table holds fifty one elements now, each with a citation, and an unknown element is refused rather than stepped over.

Fixing that exposed the defect underneath, which was bigger and much quieter. The valence field sat in the data and was never read. Magnesium oxide and table salt came out within a tenth of an electron volt of each other despite magnesium oxide holding roughly four times the lattice energy, because charge was not in the arithmetic at all. Adding the ionic charge product cut mean error by a third, to 0.491 eV per atom across eighteen compounds with published values to check against.

Ranking accuracy sits at 77 percent and the repair did not move it. The test floors at 65 rather than at today's number, so a later change that costs a couple of points reads as a change rather than as a fall from a high water mark that happened to be measured on a Thursday.

Two repairs in one day and only the second one mattered. The first was a program that did not know what it did not know. The second was a program that had the answer sitting in front of it and never looked.
