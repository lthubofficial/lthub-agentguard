LT Hub™ AgentGuard — AG-C124

Replay Cache Persistence and Restart Behaviour Simulation

Test ID: AG-C124
Test name: Replay Cache Persistence and Restart Behaviour Simulation
Result: PASS — 11/11 checks passed
Failed checks: 0
Scope: Local Python simulation
Evidence status: [V] Execution output supplied by the user

1. Objective

Investigate whether previously consumed verification responses can be replayed after an application restart resets its in-memory replay cache.

The simulation compares an in-memory replay cache with a separately retained, simulated replay-state store.

2. Test results

No.| Test condition| Expected| Observed
1| Initial valid response| True| True
2| Duplicate before restart| False| False
3| Old response after memory-cache reset| True| True
4| Fresh response using simulated persistent cache| True| True
5| Consumed response rejected| False| False
6| Old response rejected after simulated restart| False| False
7| Corrupted store| False| False
8| Missing replay history| False| False
9| Unavailable store| False| False
10| Invalid replay-history entry| False| False
11| Fresh response after simulated restart| True| True

Execution summary:

- Total checks: 11
- Passed: 11
- Failed: 0

3. Verified observations

[V] A valid verification response was initially accepted.

[V] Reusing the response before resetting the in-memory cache was rejected.

[V] After replacing the in-memory cache with a new instance, the previously consumed response was accepted again.

Finding: The simulation reproduced an in-memory replay-cache reset weakness.

[V] The simulated persistent replay-state store rejected a previously consumed response.

[V] The same simulated store continued rejecting that response after creating a new cache instance.

[V] Corrupted, missing, unavailable and malformed replay-state data caused authorization to fail closed in the tested cases.

4. Security interpretation

[I] An in-memory replay cache alone is insufficient to prevent replay across application restarts if consumed-response history is lost.

[I] Retaining replay history outside the replaceable cache object can prevent the demonstrated replay scenario, provided the retained history is trustworthy and correctly updated.

[I] Fail-closed handling is important when replay history cannot be loaded or validated.

Core security principle:

A restart must not erase the security history required to reject previously consumed authorization responses.

5. Critical limitations

This was a local Python simulation.

- The restart was simulated by creating new cache objects.
- The persistent store was an in-memory Python object, not a disk database.
- No real application or operating-system process restart was performed.
- No durable database transaction or crash recovery was tested.
- No atomic write guarantees were established.
- Concurrent requests and race conditions were not tested.
- The HMAC key was fixed test material.
- No real network, payment or production environment was accessed.

Consequently, this test does not establish durable or production-grade replay protection.

6. Conclusion

[V] AG-C124 passed all 11 expected test checks.

The simulation reproduced a replay weakness when the in-memory cache was reset and demonstrated that a separately retained simulated replay store rejected the old response.

[I] These results justify further testing of durable replay-state storage, crash recovery and atomic updates.

The simulated store must not be described as a verified production persistence mechanism.

7. Recommended next investigation

AG-C125 — Persistent Replay-State Integrity and Tampering Simulation

Investigate whether replay-state records can be modified, deleted, replaced or manipulated without detection.

Proposed investigation areas:

- Modification of previously consumed nonce records.
- Deletion of replay history.
- Replacement of stored replay-state data.
- Integrity verification of replay-state records.
- Corrupted integrity metadata.
- Fail-closed behaviour when integrity verification fails.

8. Evidence classification

- [V] Verified: Supplied execution output shows 11/11 expected outcomes.
- [I] Interpretation: Resetting an in-memory replay cache can permit reuse of previously consumed responses.
- [H] Hypothesis: Independently protected durable replay-state storage with atomic updates could improve replay resistance across real restarts. This requires separate testing.

LT Hub™ AgentGuard

Evidence before claims. Human oversight before consequential action.