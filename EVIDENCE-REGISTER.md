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

## 19. Source Record — OWASP LLM03:2025 Supply Chain

Record ID: E014
Research Series: LT Hub™ AgentGuard AI Agent Security Risk Research Series
Research Date: 2026-10-25
Evidence Status: Source reviewed; proposed controls not yet tested
Primary Source: OWASP GenAI Security Project — LLM03:2025 Supply Chain
Source URL: https://genai.owasp.org/llmrisk/llm032025-supply-chain/

19.1 Research Question

How can compromised, outdated, unverified, or improperly licensed third-party components undermine the security and integrity of an AI application or agent?

19.2 Source Findings

[V] Verified — Source description

The OWASP LLM03:2025 page identifies supply-chain vulnerabilities affecting the integrity of training data, models, deployment platforms, software dependencies, and other third-party components. It describes risks from tampering, poisoning, vulnerable packages, outdated models, weak model provenance, compromised fine-tuning adapters, and unclear supplier terms or privacy policies.

[V] Verified — Mitigation guidance published by OWASP

The source recommends measures including:

- Vetting suppliers, data sources, terms and conditions, and privacy policies.
- Scanning, managing, and patching vulnerable or outdated software components.
- Evaluating third-party models through security testing and AI red teaming.
- Maintaining an accurate Software Bill of Materials (SBOM) or evaluating relevant AI/ML bill-of-materials approaches.
- Tracking software and dataset licences.
- Verifying model origins and using integrity checks, hashes, and signing where appropriate.
- Monitoring collaborative development and model-handling environments.
- Testing supplied models and data for signs of tampering or poisoning.
- Maintaining patching policies and using integrity protections for models deployed on devices.

These are recommendations described by the source, not controls confirmed as implemented by LT Hub™.

19.3 Security Implications

[I] Inferred

An AI agent may inherit risks from the models, libraries, plugins, datasets, adapters, and services on which it depends. A component that appears trustworthy may still have an uncertain origin or contain an unrecognised vulnerability.

For agent security, checking the agent's permissions alone may therefore be insufficient. Its dependency inventory, supplier trust, update process, and component integrity also require consideration.

19.4 Proposed AgentGuard Controls

All controls below are [H] Hypotheses until implemented and tested.

- AG-C025 — Dependency Inventory: Record relevant software packages, model providers, model versions, plugins, and external services.
- AG-C026 — Source and Provenance Verification: Define checks for confirming the origin and identity of downloaded models and other security-sensitive components.
- AG-C027 — Integrity Verification: Where supported, verify trusted hashes or digital signatures before accepting or deploying components.
- AG-C028 — Vulnerability and Update Review: Establish a process for identifying outdated or vulnerable dependencies and recording patch decisions.
- AG-C029 — Supplier and Licence Review: Record supplier trust considerations, applicable software or dataset licences, and relevant privacy terms.

19.5 Proposed Validation Plan

Test status: NOT RUN

Use a controlled test environment and synthetic or non-sensitive sample data.

1. Create an inventory containing a small set of sample dependencies and model artefacts.
2. Introduce a deliberately incorrect expected hash for a harmless test file.
3. Check whether the proposed integrity procedure detects the mismatch and prevents acceptance under the defined test rules.
4. Include a sample dependency with an intentionally outdated version in the test inventory and check whether the review procedure flags it.
5. Record the expected result, observed result, evidence, limitations, and any corrective action.

Do not download or execute suspicious models, packages, or malware to conduct this test. A written procedure or successful demonstration with sample files does not establish the security of a production AI agent.

19.6 Evidence and Limitations

- The OWASP page supports the recorded descriptions of supply-chain risks and recommended mitigations.
- [I] The implications for an individual AI agent depend on its actual architecture, dependencies, deployment environment, and access.
- [H] AG-C025–AG-C029 are proposed controls; their effectiveness remains unverified.
- No implementation, independent audit, or security test result is claimed by this record.

19.7 Research Conclusion

AI agent security includes the integrity and trustworthiness of the components on which the agent depends. LT Hub™ AgentGuard proposes tracking dependencies, checking component provenance and integrity, reviewing vulnerabilities and updates, and documenting supplier and licence risks. These controls must be implemented and validated before any effectiveness claim is made.

