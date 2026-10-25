LT Hub™ AgentGuard — Evidence Register

Document ID: LT-AG-ER-001
Version: 1.0
Status: Initial register template
Project: LT Hub™ AgentGuard

1. Purpose

This register tracks the sources, verification status, limitations, and claims used in LT Hub™ AgentGuard AI security research.

Its purpose is to make claims traceable, distinguish evidence from interpretation, document uncertainty, and prevent unsupported claims from being presented as established facts.

Creating this register does not independently verify any security claim.

2. Evidence Classification

Label| Meaning| Requirement
[V] Verified| A specific claim is supported by relevant, identifiable evidence.| Record the source or reproducible observation and explain what it supports.
[I] Inferred| A reasoned interpretation of available evidence.| Record the evidence, reasoning, and limitations.
[H] Hypothesis| A proposition requiring investigation or testing.| State what evidence or experiment could support or challenge it.

Verification applies to a specific claim, not automatically to an entire source.

3. Evidence Record Fields

Each substantive claim should have:

1. Evidence ID.
2. Exact claim.
3. Evidence classification.
4. Source title and author or publisher.
5. Direct source URL, where available.
6. Publication date, if known.
7. Access date.
8. Supporting passage or reproducible observation.
9. Limitations and uncertainty.
10. Verification status.
11. Reviewer notes and next steps.

Never invent missing source details. Mark unavailable information as unknown or not recorded.

4. Initial Research Register

These are research topics awaiting source review, not verified findings.

Evidence ID| Research topic| Initial classification| Status
LT-AG-E001| Prompt injection and untrusted instructions| [H]| Source review required
LT-AG-E002| Least-privilege permissions for AI agents| [H]| Source review required
LT-AG-E003| Human approval for consequential actions| [H]| Source review required
LT-AG-E004| Credential and secret protection| [H]| Source review required
LT-AG-E005| Validation of tool outputs| [H]| Source review required
LT-AG-E006| Audit logging and accountability| [H]| Source review required

5. Source Quality Review

Evaluate each source by asking:

- Is the author or publisher identifiable?
- Does the source support the exact claim?
- Is its publication date known and the information still applicable?
- Does it provide primary evidence, reproducible testing, or a transparent methodology?
- Are limitations and conflicts of interest disclosed?
- Do other relevant sources corroborate the claim where necessary?
- Does the cited passage support the wording used?

Official guidance establishes what an organization documents or recommends. It does not automatically prove that a control is effective in every implementation.

6. Verification Workflow

Claim → Source discovery → Source inspection → Claim matching → Limitation review → Classification → Review

For each claim:

1. Define precisely what is being asserted.
2. Find a relevant, authoritative source.
3. Inspect the source itself rather than relying only on a search snippet.
4. Record the supporting passage.
5. Check the source's date and applicability.
6. Identify uncertainty and contradictory evidence.
7. Assign an evidence classification.
8. Record the review date and follow-up work.

Distinguish published guidance from demonstrated test results.

7. Conflicting Evidence

When sources disagree:

- Record the competing claims and their sources.
- Compare dates, methods, scope, and assumptions.
- Do not silently discard contradictory findings.
- Reduce confidence when disagreement remains unresolved.
- Document what further evidence could resolve the issue.

8. Research Integrity Rules

- Do not fabricate citations, quotations, URLs, dates, or test results.
- Do not label AI-generated text as independently verified evidence.
- Do not confuse a proposed control with an implemented control.
- Do not claim a test passed without recording its procedure and observed result.
- Correct inaccurate records transparently.
- Never publish credentials, confidential client information, or sensitive personal data.
- Separate source statements from researcher interpretation.

9. Review and Maintenance

Review records when a source changes, new evidence contradicts an existing claim, relevant security guidance is updated, testing reveals a limitation, or the research scope changes.

Record the date and reason for significant status changes.

10. Current Status

Status: Register structure established; source-level verification outstanding.

No external claim is declared verified solely by this template. The initial research topics require source discovery, inspection, and claim-specific evaluation.

11. Next Actions

