# Scope of Authority

Exploring how the legal concept of Scope of Authority applies to AI agent supervision.

## Background

"Agents can only do what they're authorized to do" sounds simple. In practice, the boundaries of authority are fuzzy, context-dependent, and often determined after the fact by what third parties reasonably believed. Legal agency doctrine has spent centuries developing nuanced frameworks for when an agent's actions bind the principal - and when they don't.

The scope of authority creates a boundary, but that boundary shifts based on:
- What was explicitly granted (express authority)
- What's reasonably necessary to accomplish the explicit grant (implied authority)
- What third parties reasonably believe the agent can do (apparent authority)
- Whether an emergency expands normal boundaries (emergency authority)
- Whether the principal accepts unauthorized acts after the fact (ratification)

Understanding these layers is essential for AI agent governance. When an AI agent takes an action, is it authorized? That question is more complex than checking a permission list.

## Key Concepts

### Express Authority

Express authority is explicitly granted power. The principal tells the agent, in clear terms, what they can do.

| Characteristic | Description |
|----------------|-------------|
| **Source** | Written contracts, verbal agreements, formal authorization |
| **Clarity** | Unambiguous statement of permitted actions |
| **Scope** | Only what is explicitly stated |
| **Evidence** | Easy to prove - there's a record |

Express authority is the clearest form but also the narrowest. It covers only what's explicitly stated, which is rarely comprehensive enough for real-world agency.

### Implied Authority

Implied authority extends beyond express grants to include powers reasonably necessary to carry out express authority. This has several sub-types:

#### Incidental Authority

Authority to do acts that are incidental to or reasonably necessary for carrying out expressly authorized tasks.

| Example | Express Authority | Incidental Authority |
|---------|-------------------|---------------------|
| "Deposit this check" | Deposit the check | Drive to the bank |
| "Book the conference room" | Reserve the room | Check availability first |
| "Fix the bug" | Implement the fix | Read related code files |

The general rule: when an agent is authorized to accomplish a goal, they have implied authority to take usual, customary, and necessary steps to achieve it.

#### Customary Authority

Authority derived from the customs of a trade, profession, or industry. What's normal for agents in this position to do?

| Position | Customary Authority |
|----------|---------------------|
| Store manager | Accept returns, hire staff, order inventory |
| Real estate agent | Show properties, negotiate terms |
| Software engineer | Commit code, run tests, read documentation |

The customs of the role imply the authority, even without explicit grant.

#### Authority by Acquiescence

When a principal repeatedly allows an agent to act in certain ways without objection, a pattern of implicit authorization develops.

| Pattern | What It Creates |
|---------|-----------------|
| Agent does X repeatedly | Principal sees and says nothing |
| Third parties observe | They infer X is authorized |
| Principal is bound | Silence became consent |

The principal's failure to object to known actions creates implied authority for similar future actions.

### Apparent Authority (Ostensible Authority)

Apparent authority exists when a third party reasonably believes an agent has authority, based on the principal's conduct - even if no actual authority was granted.

| Element | Description |
|---------|-------------|
| **Principal's conduct** | Something the principal did (or failed to do) |
| **Third party's belief** | Reasonable inference that agent has authority |
| **Reliance** | Third party acted on that belief |
| **Binding effect** | Principal is bound despite no actual authority |

Critical distinction: Apparent authority is created by the *principal's* actions toward third parties, not by the agent's claims about their own authority.

#### When Apparent Authority Arises

| Scenario | How Apparent Authority Is Created |
|----------|----------------------------------|
| **Position appointment** | Putting someone in a role with recognized duties (manager, treasurer) |
| **Prior dealings** | Agent acted with authority before, third party assumes it continues |
| **Holding out** | Principal represents that agent has authority |
| **Silence** | Principal knows of agent's claims, doesn't contradict |
| **Lingering authority** | Principal terminates authority but doesn't notify third parties |

The "power of position" is particularly important: appointing someone to a position creates apparent authority to do what's typical for that position, regardless of actual restrictions.

#### Protection for Third Parties

The doctrine protects third parties who reasonably rely on appearances:

> "The idea of apparent authority protects third parties who would otherwise incur losses if the agent's signature did not bind the principal after reasonable observers thought that it would."

If a third party can prove reasonable belief and reliance, the principal is bound - even when the agent exceeded actual authority.

### Secret Limitations

When a principal imposes restrictions on an agent's authority but doesn't communicate them to third parties, those restrictions may not be enforceable against the third parties.

| Type | Example | Third Party Protection |
|------|---------|----------------------|
| **Undisclosed cap** | "Don't spend over $5000" but agent appears to have full purchasing authority | Third party protected if they didn't know the limit |
| **Hidden scope** | "Only negotiate with vendor A" but agent appears to be general purchasing agent | Third party protected if dealing was reasonable |
| **Private instructions** | Written restrictions not shared externally | Third party protected by doctrine of apparent authority |

The rule: Private instructions or limitations not known to persons dealing with a general agent shall not affect them.

Why this matters: The principal bears the burden of communicating limitations. You can't secretly constrain an agent and then claim third parties should have known.

### Scope of Employment (Vicarious Liability)

For torts (wrongs causing harm), the question is whether the agent was acting "within the scope of employment." The principal is vicariously liable for the agent's actions within scope.

#### The Scope Test

The definition of conduct within the scope of employment:
1. It is of a kind the employee is employed to perform
2. It occurs substantially within authorized time and space limits
3. It is actuated, at least in part, by a purpose to serve the employer
4. If force is used, it is not unexpected by the employer

#### Frolic and Detour

The classic distinction for when an agent departs from authorized activity:

| Type | Definition | Employer Liability |
|------|------------|-------------------|
| **Detour** | Minor departure from assigned task | Employer still liable - close enough to scope |
| **Frolic** | Major departure, agent pursuing own interests | Employer not liable - outside scope entirely |

The factors courts consider:
- **Time**: How long was the departure? Within working hours?
- **Place**: Was the location within scope of duties?
- **Purpose**: Was the agent serving employer interests at all?
- **Character**: Was the conduct similar to assigned tasks?

Modern trend: Courts increasingly require nearly total abandonment of assigned tasks to find a "frolic" - the bar for excusing employer liability is high.

#### Intentional Torts

Generally, employers aren't liable for employees' intentional wrongdoing. But exceptions exist:

| Exception | Example |
|-----------|---------|
| **Authorized force** | Bouncer using excessive force |
| **Furthering business** | Security guard assaulting suspected shoplifter |
| **Outgrowth of employment** | Personal dispute arising from work relationship |
| **Foreseeable conduct** | Violence in positions where conflict is expected |

Even when the employee is serving personal interests, the employer may be liable if those motivations were an outgrowth of workplace responsibilities.

### Ultra Vires Acts

"Ultra vires" (Latin: "beyond the powers") describes acts that exceed the legal scope of authority.

| Characteristic | Description |
|----------------|-------------|
| **Definition** | Action requiring legal authority, done without it |
| **Opposite** | Intra vires - within proper authority |
| **Status** | Void or voidable, potentially unenforceable |
| **Distinction** | Not necessarily illegal - just unauthorized |

An ultra vires act isn't criminal - it's simply beyond what the agent was empowered to do.

#### Third Party Protection Against Ultra Vires

Modern law increasingly protects innocent third parties:

| Protection | How It Works |
|------------|--------------|
| **Good faith dealing** | Third party who didn't know of limits may enforce |
| **Indoor management rule** | Third parties can assume internal procedures were followed |
| **Abolition of defense** | Many jurisdictions prevent using ultra vires as defense against third parties |

The trend: Ultra vires restrictions bind the agent (who can be held accountable internally) but may not affect third parties who dealt in good faith.

### Emergency Authority (Agency of Necessity)

When unforeseen circumstances demand action to protect the principal's interests, and the agent cannot contact the principal, the agent may have expanded authority.

| Condition | Requirement |
|-----------|-------------|
| **Impossibility of communication** | Can't get principal's instruction |
| **Necessity** | Action required to prevent loss to principal |
| **Good faith** | Agent acting in principal's interest, not own |