Next action: Review the proposed controls, preserve the evidence labels, and commit this record to the root-level "EVIDENCE-REGISTER.md".

## 20. Source Record — OWASP LLM04:2025 Data and Model Poisoning

Record ID: E015
Research Series: LT Hub™ AgentGuard AI Agent Security Risk Research Series
Research Date: 2026-10-25
Evidence Status: Official source reviewed; proposed controls not yet tested
Primary Source: OWASP GenAI Security Project
Source URL: https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/

20.1 Research Question

How can manipulated datasets, compromised model artefacts, or hidden backdoors undermine the reliability and security of AI agents?

20.2 Source Findings

[V] Verified — Source description

OWASP describes data poisoning as the manipulation of pre-training, fine-tuning, or embedding data to introduce vulnerabilities, backdoors, or biases. Possible consequences include degraded performance, harmful or biased outputs, and exploitation of downstream systems.

The source distinguishes several potential exposure points across the model lifecycle, including training datasets, fine-tuning datasets, embedding data, and external data sources.

[V] Verified — Source-described risks and examples

The source identifies risks including:

- Unverified or malicious training data influencing model outputs.
- Biased, toxic, misleading, or inaccurate data.
- Manipulation of data used during model development.
- Backdoors that activate only when a particular trigger is encountered.
- Potentially malicious model files that may execute code when loaded through unsafe serialization mechanisms.
- Inadequate restrictions on which data sources a system can access.

[V] Verified — Source mitigation guidance

OWASP recommends measures that include tracking data origins and transformations, vetting data suppliers, validating outputs against trusted sources, sandboxing exposure to unverified data, using data version control, applying infrastructure access restrictions, testing robustness, and monitoring for anomalous training loss or model behaviour.

These are source recommendations, not evidence that LT Hub™ has implemented or validated these protections.

20.3 Security Implications

[I] Inferred

An AI agent may produce unsafe or unreliable decisions even when its permission controls appear appropriate if the underlying model or data has been compromised.

Agent security should therefore consider both what an agent is allowed to do and the integrity of the model and information influencing its decisions.

A normal successful response does not, by itself, establish that a model is free from hidden backdoors.

20.4 Proposed AgentGuard Controls

The following controls are [H] Hypotheses pending implementation and testing.

- AG-C030 — Data Provenance: Record the origin, version, collection date, and transformations of datasets used in research or model-development workflows.
- AG-C031 — Dataset Change Tracking: Maintain versioned records and compare dataset changes before accepting an updated version.
- AG-C032 — Untrusted Data Isolation: Define boundaries for processing unverified external data without granting it unrestricted access to sensitive systems.
- AG-C033 — Model Integrity Review: Document model origin, version, available integrity information, and review status before use.
- AG-C034 — Poisoning-Robustness Evaluation: Establish a controlled evaluation process using benign synthetic examples and documented expected behaviour.
- AG-C035 — Behaviour Anomaly Monitoring: Record unexpected changes in output quality or behaviour and define a review process before approving model updates.

20.5 Proposed Validation Plan

Test status: NOT RUN

Use a controlled environment, harmless synthetic data, and a mock application. Do not deliberately poison a production model or introduce malicious model files.

1. Create a small synthetic dataset with documented expected labels and provenance.
2. Produce a modified copy containing a known, harmless label inconsistency.
3. Run the proposed dataset comparison and validation procedure.
4. Record whether the discrepancy is detected and what action the procedure recommends.
5. Compare outputs from a mock application using the baseline and modified datasets, without treating this limited demonstration as proof of general poisoning resistance.
6. Record test conditions, expected and observed results, limitations, and corrective actions.

This test can evaluate the proposed dataset-review process. It cannot prove that a real AI model has no backdoors or is resistant to all poisoning attacks.

20.6 Evidence and Limitations

- [V] The OWASP source supports the recorded descriptions of poisoning risks and mitigation recommendations.
- [I] The consequences for a particular agent depend on its model, data pipeline, architecture, and deployment environment.
- [H] AG-C030–AG-C035 are proposed controls and have not been demonstrated effective.
- No production model has been tested as part of this record.
- No claim of complete poisoning prevention or model integrity is made.

