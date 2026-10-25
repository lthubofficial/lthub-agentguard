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

## 14. Source Record — Role Based Access Control (RBAC)

Evidence ID: LT-AG-E009

Source title: Role Based Access Control (RBAC)

Publisher: National Institute of Standards and Technology (NIST)

Source URL: https://csrc.nist.gov/projects/role-based-access-control

Page update date: 2026-03-04 (as displayed on the page)

Access date: 2026-10-25

Source type: Official access-control research project page

Source findings

Claim 1 — [V] Source content: The NIST project page discusses role-based access control (RBAC), attribute-based access control (ABAC), and related access-control research.

Supporting reference: The page sections titled “RBAC vs. ABAC (Attribute Based Access Control)” and “Primary References and Background.”

Claim 2 — [V] Source content: The page lists research on RBAC models, access-control configuration vulnerabilities, and the characteristics and trade-offs of RBAC and ABAC.

Supporting reference: The research references listed on the NIST project page.

Relevance to LT Hub™ AgentGuard

[I] Research implication: Access-control models are relevant to investigating how an AI agent's permissions can be limited and governed. The suitability of a particular model depends on the agent's tasks, system architecture, and authorization requirements.

Proposed control — not yet validated

- AG-C005 [H]: Investigate whether each AgentGuard tool can be assigned narrowly scoped permissions appropriate to its defined task, with authorization enforced by the system executing the action.

Proposed validation work

Identify a controlled test environment and document the permissions available to a test agent. Check whether an action outside its authorized scope is rejected by the enforcing system.

Do not perform unauthorized actions against live systems.

Required test record: Test ID, environment, configuration, authorized scope, test steps, expected result, observed result, supporting logs, date, and reviewer.

Current test status: Not run.

Limitations

The NIST page describes access-control research and references related publications. Its presence does not demonstrate that a particular AgentGuard design implements RBAC or ABAC, nor that any proposed control is effective.

Verification status: The supplied page content supports the recorded description of the source. Implementation and control effectiveness remain unverified.

Next action: Review the relevant primary research or standard before making a more specific technical claim, then design and document a controlled authorization test.

---

LT Hub™ | Creative AI Solutions Powered by Intelligence

## 15. Source Record — Human Approval and Rate Limiting

Evidence ID: LT-AG-E010

Source title: LLM06:2025 Excessive Agency

Publisher: OWASP GenAI Security Project

Source URL: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/?lang=us

Access date: 2026-10-25

Source type: Published AI application security guidance

Source findings

Claim 1 — [V] Published recommendation: OWASP describes rate limiting as a way to reduce the number of undesirable actions that can occur within a given time period, creating more opportunity for monitoring to detect problems before significant damage occurs.

Supporting reference: The rate-limiting mitigation passage supplied from the official OWASP LLM06:2025 page.

Claim 2 — [V] Published example: OWASP describes a personal assistant with mailbox access whose email extension has sending functionality beyond the intended message-reading task.

Supporting reference: The “Example Attack Scenarios” section of the official LLM06:2025 page.

Claim 3 — [V] Published mitigation examples: OWASP describes reducing excessive functionality, using read-only OAuth permissions where appropriate, requiring user review before sending drafted email, and applying rate limits to the sending interface.

Supporting reference: The mailbox attack scenario and its accompanying mitigation discussion.

Relevance to LT Hub™ AgentGuard

[I] Research implication: Human confirmation, narrow permissions, limited tool functionality, and rate limiting are complementary safeguards to investigate for AI agents performing consequential actions.

Proposed controls — not yet validated

- AG-C006 [H]: Require explicit human confirmation before defined high-impact actions.
- AG-C007 [H]: Apply rate limits to selected consequential tool actions.
- AG-C008 [H]: Separate read-only capabilities from write or send capabilities where the system permits.
- AG-C009 [H]: Monitor rejected actions and unusual activity, subject to appropriate logging and privacy safeguards.

Proposed validation work

In a controlled test environment, define an agent task that drafts an email without sending it. Verify whether the system requires human confirmation before any send action. Separately, test whether configured rate limits reject requests exceeding the defined threshold.

Do not test against real mailboxes or send unsolicited messages.

Required test record: Test ID, environment, configuration, threshold, exact steps, expected result, observed result, logs, date, and reviewer.

Current test status: Not run.

Limitations

The cited OWASP material documents guidance and an illustrative attack scenario. It does not prove that the proposed AgentGuard controls are implemented or effective. Rate limiting alone does not prevent every unauthorized action, and human approval must be enforced by the surrounding system to be meaningful.

