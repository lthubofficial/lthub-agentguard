LT Hub™ AgentGuard — Test 108

Test ID: AG-C108
Test name: Single-Use Approval Replay Prevention
Scope: Local Python decision-logic simulation

Result

PASS — 12/12 test cases passed; 19 individual attempts checked; 0 unexpected outcomes.

Objective

Evaluate whether a simulated approval token can be consumed only once and whether subsequent attempts to reuse the same token are blocked.

Evidence

The supplied corrected Google Colab execution output records 12 passing test cases:

1. First use of approval token.
2. Replay of previously consumed token.
3. Different token remains usable.
4. Repeated replay attempts.
5. Empty token.
6. Whitespace token.
7. Null token.
8. Numeric token.
9. Case-sensitive token distinction.
10. Replay after another token is consumed.
11. Independent guard instance.
12. Missing token.

The corrected implementation checks individual attempts within each sequence, rather than checking only the final result.

All 12 test cases passed, with 19 individual attempts evaluated.

Interpretation

The simulation demonstrates single-use token behaviour within one in-memory guard instance.

A first valid token use returns "APPROVED_ONCE". Subsequent use of the same token returns "REPLAY_BLOCKED".

Different token strings are accepted independently. Invalid or missing tokens return "STATUS_UNCERTAIN".

Limitations

This was a local Python simulation using an in-memory set to track consumed tokens.

It did not test persistence across process restarts, concurrent requests, distributed systems, atomic database operations, cryptographic approval authenticity, transaction-hash binding, authorization or real payment execution.

The independent guard instance test demonstrates separate in-memory state, not shared replay protection across instances.

The results do not establish production readiness or prove that the wider AgentGuard project is secure.

Conclusion

The supplied corrected execution output supports a PASS for the 12 defined Test 108 cases within the stated simulation scope.

Evidence principle: Evidence before claims. Human oversight before consequential action.