20.7 Research Conclusion

Data and model integrity are important parts of AI agent security. LT Hub™ AgentGuard proposes tracking dataset provenance, controlling untrusted data, reviewing model integrity, and testing for unexpected behaviour using safe, controlled procedures. These controls remain hypotheses until implemented and evaluated.

Next action: Append this record after E014 in the root-level "EVIDENCE-REGISTER.md", preserve the evidence labels, and commit the change.

## 21. Source Record — System Prompt Leakage

Record ID: E016
Research Series: LT Hub™ AgentGuard AI Agent Security Risk Research Series
Research Date: 2026-10-25
Evidence Status: Source identification requires confirmation; proposed controls not tested
Primary Source: OWASP GenAI Security Project
Source URL: https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/

21.1 Research Question

Can an AI application disclose internal instructions, configuration details, or sensitive information through model responses, and what protections reduce the resulting risk?

21.2 Source Findings

[V] Verified — Pending exact source confirmation

Record the page's exact title, risk identifier, and relevant mitigation language here after checking the source itself. Do not classify the claims below as independently verified until the page's content has been confirmed.

[I] Inferred — General security implication

System prompts may contain internal instructions or implementation details. A model may reveal some of this text when responding to user requests. However, a system prompt should not be treated as a secure storage location for passwords, API keys, or other secrets.

Disclosure of a prompt does not automatically mean an application has exposed protected data. The impact depends on what the prompt contains and what security boundaries the application enforces elsewhere.

21.3 Proposed AgentGuard Controls

All controls below are [H] Hypotheses until implemented and tested.

- AG-C036 — Secret Exclusion: Do not place credentials, private keys, or other actual secrets in system prompts.
- AG-C037 — External Authorization: Enforce sensitive data access through application-level authorization rather than relying on instructions telling the model not to disclose information.
- AG-C038 — Disclosure Testing: Use harmless synthetic prompts and canary strings to test whether internal test instructions are returned in responses.
- AG-C039 — Sensitive Output Review: Define checks for accidental disclosure of sensitive configuration or internal information.
- AG-C040 — Least Privilege: Restrict the tools and data available to an agent to those required for its task.
- AG-C041 — Incident Logging: Where appropriate and privacy-safe, record test outcomes and suspected disclosure events without logging actual secrets.

21.4 Proposed Validation Plan

Test status: NOT RUN

1. Create a mock application containing a harmless synthetic instruction, such as "TEST-ONLY-CANARY-741".
2. Send a documented set of benign and adversarial test requests to the mock application.
3. Record whether the canary string appears in any output.
4. Check whether the application independently restricts access to a mock protected resource.
5. Record expected results, observed results, test limitations, and corrective actions.

Do not use real credentials, private personal information, or production secrets in these tests. A test that does not reveal the canary string is not proof that all prompt-leakage attacks are prevented.

21.5 Evidence and Limitations

- [V] Exact OWASP source findings remain pending confirmation against the page content.
- [I] Potential impact depends on the information disclosed and the application's access-control design.
- [H] AG-C036–AG-C041 are proposed controls, not confirmed implementations.
- No test has been performed, and no claim of complete prevention is made.

21.6 Research Conclusion

Prompt confidentiality is not a substitute for security boundaries. LT Hub™ AgentGuard proposes excluding real secrets from prompts, enforcing authorization outside the model, limiting agent privileges, and evaluating disclosure with synthetic test data. The source-specific claims must be confirmed before this record is considered fully verified.

Next action: Confirm the source's exact title and content, complete the evidence section, then append this record after E015 in the root-level "EVIDENCE-REGISTER.md".

## 22. Source Record — OWASP LLM08:2025 Vector and Embedding Weaknesses

Record ID: E017
Research Series: LT Hub™ AgentGuard AI Agent Security Risk Research Series
Research Date: 2026-10-25
Evidence Status: Official source reviewed; proposed controls not yet tested
Primary Source: OWASP GenAI Security Project
Source Title: LLM08:2025 Vector and Embedding Weaknesses
Source URL: https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/