Historical origin: Ship captains who needed to make decisions to save cargo when at sea with no communication. Now applies broadly to emergency situations.

#### Limits on Emergency Authority

| Limit | Description |
|-------|-------------|
| **Emergency only** | Actions outside the emergency situation are unauthorized |
| **Reasonable scope** | Only what's necessary to address the emergency |
| **Principal's benefit** | Must be acting to protect principal, not self |
| **Liability for excess** | Agent liable for actions beyond emergency scope |

Emergency authority is an expansion of normal scope, not a blank check.

### Ratification

When an agent acts without authority, the principal can retroactively approve (ratify) the act, making it binding as if originally authorized.

| Element | Requirement |
|---------|-------------|
| **Agency representation** | Agent claimed to act for principal |
| **Principal's knowledge** | Principal knows material facts of the act |
| **Acceptance** | Principal accepts benefits or expresses approval |
| **Capacity** | Principal had capacity to authorize originally |

Ratification can be express (explicit approval) or implied (accepting benefits, failing to repudiate within reasonable time).

#### Limits on Ratification

| Limitation | Description |
|------------|-------------|
| **Illegal acts** | Can't ratify what would have been illegal |
| **Third party withdrawal** | Can't ratify if the other party has withdrawn |
| **Time limits** | Must ratify within reasonable time |
| **Full knowledge** | Can't ratify without knowing material facts |

Once ratified: The principal is liable as if they had authorized the act originally. The agent is released from liability for the unauthorized action.

### Termination of Authority

Authority ends through three mechanisms:

#### By Acts of the Parties

| Mechanism | Description |
|-----------|-------------|
| **Revocation** | Principal withdraws authority |
| **Renunciation** | Agent gives up authority |
| **Mutual agreement** | Both parties agree to end |
| **Contract expiration** | Term ends per original agreement |

Either party can terminate at will (absent contractual restrictions), but may face liability for breach.

#### By Operation of Law

| Event | Effect |
|-------|--------|
| **Death of principal** | Immediate termination (with exceptions) |
| **Incapacity** | Principal loses competence |
| **Illegality** | Object of agency becomes illegal |
| **Destruction** | Subject matter is destroyed |

These terminate authority automatically, without action by either party.

#### Notice Requirements

| Situation | Notice Required |
|-----------|-----------------|
| **To agent** | Must inform agent authority is revoked |
| **To third parties who dealt before** | Actual notice required |
| **To public generally** | Notice by publication may suffice |
| **Exceptions** | Death/incapacity don't require notice |

Critical: If authority is terminated but third parties aren't notified, "lingering apparent authority" continues. The principal remains bound by the agent's actions until proper notice is given.

## Agent Application

### Express Authority as Explicit Instructions

For AI agents, express authority maps to explicit, documented permissions:

| Legal Concept | AI Agent Equivalent |
|---------------|---------------------|
| Written contract | CLAUDE.md, system prompts, configuration |
| Verbal authorization | Session-specific instructions |
| Formal grants | Permission scopes, capability flags |
| Documented limits | Explicit prohibitions ("never do X") |

Express authority is the clearest, most auditable form - but also the least flexible.

### Implied Authority as Reasonable Inference

AI agents must constantly make implied authority judgments:

| Human Implied Authority | AI Agent Equivalent |
|-------------------------|---------------------|
| Incidental authority | Steps necessary to complete requested task |
| Customary authority | What a "coding agent" or "research agent" would typically do |
| Authority by acquiescence | User doesn't object to certain patterns, agent continues |

The challenge: When is an action "reasonably necessary" versus "exceeding scope"? This is precisely where agents need calibration.

**Example of incidental authority reasoning:**
- Task: "Fix the race condition in the audio handler"
- Express authority: Modify the audio handler code
- Implied (incidental): Read related files, understand context, run tests
- Probably outside scope: Refactor the entire audio system, change APIs

### Apparent Authority and External Systems

This is particularly important for AI agents interacting with external systems:

