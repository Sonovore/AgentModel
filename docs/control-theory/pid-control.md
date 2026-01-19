# PID Control for Agent Supervision

Exploring how PID (Proportional-Integral-Derivative) control theory applies to AI agent supervision - going beyond the surface understanding of "P for present, I for past, D for future."

## Background

| Aspect | Description |
|--------|-------------|
| **Origin** | Industrial process control, 1920s-1940s; theoretical foundations by Minorsky, Hazen, Ziegler-Nichols |
| **Domain** | Automatic control systems, process engineering, robotics |
| **Core Problem** | How to automatically adjust a control input to keep a system at a desired setpoint, despite disturbances |
| **Key Insight** | Three different types of response - to current error, to accumulated error history, and to error trend - serve complementary purposes and must be balanced |
| **Why It's Hard** | The three terms interact; tuning one affects the behavior of others; optimal settings depend on system dynamics |

The classic PID controller is everywhere: thermostats, cruise control, autopilots, industrial processes. Its ubiquity comes from a remarkable combination of simplicity (only three parameters) and effectiveness (handles most well-behaved systems). But that same simplicity makes it easy to misunderstand.

**The surface understanding:** "P responds to present error, I responds to accumulated past error, D responds to the rate of change (predicting future)."

**What that misses:** Why P alone can't eliminate steady-state error. Why I eliminates it but causes overshoot. Why D helps but amplifies noise. How the three terms interact to create behavior none exhibits alone. Why tuning is genuinely difficult. When PID fails entirely.

## The Control Loop

```
                          Disturbances
                               |
                               v
    +-------+     +------------+     +----------+     +--------+
    |       | u(t)|            | d(t)|          | y(t)|        |
r(t)|  PID  |---->|  Actuator  |---->|  Process |---->| Sensor |----+
--->| Cntrl |     |            |     |          |     |        |    |
    |       |     +------------+     +----------+     +--------+    |
    +-------+                                                       |
        ^                                                           |
        |                        e(t) = r(t) - y(t)                 |
        +-----------------------------------------------------------+
                              Error signal
```

| Symbol | Name | Description |
|--------|------|-------------|
| r(t) | Reference/Setpoint | What you want |
| y(t) | Process variable | What you measure |
| e(t) | Error | The gap: r(t) - y(t) |
| u(t) | Control output | What the controller commands |
| d(t) | Disturbances | External forces acting on the process |

**The controller's job:** Generate u(t) based on e(t) to drive e(t) toward zero.

## Key Concepts

### The Three Control Actions

#### Proportional Control (P)

The output is proportional to the current error:

```
P_output = Kp * e(t)
```

| Characteristic | Explanation |
|---------------|-------------|
| **Response** | Larger error = stronger correction |
| **Speed** | Fast initial response |
| **Steady-state** | Cannot eliminate steady-state error in many systems |
| **Stability** | Generally stable within limits |

**Why P alone isn't enough - the steady-state error problem:**

Consider a temperature control system. The setpoint is 70°F. At 60°F, the error is 10°F, so the heater runs at output = Kp * 10. As temperature rises to 68°F, error drops to 2°F, output drops to Kp * 2. At some point, the heat lost to the environment equals the heat from the reduced controller output - the system reaches equilibrium *before* hitting the setpoint.

The heater is working exactly hard enough to balance heat loss at, say, 68°F. To get to 70°F, the controller would need to work harder - but it's only producing output proportional to the 2°F error. This is **offset** or **droop**.

```
High Kp:
- Smaller steady-state error (but never zero)
- Faster response
- Risk of overshoot
- Risk of oscillation if Kp too high

Low Kp:
- Large steady-state error
- Sluggish response
- More stable but unresponsive
```

**The fundamental limitation:** P-only control treats each moment independently. It has no memory of the past and no anticipation of the future. This is both its simplicity and its limitation.

#### Integral Control (I)

