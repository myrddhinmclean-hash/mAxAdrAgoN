---
title: "Two Versions, XORed, and No Key Required"
date: "2026-09-03"
hoard: "machine"
summary: "The keystream came from the master key and the key name with no nonce, so two values stored under the same name shared a keystream and XORing the pair cancelled it. A stored secret came out with no key involved at all. Replaced on 2026-09-03."
---

# Two Versions, XORed, and No Key Required

SovereignVault derived its keystream from the master key and the key name, with no nonce anywhere, so two values written under the same name shared a keystream and a stored secret could be recovered by XORing the two together, with no key involved at all.

The pitch is not the problem. A central database is one place to breach, one company to be locked into, and one log that nobody outside it can read. So keep the data on a disk you own, under an identity you generated. Hand out scoped tokens that expire rather than the master key. Hash chain every touch so the log cannot be quietly rewritten.

Then the cipher, which is where it fell over. Keystream from master key plus key name and nothing else. Write a value under a name, write a second value under that same name later, and the two ciphertexts carry the same keystream. XOR the pair and the keystream cancels itself out, leaving the two plaintexts combined and a short walk from there to either one. It also crashed above 8 KB, which is the smaller of the two faults by a distance nobody needs measured.

It is nonced per write now, with a salt per vault, and the MAC covers the nonce rather than stopping at the ciphertext.

It is still cryptography built by hand, in the one application where building it by hand is least defensible. A vault is exactly where an audited primitive earns the dependency it costs you.

4 tests pass. The cipher is better than it was that morning, and better than it was is not a security property.