Verification status: The supplied passage supports the recorded source findings. AgentGuard implementation and control effectiveness remain unverified.

Next action: Identify the exact actions that require approval, define safe rate limits for a test environment, and document reproducible test results before changing any proposed control's status.

## 16. Source Record — OWASP LLM01:2025 Prompt Injection

Evidence ID: LT-AG-E011

Source title: LLM01:2025 Prompt Injection

Publisher: OWASP GenAI Security Project

Source URL: https://genai.owasp.org/llmrisk/llm01-prompt-injection/

Access date: 2026-10-25

Source type: Published AI application security guidance

Source findings

Claim 1 — [V] Published assessment: OWASP states that prompt injection vulnerabilities arise from the nature of generative AI and that foolproof prevention methods are unclear.

Supporting reference: The “Prevention and Mitigation Strategies” section of the official LLM01:2025 page.

Claim 2 — [V] Published recommendations: OWASP describes measures including constraining model behaviour, validating expected output formats, filtering inputs and outputs, enforcing least-privilege access, requiring human approval for high-risk actions, segregating untrusted external content, and conducting adversarial testing.

Supporting reference: The seven mitigation measures listed in the official LLM01:2025 page.

Claim 3 — [V] Published examples: OWASP describes direct and indirect prompt injection, malicious instructions in retrieved documents, multimodal injection, payload splitting, and obfuscated or multilingual attacks, among other scenarios.

Supporting reference: The “Example Attack Scenarios” section of the official LLM01:2025 page.

Relevance to LT Hub™ AgentGuard

[I] Research implication: An AI agent's security cannot rely only on its system prompt. Research should examine trust boundaries, tool permissions, input and output handling, human authorization, and adversarial testing.

Proposed controls — not yet validated

- AG-C010 [H]: Clearly identify external documents, webpages, emails, and retrieved content as untrusted input.
- AG-C011 [H]: Enforce tool permissions and authorization outside the model's natural-language instructions.
- AG-C012 [H]: Validate tool arguments and structured outputs against predefined rules before execution.
- AG-C013 [H]: Require human approval for defined high-impact operations.
- AG-C014 [H]: Test direct and indirect prompt-injection scenarios in a controlled environment.

Proposed validation work

In an isolated test environment, provide a test agent with a benign task and a document containing an instruction that conflicts with the task.

Observe whether the agent treats the document's instruction as untrusted content, whether it attempts restricted tool calls, and whether external authorization controls reject unauthorized actions.

Use synthetic data only. Do not test against real accounts, private documents, or live systems.

Required test record: Test ID, environment, model and configuration, test input, expected behaviour, observed behaviour, tool-call trace, authorization outcome, date, and reviewer.

Current test status: Not run.

Limitations

OWASP guidance describes risks and mitigation approaches; it does not establish that LT Hub™ AgentGuard implements these controls or is resistant to prompt injection. No single proposed control should be assumed to prevent every attack. Control effectiveness must be assessed through documented testing.

Verification status: The supplied source passage supports the recorded descriptions of OWASP's guidance. AgentGuard implementation and effectiveness remain unverified.

Next action: Review the proposed controls, select a safe test scenario, and document actual observations before changing any hypothesis to a validated status.

## 17. Source Record — OWASP LLM02:2025 Sensitive Information Disclosure

Evidence ID: LT-AG-E012

Source title: LLM02:2025 Sensitive Information Disclosure

Publisher: OWASP GenAI Security Project

Source URL: https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/

Access date: 2026-10-25

Source type: Published AI application security guidance

Source findings

Claim 1 — [V] Published guidance: The supplied OWASP passage recommends sanitizing sensitive data, validating inputs, enforcing least-privilege access, and restricting access to data sources.

Supporting reference: The “Prevention and Mitigation Strategies” section supplied from the official LLM02:2025 page.

Claim 2 — [V] Published guidance: The passage discusses privacy techniques, user education, transparency about data use, secure configuration, and tokenization or redaction as possible safeguards.

Supporting reference: The privacy, user education, secure configuration, and advanced-techniques subsections.

Claim 3 — [V] Published examples: The passage describes potential sensitive-data exposure through inadequate sanitization, targeted prompt injection, and the inclusion of sensitive information in training data.

Supporting reference: The “Example Attack Scenarios” section.

Relevance to LT Hub™ AgentGuard

