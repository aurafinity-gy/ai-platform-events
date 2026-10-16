# Events domain architecture

This is the initial independent domain increment. Events owns event-series intent, business occurrences, participation/RSVP, costs, team proposals and organizer approval semantics. Activity-specific policy is separate; recreational hockey is the first policy.

Foundation owns generic recurrence calculation/durable scheduling, identity/platform controls, orchestration, model/tool governance and platform audit. Events must use public versioned contracts and never Foundation private tables.

Key invariants: recurring intent retains local wall time plus IANA timezone; money is integer minor units plus currency and allocation conserves the total; a full hockey proposal requires exactly 20 skaters plus two goalies with each participant exactly once; persisted proposals must bind a fixed roster revision/input hash; AI is advisory and cannot publish.

The Python package is standard-library-only. RecurringIntent records recurrence but intentionally does not materialize recurrence rules, avoiding duplication of Foundation scheduling-core. The optimizer is deterministic exhaustive search for the bounded 20-skater roster and returns explicit infeasibility instead of silently relaxing hard constraints.

App Starter dependencies: TanStack Start/BFF, FastAPI/OpenAPI, auth/session, PostgreSQL/FORCE RLS skeleton, migrations, architecture checks, Playwright/accessibility and deployment/rollback conventions. These are deferred for adoption from the accepted starter rather than duplicated here.