The output is proportional to the accumulated error over time:

```
I_output = Ki * integral(e(t) dt)
```

| Characteristic | Explanation |
|---------------|-------------|
| **Response** | Grows as long as error persists |
| **Memory** | Accumulates past errors |
| **Steady-state** | Eliminates steady-state error (eventually) |
| **Stability** | Can cause overshoot and oscillation |

**How I eliminates steady-state error:**

Back to the temperature example. At 68°F with 2°F error, P-only output has stabilized. But with integral action, each moment at 68°F adds to the integral term. The integral keeps growing as long as any error exists. Eventually, the I-term grows large enough to provide the additional drive needed to reach 70°F.

Only when error reaches zero does the integral stop growing. This is why I-action *must* eliminate steady-state error - as long as there's any error, I keeps accumulating, eventually providing whatever output is needed.

**The overshoot problem:**

The integral has memory but no foresight. By the time the process reaches the setpoint, the integral has accumulated a significant value from all the past error. That accumulated value doesn't instantly disappear - it pushes the system past the setpoint.

```
Time →
Error:     [large error] → [decreasing] → [zero] → [overshoot!]
Integral:  [growing]     → [growing]    → [max]  → [slowly decreasing]
```

The system overshoots because the integral "remembers" all that past error and keeps pushing even after the target is reached.

**Integral time constant (Ti):**

Often expressed as Ki = Kp / Ti, where Ti is the integral time constant. Larger Ti = slower integral action = less overshoot but slower steady-state error elimination.

#### Derivative Control (D)

The output is proportional to the rate of change of error:

```
D_output = Kd * d(e(t))/dt
```

| Characteristic | Explanation |
|---------------|-------------|
| **Response** | Reacts to how fast error is changing |
| **Anticipation** | "Predictive" - sees trends before they fully develop |
| **Damping** | Opposes rapid changes, reduces overshoot |
| **Stability** | Can amplify noise |

**How D provides damping:**

When the process is approaching the setpoint quickly, the derivative of error is large and negative. The D-term produces a negative output (assuming positive Kd), which acts as a brake - reducing the control effort as the setpoint approaches.

This is why D is called "anticipatory" - it responds to the trend. If error is decreasing rapidly, D anticipates that continuing at this rate will cause overshoot and applies correction *before* the overshoot occurs.

```
Error approaching zero:
  de/dt is large and negative → D-output is negative → "brake"

Error increasing (moving away from setpoint):
  de/dt is positive → D-output is positive → "accelerate correction"
```

**The noise problem:**

Derivative amplifies high-frequency signals. Real measurements always have noise - small, rapid fluctuations. The derivative of noise is large (rapid changes in small signals). D-action can respond more to measurement noise than to actual process changes.

```
Actual signal:    ~~~~~~smooth trend~~~~~~
With noise:       ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
Derivative of noise: EXTREMELY NOISY - huge spikes
```

This is why many industrial controllers use PI instead of PID - the derivative term is often more trouble than it's worth.

### The Combined PID Output

```
u(t) = Kp * e(t) + Ki * integral(e(t) dt) + Kd * d(e(t))/dt
```

Or in the standard form:

```
u(t) = Kp * [e(t) + (1/Ti) * integral(e(t) dt) + Td * d(e(t))/dt]
```

where Ti is integral time and Td is derivative time.

**How the terms work together:**

| Situation | P Response | I Response | D Response | Combined |
|-----------|-----------|------------|------------|----------|
| Large error, steady | Large | Growing | Zero | Strong drive |
| Small error, steady | Small | Growing slowly | Zero | Persistent drive |
| Error decreasing fast | Decreasing | Still positive | Negative (brake) | Dampened approach |
| Error increasing fast | Increasing | Growing faster | Positive (accelerate) | Aggressive correction |
| Zero error, overshooting | Zero | Positive (past memory) | Negative (opposing trend) | D fights I |

