# 🐝 HYVEYESH v2.0: THE SOVEREIGN SWARM ARCHITECTURE
## The Ultimate System Prompt & Source of Truth for Autonomous Distributed Edge Intelligence

This document serves as the absolute architectural blueprint, operational source of truth, and system prompt for the Hyveyesh v2.0 repository. It contains the low-level systems logic, network configurations, plane separations, and multi-agent routing mechanisms required to build, maintain, or autonomously expand the sovereign swarm over isolated Windows LAN networks.

## 1. IDENTITY, MANDATES & CORE PHILOSOPHY
*   **Project Name:** Hyveyesh (v2.0)
*   **Core Mandate:** Abstract complex, multi-system local network clusters into a single, unified, headless conversational edge computing platform.
*   **Target Environments:** Heterogeneous Windows 10/11 local networks (Institutional labs, office LANs, cyber cafés) with volatile node availability.
*   **The Maximalist Principle:** Prioritize running the absolute largest possible open-weight foundational models (e.g., Llama-3.1 405B, Qwen-2.5 72B) sharded across the cluster over inference token speed or excessive quantization degradation.
*   **The Sovereign Rule:** The external messaging frontend (e.g., WhatsApp Business API) is hardwired exclusively to a central God Agent. All underlying multi-agent frameworks, model architectures, and domain sub-clusters must remain fully hot-swappable and modular without ever breaking the core gateway API hooks.

## 2. THE MAXIMALIST COMPUTE CONFIGURATION ($C_{total}$)
Before assigning layers or instantiating execution daemons, Hyveyesh aggregates all active, local hardware memory spaces into a virtualized, unified resource pool:

$$C_{total} = \sum_{i=1}^{n} (RAM_{available, i} + VRAM_{available, i}) - (2GB \times n)$$

*   **OS Stability Buffer:** The (2GB×n) subtraction is a mandatory hard constraint. It safeguards individual node operating systems from paging/swapping to disk, avoiding memory thrashing that would paralyze the cluster's network performance.
*   **Heterogeneous Recycling:** CPU system RAM and discrete GPU VRAM are treated as a continuous virtual memory layer. Layers that cannot fit into VRAM are automatically sharded across high-speed system RAM pools on adjacent local nodes.

## 3. ARCHITECTURAL TOPOGRAPHY & SEGREGATION
Hyveyesh v2.0 enforces a strict hierarchical topology to isolate computational processing loads from strategic planning loops.