- [ ] Locate authoritative sources on AI agent security and prompt injection.
- [ ] Review primary documentation and relevant security guidance.
- [ ] Populate records with actual source details.
- [ ] Match each claim to a supporting passage.
- [ ] Document limitations and conflicting evidence.
- [ ] Review the register before drawing conclusions.

---

LT Hub™ | Creative AI Solutions Powered by Intelligence

Evidence before claims. Uncertainty documented. Conclusions open to review.

## 12. Source Record — OWASP Top 10 for LLM Applications (2025)

Evidence ID: LT-AG-E007

Source title: OWASP Top 10 for Large Language Model Applications (2025)

Publisher: OWASP GenAI Security Project

Source URL: https://genai.owasp.org/llm-top-10/

Access date: 2026-10-25

Source type: Published AI security risk guidance

Verified source finding [V]: The OWASP 2025 taxonomy identifies risks including Prompt Injection (LLM01), Sensitive Information Disclosure (LLM02), Improper Output Handling (LLM05), and Excessive Agency (LLM06).

Relevance to LT Hub™ AgentGuard: This source supports investigating instruction manipulation, sensitive information exposure, unsafe handling of model outputs, and excessive agent permissions.

Limitations: The OWASP taxonomy is published guidance. It does not prove that LT Hub™ AgentGuard has implemented effective controls, passed security tests, or is free from vulnerabilities.

Verification status: The source page has been reviewed for the finding stated above.

Related source — Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/?lang=us

Next action: Review the source's mitigation guidance and record individual claims with supporting references before treating proposed controls as validated.

## 13. Source Record — OWASP LLM06:2025 Excessive Agency

Evidence ID: LT-AG-E008

Source title: LLM06:2025 Excessive Agency

Publisher: OWASP GenAI Security Project

Source URL: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/?lang=us

Access date: 2026-10-25

Source type: Published AI application security guidance

Source findings

Claim 1 — [V] Source classification: OWASP identifies Excessive Agency as a risk in its 2025 Top 10 for Large Language Model Applications.

Supporting reference: The official LLM06:2025 page identifies the risk and describes how an AI application can take damaging actions in response to unexpected, ambiguous, or manipulated model outputs.

Claim 2 — [V] Source description: OWASP identifies excessive functionality, excessive permissions, and excessive autonomy as typical root causes.

Supporting reference: The “Root Cause” discussion on the official LLM06:2025 page.

Claim 3 — [V] Published recommendation: OWASP recommends limiting available extensions and their functionality, minimizing permissions, requiring human approval for high-impact actions, and enforcing authorization in downstream systems.

Supporting reference: The “Prevention and Mitigation Strategies” section on the official LLM06:2025 page.

Relevance to LT Hub™ AgentGuard

[I] Research implication: Restricting an agent's available tools, permissions, and independent authority may reduce opportunities for unintended or unauthorized actions. The effectiveness of specific controls depends on implementation and testing.

Proposed controls — not yet validated

- AG-C001 [H]: Limit each agent to the tools required for its defined task.
- AG-C002 [H]: Enforce least-privilege permissions in the systems that execute tool requests.
- AG-C003 [H]: Require explicit human approval before defined high-impact actions.
- AG-C004 [H]: Record tool requests, authorization decisions, approvals, and outcomes for later review.

Proposed validation test

In a controlled test environment, define a task that requires read-only access. Attempt an unauthorized write or delete action.

Expected result: The downstream authorization control rejects the unauthorized action, and the attempt is recorded where audit logging is configured.

Required test record: Test ID, environment, configuration, exact steps, observed result, logs or other evidence, date, and reviewer.

Current test status: Not run. No test result is claimed.

Limitations

This source documents OWASP's security guidance. It does not establish that LT Hub™ AgentGuard is implemented, deployed, independently audited, or effective. The proposed controls remain hypotheses until their implementation and test results are documented.

Verification status: Source reviewed; claims about the contents of the OWASP guidance are supported by the cited source. Control effectiveness remains unverified.

Next action: Design a safe, reproducible least-privilege test and record its results before changing any proposed control to a validated status.
