---
title: "The Concept Steering Tool That Had Never Once Run"
date: "2026-09-03"
hoard: "machine"
branch: "Consciousness and AI welfare"
branch_n: "17"
summary: "A tool that turns one concept up or down inside a running model and prints all three results side by side. It had never once executed: a directory called torch with no __init__.py imported as an empty namespace package, so every availability guard passed while every test failed in setup."
---

# The Concept Steering Tool That Had Never Once Run

NeuroSteer ran for the first time in its life on 2026-09-03. The README had said three of three tests passing, and that had never once been true.

What it does is worth wanting. Steering a model usually means retraining it or arguing with it in the prompt, and neither tells you what actually moved. This reaches into the layers partway through generation, pushes a single concept up or down, and prints the untouched output beside the amplified and the suppressed. Seeing all three together is the point. Steering you cannot compare is just a different answer.

It had never executed. The environment held a directory called torch holding 5,809 files and no __init__.py, so importing torch handed back an empty namespace package. Every availability guard in the project asked whether torch imported, was told yes, and carried on. Every test then failed in setup rather than in an assertion, which is the kind of red a reader skims past on the way to the summary line.

Real PyTorch is installed and three tests pass, and those three are the first three that have ever run.

The model underneath is a toy transformer trained on nothing. It shows the mechanism and it steers nothing anybody would use, and the register says exactly that rather than leaving it to be discovered.

An import guard asks whether a name resolves. It does not ask whether the thing behind the name is the thing you meant, and a folder with the right name on it was enough.
