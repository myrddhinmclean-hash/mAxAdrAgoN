---
title: "AmoebiX Is an Arm Rack, Not a Brain"
date: "2026-08-31"
hoard: "machine"
branch: "AI agents and automation"
branch_n: "1"
summary: "Thirty two models in one config file, a library of lenses that tell each of them how to answer, and a ledger recording whether the answer changed anything. The AI is never on while the tools work."
---

# AmoebiX Is an Arm Rack, Not a Brain

The design note at the top of the project says it plainly: AmoebiX is a toolbox of local command line tools. Call a tool, read the result, decide. The AI is never on during a tool's work.

That sentence is the whole architecture. Most agent systems put the model in the middle and let it drive. This one puts the model outside and hands it a rack of arms. The tools run locally, return the minimum text needed for the next decision, and stop. Nothing is thinking between calls, which means nothing is burning tokens between calls either.

There are thirty two models configured across three kinds of backend: ordinary API calls, browser sessions driving a web interface, and a local command line binary. Sending one question to several of them at once is the entire point. They answer independently, they do not see each other's work, and a program combines the results afterward.

The instructions each model receives come from a library of lenses, and the lenses are the interesting part. A lens is a contract, not a personality. The auditor lens returns a fixed block per claim: the evidence, the source type, the source date, the support strength, what would change the conclusion. The falsifier lens builds the strongest honest case against a conclusion and then reports what survives. The quorum lens opens by telling the model that others are answering the same question right now, that it will never see their answers, and that if its honest answer is unusual then the unusual answer is the one worth having.

That last instruction exists to fight a specific failure. Models converge. Ask several the same question in the same words and they drift toward the same shape of answer, and the agreement looks like confirmation when it is only gravity. Telling a model that a program will combine the results, and that consensus is not the goal, is a cheap way to buy back some independence.

The cost controls are structural rather than advisory. Three research levels: one model, two, or three. Every round is hashed by prompt, lens and mode, so an identical rerun returns from cache and costs nothing. There is a scoreboard ranking models by usefulness, cost and latency, built from outcomes rather than reputation.

And there is one rule that binds anything using it: after acting on a panel round, log whether it influenced the decision. Influenced or not. That line goes into an append only ledger.

That ledger is the part I would keep if everything else burned. It is the only mechanism in the whole system that can eventually answer the question nobody asks about their own tools, which is whether the answers ever actually changed anything, or whether the machine has been agreeing with a decision that was already made.

Fourteen entries in it so far. Not enough to conclude anything. Enough to start counting.