**The interaction challenge:** This is why tuning is hard. Increasing Kp makes the system more responsive but also more prone to the oscillations that I can worsen. Increasing Ki eliminates offset faster but causes more overshoot. Increasing Kd dampens overshoot but amplifies noise. Each affects the others.

### Transfer Function Perspective

For those who want the mathematical intuition without the proofs:

**In the frequency domain (Laplace/s-domain):**

| Term | Transfer Function | Frequency Effect |
|------|------------------|------------------|
| P | Kp | Flat - same gain at all frequencies |
| I | Ki / s | High gain at low frequencies, decreasing with frequency |
| D | Kd * s | Low gain at low frequencies, increasing with frequency |

**What this means:**

- **I has high gain at low frequencies:** It strongly responds to slow-changing signals (like steady-state offset). But s is in the denominator, so it has infinite gain at DC (zero frequency) - that's why it eventually eliminates any constant error.

- **D has high gain at high frequencies:** It strongly responds to rapid changes. But this is also why it amplifies noise - noise is high-frequency.

- **P is frequency-independent:** It responds equally to slow and fast changes, which makes it a neutral middle ground.

**Phase effects:**

| Term | Phase Effect | What It Means |
|------|-------------|---------------|
| P | None | Output in phase with error |
| I | -90° lag | Output lags behind error (due to integration) |
| D | +90° lead | Output leads error (anticipatory) |

**Why this matters:** Phase determines whether your correction helps or hurts. If your correction arrives 180° out of phase (completely opposite), you're amplifying the error instead of correcting it. I-action adds lag (bad for stability), D-action adds lead (good for stability). This is why D improves stability margins - it compensates for the phase lag from I and from the process itself.

### Common Problems and Solutions

#### Integral Windup

**What it is:** When the control output saturates (hits its physical limits), the integral term keeps accumulating because error persists, but the extra integration can't produce any more output.

```
Scenario: Large setpoint change

Time 1: Error = 50, Integral growing, Output at max (saturated)
Time 2: Error = 40, Integral still growing (error exists!), Output still maxed
Time 3: Error = 20, Integral HUGE, Output still maxed
Time 4: Error = 0, but Integral is enormous
Time 5: Output finally comes off max, but Integral drives massive overshoot
```

The integral "wound up" during saturation. When the constraint is removed, all that accumulated integral produces huge overshoot.

**Anti-windup strategies:**

| Strategy | Mechanism |
|----------|-----------|
| **Conditional integration** | Stop integrating when output is saturated |
| **Back-calculation** | When saturated, reduce integral to match actual output |
| **Clamping** | Limit the integral term to a maximum value |
| **Integrator leakage** | Integral slowly decays toward zero |

Most practical implementations use conditional integration or back-calculation. The key insight: don't accumulate integral when you can't act on it.

#### Derivative Kick

**What it is:** When the setpoint changes suddenly, the derivative of error is instantaneously huge (step change = infinite derivative in theory). This causes a spike in the D-output.

```
Setpoint:   ---[step change]---
d(error)/dt:    [huge spike!]
D-output:       [huge spike!]
```

This spike kicks the actuator hard - potentially damaging equipment or causing instability.

**Solution - Derivative on Measurement:**

Instead of calculating derivative of error, calculate derivative of the process variable (measurement) only:

```
Standard:  Kd * d(e)/dt = Kd * d(r - y)/dt = Kd * (dr/dt - dy/dt)
On PV:     -Kd * dy/dt  (ignore setpoint changes)
```

The measurement changes smoothly even when the setpoint jumps. This eliminates derivative kick while preserving the damping benefit during normal operation.

Many industrial controllers use this by default: "Derivative on PV."

#### Noise Sensitivity

**The problem:** D amplifies high-frequency noise, causing control output to chatter.

**Solutions:**

