# Corrected skill candidate identity

This record freezes the five skill bytes used for the lean QuietFollow behavioral pilot. It is a
candidate identity, not a readiness, installation, integration, or release claim.

## Authority bindings

- Plan: `MODULE6-LEAN-PLAN-v1`, commit `feebad5d67614da5d25439c0ae38c2164becdbf2`,
  tree `db52321f6fe978a03953f0ed6c5c3e2d6bd88370`, SHA-256
  `182e45c458fc631a9b367635c384e3b8c0af409355bd7a75e08fea345e65f1ed`.
- Plan review: `MODULE6-LEAN-PLAN-REVIEW-v6`, SHA-256
  `bcc003193b614c3c74ce6f63edd7f84a66adc826881ff41e14c6e4fe204477e9`, verdict
  `PLAN_PASS`, findings empty.
- Accepted Product decision: commit `4422573db8bbbac644906dda7f2990c64a338fcc`, tree
  `218e89c774dc8c5727f3a4130ed6bb146fce8f8b`, SHA-256
  `44ff96efe60ef9ffefe6b1688f6b800a7bb3d5928d1bb376fabc3a241fa91dc6`.
- Owner acceptance record SHA-256:
  `612e8d8a4a457f142114e057567258d0167c0be3c7eeb99f1cb1ca646d96321d`.

## Corrected five-file bytes

- Identity: `MODULE6-LEAN-SKILL-v1`.
- Skill commit: `0070e4c307e785cfeafae41ee4aa70151de1df7c`.
- Skill tree: `639c579dddec3b4039e347c89952d4f254e628b2`.
- Sole parent: `cc9acaa48c93583ea6944075bbacbe547a4100f3`.
- Fixed-order checksum file: `candidate/skill-after.sha256`.
- Checksum-file SHA-256:
  `c3e8c4dc28d76464118ae7aaa9175980dce7fac40f896e521ee67b1428707fdd`.
- Independent exact-skill review: `candidate/skill-change-review.md`, SHA-256
  `9a48c6891ed00c455a2f9da4d8ce679ffc09de89caf93598ca73292aa9d13cf0`, verdict `PASS`,
  findings Critical `0`, Important `0`, Minor `0`.
- Review-record commit: `f3aa727bac1f05ea1b3794f9f089cf53d0a13d85`.

Every current attempt must bind this skill commit/tree and checksum-file digest. Any change to one
of the five skill bytes invalidates the review and requires a new candidate identity and review.
