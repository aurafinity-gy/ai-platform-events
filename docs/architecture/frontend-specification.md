# Frontend specification

Adopt App Starter UI/BFF once accepted; no frontend framework files are introduced here.

Primary routes: events list, new series, occurrence detail/RSVP/cost, team proposal comparison and participant profile. Mobile participant flow is invitation to RSVP to roster/cost status. Organizer flow is create series, freeze roster, request deterministic proposals, compare, approve/publish and record completion/manual receipts.

Every route needs loading, empty, filtered-empty, denied, expired-session, validation, stale/conflict, failure and success states. Team comparison shows feasibility, balance delta, repeated-pair metric and warnings without exposing private skill observations. Keyboard navigation, reduced motion and WCAG 2.2 AA are acceptance targets. Authorization remains server authoritative.
