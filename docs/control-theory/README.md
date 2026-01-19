# Control Theory

Mental models from control systems engineering applied to AI agent supervision.

## Purpose

Control theory provides mathematical frameworks for understanding how systems respond to inputs, maintain stability, and achieve desired states through feedback. These concepts map directly to agent supervision: how much oversight, how fast to adjust, when systems become unstable.

## Status

**Current phase:** Identification - listing relevant models, not yet researching.

## Mental Models to Explore

### Foundational Concepts

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Feedback Loops | Classical control | Positive vs negative feedback in supervision |
| Open vs Closed Loop | Classical control | When to monitor vs trust |
| Stability | Lyapunov, others | When does supervision cause oscillation vs convergence? |
| Controllability | Kalman | Can you actually steer the agent to desired states? |
| Observability | Kalman | Can you infer agent state from outputs? |

### Response Characteristics

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| PID Control | Industrial control | Proportional/Integral/Derivative response to errors |
| Gain & Bandwidth | Bode analysis | How much correction, how fast? |
| Overshoot & Settling Time | Step response | Supervision that over-corrects vs under-corrects |
| Dead Time / Lag | Process control | Delay between action and observable effect |
| Hysteresis | Nonlinear systems | Different thresholds for increasing vs decreasing oversight |

### System Dynamics

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Transfer Functions | Laplace domain | Input-output relationships without internal details |
| State Space Models | Modern control | Full internal state representation |
| Feedforward Control | Anticipatory control | Acting before errors occur |
| Cascade Control | Process control | Nested control loops (supervisor supervising supervisor) |
| Model Predictive Control | MPC | Planning based on predicted future states |

### Robustness & Limits

| Model | Source | Why It Might Apply |
|-------|--------|-------------------|
| Gain Margin / Phase Margin | Stability analysis | How close to instability? |
| Robust Control | H-infinity | Performance despite uncertainty |
| Adaptive Control | Self-tuning | Adjusting parameters as system changes |
| Saturation & Windup | Actuator limits | What happens when corrections hit limits? |

## Priority Assessment

| Model | Relevance | Complexity | Suggested Priority |
|-------|-----------|------------|-------------------|
| Feedback Loops | Very High | Low | 1 |
| PID Control | High | Medium | 1 |
| Stability | High | Medium | 1 |
| Observability/Controllability | High | Medium | 2 |
| Hysteresis | Medium | Low | 2 |
| Cascade Control | Medium | Medium | 2 |
| Adaptive Control | High | High | 3 |
| Model Predictive Control | Medium | High | 3 |

## Key Questions

1. What's the "transfer function" of an LLM agent? (Input prompt → output action)
2. How do we measure stability in agent supervision? What are the oscillation modes?
3. What's the equivalent of "gain" in supervision intensity?
4. When does tight feedback cause instability rather than convergence?

## Related Directories

- [Management](../management/) - Human supervision patterns
- [Distributed Systems](../distributed-systems/) - Multi-agent coordination
- [Safety Engineering](../safety-engineering/) - Failure handling