22.1 Research Question

Can weaknesses in vector databases, embeddings, or retrieval-augmented generation (RAG) systems expose unauthorised information, introduce manipulated content, or cause an AI application to return misleading results?

22.2 Source Findings

[V] Verified — Source description

OWASP identifies security risks associated with how vectors and embeddings are generated, stored, and retrieved in systems using RAG. Exploitation of these weaknesses can potentially inject harmful content, manipulate model outputs, or expose sensitive information.

[V] Verified — Risks described by OWASP

The source identifies these risk areas:

- Unauthorised access and data leakage: Inadequate access controls may allow sensitive information to be retrieved by users or applications without permission.
- Cross-context information leakage: Shared vector databases may expose information between user groups or applications when separation is inadequate.
- Embedding inversion: An attacker may attempt to recover source information from embeddings.
- Data poisoning: Malicious or unverified information entering a knowledge base may manipulate retrieval and subsequent model responses.
- Behaviour alteration: Retrieval augmentation may change aspects of a model's responses, including qualities such as empathy.

[V] Verified — Mitigation guidance described by OWASP

The source recommends:

- Fine-grained, permission-aware access controls and logical separation of datasets.
- Validation of knowledge sources and checks for integrity or poisoning.
- Classification and tagging of information according to access requirements.
- Detailed, tamper-resistant or immutable retrieval logs to support monitoring and investigation.
- Validation of documents before they enter a RAG knowledge base.
- Evaluation of how retrieval augmentation affects the model's behaviour.

These are recommendations from the source, not proof that LT Hub™ has implemented them or that they are effective in a particular system.

22.3 Security Implications

[I] Inferred

An AI agent may enforce restrictions on its tools while still receiving information that it should not have retrieved. Security therefore depends on the retrieval layer's access controls as well as the agent's own permissions.

In multi-user systems, filtering search results only after sensitive records have already entered the model's context may be insufficient. Access restrictions should be enforced at the data retrieval boundary.

A vector database containing no obvious plain-text passwords should not automatically be considered safe: embeddings may still reveal information about their source data.

22.4 Proposed AgentGuard Controls

All controls below are [H] Hypotheses until implemented and tested.

- AG-C042 — Permission-Aware Retrieval: Require each retrieval request to enforce the requesting user's or agent's authorised access scope.
- AG-C043 — Dataset Separation: Define and test logical separation between datasets belonging to different users, organisations, or sensitivity classes.
- AG-C044 — Knowledge-Source Validation: Validate provenance, document content, and integrity before accepting information into a retrieval index.
- AG-C045 — Retrieval Audit Trail: Record retrieval decisions, access outcomes, and relevant identifiers while minimising sensitive information in logs.
- AG-C046 — Embedding Privacy Review: Assess whether the chosen embedding and storage design creates unacceptable exposure of source information.
- AG-C047 — Retrieval Behaviour Evaluation: Test whether adding or updating retrieved documents changes answers in unexpected or unsafe ways.

22.5 Proposed Validation Plan

Test status: NOT RUN

Use a small mock retrieval application with synthetic records. Do not use real personal, confidential, or commercially sensitive information.

1. Create two mock users, User A and User B, with separate access permissions.
2. Add harmless synthetic documents assigned to each user.
3. Run retrieval queries as both users and record which documents are returned.
4. Include a query designed to match a document that belongs exclusively to the other user.
5. Check whether the retrieval layer blocks unauthorised results before they are supplied to the model.
6. Record expected results, observed results, test conditions, limitations, and corrective actions.

Pass criterion for this specific test: No document outside the requesting user's authorised scope is returned to the model context.

A passing test only supports the tested configuration and scenarios. It does not establish that every access-control bypass, embedding inversion attack, or poisoning technique has been prevented.

22.6 Evidence and Limitations

- [V] The official OWASP source supports the recorded risk descriptions and mitigation recommendations.
- [I] The impact on a specific AI agent depends on its retrieval architecture, permissions, data sensitivity, and deployment environment.
- [H] AG-C042–AG-C047 are proposed controls; their effectiveness has not been demonstrated.
- Test status: NOT RUN.
- No production security audit or independent validation is claimed.

