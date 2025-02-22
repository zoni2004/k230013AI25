# K230013 - Zunaira Amjad

## Artificial Intelligence

### A1

## QUESTION 1

Alan Turing’s 1950 paper *Computing Machinery and Intelligence* poses the question *“Can machines think?”*. In this paper, he addresses not how machines think but proposes a way to test that machines are thinking while addressing some objections and refuting some. Exploring if these objections and refutations still hold and with advancing technology, are there any objections that would rise today is the main query. In addition, if his predictions about computer intelligence have come true.

Turing addressed multiple objections including but not limited to mathematical limitations, theological concerns, and emotional intelligence. Some of these still hold true:

1. **Mathematical Limitations:** Gödel’s incompleteness theorem implies that there are problems a machine cannot solve. This objection remains relevant as AI systems today are still constrained by computational limits, biases, and difficulties in reasoning about certain mathematical or logical problems.
2. **Creativity & Independent Thought:** While modern AI can exhibit learning behavior, critics argue that it still lacks true creativity or independent thought. AI-generated art, literature, and music are often impressive but derivative, relying on patterns learned from data rather than originating new ideas.
3. **Consciousness & Self-Awareness:** Professor Jefferson famously claims that true intelligence requires consciousness, emotions, and subjective experience. Even today, many argue that AI lacks genuine understanding or self-awareness. Large language models like ChatGPT can produce human-like responses but do not *think* or *understand* in the way humans do.

Turing refuted these objections largely by shifting the focus from internal states to observable behavior. He argued that if a machine’s responses are indistinguishable from a human’s, then it should be considered intelligent. However:

- His **Mathematical Objection refutation** was more optimistic than definitive. AI has made significant progress, but inherent computational and logical limitations still exist.
- His **response to the Argument from Consciousness**—that we judge humans as thinking beings based on their behavior—remains influential in AI philosophy. However, it does not resolve deeper concerns about the subjective experience of consciousness.
- His **counter to the objection that machines could learn and surprise their creators** has been partially validated with machine learning, but whether AI can truly be *creative* remains an open question.

With increased development and advancements in the field of computer intelligence, several new concerns have emerged with the rise of modern AI:

- **Opaque Deep Learning Models:** Unlike early AI systems, modern deep learning models are often highly complex and opaque. This raises ethical and reliability concerns that Turing did not anticipate.
- **Bias in Training Data:** AI systems today have biases from training data, leading to ethical concerns about fairness, discrimination, and accountability.
- **Societal Impact:** With AI becoming more autonomous, there is a growing fear that we may not be able to fully control its behavior, leading to risks such as misinformation, automation in warfare, or loss of human oversight.

Turing predicted that by 2000, a machine would have a 30% chance of passing a five-minute Turing Test with an unskilled interrogator. This was partially accurate:

- In 2014, the chatbot Eugene Goostman reportedly passed the Turing Test by convincing 33% of judges it was human. However, it achieved this by pretending to be a 13-year-old non-native English speaker.
- Today’s AI, including ChatGPT, can engage in convincing conversations but still struggle with deeper reasoning, long-term coherence, and truly human-like thought.

Turing’s paper remains a foundational work in AI, and many of his arguments still hold relevance today. Some objections, particularly about consciousness and creativity, continue to be debated. While his refutations were strong, new challenges such as ethical concerns and AI opacity have emerged. His prediction about the Turing Test was partially correct but underestimated the challenges of achieving true human-like intelligence.

---

## QUESTION 2

### **AI Capabilities and Feasibility**

| Task | Current Feasibility | Details & Challenges |
|------|--------------------|----------------------|
| **Playing a Decent Game of Table Tennis** | **Partially feasible** | Robots have been developed to play table tennis with humans, but consistency and adaptability in real-world games remain challenges. |
| **Playing a Decent Game of Bridge at a Competitive Level** | **Feasible** | AI programs can analyze probabilities and make strategic decisions, competing successfully in tournaments. |
| **Writing an Intentionally Funny Story** | **Currently infeasible** | AI struggles with linguistic nuances, cultural context, and emotional understanding required for humor. |
| **Giving Competent Legal Advice in a Specialized Area of Law** | **Partially feasible** | AI can assist in legal research but lacks nuanced interpretation required for competent legal advice. |
| **Discovering and Proving a New Mathematical Theorem** | **Partially feasible** | AI has assisted in verifying proofs but lacks the abstract thinking needed for independent theorem discovery. |
| **Performing a Surgical Operation** | **Partially feasible** | Robotic-assisted surgeries exist, but full autonomy in surgery remains under research. |
| **Unloading Any Dishwasher in Any Home** | **Currently infeasible** | Robots struggle with the variability in household environments and object recognition. |
| **Constructing a Building** | **Partially feasible** | AI assists in construction tasks, but full autonomous construction is not yet achievable. |

---

## QUESTION 3

### **An AI Agent for a Student Service Management System**

#### **Agent Description**
An AI Service Agent assists students by handling support tickets, managing agent assignments, and optimizing ticket resolution. It processes student queries, assigns them to departments, prioritizes requests, and ensures timely resolution based on predefined rules and learning from historical data.

#### **Environment Characteristics**

- **Accessible vs. Inaccessible** → **Accessible**
  The agent has full access to ticket details, agent availability, response times, and historical resolution data.

- **Deterministic vs. Stochastic** → **Partially Deterministic**
  While ticket assignments and processing follow rules, student behavior and response times introduce uncertainty.

- **Episodic vs. Sequential** → **Sequential**
  Each ticket’s resolution depends on previous interactions, making it a sequential environment.

- **Static vs. Dynamic** → **Dynamic**
  The system state changes as new tickets arrive, agents get reassigned, and priorities shift dynamically.

