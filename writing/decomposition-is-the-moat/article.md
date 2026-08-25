---
published: false   # source for bin/md2post.py; Jekyll must not render it
title: "Devin Fusion Is Only Half Right. Why Cost Is the Wrong Optimization Goal."
slug: decomposition-is-the-moat
description: "Cheap delegation should be a byproduct of good decomposition, not the thing you optimize for."
date: "Jul 14, 2026"
affiliation: Independent
bibkey: zhang2026decomposition
---

Cognition shipped Devin Fusion, a harness that routes subtasks between an expensive model and a cheap one and reports real cost savings, and the whole industry is now saying the harness is the moat. I think that is half right. The router is the part everyone can see, and the part everyone can copy. The leverage sits upstream, in how you carve the task before any model runs. Cheap delegation is a byproduct of good decomposition, not the thing to chase.

## Routing shipped as a product {#shipped}

[Devin Fusion](https://cognition.com/blog/devin-fusion) runs two parallel agents: a frontier model and a cheaper "sidekick" model, each with its own persistent, cached context. The frontier model makes the significant decisions (the plan, the ambiguous calls, the final review) and delegates execution to the sidekick. A lightweight classifier decides, mid-run, when to switch which model is in charge. Cognition reports a 41% cost reduction at the same quality, and Aaron Levie ran the same experiment by hand and was surprised to find that delegation *lowered* total cost rather than raising it. His conclusion: the harness is becoming the core area of differentiation.

That last claim is the one worth pressing on. If the harness is the moat, which part of the harness? The answer people reach for is the router: the policy that decides which model runs which step. I want to argue that the router is the least defensible part of the whole thing, and that the real work happens before it.

## The sidekick optimizes cost {#sidekick}

The sidekick pattern is an economics move. Put the expensive model on the decisions, put the cheap model on the token-heavy grunt work, keep both contexts warm so switching between them does not trigger a cache miss. Everything about the design is organized around one objective: spend fewer expensive tokens without losing quality.

Cognition's own examples make this concrete. Modernizing a file to ES6 is a trivial edit, but verifying it means babysitting a slow Playwright end-to-end suite. The expensive part is watching the tests, not writing the code, so they hand the test-watching to the cheap model and save 62% with no quality loss. Ripping an unused library out of a large Go codebase is mechanical work across many files with almost no judgment calls, so the entire task goes to the cheap model, 32% cheaper at the same quality. The pattern is clear: delegation pays off when the expensive work is low-intelligence, high-token, and cleanly separable.

## Cost is the wrong target {#wrong-target}

This is where I part ways with the design. Because the sidekick's objective is cost, it back-derives a rule: the main agent should "take minimal actions, and only read what is absolutely necessary." The system is being told to read less and do less, not because the task is small, but because reading and doing cost money.

That is optimizing the wrong variable, and the failure shows up in Cognition's own results. Their launch note admits the savings are not uniform: *"serial debugging tasks necessitate accumulated context to trace the error."* In their blog, a React and Redux feature delegated to the sidekick scored only 27. Both are the same failure. The moment a task needs continuity, a cost heuristic that starves the agent of context produces a quality collapse. You told the agent to read less to save money, and it read less, and then it could not do the job.

<div class="callout">
        <strong>The anti-pattern:</strong> when cost is the objective, "minimal actions" becomes a cause you
        impose on the agent. You clamp it from the top to save money, and clamping can starve it. Cost-driven
        routing has no way to tell the difference between a step that is genuinely small and a step you are simply
        refusing to pay for.
      </div>

## Optimize the decomposition, and cost falls out {#decompose}

The fix is not a better router. It is to move the intelligence upstream, to the decomposition. Qualify each phase of the work well enough, with a clear goal and a clear definition of done, and the agent's job on any single phase becomes small. The agent then takes few actions, not because you forbade the rest, but because a well-scoped task does not need them.

Same behavior, opposite mechanism. The sidekick clamps the agent at runtime and hopes it does not starve. Good decomposition makes the clamp unnecessary at design time. Few reads are now a result of good carving, not a rule imposed on a hard task, so quality and cost move together instead of trading off. A small, well-specified task is both easy to do right and cheap to run.

This is the argument in three steps, and the order matters:

1.  Qualify each phase's goal properly, so the work is well scoped.
2.  A well-scoped phase is easy for a cheap model to execute correctly. High-quality delivery is the direct result.
3.  Cost-effectiveness is the side effect. It comes along for free, because you never had to spend expensive tokens fighting an underspecified task.

## Why this is structural, not incidental {#amortize}

Step 3 is stronger than "and it also happens to be cheaper." Good decomposition does not eliminate the cost of frontier intelligence. It relocates it. The expensive reasoning moves from runtime, where the sidekick pays for it on every step it micromanages, to design time, where you pay for it once while writing the plan.

That is the real reason it is cost-effective. You are amortizing. The frontier model (or a person, or both) is expensive exactly once, when it carves the task into the right milestones. After that, a cheap model runs many steps against a plan that already removed the hard reasoning. Compare that to paying the frontier model to sit in the loop and re-decide every step, which is what the sidekick's "delegate and monitor" actually costs. One up-front carving versus per-step micromanagement.

Which surfaces a position that neither Cognition nor most of the routing literature states outright. The sidekick says: frontier decides, cheap executes, per step. The better claim is: the frontier model's best use is not per-step manager but up-front decomposer. Spend the expensive intelligence on carving and qualifying the goals, then hand the whole execution to a cheap model. Frontier tokens on decomposition, cheap tokens on execution. Carve once, do not route every step.

## When decomposition wins, and when it does not {#when}

I want to be honest about the boundary, because "my approach is always better" is the claim a single counterexample kills. The dividing line is not how long the task is. It is whether you can understand its structure before you start.

<div class="table-wrap">
        <div class="table-caption">Table 1. Two ways to delegate, and what each optimizes.</div>
        <table>
          <thead>
            <tr><th> </th><th>Sidekick routing</th><th>Explicit decomposition</th></tr>
          </thead>
          <tbody>
            <tr><td>Optimizes for</td><td>Cost per token</td><td>Delivery per milestone</td></tr>
            <tr><td>Where intelligence is spent</td><td>Runtime, per step</td><td>Design time, once (amortized)</td></tr>
            <tr><td>Routing decision</td><td>A learned classifier, reactive</td><td>The decomposition itself, proactive</td></tr>
            <tr><td>Wins when</td><td>Structure is unknowable up front (interactive, exploratory)</td><td>Structure is plannable (you can carve it before you start)</td></tr>
            <tr><td>Failure mode</td><td>Starves the agent of context on serial, dependent work</td><td>Locked into a bad plan if you carved it wrong</td></tr>
          </tbody>
        </table>
      </div>

On plannable long-horizon work, decomposition wins, and it wins precisely on the tasks Cognition admits are its weak spot: serial, dependent chains where accumulated context matters. There is no per-step classifier to accumulate routing errors, the plan is auditable, and drift gets caught at the next milestone.

On genuinely unpredictable work, research, debugging an unknown failure, an interactive session where hard follow-ups arrive after simple prompts, the sidekick's reactivity is more robust. You cannot decompose what you cannot foresee, and a coarse milestone gate corrects more slowly than per-step routing. The sidekick also skips the up-front cost of writing a plan, which matters when the plan would be wrong anyway.

And to keep the cost accounting fair: decomposition's total has to include the price of the decomposition itself. On a one-off short task, the sidekick can be cheaper because it never pays that up-front tax. The advantage of decomposition grows with task length and with reuse. The more steps a plan governs, and the more times you run the same class of task, the harder the up-front carving amortizes in your favor.

## The actual moat {#moat}

So back to "the harness is the moat." The router, the part everyone is excited about, is the commoditizable part. Routing between a strong and a weak model is a solved genre: a small learned classifier scoring difficulty, which anyone can train and anyone can copy. If your differentiation is the router, your differentiation has a half-life.

What does not commoditize is the judgment that turns a vague, sprawling goal into five milestones that cannot be faked. That is not a model you can distill. It is taste about where a task actually splits, what "done" means at each seam, and which parts carry the accumulated context that must not be severed. The router is downstream plumbing. The decomposition is the thing worth defending.

<figure>
        <svg viewbox="0 0 720 420" role="img" aria-label="Conceptual cost versus quality frontier: a single-model curve, a sidekick point up and to the left of it, and a predicted decomposition point further up and to the left.">
          <rect x="0" y="0" width="720" height="420" fill="#fffffb"></rect>
          <!-- axes -->
          <line x1="90" y1="360" x2="670" y2="360" stroke="rgba(0,0,0,0.35)" stroke-width="1.5"></line>
          <line x1="90" y1="360" x2="90" y2="40" stroke="rgba(0,0,0,0.35)" stroke-width="1.5"></line>
          <text x="380" y="398" font-family="Inter, sans-serif" font-size="14" fill="rgba(0,0,0,0.55)" text-anchor="middle">cost per task  →</text>
          <text x="46" y="200" font-family="Inter, sans-serif" font-size="14" fill="rgba(0,0,0,0.55)" text-anchor="middle" transform="rotate(-90 46 200)">quality  →</text>
          <!-- single-model curve -->
          <path d="M 150 330 C 300 300, 460 230, 610 180" fill="none" stroke="rgba(0,0,0,0.30)" stroke-width="2"></path>
          <circle cx="150" cy="330" r="4" fill="rgba(0,0,0,0.45)"></circle>
          <circle cx="380" cy="270" r="4" fill="rgba(0,0,0,0.45)"></circle>
          <circle cx="610" cy="180" r="4" fill="rgba(0,0,0,0.45)"></circle>
          <text x="620" y="176" font-family="Inter, sans-serif" font-size="13" fill="rgba(0,0,0,0.5)">single model</text>
          <!-- sidekick point -->
          <path d="M 300 200 L 300 200"></path>
          <circle cx="330" cy="205" r="7" fill="#2f5fd0"></circle>
          <text x="345" y="200" font-family="Inter, sans-serif" font-size="13" fill="#2f5fd0" font-weight="600">sidekick (measured)</text>
          <!-- decomposition point -->
          <circle cx="215" cy="150" r="7" fill="#1f8a4c"></circle>
          <text x="230" y="146" font-family="Inter, sans-serif" font-size="13" fill="#1f8a4c" font-weight="600">decomposition (predicted)</text>
          <!-- up-left arrow annotation -->
          <text x="150" y="70" font-family="Inter, sans-serif" font-size="13" fill="rgba(0,0,0,0.5)">better = up and to the left</text>
          <path d="M 250 78 C 210 95, 185 115, 170 138" fill="none" stroke="rgba(0,0,0,0.3)" stroke-width="1.3" stroke-dasharray="3 3"></path>
        </svg>
        <figcaption>
          Figure 1 (conceptual, not measured). On a cost versus quality frontier, up and to the left is better:
          more quality for less money. Fusion reports the sidekick sitting above the single-model curve. The
          claim this post makes is that explicit decomposition sits further up and to the left on plannable
          long-horizon tasks. The green point is a prediction, not a result. Section 8 is about turning it into
          a result.
        </figcaption>
      </figure>

## What I would measure next {#measure}

A thesis is cheap. The honest version of this argument is an experiment, and it does not require training a model or building a new environment. It is inference-only measurement on existing tasks:

- Take a set of plannable long-horizon tasks that already exist.
- Run two arms with the same cheap executor model: one with sidekick-style runtime delegation, one with explicit decomposition plus milestone gates.
- Measure de-confounded token cost (completion and new input, not re-sent history) and quality per task.
- Plot the cost versus quality frontier and see whether decomposition dominates.

Three things keep it honest. The sidekick baseline has to be faithful, not a strawman. The cost of the decomposition itself has to be counted in the decomposition arm's total, or the comparison is rigged. And the strongest result is not "mine is better," it is the crossover: decomposition dominates on plannable long-horizon work, reactive routing holds the unpredictable regime, and here is where the line falls. If that curve reproduces Cognition's own serial-debugging caveat as a measured effect, the benchmark is measuring the right thing.

That is the follow-up. For now the claim stands on its own logic: the router is the part you can copy, the decomposition is the part you cannot, and cheap delegation is what you get for free when you carve the task well, not the thing you should be optimizing for in the first place.

## References {#references}

1.  Cognition. "Devin Fusion." [cognition.com/blog/devin-fusion](https://cognition.com/blog/devin-fusion), 2026.
2.  Cognition. Launch thread, on non-uniform cost savings and serial debugging. [x.com/cognition](https://x.com/cognition/status/2076714968334913786), 2026.
3.  Aaron Levie. On the Fable-as-manager cost experiment and the harness as differentiation. [x.com/levie](https://x.com/levie/status/2076839463410671637), 2026.
4.  Ong et al. "RouteLLM: Learning to Route LLMs with Preference Data." LMSYS, [lmsys.org](https://www.lmsys.org/blog/2024-07-01-routellm/), 2024.
