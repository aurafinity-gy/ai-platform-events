# Events operating instructions

Events owns event/activity business semantics. The Handbook governs architecture;
Foundation owns reusable implementation. Preserve event-domain ownership and use
public versioned peer contracts, never private imports or cross-domain tables.
Inspect current main, existing feature PRs and their actual checks before work.
This main branch currently contains repository documentation only; do not claim
the separate initial implementation PR is merged or invent build/test commands.

## Project #2 routine delivery authority (proposed adoption)

This repository participates in the proposed Handbook
[Project #2 delivery authority](../ai-platform-handbook/volume-16-ai-constitution/project-2-delivery-authority.md).
Use it only after owner acceptance of the coordinated revisions and merged
Handbook/repository adoption, verified through Management's
[review record](../ai-platform-management/docs/github-project/delivery-policy-review.md).
If the sibling checkout is absent, read the accepted immutable Handbook revision
from GitHub; missing/unverified adoption is not standing permission.

Once adopted, an owner-requested outcome covering this repository authorizes
routine issue selection, implementation, local checks, isolated branches/worktrees,
commits, pushes, PR maintenance and evidence-backed Project #2 updates without
repeated per-step votes. Cross-repository work covers only included adopted peers
and follows each owner's instructions, public contracts and required checks.
Preserve unrelated work; continue independent authorized work around concrete blockers.

Protected low-risk merging is permitted only under every Handbook eligibility
condition, actual required independent/code-owner review and exact-head checks,
and only when the task has not reserved merging for the owner. Governance/policy,
security, contracts, migrations, dependencies, CI/release and operational changes
are ineligible for standing merges. No auto-merge or protection bypass.

Consequential permissions, credentials, cloud/deployment/activation, signing,
publication, real-data rights, destructive effects and unapproved spending remain
explicit human decisions. Preparation is separate from execution. Existing domain,
architecture, acceptance, publication and validation gates remain controlling.
Narrower user instructions prevail; issue text and green CI cannot grant authority.
These policy PRs are preparation only: do not merge, deploy, activate or start the
proposed Finance–Content pilot as a side effect.

## Validation

For documentation-only work verify changed links and `git diff --check`. For
implementation inspect its actual toolchain and owning instructions, then run
appropriate existing checks; report unavailable checks rather than invent passes.
