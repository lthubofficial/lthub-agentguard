AG-C130 — Cryptographic Recovery Snapshot Integrity and Tampering Detection

Project: LT Hub™ AgentGuard
Test ID: AG-C130
Category: Cryptographic integrity / recovery snapshots / tampering detection
Result: PASS — 15/15 checks passed
Execution scope: Local Python cryptographic simulation

1. Objective

Investigate whether HMAC-SHA256 integrity verification can detect modifications, substitutions, malformed recovery snapshots and unauthorized integrity tags before recovery is permitted.

2. Test results

- Total checks: 15
- Passed: 15
- Failed: 0

Final result: PASS — Snapshot integrity and tampering detection checks completed.

3. Evidence register

Test area| Observed result
Valid snapshot verification| Successful
Modified nonce history| Detected
Modified version| Detected
Snapshot substitution| Rejected
Tampered integrity tag| Rejected
Unrelated-key tag| Rejected
Missing integrity tag| Rejected
Empty integrity tag| Rejected
Malformed snapshot structures| All rejected
Valid snapshot recovery| Successful
Recovered version| Matched
Recovered nonce history| Matched
Tampered snapshot recovery| Rejected
Same-key tag consistency| Confirmed
Different-key tag distinction| Confirmed

4. Technical implementation

The simulation uses:

- HMAC-SHA256.
- Python's "hmac" and "hashlib" libraries.
- Canonical JSON serialization.
- Sorted nonce history.
- Constant-time tag comparison through "hmac.compare_digest".
- Snapshot structure validation before verification and recovery.

The integrity tag is calculated over the canonical representation of the snapshot's version and nonce history.

5. Security findings

Finding A — Snapshot modification detection

[V] Changes to nonce history and snapshot version were detected.

[V] Substituted snapshot contents did not verify against the original integrity tag.

[I] Cryptographic integrity verification can help detect unauthorized snapshot modification when the verification key remains protected.

Finding B — Integrity-tag validation

[V] Tampered, missing and empty tags were rejected.

[V] A tag generated with an unrelated key was rejected.

[I] An attacker without the correct secret key should not be able to generate a valid HMAC for modified snapshot contents, assuming the key remains secret and the cryptographic implementation is sound.

Finding C — Recovery validation

[V] A valid snapshot was recovered successfully.

[V] The recovered version and nonce history matched the supplied snapshot.

[V] A tampered snapshot was not recovered.

6. Limitations

- The test key is hardcoded in the local Python simulation.
- No independently protected key-management authority was used.
- No hardware security module or operating-system key store was tested.
- No real database or durable storage was tested.
- No production recovery service was tested.
- No key rotation or key revocation process was tested.
- No digital signatures or public-key verification were tested.
- No production payment or external authorization system was involved.

The simulation does not establish production-grade key protection or security assurance.

7. Conclusion

AG-C130 completed with 15/15 checks passing.

The simulation demonstrated HMAC-SHA256-based detection of modified snapshot contents, substituted snapshots, invalid tags and malformed recovery data.

Further investigation should examine independently protected integrity keys, key rotation, recovery authority separation and durable snapshot storage.

Evidence classification: Local Python cryptographic simulation evidence.

Production assurance: Not established.

LT Hub™ AgentGuard principle:

Evidence before claims. Human oversight before consequential action.

Human Authority is a Security Boundary.