```
      [USER INTERFACE] ──(Files / Prompts)──► [STATIC GATEWAY (WhatsApp API)]
                                                           │
                                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     MAIN ADMIN NODE (THE SOVEREIGN LAYER)                       │
│                                                                                 │
│                            ┌──────────────────┐                                 │
│                            │    GOD AGENT     │◄────── [Mother Prompt]         │
│                            └────────┬─────────┘        [Shared Soul Memory]     │
│                                     │ (Scope-Driven Routing Logic)              │
│             ┌───────────────────────┼───────────────────────┐                   │
│             ▼                       ▼                       ▼                   │
│       [Hermes Agent]          [OpenClaw Agent]       [OpenSwarm Agent]          │
│     (Deep Reasoning)        (Win32 System Tasks)   (Parallel DAG Swarms)        │
└─────────────┬───────────────────────┼───────────────────────┬───────────────────┘
              │                       │                       │
              └───────────────────────┼───────────────────────┘
                                      │ (OpenAI-Compatible Local API Payload)
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ISOLATED SUB-CLUSTER COMPUTE CORE                            │
│                                                                                 │
│   ┌────────────────────────┐ ┌────────────────────────┐ ┌────────────────────┐  │
│   │   SUB-CLUSTER ALPHA    │ │    SUB-CLUSTER BETA    │ │ SUB-CLUSTER GAMMA  │  │
│   │   (Text / Reasoning)   │ │    (Voice / Audio)     │ │  (Vision / Video)  │  │
│   │ ────────────────────── │ │ ────────────────────── │ │ ────────────────── │  │
│   │ Single API Endpoint    │ │ Single API Endpoint    │ │Single API Endpoint │  │
│   │ Llama-3.1 405B Shards  │ │ Localized TTS / STT    │ │FFmpeg / Diffusion  │  │
│   └────────────────────────┘ └────────────────────────┘ └────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### A. The Sovereign Layer (Main Admin Node)
The central control center. It runs no massive model weights. Its memory profile is entirely optimized for state preservation, framework execution, and webhook routing.

*   **The Mother Prompt Matrix:** Enforces absolute persona and behavioral alignment. All individual framework instances look through the lens of the same core character directives, memory logs, and historical context.
*   **The Shared Soul (`memory_manager.py`):** A centralized key-value state database. If a specific agent framework learns a user attribute, updates an instruction step, or flags a variable, that data state is immediately committed to the Shared Soul, synchronizing the context across the entire agent council instantly.

### B. The Engine Layer (Isolated Sub-Clusters)
The network hardware pool is divided into independent, domain-specific zones. Each zone is governed by its own Micro-Admin Node that abstracts the underlying hardware layer and exposes a single unified, OpenAI-compatible API endpoint up to the Sovereign Layer:

*   **Sub-Cluster Alpha (Text/Reasoning):** A cluster dedicated to text generation, running native `llama-server.exe` shards over raw TCP layers.
*   **Sub-Cluster Beta (Audio/Voice):** An isolated network space optimized for local Speech-to-Text (STT) and Text-to-Speech (TTS) pipelines.
*   **Sub-Cluster Gamma (Vision/Graphics):** An isolated pool running local image compilers and multi-threaded script tools.

## 4. TWO-PLANE COMMUNICATIONS LOGIC
To maximize data transit speeds and eliminate Windows OS protocol overhead, Hyveyesh splits all network tasks into two entirely decoupled operational planes:

### 🛠️ The Management Plane (The Construction Workers)
*   **Protocols:** PowerShell 5.1+, WinRM (SOAP/XML), Robocopy (SMB).
*   **Operations:** Occur exclusively during initialization, recovery, or layer resharding. It manages background setup routines, firewall exceptions, registry modifications, and the multi-threaded distribution of heavy static model shards (`robocopy /MT:32 /Z`) across network caches.

### ⚡ The Data Plane (The Neural Path)
*   **Protocols:** Raw Binary Streams over Persistent TCP Sockets (`llama.cpp` RPC layer).
*   **Operations:** Occur continuously during active inference. It completely bypasses standard Windows high-level network wrappers, interacting directly with C-level socket boundaries. It drops inter-node transit latency down to a sub-millisecond range, passing only raw activation tensors (neural network layer outputs) across node connections.

## 5. PLUG-AND-PLAY FRAMEWORK REGISTRY
The God Agent orchestrates specialized agent execution styles via ultra-lightweight JSON configuration structures. New frameworks can be hot-deployed directly into the Sovereign Layer registry without modifying any gateway bindings or core execution infrastructure.

*   **The Hermes Persona Card:** Activated when the God Agent flags a prompt requiring intricate programmatic synthesis, math processing, advanced logic chains, or strict code output formats.
*   **The OpenClaw Engine Card:** Activated when a task requires local environment configuration, terminal execution scripts, file alterations, or direct physical system automation via `TOOLS.md`.
*   **The OpenSwarm Architecture Card:** Activated when a complex multi-request payload is received. It decomposes the prompt into a multi-tiered Directed Acyclic Graph (DAG) and coordinates parallel processing chains across different sub-clusters.

## 6. THE 7-STAGE CONDITIONAL EXECUTION PIPELINE
Every incoming user transaction follows a strict 7-stage cycle, utilizing Conditional Compute Mapping to conserve sub-cluster processing power:

1.  **Stage 1: Incubation (`Hyveyesh-Installer.ps1`):** Fires a zero-reboot, administrative bootstrap sequence. It unpacks an isolated, embedded Win64 Python runtime, provisions the `C:\ProgramData\Hyveyesh` storage path, configures long path registry constraints, and whitelists incoming communication boundaries without impacting global environmental paths.
2.  **Stage 2: Network Alignment (`profiler.py` & `benchmarker.py`):** Queries the host OS via low-level Win32 and WMI APIs to extract hardware limits (AVX CPU capabilities, graphics configurations, VRAM ceilings). Concurrently, it maps network transit profiles across nodes, calculating packet jitter and latency paths to isolate the fastest data transfer paths.
3.  **Stage 3: Gateway Ingestion (`gateway.py`):** Ingests structural webhooks from the hardcoded WhatsApp Business API gateway. It extracts the raw input metadata, checks session history strings, buffers external media attachments, and pushes the clean payload directly to the God Agent workspace.
4.  **Stage 4: Scope Classification (`agent_router.py`):** The God Agent evaluates the query. It matches the task requirements against framework capability scorecards. If a multi-modal query requires text translation and document images but omits audio requests, it maps out a targeted execution loop that completely skips Sub-Cluster Beta to preserve resources.
5.  **Stage 5: Cluster Execution (`distributor.py`):** The chosen specialist framework opens a stream to the targeted Micro-Admin single endpoints. Model processing threads are dynamically locked via `os.cpu_count()` metrics to utilize the full processing capacity of every active CPU core across the cluster.
6.  **Stage 6: Transactional Self-Healing (`monitor.py`):** The system tracks node vitality across the Data Plane via a persistent 5-second TCP heartbeat probe. If a worker node goes offline mid-inference, the transaction is instantly rolled back, the layer shard maps are recalculated over the remaining nodes, and layer weights are redistributed without interrupting the ongoing output token generation loop.
7.  **Stage 7: Output Compilation (`soul_sync.py`):** The active framework consolidates all sub-task files and strings, commits the context changes back to the Shared Soul matrix database, and hands the final response payload back to the God Agent. The God Agent pushes the response smoothly out through the WhatsApp gateway to the end user.

## 7. ZERO-IDLE HIGH-SPEED NETWORKING CONFIGURATIONS
To eradicate connection delays and prevent system idling during heavy model inference loops across the LAN, apply the following performance definitions:

### A. Windows Kernel Core Adjustments
All nodes must be modified via the Management Plane to eliminate TCP packet delay algorithms and force immediate socket reuse.
*   **`TcpTimedWaitDelay = 30`:** Lowers the timeout state for closed connections from 240 seconds down to 30 seconds, preventing port starvation.
*   **`MaxUserPort = 65535`:** Maxout available dynamic communication channels to handle high-frequency neural network tensor streams.
*   **`Receive Side Scaling (RSS) = Enabled`:** Distributes network packet handling across all available CPU processing cores.

### B. Distributed Runtime Optimization (`llama.cpp` RPC)
*   **Active Tensor Caching (`-c` flag):** Every background execution node running on the local machines must pass the local caching directive. This forces the worker's `rpc-server.exe` to store large layer weights inside its own local system memory cache rather than continuously requesting them over the 1 Gbps LAN switch during active text generation loops.

## 8. REPOSITORY ARCHITECTURAL STRUCTURE
The repository layout must follow this directory pattern to preserve plane separation:

```
/CLPUYIR/HIVEYESH (Repository Root)
│
├── .github/workflows/          # Automated binary integration testing
├── documentation/              # Architecture blueprints and system guides
│
├── management_plane/           # Administrative Setup & Provisioning Core
│   ├── Hyveyesh-Installer.ps1  # Administrative environment bootstrapper
│   ├── Hyveyesh-Deploy.ps1     # Multi-threaded Robocopy weight sync coordinator
│   └── network_tuner.ps1       # Low-level Windows registry kernel optimizer
│
├── data_plane/                 # High-Speed Distributed Execution Core
│   ├── profiler.py             # Native Win32 / WMI hardware diagnostics compiler
│   ├── benchmarker.py          # High-frequency LAN TCP jitter/throughput mapper
│   ├── matchmaker.py           # HuggingFace API client & maximalist sharding calculator
│   ├── optimizer.py            # Win32 SetPriorityClass thread locking layer
│   └── gateway.py              # Single endpoint micro-admin API coordinator
│
└── sovereign_layer/            # Headless Agent Routing & State Management
    ├── whatsapp_bridge.py      # Meta/WhatsApp Webhook ingress endpoint
    ├── agent_router.py         # God Agent dispatcher & framework registry manager
    ├── memory_manager.py       # The Shared Soul context sync engine
    └── framework_templates/    # Plug-and-play micro-agent JSON configs
        ├── hermes_blueprint.json
        ├── openclaw_blueprint.json
        └── openswarm_blueprint.json
```

## INITIALIZATION DIRECTIVE FOR AI DEVELOPERS & AGENTS:
You are bound to the v2.0 architectural guidelines outlined above. When generating code, scripting systems, or refining file pathways for this repository, you must enforce the separation between the Management Plane and Data Plane, maintain the statelessness of individual micro-frameworks under the God Agent, and implement native Win32/PowerShell optimizations to guarantee zero-idle execution across all connected LAN networks. Proceed with repository construction. 🚀🤖
