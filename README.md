<p align="center">
  <strong>AXKI AI Governance Kit</strong>
</p>

<p align="center">
  <strong>4 governance skills for Claude Code. 4 governance commands for Codex CLI. Two AIs. Zero hallucinations shipping to prod.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"/></a>
  <img src="https://img.shields.io/badge/Claude%20Code-skills-0F1658" alt="Claude Code Skills"/>
  <img src="https://img.shields.io/badge/Codex%20CLI-commands-367FC8" alt="Codex CLI Commands"/>
  <img src="https://img.shields.io/badge/version-1.0.0-EDEDED" alt="v1.0.0"/>
  <a href="https://axki.ca"><img src="https://img.shields.io/badge/built%20by-AXKI%20Consulting-E4AF4C" alt="Built by AXKI"/></a>
</p>

---

## What this is

A governance kit that puts one AI in charge of building, and another in charge of challenging it.

The pattern: your executor AI writes code. Your reviewer AI audits every plan, package, and commit before it ships. Neither one trusts the other blindly. That's the point.

Built on the **Boris Cherny governance framework** (Explore, Plan, Implement, Commit) with adversarial validation baked in at every gate.

---

## The problem this solves

AI coding tools hallucinate package names. They do it confidently. Attackers scrape those hallucinated names, register the packages with malware inside, and wait for you to run `npm install`.

The fix is not to stop using AI. The fix is to add a second AI that challenges the first one before anything gets installed or committed.

This kit gives you Claude Code skills and Codex CLI commands to do that in under 2 minutes.

---

## Public invocation names

Claude Code uses skills. Codex uses commands. The governance concepts are the same, but the invocation syntax is intentionally different to avoid copy-paste confusion.

### Claude Code Skills

| Skill | Role | What it does |
|-------|------|--------------|
| `/skill:axki-init` | Setup | Declares executor and reviewer roles for the session |
| `/skill:axki-validate` | Reviewer | Scores every item in the plan: PASS / FAIL / PARTIAL. Blocks on anything under threshold |
| `/skill:axki-checklist` | Reviewer | Pre-commit audit: phases, gates, atomic commits, memory discipline |
| `/skill:axki-watchdog` | Reviewer | Adversarial audit. Assumes the executor is trying to look productive. Finds the gaps |

### Codex Commands

| Command | Role | What it does |
|---------|------|--------------|
| `/codex:axki-init` | Setup | Declares executor and reviewer roles for the session |
| `/codex:axki-validate` | Reviewer | Scores every item in the plan: PASS / FAIL / PARTIAL. Blocks on anything under threshold |
| `/codex:axki-checklist` | Reviewer | Pre-commit audit: phases, gates, atomic commits, memory discipline |
| `/codex:axki-watchdog` | Reviewer | Adversarial audit. Assumes the executor is trying to look productive. Finds the gaps |

---

## Installation

### Claude Code

Copy the skills folder into your project:

```bash
cp -r .claude/ /path/to/your/project/.claude/
```

Available as:

```
/skill:axki-init
/skill:axki-checklist
/skill:axki-validate
/skill:axki-watchdog
```

### Codex CLI

Copy the Codex config into your project root:

```bash
cp codex/AGENTS.md /path/to/your/project/AGENTS.md
cp -r codex/commands/ /path/to/your/project/.codex/commands/
```

Available as:

```
/codex:axki-init
/codex:axki-checklist
/codex:axki-validate
/codex:axki-watchdog
```

---

## Usage

**Step 1 — Declare roles at session start**

Claude Code:

```
/skill:axki-init executor=claude reviewer=codex
```

Codex CLI:

```
/codex:axki-init executor=codex reviewer=claude
```

When benchmarks shift and you want to swap models, change the executor/reviewer values. Keep Claude Code invocations on `/skill:axki-*` and Codex CLI invocations on `/codex:axki-*`.

**Step 2 — Validate before you write a single line**

Claude Code:

```
/skill:axki-validate
```

Codex CLI:

```
/codex:axki-validate
```

The reviewer scores your plan. No GO = no code.

**Step 3 — Check before every commit**

Claude Code:

```
/skill:axki-checklist
```

Codex CLI:

```
/codex:axki-checklist
```

**Step 4 — Run the watchdog at session end**

Claude Code:

```
/skill:axki-watchdog
```

Codex CLI:

```
/codex:axki-watchdog
```

The reviewer assumes the executor is lying. It will find out.

---

## The Boris Cherny Framework

```
EXPLORE  -->  PLAN  -->  IMPLEMENT  -->  COMMIT
   |            |              |              |
 GATE 1      GATE 2         GATE 3        GATE 4
(GO req)    (GO req)       (GO req)     (GO Prod)
```

Core rules: phases are sequential, no skipping. Human-in-the-loop approval at every gate. Atomic commits only. Stop-hooks until tests are green.

Project-specific AGENTS.md / CLAUDE.md instructions override this generic framework. If the project uses lane worktrees, create real git worktrees in the project-approved lanes directory; otherwise follow the project's AGENTS.md/CLAUDE.md workflow. Push the approved target branch/current session branch only when authorized.

---

## Free resources included

The `pdf/` folder contains the **AXKI AI Coding Governance Kit**: full framework walkthrough, template cores, real adversarial validation screenshot, and install reference.

---

## Built by AXKI

**Max Dion** — Fractional CTO and AI Automation Partner

I help engineering teams and non-developer founders implement structured AI governance so they ship faster without losing control.

Montreal, Canada. Clients in Canada, USA, Europe, and Latin America.

- Website: [axki.ca](https://axki.ca)
- Email: [max@axki.ca](mailto:max@axki.ca)
- LinkedIn: [Max Dion](https://www.linkedin.com/in/maxxdion-no1/)

**Need help implementing this in your stack?**
[Book a free 30-minute strategic discovery call](https://calendar.app.google/cuhqb3tSsnx6CYWZ8). We look at what you have, identify the gaps, and build a plan. No sales pitch.

---

## License

MIT. Use it, fork it, build on it. Keep the attribution in the LICENSE file.

See [LICENSE](LICENSE) for full terms.