22.7 Research Conclusion

Vector and embedding security is an important part of protecting AI applications that retrieve external knowledge. LT Hub™ AgentGuard proposes permission-aware retrieval, dataset separation, knowledge-source validation, privacy review, and retrieval monitoring. These controls must be implemented and tested before their effectiveness can be claimed.

Next action: Append this record after E016 in the root-level "EVIDENCE-REGISTER.md", preserve the evidence labels, and commit the update.

## 23. Source Record — OWASP LLM09:2025 Misinformation

Record ID: E018
Research Series: LT Hub™ AgentGuard AI Agent Security Risk Research Series
Research Date: 2026-10-25
Evidence Status: Source identified; proposed controls not yet tested
Primary Source: OWASP GenAI Security Project
Source Title: LLM09:2025 Misinformation
Source URL: https://genai.owasp.org/llmrisk/llm092025-misinformation/

23.1 Research Question

How can an AI application produce unsupported, inaccurate, or misleading information, and how can an AI agent reduce the risk of people or downstream systems relying on those outputs?

23.2 Source Findings

[V] Verified — Source identification

The source selected for this record is the OWASP GenAI Security Project page titled LLM09:2025 Misinformation.

[V] Source-content verification required

Before marking individual mitigation statements as verified, check their exact wording against the opened page. The source topic alone does not independently verify every example or recommendation listed in this record.

Relevant points to check on the source page include:

- Hallucinations and confidently stated incorrect information.
- Bias, incomplete context, or misleading generated content.
- Risks when users rely on AI output without independent verification.
- Recommendations for human oversight, cross-checking, and validation of critical outputs.

Record only claims that the source actually supports.

23.3 Security Implications

[I] Inferred

An AI agent can produce a technically well-formatted response that is nevertheless factually wrong. If that response triggers an external action, informs a business decision, or is published without review, the consequences may extend beyond the conversation itself.

A confident tone, fluent writing, or citation-like formatting is not proof that a claim is true.

For LT Hub™ AgentGuard, factual reliability should be treated separately from permission control: an agent may be authorised to perform an action but still base that action on inaccurate information.

23.4 Proposed AgentGuard Controls

All controls below are [H] Hypotheses until implemented and tested.

- AG-C048 — Claim-to-Source Traceability: Record the source supporting each material factual claim in a research report.
- AG-C049 — Evidence Classification: Separate verified claims, inferences, and hypotheses using the LT Hub™ [V]/[I]/[H] framework.
- AG-C050 — Independent Cross-Checking: Require additional source checks for high-impact or disputed claims.
- AG-C051 — Human Review Gate: Require human approval before publishing or acting on high-impact, unverified outputs.
- AG-C052 — Uncertainty Disclosure: Clearly identify missing evidence, unresolved contradictions, and limitations.
- AG-C053 — Output Validation: Define checks for source relevance, claim accuracy, date sensitivity, and unsupported conclusions before a report is approved.

23.5 Proposed Validation Plan

Test status: NOT RUN

Use a small, controlled set of synthetic research statements and public, non-sensitive reference material.

1. Create a test set containing supported claims, unsupported claims, and claims that cannot be resolved from the available evidence.
2. Require the proposed review process to assign an evidence status to each claim.
3. Check whether supported claims have relevant source references.
4. Check whether unsupported claims are flagged instead of being presented as verified.
5. Check whether uncertain claims are labelled as unresolved rather than silently treated as facts.
6. Record expected results, observed results, false positives, missed errors, and limitations.

Proposed pass criterion: The review process flags every deliberately unsupported test claim and does not label it verified without supporting evidence.

This test evaluates only the defined sample and review procedure. It cannot prove that a model will never generate misinformation or that all source references are accurate.

23.6 Evidence and Limitations

- [V] The page identity is recorded; detailed source-specific claims must be checked against its content.
- [I] The consequences of misinformation depend on the application's use, the audience, and whether outputs trigger decisions or actions.
- [H] AG-C048–AG-C053 are proposed controls, not confirmed implementations.
- Test status: NOT RUN.
- No claim of complete factual accuracy or misinformation prevention is made.