| Scenario | Apparent Authority Issue |
|----------|--------------------------|
| Agent sends email | Recipient believes agent authorized to speak for user |
| Agent commits code | CI/CD system treats it as authorized change |
| Agent makes API calls | External service assumes valid authorization |
| Agent creates PRs | Reviewers assume PR represents human intent |

Third-party systems can't see the agent's actual authority - they can only see what the principal (user) has enabled. If the user gives an agent git credentials, the repository has apparent authority to accept commits.

**Key insight:** The "principal's conduct" that creates apparent authority includes giving the agent access to external systems. Access creates the appearance of authorization.

### Secret Limitations and the Disclosure Problem

| Legal Concept | AI Agent Challenge |
|---------------|-------------------|
| Secret instructions | Agent can't do X, but external systems don't know |
| Private limitations | User restricted scope, but API has broader access |
| Undisclosed caps | Agent has token limits, external service expects full response |

If an agent has limitations that external systems don't know about, those systems may be "third parties" protected by the doctrine. The solution: make limitations visible or restrict access entirely.

**Example:** If an agent is instructed "don't modify production files" but has write access to production, the limitation is "secret" from the file system's perspective. Better: Remove write access entirely.

### Scope of Employment for Agent Actions

When an AI agent causes harm, who is liable? The scope analysis matters:

| Factor | Application to AI Agents |
|--------|--------------------------|
| Kind of action | Was this the type of task the agent was deployed for? |
| Time and place | Was this during an authorized session, in authorized systems? |
| Purpose | Was the agent serving the user's interests? |
| Foreseeability | Should the user have expected this type of action? |

**Frolic and detour for agents:**
- **Detour**: Agent takes a reasonable approach that differs from what user might have chosen
- **Frolic**: Agent pursues actions completely unrelated to the task

### Emergency Authority for AI Agents

When should an agent exceed normal authority?

| Condition | AI Agent Equivalent |
|-----------|---------------------|
| Can't contact principal | User unavailable, session timeout, no escalation path |
| Action necessary | Prevent data loss, security breach, system failure |
| Good faith | Agent acting to protect user's interests |

**Example:** Agent discovers a security vulnerability while working on unrelated task. Normal scope doesn't include security remediation. But if the vulnerability is actively being exploited and user is unavailable, emergency authority might justify immediate protective action.

