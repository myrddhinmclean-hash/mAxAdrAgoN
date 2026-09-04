# Editor notes: Two Versions, XORed, and No Key Required

SOURCE LEDGER
- Register state note for SovereignVault, archived 2026-09-04: cipher breakable and replaced on 2026-09-03, 4 tests, keystream derived from master key and key name with no nonce, two values under the same name sharing a keystream, recovery by XORing two versions with no key, the crash above 8 KB, now nonced per write with a per-vault salt and the MAC covering the nonce, still hand-built cryptography where an audited primitive belongs.
- Register detail text for the scoped expiring tokens and hash-chained access framing.

INVENTIONS
- "a short walk from there to either one" is mine. XORing two ciphertexts under a shared keystream yields the XOR of the plaintexts; separating them takes further work that the record does not describe and I have not verified was performed. The source says a stored secret "was recovered", so the recovery happened; the phrase about the short walk is my characterisation of the step between.
- "by a distance nobody needs measured" is mine.
- "so the log cannot be quietly rewritten" states the purpose of hash chaining, which the source implies rather than says.
- "better than it was is not a security property" is mine.

GAPS LEFT OPEN
- Which audited primitive would be the right dependency is not named in the record, and the entry does not name one either.
- Whether anything was ever stored in a real vault under the broken cipher is not recorded, and that is the question a reader will have.

CONTRADICTIONS FOUND
- None.

WEAKEST PASSAGE
The XOR paragraph. It is the most technical passage in the batch and the one most likely to be read by somebody who knows more about it than the record contains.
