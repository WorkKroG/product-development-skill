# Part 5 — coordination, scaling, and stress probes

The remaining cases exercised plan review, decision reuse, durable task routing, permission denial,
model constraints, WIP preservation, architecture reconsideration, and a bounded cross-module
decision. E10 used four distinct tracked stages: architecture analysis, independent review, one
synthetic owner decision, and revised affected/unaffected routing. No real native message or external
action was sent.

Current case results are all PASS: E08, E10, E11, E17, E20, E21, E22, E25, and E33. Their exact
request, response, evaluation, evaluator-prefix, and support hashes are recorded in the run index and
the compact execution record.

Stress probes SU02–SU06 are also current PASS:

- SU02 stopped an automatic third cycle after two fruitless rounds.
- SU03 preserved valid bytes, rejected reconstruction, and reran only missing evidence.
- SU04 separated a required guarantee from a reviewer's broader preferred mechanism.
- SU05 attempt 2 retained non-negotiable sensitive-data protection while allowing bounded synthetic work.
- SU06 permitted a bounded checker trial after measured repetition and risk justified it.

Together with SU01, the six probes cover the Product proportionality rules. The complete matrix is
21 E-cases plus six probes, all current PASS. Requested model assignments do not prove accepted or
runtime identities; unavailable provenance facts remain Unknown. No post-pilot candidate change was
made, so no impact analysis or carried-forward credit was needed.
