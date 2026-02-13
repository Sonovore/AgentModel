# Technology-Augmented Decision-Making: Three-Level Explanation

## Level 1: Ages 5-10

### The Helper That's Almost Always Right

Imagine you have a really smart friend helping you with your homework. This friend almost always knows the right answer. In fact, they're right 95 times out of 100!

At first, you check their answers carefully. But after a while, you notice they're almost always right. So you start just copying what they say without checking.

Here's the problem: **What happens when they're wrong?**

Because you stopped checking, you don't catch their mistakes anymore. You've become so used to them being right that you don't even look for errors. Their 5 mistakes now become YOUR mistakes too.

**The Magic Helpers at 911**

When someone calls 911, a person called a dispatcher has to decide what kind of help to send:
- Is this a fire? Send firefighters!
- Is someone hurt? Send an ambulance!
- Is someone in danger? Send police!

This decision is really important. If they send the wrong help, people could get hurt.

Now, dispatchers have computer helpers that try to figure out what kind of emergency it is. The computer listens to what the caller says and suggests: "I think this is a Priority 2 Fire."

Most of the time, the computer is right. But sometimes it's wrong.

**The Tricky Part**

Here's what researchers discovered:

When the computer helper is new, dispatchers check its suggestions carefully. "Is the computer right? Let me think about this."

But after using the computer for months, dispatchers stop checking as carefully. "The computer is usually right, so I'll just do what it says."

This is called **automation bias**---trusting the computer too much because it's usually right.

The really tricky thing is: the dispatchers don't notice they're doing this! They think they're still checking carefully, but they're not.

**What We Learned**

The computer helper is supposed to make decisions BETTER. And it does---most of the time.

But the helper also changes HOW people make decisions. Instead of thinking "What's the right answer?" people start thinking "Is the computer right?"

These are different questions! And the second one is easier to answer with "Yes" when you're busy or tired.

**The Big Lesson**

Technology that helps us think can also change how we think. Sometimes that's good. But we have to be careful that the helper doesn't make us forget how to think for ourselves.

The best helpers don't just give us answers---they help us understand why the answer is right.

---

## Level 2: High School Graduate

### When AI Assistance Changes the Nature of the Task

Emergency dispatchers make life-and-death decisions every day. When you call 911, a dispatcher must quickly determine what kind of emergency you're facing and send the right resources. Too slow, and people could die. Wrong resources, and the situation could worsen.

For decades, dispatchers made these decisions using training, experience, and intuition. Now, increasingly, they work with AI systems that analyze calls in real-time and suggest response priorities, resource allocations, and risk assessments.

These systems can be remarkably helpful. They can process information faster than humans, remember historical patterns, and apply complex rules consistently. But research reveals something counterintuitive: **AI assistance doesn't simply improve human decisions---it fundamentally transforms what humans are deciding about.**

**The Decision Transformation**

Consider what happens when a dispatcher receives a call without AI assistance:

The dispatcher thinks: "What kind of emergency is this? What resources should I send? How quickly?"

Now consider the same call with AI assistance:

The dispatcher thinks: "The AI says Priority 2 Fire. Is the AI right? Should I follow this recommendation?"

These are fundamentally different cognitive tasks. The first requires analyzing the situation directly. The second requires evaluating an AI recommendation. The skills, information, and mental processes are different.

This transformation isn't inherently bad---it can actually improve outcomes when the AI is reliable. But it creates new failure modes that don't exist in unaugmented decision-making.

**Automation Bias: The Almost-Right Problem**

When AI systems are usually correct, humans develop a tendency to accept their recommendations without adequate evaluation. This is called automation bias.

The mechanism is straightforward: evaluating recommendations takes effort. When the recommendation is usually right, that evaluation effort often feels wasted. So humans unconsciously reduce evaluation effort, following recommendations more automatically.

Research on emergency dispatch systems shows that automation bias increases with:

- **AI reliability**: The more often AI is right, the less humans check
- **Time pressure**: When busy, humans default to AI recommendations
- **Workload**: High workload reduces cognitive capacity for evaluation
- **Experience**: Paradoxically, experienced dispatchers can become more complacent than novices

