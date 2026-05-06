<p align="center">
  <strong>AXKI AI Governance Kit</strong>
</p>

<p align="center">
  <strong>6 slash commands. Two AIs. Zero hallucinations shipping to prod.</strong>
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

A set of slash commands that put one AI in charge of building, and another in charge of challenging it.

The pattern: your executor AI writes code. Your reviewer AI audits every plan, package, and commit before it ships. Neither one trusts the other blindly. That's the point.

Built on the **Boris Cherny governance framework** (Explore, Plan, Implement, Commit) with adversarial validation baked in at every gate.

---

## The problem this solves

AI coding tools hallucinate package names. They do it confidently. Attackers scrape those hallucinated names, register the packages with malware inside, and wait for you to run `npm install`.

The fix is not to stop using AI. The fix is to add a second AI that challenges the first one before anything gets installed or committed.

This kit gives you the commands to do that in under 2 minutes.

---

## Commands

### Governance (4 commands)

| Command | Role | What it does |
|---------|------|--------------|
| `/axki:init` | Setup | Declares executor and reviewer roles for the session |
| `/axki:validate` | Reviewer | Scores every item in the plan: PASS / FAIL / PARTIAL. Blocks on anything under threshold |
| `/axki:checklist` | Reviewer | Pre-commit audit: phases, gates, atomic commits, memory discipline |
| `/axki:watchdog` | Reviewer | Adversarial audit. Assumes the executor is trying to look productive. Finds the gaps |

### Content (2 commands)

| Command | Role | What it does |
|---------|------|--------------|
| `/axki:linkedin-post` | Executor | Generates a LinkedIn post in AXKI brand voice (howto / story / insight / cta) |
| `/axki:linkedin-carousel` | Executor | Generates a full carousel: slides, image prompts, companion post, hashtags |

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
/skill:axki-validate
/skill:axki-checklist
/skill:axki-watchdog
/skill:axki-linkedin-post
/skill:axki-linkedin-carousel
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
/codex:axki-validate
/codex:axki-checklist
/codex:axki-watchdog
```

---

## Usage

**Step 1 — Declare roles at session start**

```
/axki:init executor=claude reviewer=codex
```

or flip it:

```
/axki:init executor=codex reviewer=claude
```

When benchmarks shift and you want to swap models, change the init. Nothing else changes.

**Step 2 — Validate before you write a single line**

```
/axki:validate
```

The reviewer scores your plan. No GO = no code.

**Step 3 — Check before every commit**

```
/axki:checklist
```

**Step 4 — Run the watchdog at session end**

```
/axki:watchdog
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

Core rules: phases are sequential, no skipping. Human-in-the-loop approval at every gate. Atomic commits only. Real git worktrees. Stop-hooks until tests are green.

---

## Free resources included

The `pdf/` folder contains the **AXKI AI Coding Governance Kit** (14 pages): full framework walkthrough, all 3 template cores, real adversarial validation screenshot, and install reference.

---

## Built by AXKI

**Max Dion** — Fractional CTO and AI Automation Partner

I help engineering teams and non-developer founders implement structured AI governance so they ship faster without losing control.

Montreal, Canada. Clients in Canada, USA, Europe, and Latin America.

- Website: [axki.ca](https://axki.ca)
- Email: [max@axki.ca](mailto:max@axki.ca)
- LinkedIn: [Max Dion](https://linkedin.com/in/maxdion)

**Need help implementing this in your stack?**
Book a free 30-minute strategic discovery call at [axki.ca](https://axki.ca). We look at what you have, identify the gaps, and build a plan. No sales pitch.

---

## License

MIT. Use it, fork it, build on it. Keep the attribution in the LICENSE file.

See [LICENSE](LICENSE) for full terms.