23.7 Research Conclusion

AI agent reliability requires more than fluent responses. LT Hub™ AgentGuard proposes traceable sources, explicit evidence labels, independent checks, human review for high-impact outputs, and uncertainty disclosure. These controls remain hypotheses until implemented and evaluated.

Next action: Verify the relevant source passages, append this record after E017 in the root-level "EVIDENCE-REGISTER.md", and commit the update.

## 24. Source Record — OWASP LLM10:2025 Unbounded Consumption

Record ID: E019
Research Series: LT Hub™ AgentGuard AI Agent Security Risk Research Series
Research Date: 2026-10-25
Evidence Status: Source identified; proposed controls not yet tested
Primary Source: OWASP GenAI Security Project
Source Title: LLM10:2025 Unbounded Consumption
Source URL: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/

24.1 Research Question

How can an AI application or agent consume excessive resources, exhaust usage limits, increase operational costs, or degrade service availability, and what controls can reduce these risks?

## 24.2 Source Findings

[V] Verified against the reviewed OWASP LLM10:2025 source passage

The OWASP GenAI Security Project page identifies unbounded consumption as a risk associated with excessive and uncontrolled model inference. Described consequences include denial of service, economic losses, model theft, and service degradation.

The reviewed prevention and mitigation section lists 15 strategies:

1. Input validation and reasonable input-size limits.
2. Limiting exposure of logits and log probabilities.
3. Rate limiting and user quotas.
4. Dynamic resource-allocation management.
5. Timeouts and throttling for resource-intensive operations.
6. Sandboxing and restrictions on access to network resources, internal services, and APIs.
7. Logging, monitoring, and anomaly detection for unusual resource consumption.
8. Watermarking to help identify unauthorised use of model outputs.
9. Graceful degradation under heavy load.
10. Limits on queued actions and total actions, with dynamic scaling and load balancing.
11. Adversarial robustness training.
12. Filtering known glitch tokens before they enter the model's context.
13. Access controls, including role-based access control (RBAC) and least privilege.
14. A centralised inventory or registry for production ML models.
15. Automated MLOps deployment with governance, tracking, and approval workflows.

[I] Inferred

For an AI agent, request limits, quotas, resource monitoring, timeouts, sandboxing, and restrictions on queued actions may help reduce resource-exhaustion risks. The effectiveness of each measure depends on the system architecture and implementation.

[H] Hypothesis — Proposed control effectiveness

AG-C054–AG-C060 are proposed controls. Their implementation and effectiveness have not yet been demonstrated by this research series. The hypothesis that these controls will reduce relevant resource-exhaustion risks remains untested until supported by documented validation.

Evidence limitation

Verification of the OWASP source passage establishes that the cited recommendations appear in the reviewed source. It does not establish that every recommendation has been independently evaluated or that any proposed control has been implemented, tested, or shown effective in LT Hub™ AgentGuard. No claim of complete prevention is made.

24.3 Security Implications

[I] Inferred

An AI agent that repeatedly calls a model, retries failed operations, processes oversized inputs, or launches multiple downstream tasks may consume resources beyond the intended budget.

The risk can be amplified when an agent has permission to invoke tools repeatedly without clear stopping conditions.

Resource limits should therefore apply to the overall workflow, not only to an individual model request. Cost, request frequency, processing time, and downstream action counts may all require independent controls.

24.4 Proposed AgentGuard Controls

All controls below are [H] Hypotheses until implemented and tested.

- AG-C054 — Request Rate Limits: Validation Plan
Status: Proposed; not yet tested.
Risk addressed: Excessive request frequency leading to resource exhaustion, service degradation, or unexpected consumption.
Test method: In an authorised test environment, configure a known request-rate threshold. Send requests below, at, and above the threshold, including a controlled concurrent-request scenario.
Expected result: Requests within the permitted rate are handled according to policy. Excess requests are limited according to the configured enforcement behaviour. Relevant outcomes are logged, and normal operation resumes according to the documented recovery policy.
Evidence to retain: Configuration and threshold; test timestamp; request counts and rates; observed responses; enforcement logs; any errors or bypasses; and the final test result.
Pass criteria: All predefined scenarios satisfy the expected behaviour, with no unexplained enforcement failures. Any failed scenario must be recorded and investigated.
Limitations: No implementation or test result is claimed until the test has actually been performed and its evidence reviewed.