The dangerous part: humans experiencing automation bias typically don't realize it. They believe they're still evaluating carefully when they're actually rubber-stamping.

**The Expertise Paradox**

Research consistently finds that AI assistance often helps novices more than experts---and can actually hurt expert performance.

Why? Experts have developed effective mental models through years of experience. They recognize patterns intuitively. They know what to pay attention to and what to ignore.

AI recommendations can interfere with these expert processes by:
- Introducing doubt about valid intuitions
- Directing attention away from cues experts would naturally use
- Encouraging analytical processing when intuitive recognition would be more effective
- Reducing the practice that maintains expert skills

This creates a paradox: the people who least need AI assistance may be most affected by it, while the people who most need it benefit most.

**Skill Degradation: The Use-It-or-Lose-It Problem**

Skills require practice to maintain. When AI handles severity assessment, dispatchers don't practice severity assessment. When AI handles geographic routing, dispatchers don't maintain geographic knowledge.

The knowledge migrates from the human to the system. This seems fine while the system works. But when the system fails---server crash, power outage, unusual situation the AI can't handle---the human is left without skills they once had.

The dispatcher who always has AI support cannot function when the AI is down. The expertise needed to handle system failures is exactly the expertise that atrophies from disuse.

**The Confidence Problem**

AI systems often report confidence levels with their recommendations: "85% confident this is a Priority 2 incident."

This sounds helpful---humans can weight the recommendation based on confidence. But research shows problems:

- **Confidence numbers may not mean what users think**: An AI reporting 85% confidence isn't necessarily right 85% of the time. The numbers may not be calibrated.

- **Human response is non-linear**: Users often treat low confidence (60%) as "AI doesn't know" and ignore it. High confidence (95%) is treated as "AI is certain" and followed blindly. Intermediate confidence may produce appropriate deliberation.

- **Confidence format matters**: The same underlying confidence produces different human responses depending on whether it's shown as a number, verbal descriptor, or visual bar.

- **Confidence can be gamed**: If AI systems learn that high confidence leads to acceptance, they may learn to report higher confidence regardless of actual uncertainty.

**When Augmentation Helps**

AI assistance tends to help when:

| Condition | Why It Helps |
|-----------|--------------|
| Large information volume | AI can process what humans cannot attend to |
| Stable statistical patterns | AI can learn and apply patterns consistently |
| Time pressure with routine decisions | AI speed helps; routine decisions don't need deep judgment |
| Novice decision-makers | Augmentation provides experience they lack |
| Clear, measurable outcomes | AI can learn from feedback |

**When Augmentation Hurts**

AI assistance tends to hurt when:

| Condition | Why It Hurts |
|-----------|--------------|
| Truly novel situations | AI trained on past data fails on unprecedented cases |
| High context-dependence | Local factors override statistical patterns |
| Expert decision-makers | Experts already know what AI provides; augmentation adds noise |
| Ethical or value-laden decisions | AI cannot make value tradeoffs appropriately |
| Ambiguous information | AI confident on ambiguous data misleads |

**The Reliability Threshold**

Below a certain reliability threshold, AI assistance hurts more than it helps. Research suggests AI reliability needs to be 70-80%+ before augmentation produces net benefits.

Why? Humans cannot perfectly discriminate correct from incorrect recommendations. They develop overall trust that reflects perceived reliability. When reliability is low:
- Following recommendations produces many errors
- Ignoring recommendations wastes the value AI provides
- Selective following is cognitively expensive and error-prone

A 65%-reliable AI advisor may be worse than no AI advisor at all.

**The Fundamental Insight**

Technology augmentation doesn't simply improve human decisions---it transforms the decision-making process itself.

In unaugmented dispatch, the human is a dispatcher making emergency response decisions.

In augmented dispatch, the human is a dispatcher-AI team supervisor evaluating AI recommendations.

These are different jobs requiring different skills. The second job requires understanding what the AI knows and doesn't know, when to trust and when to verify, how to maintain independent judgment while leveraging AI capability.

