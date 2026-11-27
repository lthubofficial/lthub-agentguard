AG-C131 — Cryptographic Recovery Key Separation and Rotation Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C131
Status: PASS — 15/15 checks passed
Failures: 0
Test scope: Local Python simulation
Evidence classification: [V] Observed test output | [I] Interpretation

1. Objective

Evaluate whether a simulated recovery system can manage cryptographic key rotation, support a controlled transition between old and new keys, revoke retired keys, and reject invalid key references or tampered recovery snapshots.

2. Test implementation

The simulation used:

- HMAC-SHA256 for snapshot integrity verification.
- A simulated key registry.
- An active key identifier.
- A transition-key allowance.
- A key-revocation mechanism.
- Canonical JSON serialization.
- "hmac.compare_digest()" for tag comparison.
- Recovery snapshot validation.

The test used locally defined old, new, and unrelated test keys.

3. Observed results

#| Test condition| Result
1| Original key verifies valid snapshot| PASS
2| Original snapshot recovers correctly| PASS
3| New recovery key introduced| PASS
4| New key becomes active| PASS
5| New key verifies newly signed snapshot| PASS
6| Old key accepted during transition| PASS
7| Old-key recovery works during transition| PASS
8| Unknown key identifier rejected| PASS
9| Substituted key identifier rejected| PASS
10| Unrelated key material rejected| PASS
11| Modified recovery snapshot rejected| PASS
12| Old key successfully revoked| PASS
13| Previously valid old-key snapshot rejected after revocation| PASS
14| New-key recovery succeeds after rotation| PASS
15| Malformed recovery snapshot cannot be recovered| PASS

4. Final execution evidence

- Total checks: 15
- Passed: 15
- Failed: 0

Observed execution result:

"PASS — SIMULATED KEY ROTATION AND REVOCATION CHECKS PASSED"

5. Evidence assessment

[V] Verified within the supplied local test execution:

- The original key verified its valid snapshot.
- The new key became the active verification key.
- The old key remained accepted during the configured transition.
- Unknown and substituted key identifiers were rejected.
- Unrelated key material did not verify the snapshot.
- Snapshot modification was detected.
- The old key was rejected after simulated revocation.
- Recovery using the new key continued after rotation.
- Malformed recovery data was rejected.

[I] Interpretation:

The simulation demonstrates that the implemented key registry and verification logic can enforce a defined key-transition and revocation sequence under the tested conditions.

It provides additional evidence for the recovery-integrity research area following AG-C130.

6. Limitations

This test does not establish:

- Independent cryptographic key custody.
- Actual process or machine-level key isolation.
- Hardware Security Module (HSM) protection.
- Operating-system keystore protection.
- Secure key generation or distribution.
- Production key rotation or revocation.
- Key backup and disaster recovery.
- Resistance to privileged attackers.
- Distributed-system consistency.
- Production payment or transaction security.

The test keys and registry remain inside the same Python process. Revocation is enforced by the simulated registry; the underlying old key material remains present in its internal dictionary.

7. Conclusion

[V] All 15 simulated checks passed with zero failures.

[I] The results support the conclusion that the tested implementation handled the defined key-rotation, transition, revocation, and recovery scenarios correctly.

[H] Independent key custody and hardened key-management infrastructure may provide stronger protection, but those capabilities require separate implementation and testing.

AG-C131 is a local research simulation, not a production security certification.

8. Research principle

Evidence before claims. Human oversight before consequential action.

LT Hub™ AgentGuard
Human Authority is a Security Boundary.