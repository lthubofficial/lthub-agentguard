LT Hub™ AgentGuard — AG-C120

Process Isolation and Verification Authority Separation Simulation

Test ID: AG-C120
Test name: Process Isolation and Verification Authority Separation Simulation
Result: PASS — 10/10 checks passed, 0 failed
Environment: Google Colab / local Python multiprocessing
Scope: Local operating-system process simulation

1. Objective

Evaluate whether an application process can request integrity verification from a separately running verification authority without receiving the authority's secret key through the documented application interface.

2. Method

The simulation used Python multiprocessing and a communication pipe to create two separate operating-system processes:

- Application process: Sends verification requests and receives decisions.
- Verification authority process: Holds the test HMAC-SHA256 key, validates presented integrity tags and returns Boolean decisions.

The authority generated a trusted integrity tag during setup. The application used the tag to request verification without being directly supplied with the secret key.

3. Execution results

Check| Expected| Observed| Result
Authority runs in a separate process| True| True| PASS
Valid trusted actor accepted| True| True| PASS
Modified actor rejected| False| False| PASS
Tampered integrity tag rejected| False| False| PASS
Forged tag from unrelated key rejected| False| False| PASS
Application receives Boolean decision| True| True| PASS
No public key retrieval method exposed| False| False| PASS
Empty actor rejected| False| False| PASS
Malformed input does not authorize| False| False| PASS
Verification response does not expose test key| True| True| PASS

Total checks: 10
Passed: 10
Failed: 0

4. Verified observations [V]

The supplied execution output demonstrates that:

1. The authority and application had different process IDs.
2. The authority accepted a valid actor and matching integrity tag.
3. Modified actor identities were rejected.
4. Tampered and unrelated-key forged tags were rejected.
5. The application received Boolean verification decisions.
6. Empty and malformed inputs did not result in authorization.
7. The documented application client exposed no public key-retrieval method.
8. The verification response was a Boolean rather than the test key.

5. Security interpretation [I]

The simulation demonstrates that an application and verification authority can communicate across separate local operating-system processes.

The authority retained the test key within its own process during the simulation. The application requested verification through inter-process communication rather than directly performing HMAC verification.

This is an architectural improvement over the same-process arrangements investigated in AG-C117, AG-C118 and AG-C119.

6. Security limitations

- Both processes ran on the same local machine.
- No remote server or network boundary was tested.
- No hardware-backed key storage or external key-management service was used.
- No protection against operating-system administrator or root access was tested.
- The authority process was not hardened against process compromise.
- Same-machine process separation does not guarantee that privileged attackers cannot inspect process memory.
- The integrity tag was supplied to the application during setup; it is not the secret key.
- No real user authentication, payment transaction or production environment was tested.

7. Relationship to previous tests

- AG-C117: HMAC integrity protection simulation.
- AG-C118: Same-process integrity key exposure and forgery reproduced.
- AG-C119: Simulated application-facing verification interface behaviour confirmed.
- AG-C120: Separate-process verification authority simulation confirmed.

8. Conclusion

AG-C120: PASS — PROCESS SEPARATION SIMULATION CONFIRMED.

All 10 checks matched their expected outcomes.

The test provides evidence that a local application process can request verification from a separately running authority without receiving the secret key through the documented interface.

It does not establish secure key custody, resistance to privileged attackers, remote isolation or production-grade security.

Evidence classification: Execution output supplied by the project operator.

LT Hub™ AgentGuard principle: Evidence before claims. Human oversight before consequential action.