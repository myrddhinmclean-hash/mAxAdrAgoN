---
title: "The Decoder Was Fine. The Measurement Was Wrong."
date: "2026-09-03"
hoard: "machine"
summary: "It was written up as broken and it was never broken. The measurement read the x component of a population vector against an angle in radians, so a working decoder looked like a coin toss. Measured properly, error falls from 42.9 degrees at four channels to 7.4 at sixty."
---

# The Decoder Was Fine. The Measurement Was Wrong.

SynapseDecode was written up as broken on 2026-09-03 and the write up was wrong. The decoder had been working the whole time. What failed was the thing measuring it.

The algorithm is old and it is elegant. One motor neuron on its own is nearly useless, firing hardest for a single direction and vaguely for everything else. Let every channel vote for the direction it prefers, weight each vote by how hard that channel is firing, and the sum points where the arm meant to go. Population vector decoding, and it holds.

The measurement read the x component of that vector and scored it against an angle in radians. Two quantities with nothing to do with each other, lined up and graded, and a working decoder came out looking like a coin toss.

Measured properly over two hundred trials per point, decode error falls from 42.9 degrees at four channels to 7.4 degrees at sixty. Error times the square root of the channel count holds between 57 and 69 from twelve channels upward, which is the relationship this algorithm is known for and the reason to trust the implementation rather than the graph.

Two tests pass, and the tests are not the interesting part. The sweep is, because the sweep is the only thing in the project that compares a decoded angle against the angle that was intended.

The retraction stays in the findings file. Deleting it and leaving the corrected numbers would read better, and a record that tidies away its own mistakes is worth nothing.

It is not a clinical device. Nothing here restores mobility to anyone, and the twenty millisecond figure that makes a prosthetic feel like your own arm belongs to the algorithm rather than to this program.

A confident claim that somebody else's code is broken should cost more scrutiny than a claim that it works, not less. It went the other way three times in one day, and measuring again turned out to be cheaper than rewriting every single time.