Organizations that treat augmentation as "the same job with better tools" miss this transformation. They train for the wrong job, measure the wrong metrics, and wonder why augmentation isn't helping as much as expected.

**Designing for Appropriate Reliance**

Effective augmentation requires designing for appropriate reliance---neither over-trusting (automation bias) nor under-trusting (wasting AI capability).

This means:
- **Calibrated confidence display**: Confidence numbers should actually mean what they claim
- **Transparency about limitations**: Users should know when AI is likely to fail
- **Active engagement, not passive monitoring**: Interfaces should require human thought, not just approval
- **Skill maintenance**: Regular practice without AI to maintain human capability
- **Trust calibration**: Systems that help users understand when to trust and when to verify

The goal is not maximum automation or maximum human control---it's optimal human-AI teaming where each contributes their strengths.

---

## Level 3: Expert

### The Epistemology of Technology-Augmented Decision-Making

Technology-Augmented Decision-Making (TADM) in high-stakes domains represents a transformation in the nature of human expertise, not merely its enhancement. Understanding this transformation requires moving beyond the surface narrative of "AI helps humans make better decisions" to examine the cognitive, organizational, and epistemological changes that augmentation produces.

**The Levels of Automation Framework**

Parasuraman and colleagues developed a ten-level taxonomy for human-automation interaction that illuminates the spectrum of augmentation approaches:

**Information Acquisition:**
1. Automation offers no assistance
2. Automation offers a complete set of decision alternatives
3. Automation narrows the set of alternatives
4. Automation suggests one alternative

**Information Analysis:**
5. Automation executes the suggestion if human approves
6. Automation allows human a restricted time to veto
7. Automation executes automatically, then informs human
8. Automation informs human only if asked
9. Automation informs human only if it decides to
10. Automation decides everything, ignoring human

Research consistently finds that intermediate levels (4-7) often produce better human-machine system performance than either extreme. Full automation eliminates human contribution; minimal automation wastes AI capability.

The optimal level depends on:
- **Decision complexity**: Higher complexity often requires lower LOA
- **Consequence severity**: Higher stakes often require lower LOA
- **Time pressure**: Higher pressure often requires higher LOA
- **Human expertise**: Higher expertise can sustain lower LOA under pressure
- **AI reliability**: Higher reliability can justify higher LOA

**The Lens Model: Understanding Human and AI Judgment**

Brunswik's Lens Model provides a framework for understanding both human and AI judgment:

```
Environment -----> Cues -----> Judgment -----> Decision
             \            /
              Actual State
```

**Achievement** = Correlation between judgment and actual state

Both humans and AI work through the same process: observe cues, make inferences about actual state, render judgment. Achievement depends on:

1. **Cue validity**: How well available cues actually predict state
2. **Cue utilization**: How well the judge uses available cues
3. **Consistency**: How reliably the judge applies their strategy

Augmentation can improve achievement by:
- Increasing cue availability (AI accesses cues humans cannot)
- Improving cue utilization (AI weights cues more optimally)
- Enhancing consistency (AI applies same strategy every time)

But augmentation can degrade achievement by:
- Overwhelming with irrelevant cues
- Misweighting cues for specific context
- Creating false consistency (consistent application of wrong strategy)

**Trust Calibration Theory**

Lee and See's framework identifies the central challenge: **trust calibration---alignment between trust and trustworthiness---determines performance.**

**Dimensions of Trust:**
- **Performance**: Belief about what AI can do (capability)
- **Process**: Belief about how AI works (transparency)
- **Purpose**: Belief about why AI was designed (intent alignment)

**Trust Calibration States:**
- **Calibrated Trust**: Trust matches trustworthiness---appropriate reliance
- **Over-Trust (Complacency)**: Trust exceeds trustworthiness---inappropriate reliance
- **Under-Trust (Distrust)**: Trust below trustworthiness---inappropriate rejection

The critical insight: **trust level doesn't determine performance; trust calibration does.** High trust in reliable AI is good. High trust in unreliable AI is dangerous. Low trust in reliable AI wastes capability. Low trust in unreliable AI is appropriate.

