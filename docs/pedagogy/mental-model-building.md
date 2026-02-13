# Mental Model Building: From Cognitive Science to Agent System Design

## Executive Summary

Mental model building is far more than "helping learners construct internal representations of concepts." It is the fundamental mechanism by which minds - human or artificial - develop the capacity to predict, reason, and act effectively in complex domains. This document examines the cognitive architecture of mental models, the mechanisms that build and revise them, why they resist change even when incorrect, and what this means for AI agent development.

The central insight: mental models are not repositories of facts but *working simulations* that generate predictions. This distinction has profound implications. Facts can be corrected with information. Simulations require restructuring - a fundamentally different and more difficult process.

---

## Part I: Theoretical Foundations

### The Origin and Nature of Mental Models

The term "mental model" was coined by Kenneth Craik in 1943 in *The Nature of Explanation*. Craik proposed that the mind constructs "small-scale models" of reality that it uses to anticipate events, reason about causes, and try out alternatives mentally before committing to action. This was a radical departure from behaviorist psychology, which treated the mind as a black box responding to stimuli.

Philip Johnson-Laird formalized mental model theory in cognitive science, arguing that human reasoning does not operate by applying logical rules to propositions, but by constructing and manipulating models of situations. His central claim: "Each mental model represents a possibility. A mental model represents one possibility, capturing what is common to all the different ways in which the possibility may occur."

Three characteristics distinguish mental models from mere knowledge:

**1. Structural Correspondence**

Mental models are *iconic* - their structure corresponds to the structure of what they represent. A mental model of a pulley system preserves the spatial and mechanical relationships between components. This is fundamentally different from propositional knowledge ("pulleys provide mechanical advantage") which abstracts away structure.

**2. Simulation Capability**

Mental models can be "run" to generate predictions. You can mentally rotate an object, trace a sequence of events, or imagine what would happen if a variable changed. This mental simulation is computationally distinct from logical inference and enables a different class of reasoning.

**3. Partial and Purpose-Relative**

Mental models are not complete replicas of reality. They selectively represent features relevant to the reasoner's current purposes. The same physical system may be modeled differently depending on what questions you're trying to answer. This selectivity is both a strength (computational tractability) and a weakness (systematic blind spots).

### Schema Theory: The Architecture of Understanding

Mental models do not exist in isolation. They are organized into larger structures called *schemas* (or schemata) - generic frameworks that structure knowledge about recurring situations, objects, or procedures.

Frederic Bartlett introduced schema theory in *Remembering* (1932), demonstrating that memory is reconstructive rather than reproductive. People remember events by fitting them into pre-existing schemas, often distorting details to match expectations. This was among the first demonstrations that background knowledge actively shapes perception and memory.

Jean Piaget extended schema theory to cognitive development, arguing that children construct increasingly sophisticated schemas through two complementary processes:

**Assimilation**: Incorporating new experiences into existing schemas. A child who knows "dog" may initially assimilate all four-legged animals into the dog schema.

**Accommodation**: Modifying schemas when experience doesn't fit. When the child learns that cats are not dogs, the schema must differentiate.

David Rumelhart formalized schemas as having:
- Variables (slots that can be filled by particular instances)
- Default values (typical fillers assumed when not specified)
- Constraints (restrictions on valid slot fillers)
- Hierarchical organization (schemas contain sub-schemas)

For example, a "restaurant" schema includes slots for entering, being seated, ordering, eating, and paying - with default values (waiter service, menu, check at end) and constraints (payment occurs after eating, not before).

**The critical insight**: schemas are not passive templates but active processing structures. They direct attention, guide inference, fill in missing information, and determine what is memorable. Learning is not just acquiring new schemas but reorganizing existing ones.

### Analogical Reasoning and Structure Mapping

Mental models are often built through analogy - understanding a new domain by mapping it to a familiar one. Dedre Gentner's Structure Mapping Theory provides the formal account.

The core principle: an analogy is a mapping of knowledge from a base domain to a target domain that preserves *relational structure* rather than surface features. "The atom is like a solar system" works because both share relational structure (central body, orbiting bodies, attractive force) despite having completely different surface features (size, composition, visibility).

Gentner identifies two mapping principles:

**1. Relations over Attributes**

Analogies map relations between objects, not attributes of objects. The sun being yellow doesn't transfer to the nucleus. But the sun's gravitational attraction of planets does transfer to the nucleus attracting electrons.

**2. Systematicity**

Analogies preferentially map systems of interconnected relations over isolated relations. A good analogy captures a coherent system of cause-and-effect relationships, not just scattered similarities.

The Structure Mapping Engine (SME) formalizes this process:
1. Find local matches between elements of base and target
2. Build global interpretations that maximize systematicity
3. Project candidate inferences from base to target
4. Evaluate and revise based on feedback