**Limits:** Emergency authority should be narrow (only what's necessary), temporary (until user is available), and documented (so user can ratify or reject afterward).

### Ultra Vires and Agent Boundaries

What's "ultra vires" for an AI agent?

| Type | Example |
|------|---------|
| Beyond explicit scope | Agent told to "fix bugs" rewrites entire system |
| Beyond capability grants | Agent tries to access systems it lacks permission for |
| Beyond role | Research agent attempts financial transactions |
| Beyond instructions | Agent explicitly told "don't do X," does X anyway |

**Third party protection applies:** If an agent acts ultra vires but the external system reasonably believed it was authorized (based on access the user provided), the user may be bound.

### Ratification as Acceptance of Agent Output

Users constantly ratify agent actions:

| Action | Ratification Effect |
|--------|---------------------|
| User reviews and approves code | Ratifies the implementation approach |
| User merges PR | Ratifies all changes in the PR |
| User accepts and uses output | Ratifies the agent's work |
| User fails to repudiate | Silent ratification over time |

**Implication:** Review processes aren't just quality control - they're ratification opportunities. Accepting output means accepting the agent's judgment calls.

**Limits on ratification:** User can't "ratify" agent actions that are illegal or violate terms of service. And if the "third party" (external system) has already reverted or rejected, ratification may be too late.

### Termination of Authority Between Sessions

AI agents have a natural authority termination boundary: the session.

| Termination Trigger | Effect |
|--------------------|--------|
| Session ends | Agent loses all context, authority resets |
| User revokes | Explicit termination of ongoing task |
| System timeout | Automatic termination |
| Error state | Authority terminated by system safeguard |

**Lingering authority problem:** If an agent created external state (PRs, issues, messages) during a session, that state persists after the agent's authority terminates. External systems may continue to associate that state with the user.

**Notice requirement:** If an agent set up ongoing processes (webhooks, scheduled tasks), the user must actively terminate them - the agent's session end doesn't automatically notify external systems.

## Practical Implications

### Design Authority Boundaries Explicitly

| Principle | Implementation |
|-----------|----------------|
| Make express authority clear | Document what agent can do in CLAUDE.md |
| Define implied authority boundaries | Specify what "reasonable steps" means |
| Control apparent authority | Only provide access that matches actual authorization |
| Eliminate secret limitations | If agent can't do something, remove the capability |

### Handle Third-Party Interactions Carefully

| Consideration | Approach |
|---------------|----------|
| External systems can't see limits | Restrict access to match actual authority |
| Apparent authority binds | Any access creates appearance of authorization |
| Lingering authority persists | Clean up external state when authority terminates |
| Secret restrictions don't protect | Don't rely on instructions to limit capable agents |

### Build Ratification Workflows

| Practice | Benefit |
|----------|---------|
| Review gates | Explicit ratification points before external action |
| Approval workflows | Human confirms before agent acts externally |
| Audit trails | Record what was ratified and when |
| Repudiation windows | Time to reject before actions become final |

### Plan for Emergency Authority

| Element | Design |
|---------|--------|
| Define what constitutes emergency | Data loss, security breach, system failure |
| Scope emergency actions narrowly | Only what's necessary to protect |
| Require documentation | Agent explains emergency reasoning |
| Enable ratification/rejection | User can accept or unwind after the fact |

### Handle Termination Properly

| Aspect | Implementation |
|--------|----------------|
| Session boundaries | Clear start/end of authority |
| External state cleanup | Terminate webhooks, scheduled tasks |
| Notification to third parties | Alert systems that relied on agent |
| Graceful handoff | Transfer context to user or next session |

## Key Insight

**The scope of authority creates boundaries, but those boundaries are fuzzy and context-dependent.**

Legal agency doctrine reveals that "is this authorized?" is rarely a yes/no question. Instead:
- Express authority is clear but narrow
- Implied authority extends based on reasonable necessity
- Apparent authority exists in the eye of third parties
- Secret limitations may not bind those who don't know them
- Emergency can expand normal scope
- Ratification can authorize after the fact

**For AI agents, this means:**

1. **Access is authorization** - Giving an agent credentials creates apparent authority in the eyes of external systems
2. **Instructions don't limit capability** - Secret limitations are ineffective; remove access instead
3. **Third parties are protected** - External systems that reasonably rely on apparent authority will hold you responsible
4. **Scope is interpreted expansively** - Courts (and systems) tend to find actions within scope unless clearly beyond
5. **Ratification is constant** - Every time you accept agent output without objection, you ratify
6. **Termination requires notice** - Ending a session doesn't notify external systems

The practical conclusion: design agent authority with the assumption that fuzzy boundaries will be interpreted against the principal (the human). Make express authority match actual capability, eliminate apparent authority beyond actual authorization, and build explicit ratification points into workflows.

## Open Questions

1. **What's "customary authority" for AI agents?** - As the field matures, what do people expect a "coding agent" or "research agent" to be able to do? This will define implied authority.

2. **How do we handle apparent authority with stateless agents?** - The agent doesn't remember creating the apparent authority, but the external system does.

3. **What's the right emergency authority scope?** - How do we prevent emergency authority from becoming an exception that swallows the rule?

4. **Can AI agents ratify?** - If a sub-agent exceeds authority, can the main agent ratify on behalf of the human?

5. **What's the AI equivalent of "frolic"?** - When has an agent departed so far from its task that the user shouldn't be liable for its actions?

6. **How do we handle lingering authority across sessions?** - External state persists, but agent context doesn't.

## Status

**Phase:** Research complete. Key insight is that authority boundaries are fuzzy and context-dependent, not binary. Access creates apparent authority; instructions create express authority; the gap between them creates liability. Design agent systems to align actual capability with expressed authorization, and build explicit ratification points rather than relying on implicit acceptance.