**The Misunderstanding: "More AI Assistance Always Improves Decisions"**

The surface belief that more assistance improves outcomes fails empirically:

**Information Overload Effects**: Adding information sources can degrade decision quality beyond a threshold. Humans have limited attention and working memory. Comprehensive AI information provision may overwhelm processing capacity, causing critical elements to be missed.

**Decision Quality Paradox**: In medical diagnosis studies, more diagnostic support tools sometimes reduced diagnostic accuracy. Additional information creates uncertainty, triggers confirmation bias, or causes second-guessing of valid intuitions.

**Expertise Degradation**: Experts who rely on augmentation may lose skills that made them expert. The pilot who always uses autopilot loses manual flying skills. The dispatcher who always follows AI recommendations loses situational judgment.

**The Misunderstanding: "AI Confidence Calibration Solves the Trust Problem"**

The belief that accurate confidence reporting enables appropriate trust fails on several grounds:

**Confidence ≠ Calibration**: "90% confidence" doesn't mean right 90% of the time. Most AI systems are not well-calibrated statistically. Users often don't understand what confidence numbers mean.

**Non-Linear Human Response**: Humans don't weight confidence proportionally:
- Low confidence (60%) → "AI doesn't know" → ignore
- High confidence (95%) → "AI is certain" → follow blindly
- Intermediate confidence (75%) → may produce appropriate deliberation

**Format Effects**: Same underlying confidence produces different responses:
- Numerical (0.85) vs. verbal ("highly likely") vs. visual (filled bar)
- Point estimate vs. range vs. distribution
- Recommendation confidence vs. underlying factor confidence

**Gaming Potential**: If users follow high-confidence recommendations, AI systems may learn to inflate confidence expression regardless of actual uncertainty.

**The Misunderstanding: "Explainable AI Prevents Automation Bias"**

Explanations can amplify automation bias as much as prevent it:

**Illusion of Understanding**: Explanations give users the feeling of understanding AI reasoning, but this feeling often exceeds actual understanding. Users report higher confidence after receiving explanations even when explanations are meaningless.

**Post-Hoc Rationalization**: For many AI systems, explanations are generated after decision, not exposing actual computational process. They are stories about why the system might have decided, not the actual reasoning.

**Confirmation Bias with Explanations**: Users inclined to accept find supporting explanations; users inclined to reject find undermining explanations. Explanations provide ammunition for pre-existing preferences rather than enabling objective evaluation.

**The Misunderstanding: "Human Oversight Ensures Safety"**

The assumption that human veto authority creates safety fails in practice:

**Automation Complacency**: When AI is usually right, humans stop critically evaluating. The error rate that matters isn't AI's error rate---it's human catch rate for AI errors. If AI is right 95% and humans catch 50% of errors, system makes 2.5% errors---possibly worse than either alone.

**Out-of-the-Loop Syndrome**: Humans in supervisory roles lose situational awareness. They're not actively engaged, so they lack context to evaluate effectively. By the time they realize something is wrong, it's too late.

**Time Pressure Compounds**: Theoretical override ability often isn't practical. The dispatcher has seconds. Reading explanation, evaluating recommendation, generating alternative takes minutes. "Oversight" becomes rubber-stamping.

**Accountability Diffusion**: When AI recommends and human approves, responsibility becomes unclear. Diffusion reduces incentives for careful evaluation.

**Failure Mode Taxonomy**

**Automation Bias and Complacency**

Definition: Tendency to favor automated recommendations over other information or own judgment.

Mechanisms:
- **Cognitive Offloading**: Using AI as cognitive prosthetic reduces mental engagement
- **Trust Generalization**: Trust built in one context generalizes to others inappropriately
- **Effort Minimization**: Following recommendations is easier than evaluating them
- **Social Proof**: AI recommendation is "what the system does"---socially safe to follow

Countermeasures:
- Variable reliability (prevents complacency but may reduce trust too much)
- Active confirmation requirements
- Periodic calibration events with disputable recommendations
- Separating information from recommendation

**Skill Degradation (Deskilling)**

Definition: Loss of human skills due to reliance on technology.