| Approach | Trade-off |
|----------|-----------|
| **Low-pass filter on derivative** | Reduces noise but adds lag, reducing D effectiveness |
| **Reduce Kd** | Less noise amplification but less damping |
| **Use PI only** | No noise from D but lose anticipatory action |
| **Filter measurement before derivative** | Adds delay to derivative response |

The filtered derivative is common:

```
D_filtered = Kd * s / (1 + s*Tf)  where Tf is filter time constant
```

This limits the high-frequency gain of D while preserving its effect at moderate frequencies.

## Tuning Methods

### Ziegler-Nichols Ultimate Gain Method

The classic empirical tuning method from 1942. Still widely used.

**Procedure:**

1. Set Ki = 0, Kd = 0 (P-only control)
2. Increase Kp until the system oscillates continuously at constant amplitude
3. Record Ku (ultimate gain) and Tu (ultimate period of oscillation)
4. Apply the formulas:

| Controller | Kp | Ti | Td |
|-----------|-----|-----|-----|
| P | 0.5 * Ku | - | - |
| PI | 0.45 * Ku | Tu / 1.2 | - |
| PID | 0.6 * Ku | Tu / 2 | Tu / 8 |

**Why it works:** The ultimate gain puts the system on the edge of instability. Backing off from that edge (0.5-0.6 of Ku) provides a stability margin while maintaining good response.

**Limitations:**
- Requires bringing the system to oscillation (not always safe or desirable)
- Produces aggressive tuning with significant overshoot (~25%)
- Assumes linear system behavior
- Doesn't account for noise

### Ziegler-Nichols Step Response Method

For open-loop systems, based on the response to a step input.

**Procedure:**

1. With controller in manual mode, apply a step change to the output
2. Record the response curve
3. Identify:
   - L = apparent dead time (delay before response begins)
   - T = time constant (time to reach 63.2% of final change)
   - K = process gain (total change in PV / change in output)

4. Apply formulas:

| Controller | Kp | Ti | Td |
|-----------|-----|-----|-----|
| P | T / (K * L) | - | - |
| PI | 0.9 * T / (K * L) | 3.3 * L | - |
| PID | 1.2 * T / (K * L) | 2 * L | 0.5 * L |

**Better for:** Systems where inducing oscillation is risky or impractical.

### Cohen-Coon Method

A refinement of step-response tuning that accounts for process dead time more accurately.

Uses the same L, T, K measurements but with different formulas that produce less aggressive (more conservative) tuning for systems with significant dead time.

**Key insight:** Dead time is the enemy of control. The longer the delay between action and effect, the more conservative the tuning must be. Cohen-Coon explicitly accounts for the L/T ratio.

### Manual Tuning Heuristics

**The practical approach for most situations:**

1. **Start with P only**
   - Set Ki = 0, Kd = 0
   - Increase Kp until response is reasonably fast but not oscillating
   - Accept the steady-state offset for now

2. **Add Integral**
   - Increase Ki slowly until steady-state error is eliminated
   - Expect some overshoot - that's normal
   - If oscillation starts, reduce Ki

3. **Add Derivative (if needed)**
   - Only if overshoot is unacceptable
   - Start with Kd very small
   - Increase until overshoot is reduced
   - If output becomes noisy, reduce Kd or filter

4. **Iterate**
   - Readjust Kp based on new I and D settings
   - Fine-tune for the specific performance requirement

**Rules of thumb:**

| Goal | Adjust |
|------|--------|
| Faster response | Increase Kp |
| Less steady-state error | Increase Ki |
| Less overshoot | Decrease Ki or Increase Kd |
| Less oscillation | Decrease Kp, Decrease Ki |
| Less noise response | Decrease Kd, Add filter |

**The fundamental trade-off:** Speed vs. stability. Fast response requires high gain, but high gain risks oscillation. Every tuning is a compromise.

### Cascade Control

**What it is:** Nested control loops where the outer loop's output is the setpoint for the inner loop.

