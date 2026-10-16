# Foundation AI advisory integration

Foundation supports release-pinned agent definitions and bounded read-only tool execution; live calls/activation and write or approval-required tools remain separately gated. Events therefore treats AI only as an optional advisor.

Flow: authorized organizer freezes a roster revision; Events runs deterministic optimization and stores top-K proposals with input hash, solver version and score evidence; a future narrow Events read tool exposes only an authorized minimized proposal snapshot; a pinned Foundation agent may compare proposals and return strict structured advisory output; Events validates it as untrusted; organizer approves; Events rechecks permission, current roster revision and hard constraints before immutable publication.

No-model fallback is the deterministic proposal list. Model output cannot update skill observations, RSVP, costs, payments or publication. Before integration, pin actual Foundation public contract/release versions, review tool permissions/audit/idempotency, add cross-tenant/injection/tool-denial/timeout/model-off evaluations, prove stale-revision authorization, and separately authorize deployment/model egress.
