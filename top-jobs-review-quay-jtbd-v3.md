# Top-jobs review: Red Hat Quay

**Source:** `QuayDraft_Master_Updated.xlsx` (Main sheet) + PR-corrected state reflected in `quay-jtbd-jobs-tab-v3.csv`
**Note:** Titles and categories reflect merged PRs #1831–#1835. Three job statements (#1, #30, #33) reflect spreadsheet state (not yet updated manually — known pending work).
**Phase:** 0 — Steps 1–2 (jobs, statements, categories only)
**Reviewed:** 2026-10-01 | **Jobs reviewed:** 136 | **Template rows skipped:** 0 | **Absorbed into parent:** 2 (original #67, #103)

---

## Executive summary

| Status | Count | Change from v2 |
|--------|-------|----------------|
| Pass | 130 | +19 |
| Needs revision | 6 | −19 |
| Blocker | 0 | −2 |

### Resolved since v2

All 2 blockers and 19 of 25 needs-revision items are cleared:

- **Blockers resolved:** #30 (category + statement work underway), #33 (category fixed; statement work underway)
- **Title revisions merged:** #63, #68–70, #73, #77, #80, #84, #113 (10 titles, PR #1832)
- **Category moves merged:** #21 → Discover, #30 → Configure, #33 → What's New, #96 → Observe (PRs #1831, #1833)
- **Structural merges merged:** original #67 nested into OAuth tokens job; original #103 GC metrics inlined into Prometheus job (PR #1834)
- **"Understand X" in Discover/Observe:** Reclassified as Pass after OCP precedent review — 7 jobs (#2, #3, #5, #6, #7, #8, #96, #99) no longer flagged

### Remaining systemic issues

1. **Three pending spreadsheet statement rewrites** — #1, #30, #33 still carry stale statements. These are tracked outside the PR workflow and require manual spreadsheet updates.
2. **"Understand X: Subtitle" colon format in Configure** — Jobs #73, #74, #75 use a `Title: Subtitle` structure not found anywhere else in the 136-job set. "Understand" is now accepted per OCP precedent; the colon format is the remaining issue.

---

## Per-job findings

| # | Current title | Status | Outcome | Statement | Title | Category | Notes |
|---|---------------|--------|---------|-----------|-------|----------|-------|
| 1 | Red Hat Quay Release Notes | Needs revision | Pass | **Fail** | Pass | Pass | Statement describes subscribing to notifications, not reading release notes. Spreadsheet update pending. |
| 2 | Understand Red Hat Quay capabilities and architecture | Pass | Pass | Pass | Pass | Pass | "Understand X" in Discover accepted per OCP precedent |
| 3 | Understand Red Hat Quay infrastructure and governance | Pass | Pass | Pass | Pass | Pass | "Understand X" in Discover accepted |
| 4 | Evaluate Quay.io as a hosted registry option | Pass | Pass | Pass | Pass | Pass | — |
| 5 | Understand Red Hat Quay's tenancy model | Pass | Pass | Pass | Pass | Pass | "Understand X" in Discover accepted |
| 6 | Understand the Red Hat Quay permissions model | Pass | Pass | Pass | Pass | Pass | "Understand X" in Discover accepted |
| 7 | Understand Clair vulnerability scanning | Pass | Pass | Pass | Pass | Pass | "Understand X" in Discover accepted |
| 8 | Understand the Quay Bridge Operator | Pass | Pass | Pass | Pass | Pass | "Understand X" in Discover accepted |
| 9 | Get started with Quay.io | Pass | Pass | Pass | Pass | Pass | — |
| 10 | Get started after deploying Quay on OpenShift Container Platform | Pass | Pass | Pass | Pass | Pass | — |
| 11 | Get started after deploying Red Hat Quay on standalone hosts | Pass | Pass | Pass | Pass | Pass | — |
| 12 | Create your first organization | Pass | Pass | Pass | Pass | Pass | — |
| 13 | Create your first repository | Pass | Pass | Pass | Pass | Pass | — |
| 14 | Push and pull your first image | Pass | Pass | Pass | Pass | Pass | — |
| 15 | View your first Clair scan | Pass | Pass | Pass | Pass | Pass | — |
| 16 | Enable and make your first Quay API call | Pass | Pass | Pass | Pass | Pass | — |
| 17 | Plan supporting infrastructure for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 18 | Choose a single registry or multiple registries | Pass | Pass | Pass | Pass | Pass | — |
| 19 | Size and subscribe to Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 20 | Plan a deployment topology | Pass | Pass | Pass | Pass | Pass | — |
| 21 | Choose a Quay.io plan | Pass | Pass | Pass | Pass | Pass | Moved Discover; pricing/discovery intent confirmed |
| 22 | Plan a Red Hat Quay proof of concept deployment | Pass | Pass | Pass | Pass | Pass | — |
| 23 | Plan a Red Hat Quay deployment on OpenShift Container Platform | Pass | Pass | Pass | Pass | Pass | — |
| 24 | Plan a Red Hat Quay high availability deployment | Pass | Pass | Pass | Pass | Pass | — |
| 25 | Plan a Red Hat Quay public cloud deployment | Pass | Pass | Pass | Pass | Pass | — |
| 26 | Plan content distribution and geo-replication | Pass | Pass | Pass | Pass | Pass | — |
| 27 | Plan container image builds with Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 28 | Install Red Hat Quay on OpenShift Container Platform | Pass | Pass | Pass | Pass | Pass | — |
| 29 | Install Red Hat Quay proof of concept | Pass | Pass | Pass | Pass | Pass | — |
| 30 | Configure IPv6 for Quay proof of concept | Needs revision | Pass | **Fail** | Pass | Pass | Statement is verbatim copy of #29. Spreadsheet update pending. Category (Configure) now correct. |
| 31 | Install Red Hat Quay in high availability | Pass | Pass | Pass | Pass | Pass | — |
| 32 | Install Clair for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 33 | Get Red Hat Quay release notifications | Needs revision | Pass | **Fail** | Pass | Pass | Statement still identical to #1. Spreadsheet update pending. Category (What's New) now correct. |
| 34 | Upgrade Red Hat Quay on OpenShift Container Platform | Pass | Pass | Pass | Pass | Pass | — |
| 35 | Upgrade a standalone Red Hat Quay deployment | Pass | Pass | Pass | Pass | Pass | — |
| 36 | Upgrade a geo-replicated Red Hat Quay deployment | Pass | Pass | Pass | Pass | Pass | — |
| 37 | Upgrade the Quay Bridge Operator | Pass | Pass | Pass | Pass | Pass | — |
| 38 | Upgrade the Clair PostgreSQL database | Pass | Pass | Pass | Pass | Pass | — |
| 39 | Downgrade or roll back Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 40 | Migrate a QuayEcosystem deployment to QuayRegistry | Pass | Pass | Pass | Pass | Pass | — |
| 41 | Migrate a standalone Red Hat Quay deployment to the Operator | Pass | Pass | Pass | Pass | Pass | — |
| 42 | Migrate Microsoft Entra ID OIDC from v1.0 to v2.0 | Pass | Pass | Pass | Pass | Pass | — |
| 43 | Manage user accounts in the registry | Pass | Pass | Pass | Pass | Pass | — |
| 44 | Group repositories by team or project | Pass | Pass | Pass | Pass | Pass | — |
| 45 | Manage image repositories | Pass | Pass | Pass | Pass | Pass | — |
| 46 | Manage robot accounts | Pass | Pass | Pass | Pass | Pass | — |
| 47 | Scale access control with teams and roles | Pass | Pass | Pass | Pass | Pass | — |
| 48 | Inspect image tags, labels, and history | Pass | Pass | Pass | Pass | Pass | — |
| 49 | Retire image tags on a schedule | Pass | Pass | Pass | Pass | Pass | — |
| 50 | Protect production tags from overwrite | Pass | Pass | Pass | Pass | Pass | — |
| 51 | Cap storage per organization | Pass | Pass | Pass | Pass | Pass | — |
| 52 | Enforce quota limits when tenants fill capacity | Pass | Pass | Pass | Pass | Pass | — |
| 53 | Enable automatic cleanup of stale tags | Pass | Pass | Pass | Pass | Pass | — |
| 54 | Set auto-prune policies at the right scope | Pass | Pass | Pass | Pass | Pass | — |
| 55 | Reclaim disk space after tags are deleted | Pass | Pass | Pass | Pass | Pass | — |
| 56 | Protect a standalone registry from data loss | Pass | Pass | Pass | Pass | Pass | — |
| 57 | Protect an Operator-managed registry from data loss | Pass | Pass | Pass | Pass | Pass | — |
| 58 | Restore an Operator-managed registry after failure | Pass | Pass | Pass | Pass | Pass | — |
| 59 | Perform health checks on deployments | Pass | Pass | Pass | Pass | Pass | — |
| 60 | Change Operator-managed features after deployment | Pass | Pass | Pass | Pass | Pass | — |
| 61 | Keep geo-replicated sites running correctly | Pass | Pass | Pass | Pass | Pass | — |
| 62 | Manage bootstrap tokens for initial automation setup | Pass | Pass | Pass | Pass | Pass | — |
| 63 | Administer the registry as a superuser | Pass | Pass | Pass | Pass | Pass | Title revised from "Recover and administer the whole registry…" |
| 64 | Get your first API workflow running | Pass | Pass | Pass | Pass | Pass | — |
| 65 | Authenticate applications with OAuth access tokens | Pass | Pass | Pass | Pass | Pass | — |
| 66 | Authenticate CI/CD with robot account tokens | Pass | Pass | Pass | Pass | Pass | — |
| 67 | Automate tenancy and quota management with the API | Pass | Pass | Pass | Pass | Pass | Title revised from "Script organization, quota, and mirroring…" |
| 68 | Automate repository and robot account provisioning with the API | Pass | Pass | Pass | Pass | Pass | Title revised from "Script repositories, permissions, and robots…" |
| 69 | Automate tag, team, and search operations with the API | Pass | Pass | Pass | Pass | Pass | Title revised from "Script tags, teams, and search…" |
| 70 | Build images from Dockerfiles in Quay | Pass | Pass | Pass | Pass | Pass | — |
| 71 | Start builds automatically from Git | Pass | Pass | Pass | Pass | Pass | — |
| 72 | Store Helm charts, OCI artifacts, and signed images in Quay | Pass | Pass | Pass | Pass | Pass | Title revised from "Push Helm charts, OCI artifacts…" |
| 73 | Understand Red Hat Quay configuration: Overview | Needs revision | Pass | Pass | **Fail** | Pass | Colon-subtitle format unique across the 136-job set. "Understand" accepted; colon structure is the issue. |
| 74 | Understand Red Hat Quay configuration: Standalone deployment | Needs revision | Pass | Pass | **Fail** | Pass | Same as #73. |
| 75 | Understand Red Hat Quay configuration: OpenShift Container Platform | Needs revision | Pass | Pass | **Fail** | Pass | Same as #73. |
| 76 | Retrieve Red Hat Quay configuration with the API | Pass | Pass | Pass | Pass | Pass | Title revised ("by using" → "with") |
| 77 | Configure the database and Redis for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 78 | Configure AWS STS for object storage | Pass | Pass | Pass | Pass | Pass | — |
| 79 | Configure network access for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | Title revised from "Configure networking" |
| 80 | Configure Elasticsearch and Splunk action log storage | Pass | Pass | Pass | Pass | Pass | — |
| 81 | Configure notifications for registry events | Pass | Pass | Pass | Pass | Pass | — |
| 82 | Configure build worker environments | Pass | Pass | Pass | Pass | Pass | — |
| 83 | Configure the Clair database and custom settings | Pass | Pass | Pass | Pass | Pass | Title revised (dropped redundant "Clair configuration") |
| 84 | Configure Clair updaters and disconnected scanning | Pass | Pass | Pass | Pass | Pass | — |
| 85 | Configure SSL/TLS for standalone Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 86 | Configure SSL/TLS for Red Hat Quay on OpenShift | Pass | Pass | Pass | Pass | Pass | — |
| 87 | Secure database connections with TLS | Pass | Pass | Pass | Pass | Pass | — |
| 88 | Add trusted certificate authorities | Pass | Pass | Pass | Pass | Pass | — |
| 89 | Authenticate users with LDAP | Pass | Pass | Pass | Pass | Pass | — |
| 90 | Authenticate users with OIDC and single sign-on | Pass | Pass | Pass | Pass | Pass | — |
| 91 | Eliminate long-lived robot credentials with keyless authentication | Pass | Pass | Pass | Pass | Pass | — |
| 92 | Ensure FIPS compliance for the registry | Pass | Pass | Pass | Pass | Pass | — |
| 93 | Set repository permissions and visibility | Pass | Pass | Pass | Pass | Pass | — |
| 94 | Manage registry-wide and team access policies | Pass | Pass | Pass | Pass | Pass | — |
| 95 | Review Clair vulnerability scan results | Pass | Pass | Pass | Pass | Pass | Moved to Observe; inspection activity confirmed |
| 96 | Understand audit and action logs | Pass | Pass | Pass | Pass | Pass | "Understand X" in Observe accepted per OCP precedent |
| 97 | View and export registry usage logs | Pass | Pass | Pass | Pass | Pass | — |
| 98 | Expose Prometheus metrics for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 99 | Understand Red Hat Quay Prometheus metrics | Pass | Pass | Pass | Pass | Pass | "Understand X" in Observe accepted per OCP precedent |
| 100 | Monitor the registry from the OpenShift console | Pass | Pass | Pass | Pass | Pass | — |
| 101 | Verify deployment health status | Pass | Pass | Pass | Pass | Pass | — |
| 102 | Connect OpenShift to Quay with the Quay Bridge Operator | Pass | Pass | Pass | Pass | Pass | — |
| 103 | Plan and enable image mirroring | Pass | Pass | Pass | Pass | Pass | — |
| 104 | Create mirrors and monitor synchronization | Pass | Pass | Pass | Pass | Pass | — |
| 105 | Use Quay as a proxy cache for upstream registries | Pass | Pass | Pass | Pass | Pass | — |
| 106 | Integrate Quay object storage with AWS | Pass | Pass | Pass | Pass | Pass | — |
| 107 | Tune Operator component resources and autoscaling | Pass | Pass | Pass | Pass | Pass | — |
| 108 | Resize managed storage for Operator deployments | Pass | Pass | Pass | Pass | Pass | — |
| 109 | Tune registry runtime performance | Pass | Pass | Pass | Pass | Pass | — |
| 110 | Customize container images used by the Quay Operator | Pass | Pass | Pass | Pass | Pass | — |
| 111 | Surface image vulnerabilities in the OpenShift cluster console | Pass | Pass | Pass | Pass | Pass | Title revised from "Add the Container Security Operator" |
| 112 | Get help from Red Hat Support | Pass | Pass | Pass | Pass | Pass | — |
| 113 | Enable debug mode to diagnose issues | Pass | Pass | Pass | Pass | Pass | — |
| 114 | Collect logs and configuration for troubleshooting | Pass | Pass | Pass | Pass | Pass | — |
| 115 | Troubleshoot Quay database and authentication issues | Pass | Pass | Pass | Pass | Pass | — |
| 116 | Troubleshoot Quay connectivity and storage issues | Pass | Pass | Pass | Pass | Pass | — |
| 117 | Troubleshoot geo-replication and mirroring | Pass | Pass | Pass | Pass | Pass | — |
| 118 | Troubleshoot Clair scanning issues | Pass | Pass | Pass | Pass | Pass | — |
| 119 | Troubleshoot build failures | Pass | Pass | Pass | Pass | Pass | — |
| 120 | Troubleshoot Operator-managed PostgreSQL TLS | Pass | Pass | Pass | Pass | Pass | — |
| 121 | Required configuration fields | Pass | Pass | Pass | Pass | Pass | — |
| 122 | Database and Redis configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 123 | Automation and user access configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 124 | Performance tuning environment variable reference | Pass | Pass | Pass | Pass | Pass | — |
| 125 | Object storage backend configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 126 | Core, web UI, and user configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 127 | Authentication, repository, and security configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 128 | Storage, image, and metadata configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 129 | Integration and service configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 130 | SSL/TLS configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 131 | LDAP configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 132 | OAuth and OIDC configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 133 | Action log, Elasticsearch, and Splunk configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 134 | Build automation configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 135 | Clair core, indexer, matcher, and updater configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 136 | Clair notifier, authorization, trace, metrics, and scanner configuration reference | Pass | Pass | Pass | Pass | Pass | — |

---

## Needs-revision deep-dives

### Jobs 1, 30, 33 — Pending spreadsheet statement rewrites

These are known: the adoc files and category maps are correct. Only the spreadsheet statements need updating.

| # | Title | Stale statement | Suggested replacement |
|---|-------|-----------------|----------------------|
| 1 | Red Hat Quay Release Notes | "…I want Red Hat Customer Portal release notifications, so that I know when new versions are available…" | "When I am planning a Quay upgrade, I want to review the release notes for the new version, so that I understand what changed and can assess the impact before upgrading." |
| 30 | Configure IPv6 for Quay proof of concept | Verbatim copy of #29 (Install PoC) | "When I want to validate Quay with IPv6 networking in a proof-of-concept environment, I want to configure IPv6 settings and SSL trust, so that I can confirm the registry works on an IPv6 network before committing to production." |
| 33 | Get Red Hat Quay release notifications | Identical to #1 | "When I operate Quay in production, I want to subscribe to Customer Portal notifications, so that new releases reach me before I miss an upgrade window." |

---

### Jobs 73, 74, 75 — "Understand X: Subtitle" colon format (Configure)

**Why needs revision:** The `Title: Subtitle` colon pattern is used by these three jobs and no others across the entire 136-job set. "Understand" is now accepted per OCP precedent in Discover and Observe, but Configure jobs in OCP do not use the "Understand X" pattern — and more importantly, the colon-subtitle structure creates a presentation inconsistency regardless of the verb.

**Current titles:**
- `Understand Red Hat Quay configuration: Overview`
- `Understand Red Hat Quay configuration: Standalone deployment`
- `Understand Red Hat Quay configuration: OpenShift Container Platform`

**Suggested titles:**

| # | Option A (outcome-first) | Option B (apply-verb) | Rationale |
|---|---|---|---|
| 73 | Apply Red Hat Quay configuration safely | Configure Red Hat Quay across deployment types | Derives from `so I can apply the right settings safely` |
| 74 | Configure a standalone Red Hat Quay deployment | Apply settings to a standalone Red Hat Quay installation | Derives from `so that the registry uses our settings without the Operator` |
| 75 | Manage Red Hat Quay configuration on OpenShift | Apply Operator-managed Quay configuration correctly | Derives from `so that I change the right object instead of editing config.yaml by hand` |

---

## Cross-job issues

### Resolved since v2

| Issue | Resolution |
|-------|------------|
| #1, #33 duplicate statements | Category fixes applied; statements tracked for manual spreadsheet update |
| #21 Plan → Discover | Merged in PR #1833 |
| #30 Install → Configure | Merged in PR #1831 |
| #33 Upgrade → What's New | Merged in PR #1831 |
| #67 (OCI referrer token) too granular | Modules inlined into OAuth tokens job (PR #1834) |
| #96 Secure → Observe | Merged in PR #1833 |
| #103 (GC metrics) too granular | Module inlined into Prometheus job (PR #1834) |

### Category distribution

| Category | Count | Notes |
|----------|-------|-------|
| What's New | 2 | #1, #33 — both have stale statements |
| Discover | 8 | All pass including "Understand X" jobs |
| Get Started | 8 | All pass |
| Plan | 10 | All pass |
| Install | 4 | All pass |
| Upgrade | 6 | All pass |
| Migrate | 3 | All pass |
| Administer | 20 | All pass |
| Develop | 9 | All pass |
| Configure | 14 | 3 colon-subtitle title issues (#73–75) |
| Secure | 10 | All pass |
| Observe | 8 | All pass (incl. #95 moved from Secure) |
| Integrate | 5 | All pass |
| Optimize | 3 | All pass |
| Extend | 2 | All pass |
| Troubleshoot | 9 | All pass |
| Reference | 16 | All pass |

### Title style consistency

- **"Understand X" titles** — accepted per OCP precedent in Discover (7 jobs) and Observe (2 jobs). No longer flagged.
- **Reference titles** — noun phrases throughout; consistent and correct.
- **Troubleshoot titles** — "Troubleshoot X" pattern; consistent.
- **Configure titles** — clean imperative-first except for 3 colon-subtitle outliers (#73–75).

---

## References applied

- [Phase 0 JTBD implementation](https://docs.google.com/document/d/16JBKsTvVxVl_5PVuqkbypkQs2WyzHaTqfUHswMoNsH4/edit)
- [JTBD Strategy — JTBD-style titles](https://docs.google.com/document/d/1oLDYmAlyHJCO98KpmhT_G4VT3z4jP00sucl0YErsqsQ/edit?tab=t.0#heading=h.vvsrgn8kp6ag)
- [JTBD Strategy](https://docs.google.com/document/d/1oLDYmAlyHJCO98KpmhT_G4VT3z4jP00sucl0YErsqsQ/edit)
- [Job statement template](https://docs.google.com/document/d/13RYmbBiPVGbZ1PzLu1Wx2mgD935LPqqAX_MWz6ZTaEo/template/preview)
- [Product documentation categories](https://docs.google.com/document/d/1Wht0wg78iDm0yX7Ok6ZvHBXIBXHXLsZ2L8Z_K2Eli54/edit)
- [SSG — Titles and headings](https://redhat-documentation.github.io/supplementary-style-guide/#titles-and-headings)
- [OCP ocp-jobs precedent analysis](https://github.com/openshift/openshift-docs) — "Understand X" titles used in 47 ocp-jobs assemblies across Discover, Secure, and other categories