```
          Outer Loop                    Inner Loop
    +-----------------+            +-----------------+
    |                 |  SP_inner  |                 |
SP_outer → PID_outer ───────────────→ PID_inner ────────→ Process ─┐
    |                 |            |                 |              |
    +-----------------+            +-----------------+              |
          ↑                              ↑                          |
          |         PV_outer             |    PV_inner              |
          +──────────────────────────────+──────────────────────────+
```

**Example:** Jacket-cooled reactor
- Outer loop: Temperature of reactor contents (slow)
- Inner loop: Temperature of cooling jacket (fast)
- The outer loop says "I need the jacket cooler" → inner loop makes it so quickly

**Why cascade helps:**
- Inner loop rejects disturbances before they affect the outer variable
- Inner loop is faster, providing quick response to inner disturbances
- Outer loop only deals with what the inner loop can't handle

**Tuning cascade:**
1. Tune inner loop first (with outer loop in manual)
2. Tune outer loop with inner loop in auto
3. Inner loop must be 3-5x faster than outer loop

## When PID Fails

### Nonlinear Systems

PID assumes linear system behavior - output proportional to input. Many real systems are nonlinear:

| Nonlinearity | Example | Problem |
|--------------|---------|---------|
| **Saturation** | Valve fully open/closed | Can't increase control further |
| **Dead band** | Stiction in valve | No response to small signals |
| **Hysteresis** | Backlash in gears | Different response up vs down |
| **Variable gain** | Heat transfer at different temperatures | Tuning that works at one point fails at another |

**Approaches:**
- Gain scheduling: Different PID parameters for different operating regions
- Adaptive control: Parameters adjust automatically
- Nonlinear control: More sophisticated algorithms

### Large Delays (Dead Time)

When the delay between action and effect is large relative to the system time constant, PID struggles.

**The problem:** By the time you see the effect of your control action, conditions have changed. The controller keeps acting based on old information.

**Rule of thumb:** If dead time > 0.5 * time constant, PID alone will struggle. Consider:
- Smith Predictor: Internal model that predicts the delayed effect
- Model Predictive Control: Plans actions accounting for delay
- Very conservative tuning (accept slow response)

### Oscillatory/Underdamped Processes

Processes with natural oscillations are hard for PID because the controller can synchronize with and amplify the oscillations.

### Integrating Processes

Processes that integrate the input (like level in a tank being filled) are tricky because they don't naturally settle to a steady state. I-action can cause instability because the process is already "integrating."

### Multiple Interacting Loops

When multiple controlled variables affect each other, tuning one loop affects the others. MIMO (multiple-input multiple-output) systems often need more sophisticated approaches than multiple independent PID loops.

## Application to AI Agent Supervision

### The Supervision Control Loop

```
    +------------+      +-----------+      +--------+
    |            | inst |           | resp |        |
Goal| Supervisor |----->|   Agent   |----->| Output |----+
--->|   (PID)    |      |           |      |Measure |    |
    |            |      +-----------+      +--------+    |
    +------------+                                       |
          ↑                                              |
          |              Error = Goal - Output           |
          +----------------------------------------------+
```

| PID Concept | Agent Supervision Analog |
|-------------|-------------------------|
| **Setpoint** | Expected output quality, task completion criteria |
| **Process variable** | Observed agent output quality |
| **Error** | Gap between expected and actual output |
| **Control output** | Supervision intensity: instruction detail, verification level, autonomy constraints |
| **Disturbances** | Novel tasks, ambiguous requirements, agent capability changes |

### Proportional Response in Supervision

**What it means:** Correction proportional to current error magnitude.

| Error Magnitude | Proportional Response |
|-----------------|----------------------|
| Small deviation from expected | Minor instruction clarification |
| Moderate error | More specific guidance, increased verification |
| Large error | Detailed step-by-step instructions, heavy oversight |
| Critical failure | Complete task takeover, stop agent |