- AG-C055 — Usage and Cost Budgets: Validation Plan

Status: Proposed; not yet tested.

Risk addressed: Excessive model usage, unexpected expenditure, and resource consumption exceeding authorised limits.

Test method: In an authorised test environment, configure a usage ceiling and budget alert where supported. Simulate usage below, near, and above the threshold. Test alert delivery separately from any enforced usage restriction. Use a simulated budget or provider-supported test mechanism where possible; do not incur unnecessary real charges.

Expected result: Usage is measured against the configured threshold. Alerts are triggered according to the documented policy. Where an enforceable usage restriction exists, further usage is restricted as specified. Any unsupported provider capability or enforcement gap is documented.

Evidence to retain: Configuration; threshold and measurement units; test timestamps; usage records; alert delivery results; observed enforcement behaviour; provider limitations; and any discrepancy between estimated and reported usage.

Pass criteria: Each configured alert and restriction behaves according to its documented acceptance criteria. Alerts must not be recorded as proof of spending enforcement. Any failed scenario or unverified capability remains explicitly documented.

Limitations: No implementation, provider capability, cost saving, or successful enforcement is claimed until supported by recorded evidence.

- AG-C056 — Input and Output Limits: Validation Plan

Status: Proposed; not yet tested.

Risk addressed: Excessive input sizes, uncontrolled output generation, and processing workloads that may cause resource exhaustion, service degradation, or unexpected usage.

Test method: In an authorised test environment, configure documented input-size, output-size, and processing-workload limits appropriate to the system. Test requests below, at, and above each applicable limit. Include oversized inputs, requests for excessive output, and workloads that exceed configured processing constraints. Use bounded test data and avoid unnecessary provider charges.

Expected result: Requests within configured limits are handled according to policy. Requests exceeding a limit are rejected, truncated, constrained, or otherwise handled according to the documented enforcement behaviour. Processing limits are applied where supported, and relevant outcomes are recorded.

Evidence to retain: Configuration and limit values; measurement units; test inputs; timestamps; observed responses; usage or processing records; enforcement logs; errors; and any unsupported capabilities or bypasses.

Pass criteria: Each tested limit behaves according to its predefined acceptance criteria. Oversized requests and excessive outputs cannot exceed the intended enforced bounds without detection. Any failed scenario or untested limit remains explicitly documented.

Limitations: Input and output limits alone do not establish protection against all forms of resource exhaustion. Tokenization overhead, concurrent requests, retries, provider-side processing, and other workload factors may require separate controls. No implementation or successful test is claimed until supported by recorded evidence.

- AG-C057 — Execution Timeouts: Validation Plan

Status: Proposed; not yet tested.

Risk addressed: Excessive resource consumption caused by stalled, slow, or long-running model calls and agent workflows.

Test method: In an authorised test environment, configure documented execution timeouts for applicable model calls and workflows. Test operations that complete within the permitted duration, operations that approach the timeout, and controlled operations that exceed it. Where supported, examine cancellation propagation, cleanup, and behaviour of dependent tasks after termination. Avoid unnecessary provider charges or disruptive workloads.

Expected result: Operations that complete within the permitted duration finish normally. Operations that exceed the configured timeout are terminated or cancelled according to the documented policy. Relevant resources are released where supported, and dependent tasks do not continue unintended work after termination. Timeout events and resulting errors are recorded.

Evidence to retain: Timeout configuration and units; test timestamps; operation duration; observed completion or termination behaviour; cancellation and cleanup logs; downstream task status; resource-use records where available; and any errors or unsupported capabilities.

Pass criteria: Each test scenario behaves according to predefined acceptance criteria. An expired timeout does not merely report an error while the underlying operation continues consuming resources unnoticed. Any cancellation failure, incomplete cleanup, or continuing downstream activity is documented as a finding.

