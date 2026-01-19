# Vicarious Liability for AI Agent Supervision

Exploring how vicarious liability doctrine from tort law applies to accountability for AI agent actions.

## Background

Vicarious liability is the legal doctrine that holds one party responsible for the wrongful acts of another. Unlike direct liability (you did something wrong), vicarious liability imposes responsibility based on relationship (someone you're responsible for did something wrong).

| Aspect | Description |
|--------|-------------|
| **Domain** | Tort law, employment law, agency law |
| **Core Principle** | A party can be liable for another's actions based on their relationship, not their own fault |
| **Latin Foundation** | Respondeat Superior - "let the master answer" |
| **Policy Rationale** | Deep pockets, risk distribution, incentive to supervise, ensuring victim compensation |
| **Key Insight** | Liability follows control. The more control you exercise, the more responsibility you bear |

**Why this matters for AI agents:** When an agent causes harm or makes errors, who bears responsibility? The traditional framework that determines human liability for other humans' actions provides the closest analogy for human liability for agent actions.

## Key Concepts

### 1. Respondeat Superior - The Foundational Doctrine

Respondeat superior ("let the master answer") is the bedrock principle: an employer is liable for the negligent acts of employees committed within the scope of employment.

| Element | Requirement | Rationale |
|---------|-------------|-----------|
| **Relationship** | Employer-employee (not independent contractor) | Control creates responsibility |
| **Scope** | Act within scope of employment | Employer shouldn't be liable for purely personal acts |
| **Nature** | Typically negligent acts (intentional acts more complex) | Negligence is foreseeable; intentional harm less so |

**The policy justifications:**

1. **Deep pockets:** Employers can bear the cost better than individual employees
2. **Risk distribution:** Cost of doing business should include cost of employee errors
3. **Incentive alignment:** Makes employers invest in training, supervision, and safety
4. **Victim compensation:** Ensures someone solvent is available to pay damages
5. **Benefit/burden symmetry:** Employer benefits from employee's work, so bears the risk

**Critical distinction:** This is strict vicarious liability - the employer's own fault is irrelevant. Even if the employer did everything right (good hiring, good training, good supervision), they're still liable for employee negligence within scope.

### 2. Scope of Employment - When Does Liability Attach?

Not every employee act creates employer liability. The act must be "within the scope of employment."

**Traditional Three-Part Test:**

| Factor | Question | Examples |
|--------|----------|----------|
| **Time and Place** | Was the act within authorized working time and location? | During work hours, at work location, on assigned routes |
| **Purpose** | Was the act in furtherance of the employer's business? | Serving customers, performing assigned duties |
| **Motivation** | Was the employee at least partially motivated by employer's interests? | Making a delivery (employer interest) even if also running personal errand |

**The "Characteristic Risk" Test (Ira S. Bushey):**

The landmark case *Ira S. Bushey & Sons, Inc. v. United States* (2d Cir. 1968) refined scope analysis. A drunken Coast Guard seaman returning from shore leave turned valves on a drydock, causing it to flood and damage a ship.

Judge Friendly's formulation: An employer should be liable for accidents that "may fairly be said to be characteristic of its activities" - not just acts done to serve the employer, but acts arising from the risks inherent in the enterprise.

| Traditional Test | Bushey Test |
|-----------------|-------------|
| Was the seaman trying to serve the Coast Guard? No. | Was a drunken seaman returning to ship a characteristic risk of naval operations? Yes. |
| Was turning valves part of his job? No. | Are sailors with ship access a foreseeable risk? Yes. |
| Traditional test: No liability | Bushey test: Liability |

**The boundaries of Bushey:**

The court noted that if the seaman had:
- Set fire to a bar while on leave - No liability (risk not characteristic of enterprise)
- Caused a car accident driving to the ship - No liability (general community risk)
- Shot someone he recognized as his wife's lover - No liability (personal life, not seafaring activity)

**Key insight:** The test is foreseeability of the *type* of risk, not the specific act. You don't need to foresee that a sailor will turn valves; you need to foresee that sailors with ship access might cause damage.

### 3. Frolic vs. Detour - The Classic Distinction

When an employee deviates from assigned duties, the deviation's extent determines liability.

| Category | Definition | Employer Liability |
|----------|------------|-------------------|
| **Detour** | Minor, brief deviation from assigned tasks | Yes - still within scope |
| **Frolic** | Substantial departure for employee's own purposes | No - outside scope |

**Detour Examples:**
- Delivery driver stops for coffee on route
- Employee takes slightly longer route to avoid traffic
- Worker makes brief personal phone call during deliveries

**Frolic Examples:**
- Delivery driver abandons route to attend baseball game
- Employee drives 50 miles off route to visit friend
- Worker takes company vehicle for weekend personal trip

**Factors courts consider:**

| Factor | Pointing to Detour | Pointing to Frolic |
|--------|-------------------|-------------------|
| **Duration** | Brief | Extended |
| **Distance** | Slight deviation | Major departure |
| **Intent** | Mixed (work + personal) | Purely personal |
| **Return** | Resuming duties | Not returning to work |
| **Expectedness** | Common employee behavior | Highly unusual |

**Modern trend:** Courts increasingly require near-total abandonment of employment duties to find a frolic. If the employee was on company premises during work hours, most negligent acts are treated as detours (within scope).

**The "re-entry" problem:** Does the employee re-enter scope of employment when returning from a frolic? Most courts say yes - when substantially returning to work duties, the employee is back within scope.

### 4. Employee vs. Independent Contractor - The Control Test

The foundational distinction: employers are generally liable for employees' torts but NOT for independent contractors' torts.

**Why the difference?**

| Factor | Employee | Independent Contractor |
|--------|----------|----------------------|
| **Control** | Employer controls how work is done | Contractor controls methods |
| **Integration** | Part of employer's business | Operates own business |
| **Tools** | Employer provides | Contractor provides |
| **Supervision** | Direct supervision | Results-only review |
| **Duration** | Ongoing relationship | Specific task/project |

**The "Right to Control" Test:**

The core question: Does the hiring party have the right to control not just *what* is done, but *how* it's done?

| Level of Control | Classification | Liability |
|-----------------|----------------|-----------|
| Control over methods, manner, means | Employee | Vicariously liable |
| Control only over results | Independent contractor | Generally not liable |

**The Economic Realities Test (federal standard):**

| Factor | Indicates Employee | Indicates Contractor |
|--------|-------------------|---------------------|
| Profit/loss opportunity | No independent profit opportunity | Bears economic risk |
| Investment | Employer invests in tools/equipment | Contractor invests |
| Permanence | Ongoing relationship | Defined project |
| Integral to business | Core business function | Ancillary service |
| Skill | Employer-directed skill use | Specialized independent skill |

**Why this matters:** Organizations often use "independent contractor" classification to avoid liability. Courts look past labels to actual relationship characteristics.

**Exceptions where liability attaches anyway:**

1. **Non-delegable duties** - Some duties can't be delegated liability-wise
2. **Inherently dangerous activities** - "Peculiar risk" doctrine
3. **Negligent selection** - Hiring a contractor you knew or should have known was unqualified
4. **Apparent authority** - Third parties reasonably believed contractor was employee

### 5. Apparent Authority - Liability for Unauthorized Acts

Even when an agent acts without actual authority, the principal may be liable if third parties reasonably relied on the appearance of authority.

**Core elements:**

| Element | Requirement |
|---------|-------------|
| **Principal's manifestation** | Principal's words or conduct created appearance of authority |
| **Third party reliance** | Third party reasonably relied on that appearance |
| **Third party's reasonable belief** | A reasonable person would believe agent had authority |

**Critical point:** Apparent authority comes from the *principal's* conduct, not the agent's claims. If the agent alone creates the false impression, there's no apparent authority.

**How apparent authority arises:**

| Mechanism | Example |
|-----------|---------|
| **Title** | Giving someone the title "Manager" implies managerial authority |
| **Prior dealings** | Agent made similar agreements before that principal honored |
| **Representation** | Principal told third party to deal with agent |
| **Failure to correct** | Principal knew of agent's overreaching, didn't stop it |
| **Industry custom** | In this industry, someone in this role typically has this authority |

**The "power of position" concept:** Appointing someone to a position carries implied authority for acts typical of that position. A "sales representative" has apparent authority to negotiate sales. A "treasurer" has apparent authority over financial matters.

**Termination problem:** Even after actual authority ends, apparent authority may linger until third parties are notified. Principals must actively inform known third parties of authority termination.

### 6. Ratification - Accepting Liability After the Fact

A principal can become liable for an agent's unauthorized acts by ratifying them after the fact.

**Methods of ratification:**

| Type | Mechanism | Example |
|------|-----------|---------|
| **Express** | Principal explicitly approves | "Yes, I affirm that agreement" |
| **Implied - acceptance of benefits** | Principal accepts fruits of unauthorized act | Keeping profits from unauthorized sale |
| **Implied - failure to repudiate** | Principal learns of act, doesn't object | Knowing agent exceeded authority, staying silent |
| **Implied - retention** | Keeping property obtained through unauthorized act | Using goods agent purchased without authority |

**Requirements for valid ratification:**

1. Principal had knowledge of material facts
2. Principal manifested intent to ratify (express or implied)
3. Ratification cannot be partial - must accept entire transaction
4. Cannot ratify void (illegal) acts

**Legal effect:** Ratification relates back to the original act. It's as if the agent had authority from the beginning.

**The corporate context:** When a corporation's board or officers learn of unauthorized acts and don't repudiate them, they may have ratified them. Silence can be acceptance.

### 7. The Borrowed Servant Doctrine - Dual Employment

When an employee temporarily works under another's direction, which employer bears vicarious liability?

**Basic framework:**

| Party | Role |
|-------|------|
| **General employer** | Original employer who lent the employee |
| **Special employer** | Borrowing party who directed the work |
| **Borrowed servant** | Employee working under special employer's direction |

**The control test for borrowed servants:**

The critical question: Who had the right to control the employee's work at the time of the tortious act?

| Factor | Points to General Employer | Points to Special Employer |
|--------|---------------------------|---------------------------|
| **Direction of work** | General employer directs | Special employer directs |
| **Right to discharge** | General employer can fire | Special employer can fire |
| **Payment** | General employer pays | Special employer pays |
| **Tools/equipment** | General employer provides | Special employer provides |
| **Nature of work** | General employer's business | Special employer's business |

**Dual employment possibility:** In some jurisdictions, both employers can be liable simultaneously if both exercised control. The employee is treated as employed by both for liability purposes.

**Common scenarios:**
- Temp agency workers directed by client company
- Equipment rental with operator
- Subcontractor workers directed by general contractor

### 8. Non-Delegable Duties - The Liability You Can't Shift

Some duties are "non-delegable" - the duty-holder cannot escape liability by hiring others to perform them.

**Core principle:** "You can delegate the work, but not the responsibility."

| Category | Examples |
|----------|----------|
| **Statutory duties** | Safety regulations, building codes |
| **Duties to invitees** | Keeping premises reasonably safe |
| **Inherently dangerous activities** | Demolition, hazardous materials |
| **Specific relationships** | Hospital's duty to patients, landlord's duty to tenants |

**Why these duties are non-delegable:**

1. **Public policy** - Some responsibilities are too important to shift
2. **Incentive alignment** - Duty-holder should remain invested in compliance
3. **Victim protection** - Ensures a solvent party is always liable
4. **Expertise mismatch** - Duty-holder chose the contractor, should bear selection risk

**How it works:**

```
Normal delegation:
Principal -> Contractor -> Work done negligently -> Contractor liable, not Principal

Non-delegable duty:
Principal -> Contractor -> Work done negligently -> BOTH liable (Principal can't escape)
```

**Critical insight:** Non-delegable duties aren't really "vicarious" liability - the principal is directly liable for failing to ensure the duty was performed, regardless of who actually performed it.

### 9. Indemnification - Contractual Liability Shifting

While vicarious liability assigns initial responsibility, indemnification contracts can shift the ultimate financial burden.

**Direction of indemnification:**

| Direction | Common Context | Purpose |
|-----------|---------------|---------|
| **Employer indemnifies employee** | Employment contracts, especially executives | Encourage bold decision-making |
| **Employee indemnifies employer** | Contractor agreements | Shift risk to party doing the work |
| **Third party indemnification** | Insurance, subcontracts | Spread risk through contract chain |

**Limitations on indemnification:**

| Limitation | Explanation |
|------------|-------------|
| **Public policy** | Can't indemnify for intentional torts or gross negligence |
| **Statutory limits** | Some jurisdictions limit employee-to-employer indemnification |
| **Insurance interaction** | May void coverage if indemnified party assumed contractual liability |
| **Bargaining power** | Courts may void adhesive indemnification clauses |

**Key distinction:** Indemnification doesn't change who's liable to the injured party. The vicariously liable principal still must pay the victim. Indemnification determines who ultimately bears the cost between the principal and agent.

### 10. Intentional Torts - The Harder Case

Vicarious liability analysis differs for intentional versus negligent acts.

**Traditional rule:** Employers are less likely to be liable for employees' intentional torts because:
- Intentional harm is less foreseeable
- Intentional acts are more likely to be personal, outside scope
- Public policy hesitates to impose liability for deliberate wrongdoing

**When intentional torts ARE within scope:**

| Situation | Example | Rationale |
|-----------|---------|-----------|
| **Authorized force** | Security guard uses excessive force | Force was contemplated by employment |
| **Furtherance of business** | Aggressive collections tactics | Acting to serve employer, even if method was wrong |
| **Job-created friction** | Bouncer assault | Job inherently involves confrontation |
| **Employer ratification** | Employer learns of act, doesn't discipline | Acceptance implies within scope |

**When intentional torts are NOT within scope:**

| Situation | Example | Rationale |
|-----------|---------|-----------|
| **Personal animosity** | Employee assaults coworker over personal dispute | Nothing to do with employment |
| **Criminal conduct** | Employee steals for personal gain | Purely personal benefit |
| **Sexual assault** | Generally not within scope | Not foreseeable exercise of employment duties |

**The "enterprise risk" approach:** Some courts extend Bushey-style analysis to intentional torts. If the job creates the opportunity or friction that leads to intentional harm, it may be within scope even without employer benefit.

## Application to AI Agents

### The Fundamental Question: What Is an AI Agent?

AI agents fit neither the "employee" nor "independent contractor" category - they're a new kind of entity. But the legal analysis still applies by analogy.

| Classification | Why AI Agents Are Similar | Why AI Agents Are Different |
|----------------|--------------------------|----------------------------|
| **Employee** | Human controls what agent does; agent acts for human's benefit; human integrates agent into their "enterprise" | No employment contract; agent doesn't have interests; can't be fired in meaningful sense |
| **Independent Contractor** | Agent has some autonomous decision-making; uses own "methods" within parameters | Human controls more than just results; agent has no independent business |
| **Tool** | Agent executes human's instructions; no independent existence | But tools don't make decisions, exercise judgment, or adapt |

**The emerging consensus:** AI agents are closer to employees than independent contractors for liability purposes because of the *control* factor. The human who deploys the agent controls:

- What tasks the agent performs (scope)
- What permissions the agent has (authority)
- What constraints the agent operates under (CLAUDE.md, system prompts)
- When the agent runs (deployment)

**Control creates responsibility.** The more control you exercise over an agent, the more liability you bear for its actions.

### Scope of Employment: What's "Within Scope" for an Agent?

For human employees, scope is defined by job duties, work hours, and work locations. For AI agents, scope is defined by:

| Human Concept | Agent Equivalent |
|---------------|------------------|
| Job description | Task delegation, prompt |
| Work hours | Session/runtime |
| Work location | File system access, network permissions |
| Company policies | CLAUDE.md, system prompt |
| Manager instructions | User prompts |

**When is an agent acting "within scope"?**

| Within Scope | Outside Scope |
|--------------|---------------|
| Executing the delegated task | Performing unrequested actions |
| Using granted permissions | Exceeding permission boundaries |
| Following CLAUDE.md instructions | Ignoring or contradicting instructions |
| Making reasonable judgment calls within task | Making unrelated decisions |
| Asking for clarification when uncertain | Taking major actions without checking |

**Applying Bushey's "characteristic risk" test:**

The question isn't "Did the agent intend to serve the human?" but "Was this type of error/harm a characteristic risk of using an AI agent?"

| Characteristic Risks of AI Agents | Not Characteristic (Probably Outside Scope) |
|----------------------------------|---------------------------------------------|
| Hallucination of facts | N/A - hard to imagine agent actions outside scope |
| Misunderstanding instructions | (Agents don't have "personal life" to divert them) |
| Over-interpretation of scope | |
| Failure to ask for clarification | |
| Errors in judgment calls | |

**Key insight:** Almost all agent actions are likely "within scope" because agents don't have personal lives, personal interests, or motivations to divert from assigned tasks. The frolic/detour distinction barely applies. An agent acting erroneously is still acting within scope - it just made an error.

### The Control-Liability Spectrum

Vicarious liability is fundamentally about control. More control = more liability.

| Control Level | Human Analog | Agent Example | Liability Implication |
|---------------|--------------|---------------|----------------------|
| **Maximum control** | Tell employee exact steps | Step-by-step instructions, no autonomy | Highest liability - agent is pure executor |
| **Task control** | Assign task, employee chooses method | Auftragstaktik - intent-based delegation | High liability - you defined the goal |
| **Outcome control** | Define desired outcome, employee figures out how | "Make the tests pass" | Significant liability - you set the objective |
| **Monitoring only** | Employee works independently, you review | Agent acts autonomously with periodic review | Still significant liability if you ratify results |
| **No control** | Independent contractor | N/A for AI agents? | Minimal liability (but hard to achieve with AI) |

**Can you disclaim control to avoid liability?**

Probably not effectively. If you:
- Deploy the agent
- Give it permissions
- Accept its output
- Benefit from its work

...you have exercised enough control for liability to attach, regardless of how much autonomy you granted within those parameters.

**The independent contractor escape doesn't work for AI agents** because the hallmarks of independent contractor status don't apply:

| Independent Contractor Hallmark | AI Agent Reality |
|--------------------------------|------------------|
| Has own business | Agent has no independent existence |
| Bears economic risk | Agent has no stake |
| Works for multiple clients | Agent exists only for your session |
| Controls own methods | Agent's methods come from training (not its own development) |
| Provides own tools | Agent runs on your infrastructure |

### Apparent Authority for Agents

What can third parties reasonably assume an AI agent can do?

**How apparent authority arises for agents:**

| Mechanism | Application |
|-----------|------------|
| **Deployment context** | Agent deployed on company website implies company authority |
| **Task description** | "Customer service agent" implies authority to resolve customer issues |
| **Platform representation** | Platform's marketing of agent capabilities |
| **Past behavior** | If agent's past commitments were honored, third parties expect future commitments to bind |
| **Lack of disclaimer** | No clear limits stated implies broader authority |

**Examples of apparent authority problems:**

| Scenario | Third Party's Reasonable Belief | Principal's Risk |
|----------|--------------------------------|------------------|
| Agent deployed to handle customer inquiries | Agent can make binding commitments about service/pricing | Principal bound by agent's unauthorized promises |
| Agent with email access | Agent can send binding communications | Principal bound by emails agent sent |
| Agent integrated with payment system | Agent can process refunds/charges | Principal responsible for unauthorized transactions |
| Agent answering questions about policies | Agent's statements reflect official policy | Reasonable reliance even if agent hallucinated |

**Limiting apparent authority:**

| Strategy | Implementation |
|----------|---------------|
| **Clear disclaimers** | "This agent cannot make binding commitments" |
| **Scope statements** | "Agent is limited to providing information, not making agreements" |
| **Human confirmation** | "Any commitment must be confirmed by a human representative" |
| **Visible limitations** | Display what the agent can and cannot do |

**The hallucination problem:** If an agent hallucinates a policy or commitment, and a third party reasonably relies on it, the principal may be bound. This is apparent authority at its most challenging - the agent stated something the principal never authorized, but the third party had no way to know.

### Ratification: Accepting Agent Actions After the Fact

Principals can ratify unauthorized agent actions, creating liability retroactively.

**How ratification happens with AI agents:**

| Ratification Method | Agent Context |
|--------------------|---------------|
| **Express approval** | Reviewing and approving agent's work product |
| **Accepting benefits** | Using code the agent wrote, keeping profits from agent's actions |
| **Failure to repudiate** | Knowing agent exceeded scope, not correcting/undoing |
| **Continued use** | Continuing to deploy agent after learning it makes problematic decisions |

**The review problem:** Every time you review agent output and accept it, you may be ratifying whatever the agent did to produce it. Even if the agent took unauthorized steps, your acceptance ratifies them.

**Practical implication:** You can't claim you're not responsible for agent actions while simultaneously benefiting from them. If you accept the agent's work product, you've ratified how it was produced.

### Non-Delegable Duties: What You Can't Offload to Agents

Some responsibilities cannot be delegated to agents - you remain directly liable regardless of how well the agent performs.

| Category | Examples | Why Non-Delegable |
|----------|----------|-------------------|
| **Professional judgment** | Legal advice, medical diagnosis, architectural design | Licensed professional personally responsible |
| **Fiduciary decisions** | Investment decisions for clients, trustee duties | Duty runs to the beneficiary personally |
| **Safety-critical decisions** | Safety system overrides, emergency response | Too important to delegate |
| **Ethical determinations** | Research ethics, human subject decisions | Requires human moral judgment |
| **Legal compliance** | Regulatory filings, contractual obligations | Organization remains responsible |

**The general principle:** The more consequential and less reversible a decision, the more likely it's non-delegable.

**Practical implications for agent supervision:**

1. **Identify non-delegable duties in your domain** - What decisions must remain human?
2. **Design agent workflows that preserve human decision points** for non-delegable matters
3. **Don't let agent efficiency pressure you into delegating the non-delegable**
4. **Accept that some things shouldn't be automated** even if they technically could be

### The Borrowed Servant Problem: Multi-Agent Scenarios

When multiple parties are involved in agent deployment, who bears vicarious liability?

| Scenario | Parties | Liability Analysis |
|----------|---------|-------------------|
| **Platform + User** | Platform provides agent, user deploys for task | Who controls the specific deployment? |
| **Orchestrator + Sub-agent** | Orchestrating agent delegates to specialized agent | Does orchestrator's "employer" control sub-agent? |
| **API Provider + Integrator** | API provides capability, integrator wraps and deploys | Integrator controls deployment, likely primary liability |
| **Fine-tuner + Base Model** | Original training + custom fine-tuning | Fine-tuner may assume liability for fine-tuning effects |

**The control question remains central:** Whoever controls the agent at the time of the harmful act bears primary vicarious liability.

**API providers' position:** Providing an API is more like selling a tool than deploying an agent. The integrator who calls the API, provides the prompt, and deploys the agent bears primary responsibility.

**But API providers aren't completely insulated:**
- Negligent design could create direct liability
- Knowledge of misuse without action could create ratification
- Marketing claims could create apparent authority

### Indemnification in Agent Contexts

Contracts can shift liability between parties in the agent deployment chain.

| Relationship | Common Indemnification | Issues |
|--------------|----------------------|--------|
| **Platform-User** | User indemnifies platform for user's agent deployments | May be unenforceable adhesion contract |
| **Employer-Employee (using agent)** | Employer typically indemnifies employee for good-faith agent use | Standard employment protection |
| **Client-Contractor** | Contractor may indemnify client for agent-assisted work product | Professional liability questions |

**Key consideration:** Indemnification doesn't protect against truly egregious conduct. If you deliberately misuse an agent to cause harm, indemnification clauses likely won't protect you.

**Insurance interaction:** Some professional liability insurance may not cover AI agent-related claims, or may exclude indemnified liability. Check coverage before assuming indemnification fully protects you.

## Practical Implications

### 1. Accept That You're Liable

If you deploy an AI agent, you bear vicarious liability for its actions within scope. Scope is broad for agents. Trying to disclaim this liability is unlikely to succeed.

**Better approach:** Accept liability, manage risk through:
- Careful scope definition
- Appropriate permission constraints
- Monitoring and verification
- Clear escalation paths

### 2. Control = Liability, But Less Control ≠ Less Liability

The paradox: You can't escape liability by giving agents more autonomy. You deployed the agent, you gave it permissions, you benefit from its work. That's enough control for liability.

**The autonomy-liability disconnect:**

| Autonomy Level | Control Exercised | Liability |
|----------------|------------------|-----------|
| Low (micromanaged) | High | High |
| High (autonomous) | Still significant | Still high |

The control you exercise *before* the agent acts (in deployment, configuration, and permission-granting) creates liability even if you don't control *how* the agent acts.

### 3. Apparent Authority Requires Active Management

Third parties will make assumptions about what your agent can do. Manage those assumptions or be bound by them.

**Practical steps:**
- Clearly state agent limitations before third-party interactions
- Design UX that doesn't imply authority the agent lacks
- Require human confirmation for binding commitments
- Monitor and correct agent overreach quickly

### 4. Ratification Is Almost Automatic

Every time you accept agent output, you may ratify how it was produced. This is nearly unavoidable if you're using agents productively.

**Practical implication:** Focus on preventing bad agent actions rather than trying to disclaim them after the fact. By the time you've accepted the output, you've ratified the process.

### 5. Some Things Shouldn't Be Delegated

Non-delegable duties exist for good reasons. The efficiency gains from agent delegation don't override the policy reasons certain decisions must remain human.

**Framework for identifying non-delegable duties:**

| Question | If Yes, Likely Non-Delegable |
|----------|------------------------------|
| Is there a professional license involved? | Yes |
| Is the decision safety-critical? | Yes |
| Is the decision legally binding? | Probably |
| Is the decision irreversible and high-stakes? | Probably |
| Would delegation offend public policy? | Yes |

### 6. The "Characteristic Risk" Frame Is Useful

Bushey's "characteristic risk" test provides a useful heuristic: If a problem is a foreseeable type of AI agent failure, you bear liability for it.

**Characteristic AI agent risks you should anticipate:**
- Hallucination
- Misunderstanding scope
- Over-confident statements
- Failure to ask for clarification
- Taking instructions too literally or too loosely
- Making unauthorized commitments

If these problems occur, you can't claim surprise. They're characteristic of the enterprise of using AI agents.

## Key Insight

**Vicarious liability doctrine tells us: You are responsible for your agent's actions within scope. Scope is broad. Control creates responsibility. Accepting output ratifies process.**

The legal framework doesn't ask whether the agent "meant to" cause harm or whether you "intended" for the agent to take that action. It asks: Did you deploy the agent? Did you benefit from its work? Did you exercise control over what it could do?

If yes, you bear responsibility for the characteristic risks of that deployment.

**For AI agent supervision, this means:**

1. **Accept the liability** - Don't waste energy trying to disclaim it
2. **Manage the scope** - Clear boundaries reduce, but don't eliminate, liability
3. **Design for non-delegation** - Keep non-delegable duties human
4. **Manage apparent authority** - Third party reliance can bind you
5. **Verify before ratifying** - Once you accept output, you've ratified the process
6. **Anticipate characteristic risks** - Foreseeable AI failures are within scope

The uncomfortable truth: Using AI agents productively requires accepting liability for their actions. The legal framework that evolved over centuries to handle human agents applies - not perfectly, but substantially - to AI agents. The human who deploys, directs, and benefits from the agent bears responsibility for its actions.

This isn't a bug. It's the mechanism by which society ensures that powerful agents remain under human accountability.

## Connections to Other Frameworks

| Framework | Connection |
|-----------|-----------|
| **Principal-Agent Theory** | Economic version of same relationship - adds incentive analysis |
| **Delegation** | Vicarious liability is the legal consequence of delegation |
| **Trust Development** | Higher trust means more autonomy, but not less liability |
| **Mission Command** | Intent-based orders don't reduce liability for outcomes |
| **Circuit Breaker** | Safety stops don't eliminate liability, but may reduce damages |

## Open Questions

1. **How will courts apply vicarious liability to AI agents?** The doctrine developed for humans - how literally will it transfer?

2. **Does the "independent contractor" classification ever apply?** Can a sufficiently autonomous agent shift liability away from the deployer?

3. **What's the standard for apparent authority with AI?** When should third parties be expected to know an agent can't make binding commitments?

4. **How does ratification work when agents run autonomously?** If an agent takes hundreds of actions, does reviewing a sample ratify all?

5. **Will new legal categories emerge?** AI agents fit neither employee nor contractor cleanly - will new frameworks develop?

## Status

**Phase:** Research complete. Key insight is that vicarious liability's control-based analysis applies strongly to AI agents. The more you control (deploy, configure, grant permissions, accept output), the more liability you bear. Attempting to disclaim this through autonomy grants doesn't work because you still control the parameters within which autonomy operates. Practical focus should be on managing scope, apparent authority, and non-delegable duties rather than trying to escape the fundamental liability that comes with agent deployment.

## Sources

- [Legal Information Institute - Respondeat Superior](https://www.law.cornell.edu/wex/respondeat_superior)
- [Ira S. Bushey & Sons, Inc. v. United States, 398 F.2d 167 (2d Cir. 1968)](https://law.justia.com/cases/federal/appellate-courts/F2/398/167/29802/)
- [Legal Information Institute - Frolic and Detour](https://www.law.cornell.edu/wex/frolic_and_detour)
- [Legal Information Institute - Apparent Authority](https://www.law.cornell.edu/wex/apparent_authority)
- [Indiana Law Journal - Vicarious Liability for AI](https://www.repository.law.indiana.edu/cgi/viewcontent.cgi?article=11519&context=ilj)
- [Utrecht Law Review - Employer's Vicarious Liability for Damage Caused by an AI Worker](https://utrechtlawreview.org/articles/10.36633/ulr.1063)
- [University of Chicago Law Review - The Law of AI is the Law of Risky Agents Without Intentions](https://lawreview.uchicago.edu/online-archive/law-ai-law-risky-agents-without-intentions)
- [Clifford Chance - Who's Responsible for Agentic AI?](https://www.cliffordchance.com/insights/thought_leadership/ai-and-tech/who-is-responsible-for-agentic-ai.html)
