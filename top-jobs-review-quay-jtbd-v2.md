# Top-jobs review: Red Hat Quay

**Source:** `QuayDraft_Master_Updated.xlsx` (Main sheet, extracted to CSV)
**Phase:** 0 — Steps 1–2 (jobs, statements, categories only)
**Reviewed:** 2026-09-25 | **Jobs reviewed:** 138 | **Template rows skipped:** 0

---

## Executive summary

| Status | Count |
|--------|-------|
| Pass | 111 |
| Needs revision | 25 |
| Blocker | 2 |

### Top systemic issues

1. **"Understand X" title pattern** — 11 jobs across Discover, Configure, and Observe categories start with "Understand," violating SSG (no "Understand" / "About" starts) and JTBD (titles should derive from the `so I can` outcome). This is the single largest pattern requiring correction.
2. **Duplicate statement** — Jobs #1 and #33 have identical statements. Job #33 is also miscategorized in Upgrade.
3. **Copy-paste error** — Job #30 has a statement copied verbatim from job #29, making it a Blocker.

---

## Per-job findings

| # | Current title | Status | Outcome | Statement | Title | Category | Suggested fixes |
|---|---------------|--------|---------|-----------|-------|----------|-----------------|
| 1 | Red Hat Quay Release Notes | Needs revision | Pass | **Fail** | Pass | Pass | Statement is about subscribing to Customer Portal notifications, not reading release notes. Rewrite statement. |
| 2 | Understand Red Hat Quay capabilities and architecture | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. See systemic deep-dive. |
| 3 | Understand Red Hat Quay infrastructure and governance | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
| 4 | Evaluate Quay.io as a hosted registry option | Pass | Pass | Pass | Pass | Pass | — |
| 5 | Understand Red Hat Quay's tenancy model | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
| 6 | Understand the Red Hat Quay permissions model | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
| 7 | Understand Clair vulnerability scanning | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
| 8 | Understand the Quay Bridge Operator | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
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
| 21 | Choose a Quay.io plan | Needs revision | Pass | Pass | Pass | **Fail** | Plan category is for architecture/topology; pricing tier selection belongs in Discover or Get Started. |
| 22 | Plan a Red Hat Quay proof of concept deployment | Pass | Pass | Pass | Pass | Pass | — |
| 23 | Plan a Red Hat Quay deployment on OpenShift Container Platform | Pass | Pass | Pass | Pass | Pass | — |
| 24 | Plan a Red Hat Quay high availability deployment | Pass | Pass | Pass | Pass | Pass | — |
| 25 | Plan a Red Hat Quay public cloud deployment | Pass | Pass | Pass | Pass | Pass | — |
| 26 | Plan content distribution and geo-replication | Pass | Pass | Pass | Pass | Pass | — |
| 27 | Plan container image builds with Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 28 | Install Red Hat Quay on OpenShift Container Platform | Pass | Pass | Pass | Pass | Pass | — |
| 29 | Install Red Hat Quay proof of concept | Pass | Pass | Pass | Pass | Pass | — |
| 30 | Configure IPv6 for Quay proof of concept | **Blocker** | Pass | **Fail** | Pass | **Fail** | Statement is verbatim copy of #29. Title does not match statement. Category should be Configure, not Install. See deep-dive. |
| 31 | Install Red Hat Quay in high availability | Pass | Pass | Pass | Pass | Pass | — |
| 32 | Install Clair for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 33 | Get Red Hat Quay release notifications | **Blocker** | Pass | **Fail** | Pass | **Fail** | Statement identical to #1. Wrong category (Upgrade). Duplicate — merge with #1 or remove. See deep-dive. |
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
| 63 | Recover and administer the whole registry as a superuser | Needs revision | Pass | Pass | **Fail** | Pass | "Recover and" is redundant; "whole" implied by superuser scope. See deep-dive. |
| 64 | Get your first API workflow running | Pass | Pass | Pass | Pass | Pass | — |
| 65 | Authenticate applications with OAuth access tokens | Pass | Pass | Pass | Pass | Pass | — |
| 66 | Authenticate CI/CD with robot account tokens | Pass | Pass | Pass | Pass | Pass | — |
| 67 | List OCI referrers with a dedicated token | Needs revision | Pass | Pass | **Fail** | Pass | Too granular for a top-level job; single-API-call; nest inside #65. |
| 68 | Script organization, quota, and mirroring from the API | Needs revision | Pass | Pass | **Fail** | Pass | Mechanism list in title (what the scripts target, not the outcome). See deep-dive. |
| 69 | Script repositories, permissions, and robots from the API | Needs revision | Pass | Pass | **Fail** | Pass | Mechanism list in title. See deep-dive. |
| 70 | Script tags, teams, and search from the API | Needs revision | Pass | Pass | **Fail** | Pass | Mechanism list in title. See deep-dive. |
| 71 | Build images from Dockerfiles in Quay | Pass | Pass | Pass | Pass | Pass | — |
| 72 | Start builds automatically from Git | Pass | Pass | Pass | Pass | Pass | — |
| 73 | Push Helm charts, OCI artifacts, and signed images | Needs revision | Pass | Pass | **Fail** | Pass | Lists what you push, not why. See deep-dive. |
| 74 | Understand Red Hat Quay configuration: Overview | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start + colon subtitle format inconsistent with rest of set. See systemic deep-dive. |
| 75 | Understand Red Hat Quay configuration: Standalone deployment | Needs revision | Pass | Pass | **Fail** | Pass | Same as #74. |
| 76 | Understand Red Hat Quay configuration: OpenShift Container Platform | Needs revision | Pass | Pass | **Fail** | Pass | Same as #74. |
| 77 | Retrieve Red Hat Quay configuration by using the API | Needs revision | Pass | Pass | **Fail** | Pass | "by using the API" is verbose; use "with the API." |
| 78 | Configure database and Redis backends | Pass | Pass | Pass | Pass | Pass | — |
| 79 | Configure AWS STS for object storage | Pass | Pass | Pass | Pass | Pass | — |
| 80 | Configure networking | Needs revision | Pass | Pass | **Fail** | Pass | Only 2 words — below SSG 3-word minimum; too generic. |
| 81 | Configure Elasticsearch and Splunk action log storage | Pass | Pass | Pass | Pass | Pass | — |
| 82 | Configure notifications for registry events | Pass | Pass | Pass | Pass | Pass | — |
| 83 | Configure build worker environments | Pass | Pass | Pass | Pass | Pass | — |
| 84 | Configure Clair database and custom Clair configuration | Needs revision | Pass | Pass | **Fail** | Pass | "Clair configuration" is redundant at end of a Clair title. |
| 85 | Configure Clair updaters and disconnected scanning | Pass | Pass | Pass | Pass | Pass | — |
| 86 | Configure SSL/TLS for standalone Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 87 | Configure SSL/TLS for Red Hat Quay on OpenShift | Pass | Pass | Pass | Pass | Pass | — |
| 88 | Secure database connections with TLS | Pass | Pass | Pass | Pass | Pass | — |
| 89 | Add trusted certificate authorities | Pass | Pass | Pass | Pass | Pass | — |
| 90 | Authenticate users with LDAP | Pass | Pass | Pass | Pass | Pass | — |
| 91 | Authenticate users with OIDC and single sign-on | Pass | Pass | Pass | Pass | Pass | — |
| 92 | Eliminate long-lived robot credentials with keyless authentication | Pass | Pass | Pass | Pass | Pass | — |
| 93 | Ensure FIPS compliance for the registry | Pass | Pass | Pass | Pass | Pass | — |
| 94 | Set repository permissions and visibility | Pass | Pass | Pass | Pass | Pass | — |
| 95 | Manage registry-wide and team access policies | Pass | Pass | Pass | Pass | Pass | — |
| 96 | Review Clair vulnerability scan results | Needs revision | Pass | Pass | Pass | **Fail** | Secure = implementing controls; reviewing scan results = Observe. |
| 97 | Understand audit and action logs | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
| 98 | View and export registry usage logs | Pass | Pass | Pass | Pass | Pass | — |
| 99 | Expose Prometheus metrics for Red Hat Quay | Pass | Pass | Pass | Pass | Pass | — |
| 100 | Understand Red Hat Quay Prometheus metrics | Needs revision | Pass | Pass | **Fail** | Pass | "Understand" start violates SSG. |
| 101 | Monitor the registry from the OpenShift console | Pass | Pass | Pass | Pass | Pass | — |
| 102 | Verify deployment health status | Pass | Pass | Pass | Pass | Pass | — |
| 103 | Monitor garbage collection metrics | Needs revision | Pass | Pass | Pass | Pass | Too granular; single-include; merge into #99 or #102. |
| 104 | Connect OpenShift to Quay with the Quay Bridge Operator | Pass | Pass | Pass | Pass | Pass | — |
| 105 | Plan and enable image mirroring | Pass | Pass | Pass | Pass | Pass | — |
| 106 | Create mirrors and monitor synchronization | Pass | Pass | Pass | Pass | Pass | — |
| 107 | Use Quay as a proxy cache for upstream registries | Pass | Pass | Pass | Pass | Pass | — |
| 108 | Integrate Quay object storage with AWS | Pass | Pass | Pass | Pass | Pass | — |
| 109 | Tune Operator component resources and autoscaling | Pass | Pass | Pass | Pass | Pass | — |
| 110 | Resize managed storage for Operator deployments | Pass | Pass | Pass | Pass | Pass | — |
| 111 | Tune registry runtime performance | Pass | Pass | Pass | Pass | Pass | — |
| 112 | Customize container images used by the Quay Operator | Pass | Pass | Pass | Pass | Pass | — |
| 113 | Add the Container Security Operator | Needs revision | Pass | Pass | **Fail** | Pass | Names the tool, not the outcome. See deep-dive. |
| 114 | Get help from Red Hat Support | Pass | Pass | Pass | Pass | Pass | — |
| 115 | Enable debug mode to diagnose issues | Pass | Pass | Pass | Pass | Pass | — |
| 116 | Collect logs and configuration for troubleshooting | Pass | Pass | Pass | Pass | Pass | — |
| 117 | Troubleshoot Quay database and authentication issues | Pass | Pass | Pass | Pass | Pass | — |
| 118 | Troubleshoot Quay connectivity and storage issues | Pass | Pass | Pass | Pass | Pass | — |
| 119 | Troubleshoot geo-replication and mirroring | Pass | Pass | Pass | Pass | Pass | — |
| 120 | Troubleshoot Clair scanning issues | Pass | Pass | Pass | Pass | Pass | — |
| 121 | Troubleshoot build failures | Pass | Pass | Pass | Pass | Pass | — |
| 122 | Troubleshoot Operator-managed PostgreSQL TLS | Pass | Pass | Pass | Pass | Pass | — |
| 123 | Required configuration fields | Pass | Pass | Pass | Pass | Pass | — |
| 124 | Database and Redis configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 125 | Automation and user access configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 126 | Performance tuning environment variable reference | Pass | Pass | Pass | Pass | Pass | — |
| 127 | Object storage backend configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 128 | Core, web UI, and user configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 129 | Authentication, repository, and security configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 130 | Storage, image, and metadata configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 131 | Integration and service configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 132 | SSL/TLS configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 133 | LDAP configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 134 | OAuth and OIDC configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 135 | Action log, Elasticsearch, and Splunk configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 136 | Build automation configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 137 | Clair core, indexer, matcher, and updater configuration reference | Pass | Pass | Pass | Pass | Pass | — |
| 138 | Clair notifier, authorization, trace, metrics, and scanner configuration reference | Pass | Pass | Pass | Pass | Pass | — |

