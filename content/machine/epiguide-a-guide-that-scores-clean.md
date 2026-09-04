---
title: "A Guide That Scores Clean and Would Cost You Three Weeks"
date: "2026-09-03"
hoard: "machine"
branch: "Longevity and biotech"
branch_n: "4"
summary: "It counts repeats inside the sequence you submit and nothing outside it, so a guide that binds somewhere else entirely in the genome comes back clean. That is the exact failure the tool exists to prevent, and since 2026-09-03 it prints the warning on every run."
---

# A Guide That Scores Clean and Would Cost You Three Weeks

EpiGuide counts repeats inside the sequence you hand it and nothing outside that sequence, so a guide matching somewhere else entirely in the genome comes back clean.

The idea underneath is sound and it is not the problem. Cutting both strands of DNA leaves a break the cell cannot always repair tidily, and when the goal is turning a gene down rather than removing it, that risk buys nothing at all. Methylation quiets the gene and leaves the sequence intact. So the job is finding guides worth ordering, and scoring where else in the genome each one might bind.

Where else it might bind is the half that is not there. No genome wide off target search exists in this program. It counts repeats within the submitted sequence, which means the failure the tool exists to prevent is precisely the failure it cannot see. Since 2026-09-03 that prints as a warning on every run rather than sitting in a README nobody opens.

The scoring weights are invented. They say so, on the same run, in the same place.

3 tests pass.

CHOPCHOP, CRISPOR and Benchling are free, validated, and already in the hands of the people whose bench time this would spend. This does not replace them, and pretending otherwise would be the expensive kind of wrong.

In a field where a bad guide costs weeks at the bench, a tool that cannot see the whole genome is a learning exercise. Saying so on the tin is the only thing that makes it safe to keep.