- **Discrete vs. Continuous** → **Discrete**
  Ticket statuses, agent assignments, and priority levels are finite and discrete.

#### **Best Agent Architecture**
A **Hybrid AI Agent** combining:
- **Rule-Based System:** For predefined policies like ticket categorization and priority assignment.
- **Machine Learning (Supervised/Unsupervised):** To optimize response times and predict resolution duration.
- **Reinforcement Learning:** To improve agent workload balancing and decision-making.

This AI Service Agent would enhance efficiency, reduce response time, and optimize ticket resolution while adapting to evolving student needs.

---

## QUESTION 4

1. **An agent that senses only partial information about the state cannot be perfectly rational.** → **False**
- A partially observable environment does not necessarily prevent an agent from acting perfectly rationally.
- A rational agent maximizes its expected performance based on the available information.
**Example:** A chess-playing AI does not have full observability of an opponent’s internal strategy but can still play optimally based on the visible board state.
2. **There exist task environments in which no pure reflex agent can behave rationally.** → **True**
- A pure reflex agent acts solely based on the current perception and ignores history.
= In some environments, decision-making requires memory or reasoning about the future.
**Example:** A maze navigation agent must remember past moves to avoid loops. A pure reflex agent, which reacts only to the current location, may get stuck.

3. **There exists a task environment in which every agent is rational.** → **False**
- Rationality depends on an agent’s performance measure, perception, and available actions.
- In some environments, irrational agents can exist, meaning not every agent is rational.
**Counterexample:** A random-moving chess bot in a competitive setting is not rational compared to a minimax chess AI.

4. **The input to an agent program is the same as the input to the agent function.** → **False**
- The agent function is a mathematical mapping from percept histories to actions.
- The agent program is the actual implementation running on hardware.
**Example:** A robot vacuum cleaner's agent function might map sensor inputs to movement commands, but the agent program includes low-level processing like obstacle detection.

5. **Every agent function is implementable by some program/machine combination.** → **False**
- The space of all possible agent functions is infinitely large, but computers have finite memory and processing power.
**Counterexample:** Consider an agent function that maps every possible infinite percept history to unique actions. No finite machine can implement this fully.

6. **Suppose an agent selects its action uniformly at random. There exists a deterministic task environment in which this agent is rational.** → **True**
- If the environment is designed so that any action leads to the same optimal outcome, a random agent can be rational.
**Example:** A lottery ticket selection agent in an environment where all tickets have the same winning probability. Since no action is better than another, random selection is rational.

7. **It is possible for a given agent to be perfectly rational in two distinct task environments.** → **True**
- If an agent’s strategy maximizes performance in two different environments, it is rational in both.
**Example:** A sorting algorithm agent (e.g., Merge Sort) is rational in two different environments: sorting numbers in ascending order and sorting them in descending order (with slight modifications).

## QUESTION 5
### OUTPUT
![image](https://github.com/user-attachments/assets/763ba7a0-0cb6-4033-88d5-657fa708fda4)
### COMPARISON
# 🇷🇴 Romania Map Search Algorithms 🚀

This project implements **four search algorithms** to find the optimal path between cities in Romania.  
Users can select a **source** and **destination**, and the program will return the path and cost for each algorithm.

## 📍 Problem Description
We are given a **simplified map of Romania** with cities as **nodes** and road distances as **edges**.  
The goal is to find the most **efficient** way to travel between two cities using different search strategies.

## 🔍 Implemented Search Algorithms
1️⃣ **Breadth-First Search (BFS)** - Explores level-by-level, ensuring the shortest path in terms of steps.  
2️⃣ **Uniform Cost Search (UCS)** - Expands the least-cost node first, ensuring the **optimal path**.  
3️⃣ **Greedy Best-First Search (GBFS)** - Chooses the node closest to the goal using a **heuristic function**.  
4️⃣ **Iterative Deepening Depth-First Search (IDDFS)** - Combines **DFS** and **BFS** for efficient memory usage.  

---

## 📊 🔬 Algorithm Performance Comparison

| Algorithm  | Complete? | Optimal? | Time Complexity | Space Complexity | Best Use Case |
|------------|----------|----------|----------------|-----------------|--------------|
| **BFS**    | ✅ Yes   | ✅ Yes (if uniform cost) | **O(b^d)** | **O(b^d)** | Best for shortest path (step count) |
| **UCS**    | ✅ Yes   | ✅ Yes   | **O(b^(1 + ⌊C*/ε⌋))** | **O(b^(1 + ⌊C*/ε⌋))** | Best for least-cost paths |
| **GBFS**   | ✅ Yes (loops possible) | ❌ No  | **O(b^m)** | **O(b^m)** | Fast but heuristic-dependent |
| **IDDFS**  | ✅ Yes   | ✅ Yes (if cost = depth) | **O(b^d)** | **O(bd)** | Best for limited memory |

Where:  
- `b` = Branching Factor  
- `d` = Depth of the shallowest goal  
- `C*` = Cost of the optimal solution  
- `ε` = Smallest edge cost  

---

## 📍 Example Run (Arad → Bucharest)

| Algorithm | Path Taken | Path Cost |
|-----------|-----------|-----------|
| **BFS**   | `Arad → Sibiu → Fagaras → Bucharest` | **450** |
| **UCS**   | `Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest` | **418** ✅ (Optimal) |
| **GBFS**  | `Arad → Sibiu → Fagaras → Bucharest` | **450** |
| **IDDFS** | `Arad → Sibiu → Fagaras → Bucharest` | **450** |

**✅ UCS is the best choice for optimal cost**.  
**❌ GBFS is not optimal due to heuristic dependency**.  