---

## Blocker deep-dives

### Job 30 — Configure IPv6 for Quay proof of concept

**Why blocker:** Statement is verbatim copy of job #29 ("Install Red Hat Quay proof of concept"). Title does not match statement. Category is Install; IPv6 configuration belongs in Configure.

**Original statement (copied from #29):** "When I want a simple proof of concept, I want to prepare a RHEL host, deploy Quay, and configure TLS, so that I can validate the product in a single-host environment."

**Rewritten job:**

- **Suggested titles:**
  - **Title A:** Configure IPv6 for a standalone proof of concept — *matches adoc scope; 7 words*
  - **Title B:** Enable IPv6 networking for Red Hat Quay — *broader; absorbs PoC and general standalone IPv6*
  - **Title C:** Set up IPv6 and SSL for a Quay proof of concept — *if SSL trust is part of the same workflow*
- **Statement:** When I want to validate Quay with IPv6 networking in a proof-of-concept environment, I want to configure IPv6 settings and SSL trust, so that I can confirm the registry works on an IPv6 network before committing to production.
- **Category:** Configure

---

### Job 33 — Get Red Hat Quay release notifications

**Why blocker:** Statement is identical to job #1. Upgrade category definition is "Move an existing environment to a newer version safely" — subscribing to release notifications is not upgrading. One of these two jobs is a duplicate and must be resolved.

**Original statement (identical to #1):** "When I operate Quay in production, I want Red Hat Customer Portal release notifications, so that I know when new versions are available before I upgrade."

**Extracted outcome:** know when new versions are available before I upgrade

**Resolution options:**

- **Option A — Merge into #1:** Rename job #1 to "Stay informed about Red Hat Quay releases." Write one statement that covers both reading release notes and subscribing to notifications. Remove #33.
- **Option B — Keep as separate What's New job:** Move #33 to What's New; differentiate the statement.
  - **Title:** Subscribe to Red Hat Quay release notifications
  - **Statement:** When I operate Quay in production, I want to subscribe to Customer Portal notifications, so that new releases reach me before I miss an upgrade window.
  - **Category:** What's New

---

## Needs-revision deep-dives

### Jobs 2, 3, 5, 6, 7, 8, 74, 75, 76, 97, 100 — "Understand X" systemic title violation

**Why needs revision:** SSG prohibits titles starting with "Understand," "Understanding," or "About." For JTBD job titles, the title derives from the `so I can` outcome — "Understand X" restates orientation intent rather than what the user gets from the job.

| # | Current title | Extracted outcome | Suggested title A | Suggested title B |
|---|--------------|-------------------|-------------------|-------------------|
| 2 | Understand Red Hat Quay capabilities and architecture | decide whether it solves our problem | Assess whether Red Hat Quay fits your needs | Choose Red Hat Quay for your container registry |
| 3 | Understand Red Hat Quay infrastructure and governance | know whether it fits our infrastructure and compliance needs | Evaluate Red Hat Quay's infrastructure and compliance fit | Plan how Red Hat Quay fits your infrastructure |
| 5 | Understand Red Hat Quay's tenancy model | plan how we will structure ownership and access | Plan user, team, and repository structure in Red Hat Quay | Structure ownership and access in Red Hat Quay |
| 6 | Understand the Red Hat Quay permissions model | grant the right access without over-permissioning | Control access to Red Hat Quay without over-permissioning | Grant the right access with Quay permission levels |
| 7 | Understand Clair vulnerability scanning | know how scanning fits into our registry strategy | Plan your Clair vulnerability scanning strategy | Decide how Clair scanning fits your registry |
| 8 | Understand the Quay Bridge Operator | decide whether to integrate cluster builds with my registry | Decide whether to use the Quay Bridge Operator | Evaluate the Quay Bridge Operator for your cluster |
| 74 | Understand Red Hat Quay configuration: Overview | apply the right settings safely | Apply Red Hat Quay configuration safely | Configure Red Hat Quay across deployment types |
| 75 | Understand Red Hat Quay configuration: Standalone deployment | registry uses our settings without the Operator | Configure a standalone Red Hat Quay deployment | Apply settings to a standalone Red Hat Quay installation |
| 76 | Understand Red Hat Quay configuration: OpenShift Container Platform | change the right object instead of editing config.yaml by hand | Manage Red Hat Quay configuration on OpenShift | Apply Operator-managed Quay configuration correctly |
| 97 | Understand audit and action logs | know what the logs mean before I export them | Interpret Quay audit and action logs | Read and understand registry audit logs |
| 100 | Understand Red Hat Quay Prometheus metrics | interpret dashboards correctly | Interpret Red Hat Quay Prometheus metrics | Read Quay Prometheus metrics correctly |

**Additional note for #74, 75, 76:** The "Title: Subtitle" colon format is not used anywhere else in the 138-job set. Drop the colon structure and rewrite each title as a standalone outcome-derived imperative.

---

### Job 1 — Red Hat Quay Release Notes (statement mismatch)

**Extracted outcome (correct):** understand what changed before upgrading

**Suggested statement:** When I am planning a Quay upgrade, I want to review the release notes for the new version, so that I understand what changed and can assess the impact before upgrading.

---

### Job 21 — Choose a Quay.io plan (category mismatch)

CCS Plan definition: "Help me choose the right architecture and topology before installing." Pricing tier selection is a purchasing/discovery decision, not architecture planning.

**Suggested category:** Discover *(natural companion to #4)* or Get Started *(natural child of #9)*
**Merge candidate:** Consider nesting inside #4 or #9 rather than keeping as a peer top-level job.

---

### Job 63 — Recover and administer the whole registry as a superuser

**Extracted outcome:** administer the entire deployment and regain access if needed

**Suggested titles:**
- **Title A:** Administer the registry as a superuser — *matches adoc filename; 6 words; clean*
- **Title B:** Manage full registry access as a superuser — *slightly more outcome language*

---

### Jobs 68, 69, 70 — "Script X, Y, and Z from the API" (mechanism lists)

Titles enumerate script targets, not outcomes. Top-level job titles should capture "goal + benefit," not `I want` mechanism lists.

| # | Current | Extracted outcome | Suggested A | Suggested B |
|---|---------|------------------|-------------|-------------|
| 68 | Script organization, quota, and mirroring from the API | script tenancy without using the UI | Automate tenancy and quota management with the API | Manage organizations and quotas without the UI |
| 69 | Script repositories, permissions, and robots from the API | script repository setup without using the UI | Automate repository and robot account provisioning with the API | Provision repositories and robot accounts from automation |
| 70 | Script tags, teams, and search from the API | script content and membership without using the UI | Automate tag, team, and search operations with the API | Manage tags and team membership from automation |

---

### Job 73 — Push Helm charts, OCI artifacts, and signed images

**Extracted outcome:** "the registry holds signed, non-image content"

**Suggested titles:**
- **Title A:** Store signed content, Helm charts, and OCI artifacts in Quay — *shifts verb to what you achieve*
- **Title B:** Extend your registry to hold non-container artifacts — *pure outcome*
- **Title C:** Push and sign OCI artifacts, Helm charts, and container images — *shorter mechanism list; keeps imperative verb*

**Child jobs to nest:** Helm chart operations, Cosign signing workflow, ORAS annotation parsing.

---

### Job 77 — Retrieve Red Hat Quay configuration by using the API

**Suggested titles:**
- **Title A:** Retrieve Red Hat Quay configuration with the API — *drops verbose "by using"*
- **Title B:** Verify Red Hat Quay configuration settings with the API — *outcome verb "Verify"*

---

### Job 80 — Configure networking

**Why needs revision:** Two words — below SSG 3-word minimum. Too generic to distinguish the job scope.

**Extracted outcome:** "the registry is reachable the way our network requires"

**Suggested titles:**
- **Title A:** Configure network access for Red Hat Quay — *5 words; adds scope*
- **Title B:** Set up IPv6 and custom ingress for Quay — *matches actual content scope*
- **Title C:** Make Red Hat Quay reachable across your network — *outcome-first*

---

### Job 84 — Configure Clair database and custom Clair configuration

**Extracted outcome:** "scanning uses the right data store and TLS settings"

**Suggested titles:**
- **Title A:** Configure the Clair database and custom settings — *drops redundant "Clair configuration"*
- **Title B:** Set up Clair's data store and custom configuration — *clearer scope distinction*

---

### Job 96 — Review Clair vulnerability scan results (category mismatch)

Secure = "Implement security controls and ensure compliance." Reviewing scan results is an inspection activity — you observe what Clair found, you do not implement a control.

**Suggested category:** Observe

---

### Job 103 — Monitor garbage collection metrics (too granular)

Single-include job mapping to a subset of Prometheus metrics already covered by #99.

**Recommendation:** Merge into #99 "Expose Prometheus metrics for Red Hat Quay" as a child section, or fold into #102 "Verify deployment health status."

---

### Job 113 — Add the Container Security Operator

**Extracted outcome:** "security findings appear in the cluster console and CLI"

**Suggested titles:**
- **Title A:** Surface image vulnerabilities in the OpenShift cluster console — *outcome-first; 8 words*
- **Title B:** Enable in-cluster image vulnerability scanning — *shorter; outcome-implied*
- **Title C:** Expose Clair scan results in OpenShift with the Container Security Operator — *keeps CSO name for discoverability*

---

### Job 67 — List OCI referrers with a dedicated token (too granular)

Single-API-call procedure involving one specific token type. Child job of #65.

**Recommendation:** Nest inside #65 "Authenticate applications with OAuth access tokens" as a child section.

---

## Cross-job issues

### Duplicates and merge candidates

| Jobs | Issue | Recommendation |
|------|-------|---------------|
| #1, #33 | Identical statements; #33 wrong category | Merge into #1 or convert to child job |
| #67 | Single-API-call; child of #65 | Nest inside #65 |
| #103 | GC metrics subset of Prometheus metrics (#99) | Merge into #99 or #102 |
| #21 | Pricing tier overlaps #4 and #9 | Relocate to Discover or nest in #9 |

### Category distribution

| Category | Count | Notes |
|----------|-------|-------|
| What's New | 1 | Fine |
| Discover | 7 | 6 of 7 need "Understand X" title fix |
| Get Started | 8 | All pass |
| Plan | 11 | #21 category mismatch |
| Install | 5 | #30 Blocker |
| Upgrade | 7 | #33 Blocker |
| Migrate | 3 | All pass |
| Administer | 21 | Largest category; all substantively pass |
| Develop | 10 | 4 title issues (#67, #68, #69, #70, #73) |
| Configure | 12 | 5 title issues (#74–76 Understand, #77 wordy, #80 too short, #84 redundant) |
| Secure | 11 | #96 category mismatch |
| Observe | 7 | 2 "Understand" titles; #103 granularity |
| Integrate | 5 | All pass |
| Optimize | 3 | All pass |
| Extend | 2 | #113 title issue |
| Troubleshoot | 9 | All pass |
| Reference | 16 | All pass |

### Title style consistency

- **"Understand X" titles** span Discover, Configure, and Observe — inconsistent with the imperative-first style used across 90% of the job set.
- **Reference titles** are all noun phrases — consistent and correct for Reference category.
- **Troubleshoot titles** all follow "Troubleshoot X" pattern — consistent.

---

## References applied

- [Phase 0 JTBD implementation](https://docs.google.com/document/d/16JBKsTvVxVl_5PVuqkbypkQs2WyzHaTqfUHswMoNsH4/edit)
- [JTBD Strategy — JTBD-style titles](https://docs.google.com/document/d/1oLDYmAlyHJCO98KpmhT_G4VT3z4jP00sucl0YErsqsQ/edit?tab=t.0#heading=h.vvsrgn8kp6ag)
- [JTBD Strategy](https://docs.google.com/document/d/1oLDYmAlyHJCO98KpmhT_G4VT3z4jP00sucl0YErsqsQ/edit)
- [Job statement template](https://docs.google.com/document/d/13RYmbBiPVGbZ1PzLu1Wx2mgD935LPqqAX_MWz6ZTaEo/template/preview)
- [Product documentation categories](https://docs.google.com/document/d/1Wht0wg78iDm0yX7Ok6ZvHBXIBXHXLsZ2L8Z_K2Eli54/edit)
- [SSG — Titles and headings](https://redhat-documentation.github.io/supplementary-style-guide/#titles-and-headings)