Limitations: A timeout does not automatically stop work already accepted by an external provider or guarantee cancellation of every downstream operation. Cancellation behaviour and residual resource consumption must be assessed separately. No implementation or successful test is claimed until supported by recorded evidence.

- AG-C058 — Agent Loop Protection: Validation Plan

Status: Proposed; not yet tested.

Risk addressed: Unbounded agent iterations, repeated retries, recursive workflow execution, and excessive resource consumption caused by workflows that fail to make progress or terminate correctly.

Test method: In an authorised test environment, configure a maximum iteration count, retry limit, and explicit workflow termination conditions. Test a workflow that completes normally, a controlled repeated-action scenario, repeated transient failures, and a scenario that reaches the configured limit. Where applicable, examine recursive calls, delegated workflows, and concurrent execution.

Expected result: Normal workflows complete within their permitted limits. Repeated actions and retries do not exceed the configured bounds. When a limit or termination condition is reached, the workflow stops or enters its documented recovery process. Relevant events and reasons for termination are recorded.

Evidence to retain: Configuration and limit values; workflow identifiers; iteration and retry counts; test timestamps; model and tool-call records where available; termination reasons; resource-usage observations; and any errors, bypasses, or incomplete cancellations.

Pass criteria: Each predefined scenario behaves according to its acceptance criteria. Iteration and retry counts remain within their enforced limits, and workflows terminate as specified when a limit is reached. Any unbounded recursion, duplicate downstream action, limit bypass, or unexplained continuation is recorded as a finding.

Limitations: Iteration and retry limits do not independently prevent every form of excessive consumption. Parallel workflows, delegated agents, nested calls, and downstream operations may require additional controls and aggregate limits. No implementation or successful test is claimed until supported by recorded evidence.

- AG-C059 — Resource Monitoring: Record resource consumption and flag unusual increases for review.
- AG-C060 — Downstream Action Limits: Restrict the number and frequency of tool calls, queued jobs, or external operations within a workflow.

Control enforcement and validation requirements

Each proposed control must specify its enforcement mechanism, applicable scope, configured threshold or decision rule, behaviour when the limit is reached, and evidence required to verify operation. Where applicable, enforcement should remain effective across retries, parallel execution, and delegated workflows.

Implementation status and test status must be recorded separately. A configured control is not considered validated until its behaviour has been tested against defined acceptance criteria and the results have been retained. Failed tests, bypasses, unsupported provider capabilities, and residual risks must be documented. No control is assumed to provide complete prevention.

24.5 Proposed Validation Plan

Test status: NOT RUN

Use a local mock application or another controlled test environment with synthetic requests. Do not deliberately overload production services or generate unexpected charges.

1. Configure a small test request limit and a fixed maximum number of workflow iterations.
2. Submit harmless synthetic requests below and above the configured threshold.
3. Simulate a repeated-task loop in the mock application.
4. Check whether the request limit and iteration cap stop further work at the intended boundary.
5. Simulate a timeout and verify that the workflow stops or enters a documented recovery state.
6. Record expected results, observed results, resource use, errors, and limitations.

Proposed pass criterion: The mock application stops processing when its configured limits are reached and records the limit event.

A passing mock test does not prove that an external AI provider, distributed application, or production agent is protected against every resource-exhaustion attack.

24.6 Evidence and Limitations

- [V] The source identity is recorded; detailed source-specific claims require checking against the page content.
- [I] Actual impact depends on provider pricing, application architecture, workload, permissions, and configured limits.
- [H] AG-C054–AG-C060 are proposed controls, not confirmed implementations.
- Test status: NOT RUN.
- No production performance test, cost guarantee, or complete denial-of-service prevention claim is made.

24.7 Research Conclusion

Unbounded consumption is an AI security and operational risk. LT Hub™ AgentGuard proposes request limits, budgets, workload restrictions, timeouts, loop protection, resource monitoring, and downstream action limits. Their effectiveness must be demonstrated through controlled tests before any success claim is made.

Next action: Verify the relevant passages on the official source page, append this record after E018 in the root-level "EVIDENCE-REGISTER.md", and commit the update.
