---
title: "The Diligence Engine With No Language Model In It"
date: "2026-08-31"
hoard: "machine"
branch: "Verification, trust, epistemics"
branch_n: "2"
summary: "A pitch deck claims 420 watt hours per kilogram, and nobody in the room can tell whether that is ambitious or physically forbidden. This one pulls the number out, finds the law that governs it, and shows the arithmetic. There is no language model anywhere near the verdict, and that is the point."
---

# The Diligence Engine With No Language Model In It

I built a tool that reads engineering pitches and tells you which numbers are impossible. There is no language model anywhere in the part that decides. In 2026 that sentence sounds like a confession, so it is worth explaining why it is the whole point.

Here is the problem it exists for. Someone hands you a pitch deck. It says the cell stores 420 watt hours per kilogram. You are an investor, or a patent lawyer, or a grant reviewer, and you have forty minutes. You cannot tell whether that number is ambitious, ordinary, or physically forbidden, and neither can anyone in the room, so the meeting proceeds on vibes and everyone nods at the graph.

AxiomTEA pulls the claim out of the document, finds the physical law that governs it, and says whether the number fits underneath the ceiling. Specific energy, efficiency, specific impulse, critical dimension, temperature, Q factor. Each one gets checked against detailed balance limits and cited literature, in code, with no opinion involved. The verdict is arithmetic. You can read the arithmetic.

Then it renders that one analysis ten different ways. The inventor sees governing equations and a protocol for falsifying his own claim in a lab. The underwriter sees a stance, decline or refer, and the named failure modes behind it. The journalist sees plain English and one analogy chosen to fit the specific law being tested. The defense buyer sees a specialty metals audit. Ten readers, ten documents, one shared object underneath, so no two of them can be told contradictory things about the same pitch. That last part is the engineering. Producing ten summaries is easy. Producing ten summaries that cannot disagree is the work.

What makes it useful is what it refuses. It is not a chatbot, and the refusal is structural rather than stylistic: the evaluation pipeline is Python standard library, and a generative model is not in the loop where verdicts happen. It does not give professional advice. A green verdict means your number does not break a law that was checked. It does not mean you have a company.

It also refuses to phone home. The audit runs entirely on the machine in front of you, which matters because the people who most need this are often the people least able to upload a confidential pitch to somebody's server. Exactly one module in the codebase is allowed to open an HTTPS connection, it handles updates only, and it loads only when you click the button. Grep the whole repository for urllib and you find it in one place. There is an environment variable that switches even that off, and a path for applying updates from a USB stick, because air gapped machines are a real deployment and not a hypothetical.

Two libraries came along for the ride. One reads PDFs, one writes them. There was a faster PDF library available and I turned it down, because its licence would have obliged me to release this tool's source under the same terms. That is not a technical decision and it does not make the program better. It is the kind of choice that only shows up years later when somebody asks a question you cannot answer.

The part I am most attached to is the smallest. Every running copy answers a health check with its version, its build time, the commit it was built from, and the exact version of each bundled library. That endpoint exists because a binary once shipped without one of those libraries while every version number in the project looked perfectly correct. The build said it was fine. The build was wrong. So now the program reports what it actually contains rather than what it believes it contains, and the release script refuses to produce a binary at all if a dependency is missing from the build environment.

The same instinct runs through the rest. Releases get hashed so you can check a specific file rather than trust a sentence about it. The documentation says the builds are traceable and then says plainly that they are not bit for bit reproducible, and names what that would take, because the honest version of a claim is more useful than the impressive one.

Most things that look impenetrable are three ordinary ideas behind a curtain. This one is two: extract the number, compare it to the limit. Everything else in the codebase exists to stop me lying to myself about whether it worked.