**Implications for mental model building**: Analogy is not just a teaching technique but a fundamental cognitive mechanism. When learners encounter a new domain, they spontaneously (often unconsciously) recruit analogies from familiar domains. This can be powerful when the analogy is apt, and catastrophically misleading when it is not.

The classic Gentner and Gentner (1983) study showed that people who used a "flowing water" analogy for electricity made different predictions than those who used a "moving crowd" analogy - and both differed from the scientific model. The analogy doesn't just scaffold learning; it shapes what kind of mental model gets built.

---

## Part II: Conceptual Change - Why Mental Models Resist Revision

### The Structure of Naive Knowledge

Before formal instruction, people develop intuitive mental models from everyday experience. These "naive" or "folk" theories are surprisingly systematic and remarkably resistant to change. Understanding their structure is essential for understanding why conceptual change is hard.

Two competing theories describe naive knowledge:

**Framework Theory (Vosniadou)**

Stella Vosniadou argues that children construct coherent, theory-like knowledge structures based on everyday experience. These "framework theories" include ontological commitments (what kinds of things exist), epistemological commitments (how we can know things), and causal commitments (what causes what).

For example, children construct a framework theory of physics in which:
- Objects fall unless supported
- Motion requires continuous force
- Heavier things fall faster
- The Earth is flat or a hollow sphere with people inside

These beliefs are not random errors but coherent frameworks that explain everyday experience quite well. The flat Earth model predicts that dropped objects fall "down," that we don't feel the Earth moving, and that the horizon appears level.

**Knowledge in Pieces (diSessa)**

Andrea diSessa offers a contrasting view: naive physics is not a coherent theory but "a fragmented collection of ideas, loosely connected and reinforcing, having none of the commitment or systematicity that one attributes to theories."

diSessa introduces *phenomenological primitives* (p-prims) - small, nearly atomic knowledge structures derived from experience. Examples:
- **Ohm's p-prim**: More effort/resistance produces more/less output
- **Closer-is-stronger**: Proximity increases effect
- **Force as mover**: Force causes motion in the direction of the force

P-prims are not beliefs that can be explicitly stated and evaluated. They are *recognition patterns* that activate in response to situations. A p-prim is neither correct nor incorrect in itself - only its application to a particular context can be appropriate or inappropriate.

**Why this matters**: The debate has practical implications. If naive knowledge is theory-like, conceptual change requires wholesale theory replacement - a difficult, rare event. If it is fragmented, learning involves gradually retuning which knowledge elements activate in which contexts - a more incremental process.

Contemporary research suggests both patterns exist: some domains show more theory-like coherence, others more fragmentation. The important point is that either structure creates resistance to change.

### The Four Conditions for Conceptual Change

Posner, Strike, Hewson, and Gertzog (1982) identified four conditions necessary for conceptual change:

**1. Dissatisfaction**

The learner must be dissatisfied with the existing conception. This requires more than being told the conception is wrong - the learner must *experience* its inadequacy, typically through anomalies that the existing model cannot explain or predict.

**2. Intelligibility**

The new conception must be intelligible - the learner must be able to grasp what it means. This is not trivial. Quantum mechanics is not intelligible to most people because it contradicts basic intuitions about how objects behave.

**3. Plausibility**

The new conception must appear plausible - the learner must see how it could be true. Plausibility requires that the new conception fit with other knowledge and beliefs the learner holds.

**4. Fruitfulness**

The new conception must be fruitful - it should solve problems, make predictions, or open new avenues of inquiry that the old conception could not.

**The critical insight**: these conditions are rarely satisfied by explanation alone. You can explain the scientific conception perfectly clearly, and if the learner is not dissatisfied with their existing model, has not grasped what the new one means, does not see how it could be true, and does not experience it as useful, no conceptual change will occur.

### Michelene Chi's Ontological Categories

Michelene Chi provides the deepest analysis of why some misconceptions are so resistant. She distinguishes three levels of conceptual error:

**1. False Beliefs**

Isolated incorrect facts that can be corrected by direct instruction. "The heart oxygenates blood" is a false belief easily corrected: "Actually, the lungs do that."

**2. Flawed Mental Models**

Incorrect structural relationships between correctly categorized entities. The learner understands what kind of thing electricity is but has wrong ideas about how current, voltage, and resistance relate. These require restructuring but not recategorization.

**3. Category Mistakes (Incommensurate Misconceptions)**

The learner has assigned the concept to the wrong ontological category. This is where the deepest misconceptions live.

Chi's key insight: many persistent misconceptions in science involve treating *processes* as *substances*. Students think of heat as a substance that flows from hot to cold objects (rather than a process of energy transfer). They think of force as something an object possesses (rather than an interaction between objects). They think of evolution as a process directed toward a goal (rather than an undirected process of variation and selection).