**The offset problem appears here too:** P-only supervision accepts persistent small errors. If you only respond proportionally to current mistakes, you'll never address systematic issues - the agent will settle to "good enough" with consistent minor flaws.

**Practical example:**
- Agent makes 10% errors on code reviews
- You provide correction proportional to each error
- Agent improves somewhat but stabilizes at 3% error rate
- With P-only, you accept that floor because small errors get small corrections

### Integral Response in Supervision

**What it means:** Accumulated history of errors gets increasing attention.

| Pattern | Integral Response |
|---------|-------------------|
| Single error, not repeated | No integral accumulation - handled by P |
| Same error type recurring | Integral grows - more fundamental intervention |
| Persistent underperformance | Large integral - systemic change to instructions/approach |
| Previously reliable, sudden errors | Integral starts fresh - investigate cause |

**Why I eliminates systematic error:** If an agent consistently makes the same type of mistake, P-only supervision treats each instance independently. I-action says: "We've corrected this before. Multiple times. The fact that it keeps happening means we need something more than per-instance correction."

**The I-action might be:**
- Rewriting base instructions
- Adding examples of the problematic case
- Implementing structural safeguards
- Removing the agent from this task type entirely

**Overshoot in supervision:** After detecting a pattern of errors, you implement heavy safeguards. The agent's performance improves, but now the safeguards are excessive - they slow down the agent on tasks it handles fine. The "integral" accumulated during the problem period causes over-correction.

### Derivative Response in Supervision

**What it means:** Responding to the rate of change of error - catching problems early.

| Pattern | Derivative Response |
|---------|---------------------|
| Sudden increase in error rate | Intervene before pattern establishes |
| Error rate decreasing | Ease back on intensive supervision |
| Rapid oscillation in quality | Dampen - don't overreact to each swing |
| Gradual drift | D misses this (slow change = small derivative) |

**D-action provides early warning:** If an agent that was making 1% errors starts making 3%, then 5%, then 8% - the derivative (rate of increase) triggers intervention before the absolute level reaches crisis.

Without D, you wait until absolute performance crosses a threshold. With D, you respond to the trend.

**Noise sensitivity in supervision:** If you track error rate over short intervals, random variation looks like trend. D-heavy supervision reacts to noise - "Errors up 50% this hour! Intervene!" when it's just statistical fluctuation.

**Solution:** Filter the derivative - look at trends over longer periods, smooth the measurement before differentiating.

### Integral Windup in Supervision

**The problem:** During periods when you cannot correct the agent (it's doing a task autonomously, you're not available, the errors are only discovered later), the "integral" keeps accumulating.

