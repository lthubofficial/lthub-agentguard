AG-C127 — Concurrent Replay-State Update and Race-Condition Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C127
Test category: Replay-state integrity / concurrency / race conditions
Result: PASS — simulated race condition reproduced and lock-protected duplicate rejection demonstrated
Execution scope: Local Python threading simulation

1. Objective

Investigate whether concurrent replay-state update requests can bypass duplicate nonce protection, produce inconsistent authorization outcomes, or cause competing version updates to overwrite one another.

The test compares an intentionally unsafe implementation with a lock-protected local simulation.

2. Test results

Total checks: 11
Passed: 11
Failed: 0

3. Evidence register

Check| Observed result
First sequential nonce submission| Accepted
Second sequential nonce submission| Rejected
Concurrent duplicate race| Both requests accepted
Shared nonce in resulting state| Present
Lock-protected duplicate handling| Exactly one accepted
Lock-protected duplicate rejection| Exactly one rejected
Lock-protected nonce state| One shared nonce
Distinct concurrent submissions| Both accepted
Distinct nonce preservation| Both preserved
Competing version updates| Only one succeeded
Final version| 1

4. Key finding: concurrent replay vulnerability

The intentionally unsafe implementation separates the duplicate check from the state update.

Both threads inspect the replay state before either thread writes the nonce. Both therefore observe that the nonce is unused and both return an accepted result.

This reproduces a time-of-check-to-time-of-use (TOCTOU) race condition in the simulated design.

Important distinction: The resulting set contains the nonce only once, but two requests were accepted. A single stored nonce does not prove that duplicate authorization was prevented.

5. Lock-protected comparison

The second implementation places the duplicate check and nonce insertion inside a shared Python thread lock.

Observed behaviour:

- One concurrent request is accepted.
- The competing duplicate request is rejected.
- Distinct nonce submissions are both accepted.
- Competing updates using the same expected version result in only one successful update.

This demonstrates the value of coordinating check-and-update operations within the local simulation.

6. Security interpretation

[V] The unsafe implementation reproduced concurrent duplicate acceptance.

[V] The lock-protected implementation rejected the competing duplicate request.

[I] Replay-state protection requires more than checking whether a nonce exists. The check and state transition must be coordinated so competing requests cannot both act on stale state.

[I] A production implementation would require suitable atomic database operations, transaction isolation, concurrency control and durable replay-state integrity.

[H] Similar race conditions may arise in distributed AI-agent payment workflows if separate workers or services independently validate and consume the same approval state. This requires further testing.

7. Limitations

- Python threading simulation only.
- No production database or transaction isolation tested.
- No actual operating-system process isolation or distributed concurrency tested.
- No multi-server or network race condition tested.
- Python thread locks do not establish cross-process or distributed atomicity.
- No real payment execution or external authorization system tested.
- No production security certification or assurance established.

8. Conclusion

AG-C127 completed with 11/11 checks passing.

The test reproduced a concurrent duplicate-acceptance vulnerability in the intentionally unsafe implementation and demonstrated duplicate rejection using a lock-protected local simulation.

The result supports further investigation into atomic replay-state updates, durable storage, transaction isolation and distributed concurrency controls.

Evidence classification: Local simulation evidence.

Final principle: Evidence before claims. Human oversight before consequential action.

LT Hub™ AgentGuard — Human Authority is a Security Boundary.