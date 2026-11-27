LT Hub™ AgentGuard — AG-C119

External Integrity Verification Boundary Simulation

Test ID: AG-C119
Test name: External Integrity Verification Boundary Simulation
Result: PASS — 10/10 checks passed, 0 failed
Scope: Local Python simulation

1. Objective

Evaluate whether an application-facing verification interface can request an integrity decision from a separately modelled verification authority without receiving the underlying test key through its documented interface.

2. Method

A local Python simulation modelled two components:

- VerificationAuthority: Generates and verifies HMAC-SHA256 integrity tags using a test secret.
- ApplicationVerificationClient: Requests verification and receives a Boolean decision or an uncertainty response.

The simulation tested valid verification, modified identities, tampered tags, forged tags, malformed inputs and the information returned to the application client.

3. Execution results

Check| Expected outcome| Result
Valid trusted actor verification| Accepted| PASS
Modified actor rejected| Rejected| PASS
Tampered integrity tag rejected| Rejected| PASS
Forged tag from unrelated key rejected| Rejected| PASS
Application receives Boolean decision| Boolean response| PASS
No public key retrieval method exposed| No documented public retrieval method| PASS
Empty actor rejected| Rejected| PASS
Empty integrity tag rejected| Rejected| PASS
Malformed input does not authorize| No authorization| PASS
Verification response does not expose test key| Key not returned in response| PASS

Total checks: 10
Passed: 10
Failed: 0

4. Verified observations [V]

The supplied execution output demonstrates that:

1. The verification authority accepted a valid actor and matching integrity tag.
2. Modified actor identities and tampered tags were rejected.
3. A tag generated using an unrelated test key was rejected.
4. The application client received a Boolean verification decision.
5. Empty and malformed inputs did not result in authorization.
6. The documented application-facing interface did not expose a public key-retrieval method.

5. Security interpretation [I]

The simulation demonstrates a useful interface design principle: an application can request an integrity decision without needing the verification key as part of its documented API.

This is a step beyond the earlier same-process key-exposure demonstration in AG-C118. However, the simulated interface does not establish a genuine security boundary.

6. Security limitations

- Both components operated in the same Python process.
- No network boundary or operating-system process isolation was tested.
- Python introspection may expose internal object references, including references to the authority.
- No hardware-backed key storage or external key-management service was used.
- No real user authentication or independently verified actor identity was tested.
- No production application, payment system or irreversible transaction was involved.
- The absence of a documented public key-retrieval method does not prove that the key cannot be extracted.

7. Relationship to previous tests

- AG-C116: Demonstrated dual-modification bypass of an unkeyed integrity fingerprint.
- AG-C117: Demonstrated HMAC-based integrity verification in a same-process simulation.
- AG-C118: Reproduced key exposure and HMAC forgery when the key was accessible.
- AG-C119: Demonstrated the expected behaviour of an application-facing verification interface.

8. Conclusion

AG-C119: PASS — SIMULATED VERIFICATION INTERFACE BEHAVIOUR CONFIRMED.

All 10 test checks matched their expected outcomes.

The result supports further investigation into separating application permissions from integrity-key custody. It does not establish external isolation, secure key custody or production-grade protection.

Evidence classification: Local simulation output supplied by the project operator.

LT Hub™ AgentGuard principle: Evidence before claims. Human oversight before consequential action.