LT Hub™ AgentGuard — AG-C125

Persistent Replay-State Integrity and Tampering Simulation

Test ID: AG-C125
Test name: Persistent Replay-State Integrity and Tampering Simulation
Result: PASS — 11/11 checks passed
Failed checks: 0
Scope: Local Python simulation
Evidence status: [V] Execution output supplied by the user

1. Objective

Investigate whether modifications, deletion, replacement or corruption of stored replay-state records can be detected.

The simulation evaluates HMAC-SHA256 integrity verification, version-based rollback detection, nonce history validation and fail-closed behaviour.

2. Test results

No.| Test condition| Expected| Observed
1| Valid initial replay-state record| True| True
2| Valid nonce recording| True| True
3| Modified nonce history detected| False| False
4| Deleted consumed nonce detected| False| False
5| Forged integrity tag rejected| False| False
6| Older signed snapshot rejected| False| False
7| Missing integrity metadata rejected| False| False
8| Corrupted record rejected| False| False
9| Unavailable storage fails closed| False| False
10| Duplicate nonce rejected| True| True
11| Fresh nonce accepted| True| True

Execution summary:

- Total checks: 11
- Passed: 11
- Failed: 0

3. Verified observations

[V] The initial replay-state record passed integrity verification.

[V] A valid nonce was recorded successfully.

[V] Adding an unauthorized nonce to the stored history was detected.

[V] Deleting a previously consumed nonce was detected.

[V] Replacing the integrity tag with a forged value was rejected.

[V] Restoring an older, previously valid signed snapshot was rejected by the simulated version trust anchor.

[V] Missing integrity metadata and corrupted record structures were rejected.

[V] Unavailable replay-state storage caused the operation to fail closed.

[V] Previously consumed nonces could not be recorded again.

[V] Fresh nonces were accepted when the replay-state integrity checks succeeded.

4. Security interpretation

[I] HMAC-SHA256 can detect modifications to authenticated replay-state data when the verification key remains protected.

[I] A separately maintained trusted version reference can help detect rollback to an older signed record.

[I] Fail-closed behaviour helps prevent authorization when replay history cannot be verified.

Core security principle:

Replay history must be protected against unauthorized modification, deletion and rollback. Its existence alone does not establish its integrity.

5. Limitations

This was a local Python simulation.

- The HMAC key was fixed test material.
- The version trust anchor was a separate simulated Python object, not an independently secured service.
- Replay-state storage was an in-memory object, not a durable database.
- No secure hardware or protected key-management system was tested.
- No real database transactions or atomic writes were tested.
- No concurrent modification or race-condition testing was performed.
- No real application restart, external authority or payment system was involved.
- The test does not establish protection against an attacker who can compromise both the integrity authority and trusted version reference.

6. Conclusion

[V] AG-C125 passed all 11 supplied test checks, with zero unexpected outcomes.

The simulation demonstrated detection of tested replay-state modifications, deletion, forged integrity metadata, rollback to an older snapshot and invalid storage conditions.

[I] Integrity verification combined with a separately maintained version reference is a useful design direction for further investigation.

These results do not establish production-grade tamper resistance or secure persistence.

7. Recommended next investigation

AG-C126 — Replay-State Write Failure and Atomic Update Simulation

Investigate what happens when replay-state updates fail partway through an operation.

Proposed areas:

- Failed writes.
- Interrupted updates.
- Version-reference mismatch.
- Partial record replacement.
- Recovery after interrupted updates.
- Fail-closed behaviour during inconsistent state.

8. Evidence classification

- [V] Verified: Supplied execution output shows 11/11 expected outcomes.
- [I] Interpretation: Integrity checks and version comparison detected the tested tampering and rollback scenarios.
- [H] Hypothesis: Properly engineered durable storage with atomic updates and independently protected integrity references could improve replay-state protection. Further testing is required.

LT Hub™ AgentGuard

Evidence before claims. Human oversight before consequential action.