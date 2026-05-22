# 🐝 Hyveyesh v2.0: Sovereign Swarm Development Mandates

## Core Directives
All development within this repository MUST adhere to the following architectural rules:

1.  **Plane Separation:** Keep the **Management Plane** (PowerShell, provisioning) strictly decoupled from the **Data Plane** (Python, high-speed inference).
2.  **Sovereign Layer Integrity:** The **God Agent** in the Sovereign Layer is the only entity that interacts with the external Gateway (WhatsApp). All other agents are internal sub-frameworks.
3.  **The Shared Soul:** All persistent state and user context MUST be managed via `memory_manager.py`. No agent should maintain local persistent state.
4.  **Maximalist Compute:** Prioritize model size over inference speed. Calculate $C_{total}$ using the formula: $C_{total} = \sum (RAM + VRAM) - (2GB \times n)$.
5.  **Native Optimization:** Utilize native Win32/WMI calls for hardware profiling and performance (e.g., `SetPriorityClass`).

## Directory Structure Source of Truth
- `/management_plane/`: Provisioning, registry tuning, weight distribution.
- `/data_plane/`: Profiling, benchmarking, distributed execution, micro-admin gateways.
- `/sovereign_layer/`: God Agent routing, memory management, agent framework configs.

## Validation Checklist
- [ ] Does this change respect the 2GB OS stability buffer?
- [ ] Does this network call bypass high-level OS wrappers in the Data Plane?
- [ ] Is this new agent framework defined as a lightweight JSON blueprint?
- [ ] Are all state changes committed to the Shared Soul?

Refer to `documentation/BLUEPRINT.md` for the full architectural specification.
