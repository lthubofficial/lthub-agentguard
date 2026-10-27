Test 88 — Concurrent First-Time Registration of Conflicting Payloads

Project: LT Hub™ AgentGuard
Test ID: AG-C088
Status: PASS — 5/5 checks
Trials: 100
Test type: Local concurrency simulation

1. Objective

Evaluate whether two concurrent requests using the same previously unused request ID, but carrying different transaction payloads, result in only one accepted registration and one recorded effect.

2. Test configuration

The simulation used request ID "REQ-088" and two competing payloads:

- Payload A: Transaction "TX-088-A", amount 1000 ZAR, recipient "SUPPLIER-A".
- Payload B: Transaction "TX-088-B", amount 2500 ZAR, recipient "SUPPLIER-B".

Each trial started with an empty request registry. Two threads were released through a barrier and attempted registration concurrently. A process-local "threading.Lock" protected the request lookup, registration, and effect recording.

3. Observed results [V]

- Trials executed: 100
- "COMMITTED" responses: 100
- "IDEMPOTENCY_CONFLICT" responses: 100
- Valid response pairs: 100/100
- Exactly one recorded effect: 100/100
- Winning request record preserved: 100/100
- Stored record matched the only effect: 100/100
- Unexpected outcomes: 0
- Checks passed: 5/5
- Overall result: PASS

4. Interpretation [I]

The observed results are consistent with the intended invariant: within this simulation, only one competing payload was registered for a request ID, while the other payload was rejected as a conflict. Each trial recorded one effect, and the stored record matched that effect.

The test supports the behaviour of the implemented control under the tested single-process conditions. It does not demonstrate that the same guarantees hold in a production payment system.

5. Limitations

- Request records and effects were stored in memory.
- Synchronization used a Python lock within one process.
- The barrier synchronized the threads before their attempts but did not guarantee simultaneous entry into the critical section.
- No database transaction, durable idempotency store, process crash, or multi-server execution was tested.
- The recorded effect was a local list entry, not an actual payment.
- The test did not establish recovery behaviour after a crash or a failure between persistent registration and an external side effect.

6. Conclusion [V]/[I]

Observed conclusion [V]: All 100 trials satisfied the five programmed checks.

Interpretation [I]: The local simulation behaved consistently with single-winner registration and conflicting-payload rejection.

Unverified hypothesis [H]: A production implementation would need durable, atomic request registration and appropriate coordination with external side effects to preserve these properties across crashes and distributed workers.

Research principle: AI may research, analyse, recommend and prepare. Humans retain authority over money, identity, sensitive information and irreversible decisions.

Next frontier: Test 89 — verify that a stored request ID and payload remain consistent when an attempted conflicting registration encounters a simulated storage failure.