Paradox: Skills most needed when technology fails are least available due to degradation.

Mechanisms:
- **Use-It-or-Lose-It**: Skills require practice to maintain
- **Knowledge Externalization**: Knowledge exists in system, not human
- **Confidence Erosion**: Humans who don't practice lose confidence in own judgment

Countermeasures:
- Regular "manual mode" operation
- Gradual handoff as human expertise develops
- AI that teaches rather than replaces
- Skill assessments independent of technology-assisted performance

**Inappropriate Trust Transfer**

Definition: Applying trust from one context where it's warranted to another where it's not.

Mechanisms:
- **Category Generalization**: Trust in "the AI" rather than specific functions
- **Halo Effect**: Good performance in one dimension creates positive impressions in others
- **Complexity Opacity**: Users don't understand architecture well enough to know when trust should transfer

Countermeasures:
- Explicit communication about capability boundaries
- Different interfaces for different functions
- Task-specific confidence indicators
- Training with explicit out-of-domain examples

**Anchoring and Insufficient Adjustment**

Definition: AI recommendations serve as anchors that humans adjust from insufficiently.

Mechanisms:
- **Anchoring Heuristic**: Fundamental cognitive bias independent of AI
- **Adjustment Effort**: Moving far from anchor requires justification
- **Social Anchoring**: AI establishes reference points; dramatic departures require explanation

Countermeasures:
- Multiple options rather than single recommendation
- Require consideration of alternatives before displaying recommendation
- Training to recognize anchoring
- AI that sometimes provides no recommendation

**Attention Tunneling**

Definition: Narrowed attention focus causing important information outside focus to be missed.

Mechanisms:
- **Visual Salience**: AI recommendations prominently displayed
- **Cognitive Focus**: Processing AI output requires attention unavailable for other sources
- **Task Definition**: If task becomes "evaluate AI," other information becomes peripheral

Countermeasures:
- Integration of AI with other information (not separate displays)
- Attention management through interface design
- Periodic reorientation to non-AI sources
- AI that points to information rather than providing conclusions

**The Fundamental Transformation**

TADM research reveals that augmentation transforms the decision problem itself, not just the decision process.

**Unaugmented dispatch decision**: "What is the appropriate response to this call?"

**Augmented dispatch decision**: "Should I follow the AI's recommendation, override it, or investigate further?"

These are fundamentally different decisions requiring different information, skills, and cognitive processes. The human is no longer a dispatcher---they are a dispatcher-AI team supervisor. This role requires:

- Understanding what AI knows and doesn't know
- Calibrating when to trust vs. verify
- Maintaining independent judgment while leveraging AI
- Knowing when human intervention adds value

**Second-Order Effects**

**Decision Authority Migration**: As AI becomes more capable, decision authority migrates to AI even without explicit authorization. When AI recommendations are usually right and following them is easier than evaluating, practical decision-maker becomes AI regardless of stated policy.

**Responsibility Diffusion**: When AI recommends and human approves, accountability becomes ambiguous. Neither has strong incentives for quality---human can say "followed AI," AI has no accountability.

**Expertise Concentration**: AI augmentation may reduce need for broad expertise distribution. Expertise concentrates in those who design and maintain AI. Creates fragility and capability constraints.

**Decision Process Standardization**: AI recommendations reflect training patterns. Following recommendations produces standardized decisions. Variation---including adaptive variation for unusual situations---decreases.

**Human-AI Skill Coevolution**: As AI capabilities change, human skills must change to complement. Both are moving targets. Training must evolve continuously.

**Design Principles for Effective Augmentation**

**Match augmentation to decision type:**

| Decision Type | Recommended Approach |
|--------------|---------------------|
| High-volume, routine | High automation with statistical oversight |
| High-stakes, novel | Low automation with comprehensive information |
| Time-critical | Pre-computed recommendations with one-click execution |
| Expertise-dependent | Expert-adjustable augmentation level |
| Legally sensitive | Audit-trail augmentation with clear accountability |

