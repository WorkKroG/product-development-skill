# E12 attempt 01 — independent Change Review B

## Verdict

**CHANGES_REQUIRED**

Reviewed B commit/tree: `896bb88d845ee79d4434e5e48e19638d4db6a042` / `50ba96b2e991fc18a0bd36d196b662f507e96e82`.

Candidate basis: the complete A..B diff embedded in the frozen request, independently verified as SHA-256 `05fdfcce490c76731b9773a0278a24a987f0c77bdd8f39e3c457f0c8040c23cd` and `7786` bytes. The frozen request identifies its range as A `723366bbbcb86f94a7f5999c1fd9080e5f668090` / tree `79532523f890388ee04c782dc4750567c1e0d947` through the reviewed B identity above.

## Requirements verdict

- **PASS** — creating a contact writes its identifier and name, and reconstruction reads them back.
- **PASS** — scheduling checks membership before copying or writing, so an unknown contact raises without mutating the store.
- **PASS** — a scheduled follow-up persists `id`, `contact_id`, `due_on`, and an empty `outcome`.
- **CHANGES_REQUIRED** — due selection does not implement date ordering for all accepted inputs; it compares unchecked strings.
- **PASS** — for a valid store, returned due records contain exactly the five requested string fields.
- **CHANGES_REQUIRED** — identifiers are not kept distinct across the contact and follow-up types, and the corresponding test never checks cross-type distinctness.
- **PASS** — malformed JSON/UTF-8 and structurally invalid stores are rejected before any write.
- **PASS** — the implementation remains limited to creation, scheduling, reconstruction, and due retrieval; outcome recording and completed-item filtering were not added.

## Findings

### F1 — Due ordering is lexical rather than date-based (requirements/correctness, high)

`quietfollow.py:24` accepts any string as `due_on`, and `quietfollow.py:42-49` accepts any string as `as_of` and selects records with `follow_up["due_on"] <= as_of`. Lexical ordering is not date ordering unless both inputs are first constrained to the same sortable representation. For example, the accepted value `2026-9-30` is chronologically before `2026-10-01` but compares greater as a string, so it is incorrectly omitted. `test_quietfollow.py:73-96` exercises only zero-padded ISO-shaped values and cannot expose this behavior.

Require either parsing and comparing actual dates, or validation/canonicalization of both scheduled and query dates before comparison. Add tests for non-canonical and invalid date strings, with an explicit rejection or normalization contract.

### F2 — Cross-type identifier distinctness is neither enforced nor tested (requirements/test adequacy, medium)

`quietfollow.py:17` and `quietfollow.py:28` draw both identifiers independently from the same unqualified generator and perform no cross-type collision check. A repeated generator value therefore permits a contact ID and follow-up ID to be equal, contrary to the stated requirement that contact and follow-up identifiers remain distinct. The specifically named test at `test_quietfollow.py:47-55` compares two contact IDs to one another and two follow-up IDs to one another, but never compares a contact ID with a follow-up ID; it would pass while the requirement is violated.

Use disjoint identifier namespaces (for example type prefixes) or enforce cross-type non-collision, and add a direct contact-versus-follow-up assertion. A deterministic generator stub should cover collision behavior without relying on probabilistic UUID output.

## Limitations

- This was a static review of the request's embedded complete diff. The named commit objects were not present in the outer repository object database, so their commit-to-tree mapping could not be independently queried there; the exact candidate diff itself was independently verified against the frozen SHA-256 and byte count.
- Tests were not executed because the allowed-effects contract permits writing only this review artifact, while executing this candidate in the available workspace would require materializing or importing code and could create additional files. The test assessment is therefore source-based.
- Failure atomicity of direct `Path.write_text` persistence was not established by the supplied tests. No atomic-write requirement is stated, so this remains a safety limitation rather than an additional blocking finding.

## Chronological operation log

1. Verified the frozen request SHA-256 as `9fc96b0387c446d1e6e91a4e5c1cc71a92d6a667aaed71121adf746d2e220888` before reading it.
2. Read the frozen request and its complete embedded A..B diff.
3. Queried the outer repository for the named A and B objects; neither object was available there, and no repository state was changed.
4. Extracted the embedded diff as a byte stream and verified SHA-256 `05fdfcce490c76731b9773a0278a24a987f0c77bdd8f39e3c457f0c8040c23cd` and byte count `7786`.
5. Reviewed requirements compliance, correctness, safety, unnecessary complexity, and test adequacy from the exact embedded candidate.
6. Wrote this review artifact only; no product file, repository ref, request, skill, index, Git state, or external service was modified.