[I] Research implication: Agent security research should examine what data an agent can access, what information enters model context, what outputs are released, and whether sensitive information is protected throughout the workflow.

Proposed controls — not yet validated

- AG-C015 [H]: Limit agent access to sensitive data required for the assigned task.
- AG-C016 [H]: Use synthetic or appropriately redacted data in research and testing.
- AG-C017 [H]: Evaluate input and output handling for unintended disclosure of sensitive information.
- AG-C018 [H]: Document data collection, retention, access, and deletion practices for any future AgentGuard implementation.
- AG-C019 [H]: Review whether secrets or sensitive values could appear in logs, error messages, or generated outputs.

Proposed validation work

In an isolated test environment, use synthetic records containing clearly identifiable test-only secret values. Test whether an agent can retrieve or disclose values outside its authorized scope.

Record whether access controls reject unauthorized retrieval and whether outputs or logs expose restricted values.

Do not use real credentials, personal information, private client data, or production systems.

Required test record: Test ID, environment, synthetic data description, authorization rules, exact steps, expected result, observed result, relevant logs, date, and reviewer.

Current test status: Not run.

Limitations

The supplied passage describes guidance and potential safeguards. It does not prove that every listed technique is suitable for every system or that LT Hub™ AgentGuard has implemented or tested any of them. Federated learning, differential privacy, and homomorphic encryption require context-specific evaluation and must not be presented as automatic guarantees against data disclosure.

Verification status: The supplied source passage supports the recorded descriptions of the guidance. AgentGuard implementation and control effectiveness remain unverified.

Next action: Review the full source and determine which data-protection risks are relevant to the proposed AgentGuard scope before designing controlled tests.

## 18. Source Record — OWASP LLM05:2025 Improper Output Handling

Evidence ID: LT-AG-E013

Source title: LLM05:2025 Improper Output Handling

Publisher: OWASP GenAI Security Project

Source URL: https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/

Access date: 2026-10-25

Source type: Published AI application security guidance

Source findings

Claim 1 — [V] Published recommendation: OWASP recommends treating model output as untrusted, validating it before passing it to backend functions, and applying a zero-trust approach.

Supporting reference: The “Prevention and Mitigation Strategies” passage supplied from the official LLM05:2025 page.

Claim 2 — [V] Published recommendations: OWASP describes output encoding appropriate to the destination context, parameterized database queries, Content Security Policies, and logging and monitoring as relevant safeguards.

Supporting reference: The output encoding, database operation, CSP, and monitoring recommendations in the supplied source passage.

Claim 3 — [V] Published examples: OWASP describes risks involving unauthorized extension functions, unvalidated data transfers, destructive SQL queries, cross-site scripting (XSS), unsafe generated email content, and insecure code or package suggestions.

Supporting reference: The six attack scenarios in the supplied source passage.

Relevance to LT Hub™ AgentGuard

[I] Research implication: An AI agent's output should not be trusted merely because the model generated it. The system receiving the output must enforce validation, authorization, and safe handling appropriate to the operation.

Proposed controls — not yet validated

- AG-C020 [H]: Validate model-generated tool arguments against a defined schema before execution.
- AG-C021 [H]: Enforce authorization in the receiving system independently of model-generated instructions.
- AG-C022 [H]: Use context-appropriate output encoding when displaying model-generated content.
- AG-C023 [H]: Use parameterized queries or prepared statements when model-generated values are used in database operations.
- AG-C024 [H]: Record relevant validation failures and rejected operations without unnecessarily logging sensitive data.

Proposed validation work

In an isolated test application, supply benign model output and deliberately malformed or unauthorized test values to a mock receiving function.

Verify that invalid arguments are rejected, unauthorized operations cannot execute, and rendered text is handled safely in its intended context.

Use mock functions and synthetic data. Do not execute destructive queries, deploy attack payloads against live systems, or test against production databases.

Required test record: Test ID, environment, receiving component, validation rules, exact steps, expected result, observed result, logs, date, and reviewer.

Current test status: Not run.

Limitations

The supplied OWASP passage documents security guidance and illustrative attack scenarios. It does not demonstrate that LT Hub™ AgentGuard implements these safeguards or that any proposed control is effective. Output encoding must match the actual output context; no single encoding or validation rule is suitable for every destination.

Verification status: The supplied source passage supports the recorded descriptions of the guidance. AgentGuard implementation and control effectiveness remain unverified.

Next action: Identify the intended receiving components in the proposed AgentGuard architecture, define their validation and authorization requirements, and conduct controlled tests before claiming effectiveness.
