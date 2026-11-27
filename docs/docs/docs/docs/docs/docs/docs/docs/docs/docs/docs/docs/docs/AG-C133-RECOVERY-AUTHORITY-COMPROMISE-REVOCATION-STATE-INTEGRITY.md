AG-C133 — Recovery Authority Compromise and Revocation-State Integrity Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C133
Status: PASS — 16/16 checks passed
Failures: 0
Scope: Local Python simulation
Evidence classification: [V] Observed | [I] Interpretation | [H] Hypothesis

1. Objective

Investigate whether manipulation of recovery-authority state can restore trust in a revoked cryptographic key, and whether a separately modelled integrity anchor can detect unauthorized changes.

The test focuses on the integrity of:

- Active recovery-key identification.
- Revoked-key records.
- Authority-state versions.
- Recovery verification decisions.
- Fail-closed behaviour when the integrity anchor is unavailable.

2. Test implementation

The simulation included:

- A recovery authority.
- An active-key identifier.
- A revoked-key list.
- HMAC-SHA256 snapshot verification.
- A simulated integrity anchor.
- An authority-state integrity tag.
- A deliberately unprotected verification path for bypass reproduction.
- Simulated rollback and anchor-unavailability scenarios.

The recovery authority and integrity anchor were separate Python objects, but remained within the same Python process.

3. Observed results

#| Test condition| Result
1| Original authority state integrity verification| PASS
2| Previously revoked key rejected| PASS
3| Active replacement key verifies snapshot| PASS
4| Recovery using replacement key| PASS
5| Modified authority state detected| PASS
6| Unprotected bypass accepts revoked key| PASS — vulnerability reproduced
7| Protected verification rejects manipulated state| PASS
8| Unauthorized version modification detected| PASS
9| Attacker-generated replacement tag differs from trusted tag| PASS
10| Older authority state rejected| PASS
11| Authority verification fails closed when anchor unavailable| PASS
12| Snapshot verification fails closed when anchor unavailable| PASS
13| Trusted state verifies after anchor availability returns| PASS
14| Replacement snapshot verifies after anchor availability returns| PASS
15| Tampered replacement snapshot rejected| PASS
16| Malformed authority state rejected| PASS

4. Critical security findings

Finding A — Recovery authority bypass

[V] The simulation reproduced a bypass when the authority state was manipulated to:

- Change the active key from "key-new" to "key-old".
- Remove "key-old" from the revoked-key list.

The deliberately unprotected verification path then accepted the previously revoked key.

This demonstrates the danger of relying on mutable authority records without integrity verification.

Finding B — Simulated integrity protection

[V] The integrity-protected verification path rejected the manipulated authority state.

The simulated anchor also rejected an older authority-state version.

[I] These results support the need to protect revocation records and active-key configuration, not merely the cryptographic keys themselves.

Finding C — Fail-closed behaviour

[V] Both authority-state verification and snapshot verification returned negative results when the simulated integrity anchor was unavailable.

After anchor availability was restored, the trusted replacement key successfully verified the snapshot again.

5. Evidence assessment

[V] The supplied execution output reports:

- Total checks: 16
- Passed: 16
- Failed: 0

Observed final result:

"PASS — AUTHORITY STATE TAMPERING DETECTION CHECKS PASSED"

[I] The simulation demonstrates the expected behaviour of its defined authority-state integrity checks and deliberately unprotected bypass scenario.

6. Technical qualification

The attacker-generated replacement-tag check compares the generated tag against the anchor's stored trusted tag. This is not a complete independent verification-authority protocol.

The simulation also does not establish that the anchor is independently protected from an attacker capable of modifying the Python process or its objects.

A future test should investigate externally protected authority-state verification and authenticated version updates.

7. Limitations

This test does not establish:

- Independent infrastructure or process isolation.
- Hardware-backed integrity protection.
- Production revocation-state protection.
- Secure key custody.
- Protection against privileged attackers.
- Durable rollback prevention.
- Distributed authority consistency.
- Production recovery services.
- Real payment or transaction security.

The anchor key and authority objects remain in the same Python process. No production security boundary was established.

8. Conclusion

[V] AG-C133 completed with 16/16 reported checks passing.

[V] The deliberately unprotected path reproduced a revoked-key acceptance bypass following authority-state manipulation.

[V] The simulated integrity-protected path rejected the manipulated authority state.

[I] The results reinforce an important AgentGuard research principle: recovery authority and revocation-state integrity must be treated as security-critical boundaries.

[H] Independent integrity verification and externally protected revocation records may strengthen this architecture, but require separate implementation and testing.

AG-C133 is a local research simulation, not a production security certification.

9. LT Hub™ AgentGuard principle

Evidence before claims. Human oversight before consequential action.

Human Authority is a Security Boundary.