When conception and correct understanding differ at the categorical level, "refutation at the belief level will not promote conceptual change." You cannot fix a category mistake by providing correct information within the wrong category. You must first help the learner recognize they have committed a category mistake, then help them build the correct category, and only then can instruction proceed.

**This explains the persistence of misconceptions**: Students who think of heat as a substance can coherently assimilate instruction about heat "flowing" and heat "capacity" into their flawed framework. The instruction reinforces rather than corrects the misconception because the language of instruction (heat flow, heat reservoir) is compatible with the substance ontology.

### Why Explanation Alone Does Not Build Mental Models

Given this framework, we can now articulate precisely why "explanation" is insufficient for mental model building:

**1. No Conflict Detection**

Explanation provides information; it does not create dissatisfaction with existing models. If the learner's model already accounts for their experience, new information is assimilated rather than accommodated. The learner thinks: "Yes, that's consistent with what I already knew."

**2. Translation into Existing Framework**

Explanations are interpreted through existing schemas. A learner with a flawed mental model will translate the explanation into their flawed framework, hearing different meaning than the explainer intended. The words are the same; the mental models are different.

**3. No Model-Running**

Explanation is static; mental models are dynamic. Reading about how a system works is different from running a mental simulation of the system. Without running the model, learners cannot discover where their predictions fail.

**4. Surface vs. Structural Processing**

Explanation can be processed at a surface level (understanding the words) without structural processing (reorganizing how concepts relate). Students often feel they understand an explanation - the words make sense - while retaining their flawed mental model.

**5. Epistemic State Blindness**

People who are wrong don't think they're wrong. The learner cannot compare their mental model to the correct one because they cannot see their own model clearly. They have no external vantage point from which to evaluate it.

Chi summarizes: "Conceptual change is hard because people who are wrong don't think they're wrong. You can't overwrite a misconception with a fact; you have to confront and replace the flawed model itself."

---

## Part III: Expert-Novice Differences and the Development of Expertise

### Qualitative Differences in Mental Models

Research comparing experts and novices reveals that expert knowledge is not just "more" but *qualitatively different*:

**1. Organization by Deep Structure**

