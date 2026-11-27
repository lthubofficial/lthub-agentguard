LT Hub™ AgentGuard — AG-C122

Verification Authority Recovery and Reconnection Behaviour

Test ID: AG-C122
Test name: Verification Authority Recovery and Reconnection Behaviour
Result: PASS — 10/10 checks passed, 0 failed
Environment: Google Colab / Python multiprocessing
Scope: Local Python simulation

1. Objective

Evaluate whether an application can safely reconnect to a verification authority after shutdown and reject integrity evidence associated with a previous authority session.

The investigation focuses on session changes, stale evidence rejection and fresh verification after recovery.

2. Method

The simulation created a verification authority in a separate local operating-system process.

The authority generated:

- A session identifier.
- A session-bound HMAC-SHA256 integrity tag.

The application used the session identifier and integrity tag when requesting verification.

The original authority was stopped, and a new authority process was started. The new authority generated a different session identifier and a new integrity tag.

The application then tested old and fresh verification evidence against the restarted authority.

3. Execution results

Check| Expected| Observed| Result
Initial authority accepts valid verification| True| True| PASS
Stopped authority is no longer running| False| False| PASS
Old connection fails closed after shutdown| False| False| PASS
Restarted authority is running| True| True| PASS
Restart creates a different session identifier| True| True| PASS
Old session identifier rejected| False| False| PASS
Old integrity tag rejected after restart| False| False| PASS
Fresh integrity tag accepted after reconnection| True| True| PASS
Modified actor rejected after reconnection| False| False| PASS
Empty actor rejected after reconnection| False| False| PASS

Total checks: 10
Passed: 10
Failed: 0

4. Verified observations [V]

The supplied execution output demonstrates that:

1. The original authority accepted valid verification.
2. The original authority stopped successfully.
3. The old connection did not authorize after shutdown.
4. A replacement authority process started successfully.
5. The restarted authority generated a different session identifier.
6. The previous session identifier was rejected.
7. The previous integrity tag was rejected after restart.
8. Fresh integrity evidence was accepted.
9. Modified actor identities were rejected after reconnection.
10. Empty actor identities were rejected.

5. Security interpretation [I]

The simulation demonstrates session-bound integrity verification under the tested local restart conditions.

The new authority session does not accept the previous session's integrity tag. Fresh verification evidence is required after reconnection.

This supports the AgentGuard design principle that recovery must not automatically restore trust in previously presented verification evidence.

6. Security limitations

- This is a local Python simulation.
- No remote service or network reconnection was tested.
- The test key is a fixed simulation key.
- No hardware-backed key management was tested.
- No persistent storage or distributed session management was tested.
- No concurrent reconnection or race-condition testing was performed.
- Process restart does not establish production-grade recovery.
- No real payment or irreversible transaction was executed.

7. Relationship to previous tests

- AG-C119: Verification interface behaviour simulation.
- AG-C120: Separate-process verification authority simulation.
- AG-C121: Verification authority failure and fail-closed behaviour simulation.
- AG-C122: Verification authority recovery and reconnection behaviour simulation.

8. Conclusion

AG-C122: PASS — AUTHORITY RECOVERY SIMULATION CONFIRMED.

All 10 checks matched their expected outcomes.

The simulation provides evidence that the restarted authority rejected old session identifiers and old integrity tags while accepting fresh verification evidence.

This does not establish production-grade recovery, secure distributed session management or hardware-backed key protection.

Evidence classification: Local execution output supplied by the project operator.

LT Hub™ AgentGuard principle: Evidence before claims. Human oversight before consequential action.