**Design for appropriate trust:**
- Provide calibration information (historical accuracy, reliability factors)
- Enable trust adjustment (transparency, verification ability)
- Prevent trust pathologies (vary reliability, require engagement)

**Preserve human skills:**
- Regular non-augmented practice
- Gradual skill handoff as expertise develops
- Testing independent of augmentation
- Clear skill requirements that persist

**Design for graceful degradation:**
- Clear indication of augmentation status
- Trained fallback procedures
- Maintained non-augmented capability
- Gradual degradation, not cliff edge

**Measure the right things:**
- Human catch rate for AI errors (not just AI accuracy)
- Appropriate override rate
- Trust calibration accuracy
- Skill maintenance levels

**The Epistemological Shift**

TADM represents an epistemological shift in how humans know and decide.

In unaugmented work, human knowledge comes from direct experience, training, and reasoning about observed facts. The human is the epistemic agent.

In augmented work, human knowledge increasingly comes from AI intermediation. The human knows what the AI tells them. They evaluate AI outputs rather than primary sources. The human becomes an epistemic supervisor of AI-generated knowledge.

This shift has profound implications:
- **What counts as knowing**: Does accepting AI output constitute knowledge?
- **What constitutes expertise**: Is expertise in the domain or in evaluating AI?
- **How errors propagate**: AI errors become human errors through acceptance
- **How learning occurs**: Learning to use AI differs from learning the domain

Organizations implementing TADM must recognize they're not just adopting a tool---they're changing the epistemological structure of work. This requires rethinking training, evaluation, career development, and the very definition of competence.

The human-AI team can outperform either alone. But this requires recognizing that the team is a new entity with new requirements, not just a human with better tools.

---

## Document Metadata

**Model Used:** Claude Opus 4.5 (claude-opus-4-5-20251101)
**Created:** 2026-01-20
**Purpose:** Three-level explanation (ages 5-10, high school, expert) for cross-disciplinary mental model research

---

## Sources

### Primary Sources

- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A Model for Types and Levels of Human Interaction with Automation. *IEEE Transactions on Systems, Man, and Cybernetics*. The foundational LOA framework.

- Lee, J. D., & See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*. Definitive trust calibration framework.

- Mosier, K. L., & Skitka, L. J. (1996). Human Decision Makers and Automated Decision Aids: Made for Each Other? In R. Parasuraman & M. Mouloua (Eds.), *Automation and Human Performance*. Foundational automation bias research.

### Secondary Sources

- Bainbridge, L. (1983). Ironies of Automation. *Automatica*. Classic analysis of automation paradoxes.

- Woods, D. D. (1996). Decomposing Automation: Apparent Simplicity, Real Complexity. In R. Parasuraman & M. Mouloua (Eds.), *Automation and Human Performance*. Complexity analysis.

- Endsley, M. R. (1995). Toward a Theory of Situation Awareness in Dynamic Systems. *Human Factors*. Situational awareness framework.

### Decision Science Foundations

- Kahneman, D., & Tversky, A. (1979). Prospect Theory: An Analysis of Decision under Risk. *Econometrica*. Foundation for understanding cognitive biases.

- Klein, G. A. (1998). *Sources of Power: How People Make Decisions*. MIT Press. Recognition-primed decision model.

- Brunswik, E. (1955). Representative Design and Probabilistic Theory in a Functional Psychology. *Psychological Review*. Lens model foundation.

### Automation Bias Research

- Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does Automation Bias Decision-Making? *International Journal of Human-Computer Studies*.

- Cummings, M. L. (2004). Automation Bias in Intelligent Time Critical Decision Support Systems. *AIAA*.

### Human-AI Teaming

- Miller, T. (2019). Explanation in Artificial Intelligence: Insights from the Social Sciences. *Artificial Intelligence*. XAI limitations analysis.

- Bansal, G., et al. (2021). Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance. *CHI*.

### Emergency Dispatch Context

- National Emergency Number Association. (2020). *Computer-Aided Dispatch Systems: Functional and Technical Requirements*.

- Loftus, R., & Stein, J. (2020). Machine Learning in Emergency Medical Services. *Prehospital Emergency Care*.