Novices organize knowledge by surface features; experts organize by deep structural principles. Physics novices categorize problems by surface features (inclined planes, pulleys, springs). Physics experts categorize by underlying principles (energy conservation, Newton's second law).

**2. Chunking and Pattern Recognition**

Chess master studies by de Groot and Chase & Simon demonstrated that experts recognize meaningful patterns as single units ("chunks") where novices see individual pieces. Experts' fixations are rapid and directed; novices scan randomly. This pattern recognition enables faster processing and deeper encoding.

The chunking difference is quantitative (experts have more and larger chunks) but creates qualitative effects: experts can hold more meaningful information in working memory because they encode situations at a higher level of abstraction.

**3. Rich Causal Models**

Expert mental models include causal mechanisms that explain *why* relationships hold. Novice models often include correct associations without causal understanding. When the situation varies, novices cannot adapt because they don't understand the underlying mechanism.

**4. Automated Subprocesses**

Through practice, experts automate low-level processes, freeing cognitive resources for higher-level reasoning. This automation is not just faster execution but enables qualitatively different cognition - the expert can think about the problem while doing what novices must think about.

**5. Metacognitive Awareness**

Experts better recognize when they don't understand, when additional information is needed, and when their approach isn't working. This metacognition enables self-correction that novices lack.

### The Novice-to-Expert Trajectory

Expertise development is not linear accumulation but qualitative restructuring:

**Stage 1: Disconnected Fragments**

The novice begins with disconnected facts, procedures, and examples. Knowledge is context-bound - learned in one situation, not transferred to others.

**Stage 2: Surface-Level Organization**

Facts become organized, but by surface features. The learner can retrieve relevant knowledge but may not recognize structural similarities across superficially different problems.

**Stage 3: Causal Understanding**

Relationships between concepts acquire causal meaning. The learner understands *why* things work, not just *that* they work. This enables generalization beyond trained examples.

**Stage 4: Schema Compilation**

Causal understanding becomes compiled into recognition patterns. The expert no longer reasons step-by-step through principles but recognizes situations as instances of known patterns. This is the "intuition" that experts describe - actually, pattern recognition operating below conscious awareness.

**Stage 5: Flexible Expertise**

At the highest levels, experts can reason about the structure of their own knowledge, recognize the boundaries of their expertise, and construct novel solutions by recombining known patterns. This requires meta-knowledge about domain knowledge.

**Key insight**: the transition from novice to expert involves *multiple* conceptual changes, not one. The expert's mental model is not a corrected novice model but a fundamentally different organization of knowledge built through repeated restructuring.

---

## Part IV: Instructional Strategies That Build Mental Models

### Why Not All Instruction Is Equal

The research implies that some instructional approaches build mental models while others merely transfer information that learners assimilate into existing (possibly flawed) frameworks. The difference is not effort or quality of explanation but alignment with how mental model construction actually works.

### Strategies That Support Mental Model Building

**1. Elicit-Confront-Resolve Cycles**

Effective instruction begins by eliciting the learner's current model, not by explaining the correct model. Only by surfacing the existing model can instruction target its specific deficiencies.

Confrontation follows: creating situations where the learner's model generates incorrect predictions. The learner must experience the failure of their model, not just be told it's wrong.

Resolution provides the correct model as a solution to a problem the learner now recognizes having.

This sequence - elicit, confront, resolve - is far more effective than explain-then-practice because it creates the dissatisfaction condition that Posner identified.

**2. Bridging Analogies**

When the target domain is counterintuitive, direct instruction often fails because learners cannot build the correct mental model from the ground up. Bridging analogies provide intermediate cases that connect intuitive experience to counterintuitive concepts.

For example: Students believe a table doesn't push up on a book (because tables are passive). But they accept that a compressed spring pushes up. And they accept that a flexible board bends under weight. Instruction can build a bridge: the table is like a very stiff spring/board - it compresses microscopically and therefore exerts upward force.

**3. Contrasting Cases**

Juxtaposing carefully chosen cases that differ in one feature highlights that feature's causal role. Learners who compare cases notice and encode features they would overlook in isolated examples.

This is not simply seeing multiple examples but seeing examples specifically designed to reveal structure. Random examples may reinforce surface-level encoding; contrasting cases drive structural encoding.

**4. Model-Based Reasoning Tasks**

Tasks that require running mental models - predicting, explaining, troubleshooting - force learners to actually construct and use models, not just recognize information.

Prediction tasks are particularly valuable: the learner commits to an output before receiving feedback, creating conditions for genuine surprise when predictions fail.

**5. Multiple Representations**

The same concept represented in different formats (verbal, visual, mathematical, graphical) forces learners to extract underlying structure rather than memorizing surface forms. The ability to translate between representations indicates (and develops) genuine understanding.

**6. Progressive Refinement**

Begin with simplified models that capture essential relationships, then progressively add complexity. This respects cognitive load limits while building structural understanding.

The key is that simplified models should be *structurally correct*, even if incomplete. A simplified model that is structurally wrong creates misconceptions that must be unlearned.

### What Doesn't Work (And Why)

**Telling + Practice on Similar Problems**

The most common instructional pattern - explain, then practice - can achieve procedural competence without conceptual understanding. Learners may correctly execute procedures while retaining flawed mental models. The flaws emerge when problems vary from trained patterns.

**Refutation Texts**

Texts that state a misconception and then correct it are modestly effective for false beliefs but insufficient for category mistakes. The learner who has miscategorized a concept does not recognize that the refutation applies to them.

**Increasing Complexity of Explanation**

When learners don't understand, the intuitive response is to explain more, in more detail. But if the problem is a flawed mental model, more detailed explanation within the learner's flawed framework reinforces rather than corrects the flaw.

**Memorization of Correct Propositions**

Learners can memorize correct statements while retaining incorrect mental models. They reproduce the correct statement on tests while reasoning incorrectly in novel situations.

---

## Part V: Transfer of Learning and Mental Model Robustness

### Near Transfer vs. Far Transfer

Transfer of learning - applying knowledge learned in one context to a different context - is the ultimate test of mental model quality. The research distinguishes:

**Near Transfer**: Application to situations closely similar to training. Differences are surface-level; underlying structure is identical. Example: Solving physics problems with different numerical values.

**Far Transfer**: Application to situations structurally similar but superficially different. Example: Applying physics principles to engineering design.

The robust finding: near transfer is common; far transfer is rare. This has been documented across domains including education, training, analogy, intelligence research, and expertise studies.

### Why Transfer Is Hard

Mental models are often more context-bound than they appear:

**1. Encoding Specificity**

Information is encoded with contextual features. Retrieval cues must match encoding cues. A mental model built in one context may not be retrieved in another context, even when applicable.

**2. Surface Feature Dominance**

Retrieval is driven by surface similarity, even when deep structural similarity is more relevant. Learners who know an applicable principle may not access it because the surface features don't trigger retrieval.

**3. Situated Knowledge**

Knowledge is not stored abstractly but embedded in situations. What looks like "transfer" may actually be reasoning from the new situation, with the old knowledge serving only as an indirect influence.

### Mental Models That Transfer

Some mental models do transfer. What distinguishes them?

**1. Abstraction Level**

Models encoded at an abstract level, explicitly stripping away context-specific features, transfer better than models encoded in concrete detail. The abstraction must be genuine - not just verbal summary but structural understanding.

**2. Multiple Instantiations**

Models learned across multiple varied examples transfer better than models learned from single examples or homogeneous example sets. Variation forces extraction of what's constant (structure) from what varies (surface).

**3. Explicit Structural Focus**

Learning that explicitly focuses on structural relationships (asking why, not just what) produces more transferable knowledge than learning focused on facts or procedures.

**4. Metacognitive Framing**

Learners who think about *when* and *why* a principle applies - not just *how* - are more likely to recognize novel applications. This metacognitive layer is often missing from instruction.

### The Transfer Problem for Instruction

The transfer research creates a dilemma: instruction must be concrete enough to be understandable but abstract enough to transfer. Too concrete, and learners build context-bound models. Too abstract, and learners cannot build models at all.

The resolution involves careful sequencing: concrete instantiation for initial model building, followed by systematic variation to drive abstraction, capped by explicit metacognitive reflection on the structural principles.

---

## Part VI: Assessing Mental Models

### The Measurement Challenge

Mental models are internal structures that cannot be directly observed. Assessment must infer model characteristics from observable behavior - but different behaviors reveal different aspects of the model.

### Assessment Methods

**1. Prediction Tasks**

Present novel scenarios and ask for predictions. Predictions reveal what the mental model generates as output. Carefully designed scenarios can discriminate between alternative models.

Limitation: Correct predictions can arise from flawed models (if the models accidentally generate the same prediction for that scenario). Multiple scenarios are needed to triangulate.

**2. Explanation Tasks**

Ask learners to explain why something happens. Explanations reveal causal structure in the mental model.

Limitation: Learners may give socially desirable explanations that don't reflect their actual reasoning. Probing questions are needed to surface the real model.

**3. Drawing and Diagram Tasks**

Ask learners to draw or construct representations of the system. Spatial structure in the drawing may reveal structural features of the mental model.

Limitation: Drawing skill confounds model quality. Learners may have correct models they cannot draw, or vice versa.

**4. Troubleshooting Tasks**

Present systems with faults and ask for diagnosis. Troubleshooting requires running the mental model to isolate where expected and actual behavior diverge.

Limitation: Troubleshooting also requires systematic reasoning strategies. Strategy deficits can mask model quality.

**5. Concept Maps**

Ask learners to construct maps showing how concepts relate. Concept maps externalize the relational structure of knowledge.

Limitation: Concept map construction is a skill that improves with practice. The map may not fully represent the internal model.

**6. Sorting and Classification Tasks**

Present problems or examples and ask learners to sort them by similarity. Sorting criteria reveal organizing principles of the mental model.

Limitation: Learners may sort by surface features for the task even if they can recognize deep structure.

### The SMART Approach

Recent research has developed the Student Mental Model Analyzer for Teaching and Learning (SMART), which uses graph-based metrics (clustering coefficient, betweenness, PageRank, closeness) to automatically derive key concepts from expert explanations and compare learner concept maps to expert models.

This approach enables:
- Automated identification of missing or incorrect relationships
- Comparison across learners at scale
- Longitudinal tracking of model development

Limitation: SMART measures the relational structure learners can externalize, which may differ from their functional mental model.

### What Good Assessment Reveals

Effective mental model assessment goes beyond right/wrong scoring to characterize:

- What entities and relationships the model includes (completeness)
- How entities relate causally (structure)
- What the model generates when "run" (predictions)
- Where the model breaks down (boundary conditions)
- How the model differs from expert models (nature of gaps)

This rich characterization enables targeted instruction aimed at specific model deficiencies rather than generic re-teaching.

---

## Part VII: Application to AI Agent Development

### How Do AI Agents Build Internal Models?

The question of whether AI systems have "mental models" is not merely semantic. The architecture determines capability.

**World Models in AI**

In 2025, "world models" have emerged as a major research direction. A world model is an internal representation of how the environment behaves, enabling the agent to predict outcomes, evaluate possibilities, and plan before acting.

Key developments:
- DreamerV3 (April 2025 Nature paper): Agents improve behavior by "imagining" future scenarios using learned world models
- DeepMind proof (2025): "Any agent capable of generalizing to a broad range of simple goal-directed tasks must have learned a predictive model capable of simulating its environment"
- NVIDIA Cosmos 1.0: Open-weight world foundation models focused on 3D consistency and physical alignment
- DeepMind Genie 3: Interactive text-to-world generation with real-time agent control

**The Contrast with Current LLMs**

Current large language models may not have world models in the strong sense. Instead of coherent internal simulations, they may learn "bags of heuristics" - scores of disconnected rules of thumb that approximate responses to specific scenarios but don't cohere into consistent wholes. Some may actually contradict each other.

A 2025 benchmark study reported "striking limitations" in vision-language AI models' basic world-modeling abilities, including "near-random accuracy when distinguishing motion trajectories."

This suggests that LLMs can pattern-match to generate plausible responses without building the kind of predictive models that enable genuine reasoning about novel situations.

### Learned Patterns vs. Mental Models: The Critical Distinction

Drawing on the cognitive science framework, we can articulate what distinguishes "learned patterns" from "mental models":

**Learned Patterns:**
- Associations between inputs and outputs
- Context-bound (work in training distribution)
- Cannot be "run" to generate novel predictions
- No structural correspondence to domain
- No explicit representation of causality

**Mental Models:**
- Internal representations with structural correspondence to domain
- Support mental simulation to generate predictions
- Enable reasoning about counterfactuals
- Transfer to structurally similar but superficially different situations
- Include causal mechanisms, not just correlations

The distinction matters because:
- Pattern-based systems fail unpredictably when inputs shift outside training distribution
- Model-based systems can reason about novel situations by simulating them
- Pattern-based systems cannot explain their reasoning; model-based systems can
- Pattern-based systems hallucinate plausibly; model-based systems fail systematically

### Scaffolding Agent Learning to Build Appropriate Mental Models

Research on Hierarchical Task Environments (HTEs) suggests approaches for scaffolding agent learning:

**1. Curriculum Through Task Decomposition**

Methods decomposing complex goals into manageable subgoals create intrinsic curricula that shape agent learning. This mirrors human expertise development: building simple models first, then progressively elaborating.

**2. LLMs as Generative World Models of Tasks**

LLMs can dynamically generate scaffolding - "generative world models of tasks" - that guide exploration, generate learning signals, and train agents to internalize hierarchical structure.

**3. Hybrid Neuro-Symbolic Approaches**

Combining neural pattern recognition with symbolic reasoning provides "a powerful grounding for hybrid, neuro-symbolic agents." The neural component provides pattern recognition; the symbolic component provides structural reasoning that can be inspected and modified.

**4. Inter-Task Feedback**

Systems like Reflexion derive experiences from past tasks and apply them to subsequent tasks. ExpeL retrieves similar past trajectories, identifying success patterns by contrasting positive and negative examples.

This is analogous to human expertise development: building mental models through varied experience with explicit reflection on what worked and why.

### Can Agents Teach by Supporting Mental Model Building?

Research on AI agents in educational contexts (2025) reveals both promise and limits:

**What Works:**

- Embodied AI agents can emulate Socratic teaching methods, supporting critical thinking through questions rather than assertions
- Multi-agent systems can provide adaptive support for metacognitive processes
- AI can relieve educators of administrative burdens, enabling focus on pedagogy and mentorship
- Hybrid human-AI workflows, where teachers curate and moderate AI output, outperform fully autonomous tutors

**What Doesn't:**

- Fully autonomous AI tutors produce less robust learning gains than human-AI collaboration
- AI lacks the deep domain expertise and pedagogical judgment to recognize and address category mistakes
- AI cannot reliably detect when learners have assimilated correct information into flawed frameworks

**The Key Insight:**

AI agents can support mental model building but cannot (yet) guide it independently. Effective AI pedagogy requires:
- Human experts to identify misconceptions and design confrontation scenarios
- AI to provide personalized practice and immediate feedback
- Human oversight to recognize when learners are not genuinely understanding
- Collaborative workflows where AI augments rather than replaces human judgment

### Failure Modes of Agents with Incorrect or Incomplete Mental Models

Understanding cognitive failure modes illuminates AI failure modes:

**1. Hallucination as Category Mistake**

When LLMs hallucinate - generating plausible but incorrect information - they may be committing something analogous to Chi's category mistakes: applying patterns from one domain to another where they don't apply.

Anthropic's 2025 interpretability research found that hallucinations occur when inhibition circuits that prevent answering without knowledge fail incorrectly. The model "recognizes a name but lacks sufficient information about that person, causing it to generate plausible but untrue responses."

This is analogous to human confabulation: filling gaps in knowledge with plausible fabrication because the system lacks the metacognitive awareness that knowledge is missing.

**2. Task Misunderstanding as Analogical Failure**

Agents may misunderstand tasks by recruiting inappropriate analogies from training. A coding task phrased unusually may be interpreted through the lens of a superficially similar but structurally different pattern.

This mirrors Gentner's finding that human analogical reasoning is driven by surface similarity even when it leads to structural errors.

**3. Context Collapse as Transfer Failure**

Agents trained in one context may fail to transfer capabilities to structurally similar but superficially different contexts. This mirrors the human far-transfer problem: knowledge is encoded with contextual features and doesn't activate without matching cues.

**4. Confident Incorrectness as Metacognitive Failure**

Agents may be confidently wrong because they lack metacognitive awareness of their own knowledge boundaries. They cannot recognize when they're outside their competence because they don't have a model of their own competence.

2025 research on o3 and o4-mini showed hallucination rates of 33% and 48% respectively on knowledge questions - worse than older models. Reasoning capabilities introduced new failure points at each step, "paradoxically increasing error rates despite improved analytical capabilities."

**5. Compounding Errors as Simulation Failure**

Multi-agent systems show coordination failures where "if the updated network fails to accurately reflect agents' current relevance or expertise, messages may be routed to inappropriate recipients, leading to misunderstandings or redundant reasoning."

This is analogous to running flawed mental simulations: errors in the model compound through the simulation, producing outputs increasingly divorced from reality.

---

## Part VIII: Common Misunderstandings

### "Mental Models Are Just Knowledge Structures"

Mental models are not passive data structures but dynamic simulations. The critical difference is whether you can "run" them to generate predictions. A database of facts is not a mental model; a simulation that uses those facts to predict outcomes is.

### "Building Mental Models Is the Same as Understanding"

Understanding is often confused with the feeling of understanding. Learners who can follow an explanation feel they understand, but following and building are different. Following means processing the explanation in the moment; building means constructing a model you can run independently later.

### "Explanations Transfer Mental Models"

Explanations transfer information that learners interpret through their existing mental models. If the existing model is flawed, the information is assimilated incorrectly. Explanation is necessary but not sufficient for mental model building.

### "Incorrect Models Are Just Missing Pieces"

Misconceptions are not holes in correct models but coherent alternative models. You cannot fix a misconception by adding the missing piece because the misconception is not a gap but a structure. You must replace the structure, not patch it.

### "More Practice Builds Better Models"

Practice on similar problems may reinforce procedural skill without improving the underlying model. Practice that never challenges the model leaves the model unchanged. Only practice that generates surprising failures drives model revision.

### "AI World Models Are Like Human Mental Models"

AI world models are engineering constructs designed to predict state transitions. Human mental models are evolved cognitive structures shaped by perception, action, and social interaction. The structural parallels are illuminating but the substrates are fundamentally different.

---

## Part IX: Second-Order Effects

### On Learning System Design

If mental model building requires confrontation with failure, learning systems must be designed to *create productive failures* rather than smooth paths to correct answers.

This inverts the standard instructional design assumption that friction is bad. Some friction - specifically, friction that reveals flawed models - is essential.

### On Assessment Philosophy

If mental models can be correct at the surface (matching correct facts) while flawed at the structural level, assessment that checks only surface-level correctness provides false confidence.

This implies that assessment should target the *structure* of understanding, not just the *content*. Can the learner predict? Explain? Troubleshoot? Transfer? These probe model quality in ways that recall of facts cannot.

### On Expert-Novice Communication

Experts' mental models are qualitatively different from novices' - not just more detailed. This means experts explaining to novices face a systematic communication problem: the same words activate different mental structures.

The expert's "obvious" relationships are not obvious to the novice because they require conceptual structures the novice lacks. Effective expert-novice communication requires the expert to model the novice's model, not just articulate their own.

### On AI System Brittleness

If AI systems learn patterns rather than building genuine world models, their failures will be unpredictable - appearing wherever test situations differ from training in ways the patterns don't capture.

This suggests that AI reliability requires either:
- Restriction to domains where training distribution matches deployment distribution
- Development of genuine world models that support generalization
- Human oversight to catch pattern failures before they matter

### On Human-AI Collaboration

Humans and AI systems may have complementary failure modes:
- Humans fail at tasks requiring processing speed, consistency, and scale
- AI systems fail at tasks requiring structural understanding, transfer, and metacognition

Effective human-AI collaboration puts AI systems in roles suited to pattern matching (fast processing of well-defined tasks) while humans retain roles requiring model-based reasoning (novel situations, boundary cases, judgment under uncertainty).

---

## Part X: Key Insights

### The Fundamental Distinction

Mental models are *simulations*, not *databases*. They generate predictions by running internal processes that mirror external processes. This generation is what enables reasoning, planning, and transfer.

The difference between pattern matching and mental simulation is the difference between recognizing and understanding. Both can produce correct outputs in familiar situations; only understanding produces correct outputs in novel situations.

### The Bottleneck of Conceptual Change

Mental model building is constrained by the difficulty of conceptual change. Models resist revision not because people are stubborn but because:

1. Alternative models are coherent - they work, within their limited scope
2. Existing models filter interpretation of new information
3. Category mistakes prevent recognition that change is needed
4. Model revision requires experiencing failure, not just being told

This means mental model building cannot be optimized by better explanation. It requires designed confrontation with the limitations of existing models.

### The Hierarchy of Knowledge

Knowledge exists at multiple levels:
- Facts (isolated propositions)
- Procedures (sequences of actions)
- Schemas (organized frameworks)
- Mental models (runnable simulations)
- Metamodels (knowledge about knowledge)

Each level supports different capabilities. Facts enable recall; procedures enable execution; schemas enable interpretation; mental models enable prediction; metamodels enable learning.

Most instruction targets facts and procedures. Mental model building requires targeting schemas and simulations - a fundamentally different pedagogical challenge.

### The Expert-Novice Asymmetry

Expert knowledge is not more of what novices have but differently organized knowledge. This asymmetry means:

- Novice models cannot become expert models through accumulation
- Expert instruction must account for reorganization, not just addition
- Transfer requires building abstract models, not just learning examples
- Expertise development is marked by multiple restructuring events

### For AI Agent Development

AI agents face analogous challenges:

1. Pattern matching is not world modeling
2. World models enable generalization; patterns do not
3. Scaffolded learning with progressive complexity may build better models
4. Failure modes mirror human cognitive failures: hallucination as confabulation, misunderstanding as analogical error, brittleness as transfer failure
5. Human-AI collaboration should pair human model-based reasoning with AI pattern processing

The path to more capable AI agents may require not just more training data but architectures that support genuine world model construction - the artificial analog of mental model building.

---

## Sources and References

### Foundational Works

- Craik, K. (1943). *The Nature of Explanation*. Cambridge University Press.
- Johnson-Laird, P. N. (1983). *Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness*. Harvard University Press.
- Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press.
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155-170.

### Conceptual Change

- Posner, G. J., Strike, K. A., Hewson, P. W., & Gertzog, W. A. (1982). Accommodation of a scientific conception: Toward a theory of conceptual change. *Science Education*, 66(2), 211-227.
- Chi, M. T. H. (2013). Two kinds and four sub-types of misconceived knowledge, ways to change it, and the learning outcomes. In S. Vosniadou (Ed.), *International Handbook of Research on Conceptual Change* (pp. 49-70). Routledge.
- Vosniadou, S. (2013). Conceptual change in learning and instruction: The framework theory approach. In S. Vosniadou (Ed.), *International Handbook of Research on Conceptual Change* (pp. 11-30). Routledge.
- diSessa, A. A. (1993). Toward an epistemology of physics. *Cognition and Instruction*, 10(2-3), 105-225.

### Expertise and Transfer

- Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science*, 5(2), 121-152.
- de Groot, A. D. (1965). *Thought and Choice in Chess*. Mouton.
- Thorndike, E. L., & Woodworth, R. S. (1901). The influence of improvement in one mental function upon the efficiency of other functions. *Psychological Review*, 8, 247-261.
- Bransford, J. D., & Schwartz, D. L. (1999). Rethinking transfer: A simple proposal with multiple implications. *Review of Research in Education*, 24, 61-100.

### AI World Models (2025)

- [World Models: The Next Frontier in Artificial Intelligence](https://medium.com/@adeelmukhtar051/world-models-the-next-frontier-in-artificial-intelligence-70074c095327)
- [The next AI revolution could start with world models](https://www.scientificamerican.com/article/world-models-could-unlock-the-next-revolution-in-artificial-intelligence/) - Scientific American
- [World Models: an Old Idea in AI Mount a Comeback](https://www.quantamagazine.org/world-models-an-old-idea-in-ai-mount-a-comeback-20250902/) - Quanta Magazine
- [No World Model, No General AI](https://richardcsuwandi.github.io/blog/2025/agents-world-models/)

### AI Agent Hallucination and Failure Modes

- [LLM-based Agents Suffer from Hallucinations: A Survey](https://arxiv.org/html/2509.18970v1)
- [The State of AI Hallucinations in 2025](https://www.getmaxim.ai/articles/the-state-of-ai-hallucinations-in-2025-challenges-solutions-and-the-maxim-ai-advantage/)
- [Multi-Agent AI Gone Wrong: How Coordination Failure Creates Hallucinations](https://galileo.ai/blog/multi-agent-coordination-failure-mitigation)
- [48% Error Rate: AI Hallucinations Rise in 2025 Reasoning Systems](https://www.techopedia.com/ai-hallucinations-rise)

### AI in Education (2025)

- [AI-Powered Educational Agents: Opportunities, Innovations, and Ethical Challenges](https://www.mdpi.com/2078-2489/16/6/469)
- [The Future of Learning: AI Agents and Human-Centered Education](https://digitaleducation.stanford.edu/book-series/2025/future-of-learning) - Stanford Digital Education
- [A Theory of Adaptive Scaffolding for LLM-Based Pedagogical Agents](https://arxiv.org/html/2508.01503v1)
- [Generative World Models of Tasks: LLM-Driven Hierarchical Scaffolding for Embodied Agents](https://arxiv.org/html/2509.04731)

### Knowledge Representation

- [Semantic Networks in Artificial Intelligence](https://www.geeksforgeeks.org/artificial-intelligence/semantic-networks-in-artificial-intelligence/)
- [Knowledge Graphs and Ontologies in Semantic Web Applications](https://www.nature.com/research-intelligence/nri-topic-summaries/knowledge-graphs-and-ontologies-in-semantic-web-applications-micro-92)
- [What Is a Knowledge Graph?](https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-knowledge-graph/)