**Scenario:**
1. Agent runs autonomously overnight
2. Makes consistent errors throughout (but you can't see them)
3. In the morning, you discover 50 flawed outputs
4. Integral has "wound up" - you now feel you need massive intervention

**The overcorrection:** You implement strict controls based on accumulated evidence. But the agent's current capability might be fine - the problems were from a specific context. The wound-up integral causes you to treat the agent as fundamentally broken when it isn't.

**Anti-windup for supervision:**
- Don't accumulate "supervision debt" during unobserved periods
- Evaluate current capability separately from historical performance
- Have a "forgiveness" mechanism - past errors don't compound forever
- Reset integral after major instruction changes (new baseline)

### Derivative Kick in Supervision

**The problem:** When goals change suddenly (new project, new requirements), the "derivative" of error is instantaneously huge.

**Scenario:**
1. Agent was doing task A well (low error)
2. Switch to completely different task B
3. Initial errors on B are expected (new territory)
4. But the derivative sees: "Error just jumped massively!"

**The overreaction:** You intervene heavily because of the sudden change in error, when actually it's just transitioning to a new domain where some initial errors are normal.

**Solution - Derivative on measurement:**
- Track the derivative of agent performance, not derivative of error-from-new-goal
- When goals change, don't let the goal-change trigger derivative response
- Recognize that goal changes aren't agent failures

### Tuning Supervision Intensity

**The parallels to PID tuning:**

| PID Tuning Concept | Supervision Tuning Analog |
|-------------------|--------------------------|
| High Kp | React strongly to every error |
| Low Kp | Accept some errors as normal variance |
| High Ki | Small persistent issues get escalating attention |
| Low Ki | Don't compound historical errors |
| High Kd | Respond strongly to trend changes |
| Low Kd | Don't overreact to fluctuations |

**Starting point heuristics:**

1. **Start with proportional response only**
   - React to current errors proportionally
   - Accept that persistent small errors may remain
   - This is stable but may not be satisfactory

2. **Add integral action**
   - Track recurring patterns
   - Address systematic issues with larger interventions
   - Watch for over-correction after problems are fixed

3. **Add derivative action (carefully)**
   - Respond to trends, not just absolute levels
   - Filter to avoid reacting to noise
   - Particularly useful for catching regressions early

**The fundamental tuning question:** How quickly should supervision adjust?

| Too Fast (high gain) | Too Slow (low gain) |
|---------------------|---------------------|
| Micromanagement | Problems persist too long |
| Agent can't learn from mistakes | Systematic errors compound |
| Supervisor burns out | Trust isn't calibrated |
| Oscillation between over/under-trust | Drift from acceptable |

### Cascade Control in Supervision

**What it means:** Nested supervision loops where outer goals set targets for inner goals.

```
Outer Loop: Project success
    ↓
Inner Loop: Task quality
    ↓
Innermost Loop: Step correctness
```

**Example:**
- Outer loop: "Complete feature X successfully" - checked at project level
- Middle loop: "Each task should produce correct output" - checked per task
- Inner loop: "Each step should be reasonable" - checked frequently

**Why cascade helps:**
- Inner loop catches small problems before they cascade
- Outer loop ensures local optimization serves global goals
- Problems are addressed at the appropriate level

**Tuning cascade supervision:**
1. Inner loops should be faster (more frequent checks)
2. Outer loops set direction but don't micromanage
3. Inner loop failures don't automatically escalate unless they represent outer loop impact

### When PID Supervision Fails

| Failure Mode | What It Looks Like | What to Do Instead |
|--------------|-------------------|-------------------|
| **Nonlinear capability** | Agent is great at A, terrible at B | Different tuning per domain; route tasks appropriately |
| **Large delay** | Errors only discovered days later | Don't over-integrate delayed feedback; separate current capability from historical |
| **Multiple interacting agents** | Correcting one affects others | Need coordinated multi-agent supervision, not independent PID per agent |
| **Unpredictable goals** | What "success" means keeps changing | PID assumes stable setpoint; need adaptive goal specification |
| **Binary outcomes** | Either success or failure, no gradation | PID needs continuous error signal; consider different framework |

## Practical Implications

### For Human-Agent Supervision

1. **Recognize which term you're applying**
   - Are you correcting the current output? (P)
   - Are you addressing a pattern? (I)
   - Are you responding to a trend? (D)
   - Appropriate response depends on which applies

2. **Watch for windup**
   - Don't let past failures compound indefinitely
   - After major changes, reset your baseline
   - Unobserved periods shouldn't accumulate supervision debt

3. **Filter before differentiating**
   - One bad output isn't a trend
   - Smooth short-term variation before reacting to "trends"
   - D without filtering causes exhausting oscillation

4. **Tune iteratively**
   - Start with proportional response to individual errors
   - Add pattern recognition (integral) if systematic issues persist
   - Add trend detection (derivative) if early warning is valuable
   - Adjust based on observed supervision dynamics

### For Automated Supervision Systems

1. **Implement anti-windup**
   - Conditional integration: don't accumulate error during periods when correction isn't possible
   - Back-calculation: when saturation prevents action, reduce integral
   - Leaky integration: gradual decay of historical weight

2. **Use derivative on measurement**
   - Don't let setpoint changes trigger derivative response
   - Track trend in actual performance, not trend in gap-from-new-goal

3. **Consider cascade architecture**
   - Inner loops for tactical corrections (faster)
   - Outer loops for strategic direction (slower)
   - Match loop speed to the timescale of the thing being controlled

4. **Acknowledge nonlinearity**
   - Agent capability isn't linear
   - Consider gain scheduling (different parameters for different regions)
   - Adaptive tuning if the system characteristics change

### Tuning Guidance

| Situation | P | I | D | Rationale |
|-----------|---|---|---|-----------|
| New agent, unknown capability | Low | Low | Low | Conservative; learn before correcting strongly |
| Proven agent, routine task | Low | Medium | Low | Trust established; integral catches drift |
| Critical task, trusted agent | Medium | Low | Medium | React to current issues; watch for regression |
| Problem agent, recovery phase | High | High | Medium | Active correction; address patterns; watch trends |
| Autonomous operation | Low | Low | Low | Can't correct in real-time; don't accumulate debt |

## Key Insight

**The surface understanding** - "P for present, I for past, D for future" - **misses the interaction dynamics and failure modes.**

The real insight is that supervision (like process control) involves three fundamentally different types of response that must be balanced:

1. **Immediate correction** (P): Respond to current deviation proportionally. Stable but accepts persistent offset.

2. **Historical pattern response** (I): Accumulated evidence demands accumulated intervention. Eliminates systematic errors but causes overshoot and windup.

3. **Trend response** (D): Anticipate based on rate of change. Provides early warning but amplifies noise.

**Each has characteristic failure modes:**
- P alone: Accepts persistent errors
- I alone: Massive overshoot
- D alone: Noise-driven chaos

**The combination works because each compensates for the others' weaknesses.** But the combination is also fragile - it requires tuning, and poor tuning produces worse behavior than any single term alone.

**The deepest insight:** PID works because it encodes a particular structure of response to error. That structure - proportional to magnitude, integral over history, derivative over trend - captures something fundamental about how corrective systems can be stable. The same structure appears in supervision because supervision is also corrective feedback.

**But PID also fails in characteristic ways:** nonlinear systems, large delays, multiple interacting loops. These failures map to supervision failures too. Recognizing when you're in a PID-failure-mode is as important as applying PID appropriately.

Supervision isn't just "more correction = better." It's about the right type and amount of correction, applied in a way that converges rather than oscillates, adapts rather than winds up, and responds to signal rather than noise.

## Open Questions

1. **What's the "sample rate" for supervision?** PID requires regular measurement. How often should you evaluate agent performance, and does irregular sampling break the mathematics?

2. **Can you measure "error" in supervision?** PID needs a numerical error signal. Agent output quality is often categorical or multi-dimensional. How do you reduce it to controllable error?

3. **What's the "actuator" in supervision?** PID assumes continuous control output. Supervision interventions are often discrete (change instructions, pause agent, add verification). How do continuous PID concepts map to discrete actions?

4. **Is agent behavior linear?** PID assumes linear systems. Agent response to supervision changes is almost certainly nonlinear. How much does that matter?

5. **What's the "time constant" of an agent?** How quickly does an agent respond to instruction changes? This determines appropriate tuning.

6. **Multi-agent supervision:** When multiple agents work together, correcting one affects others. Is independent PID per agent appropriate, or do you need MIMO control concepts?

## Status

**Phase:** Deep exploration complete. Core PID concepts mapped to supervision with attention to failure modes and tuning. Key insight is that supervision, like process control, involves balancing three types of response - proportional to current error, integral over history, and derivative over trend - and that each has characteristic failure modes that must be managed. The interaction between terms is what makes PID both powerful and difficult to tune.

**Next:** Implement supervision system with explicit P/I/D-style components and observe whether the tuning heuristics transfer.
