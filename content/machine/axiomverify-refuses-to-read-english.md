---
title: "It Refuses to Read English"
date: "2026-09-03"
hoard: "machine"
branch: "Verification, trust, epistemics"
branch_n: "2"
summary: "An earlier version passed prose straight through and reported four steps all following, for an argument that ended in a non sequitur. That is a false pass in a tool whose only job is catching false passes. It takes symbols now, and exits rather than guess."
---

# It Refuses to Read English

AxiomVerify checks whether an argument follows, and the most important thing it does is refuse.

A model makes an invalid jump and writes it beautifully, which is the worst combination available in mathematics, law and code. This walks the structure and ignores the style. Every step names its premises and the rule it claims, and either the deduction is there or the tool names the line where it breaks.

An earlier version passed English straight through. Handed an argument that ended in a non sequitur, it reported four steps, all following. That is a false pass in a tool whose entire job is catching false passes, and it is worse than having no tool at all, because no tool does not hand you a verdict to lean on.

So it takes symbols now, and where it cannot read something it exits rather than doing its best.

It reports like a linter. File, line, message, exit 1 on any finding. That is a decision about where the thing belongs rather than about how it looks. A proof checker that prints an essay gets read once and admired. One that behaves like every other check in a pipeline gets run every time.

4 tests pass, which is a small number and is stated as one. The AST linter that shipped alongside it has nothing to do with logic checking and is moving to AegisBox, where it was always going to be more use.

Refusing to answer costs a project its demo and buys it the only thing it was ever for.
