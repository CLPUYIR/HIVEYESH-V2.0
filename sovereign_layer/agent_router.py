#!/usr/bin/env python3
"""
Hyveyesh v2.0: Sovereign Swarm Architecture
File: sovereign_layer/agent_router.py
Purpose: God Agent execution routing, zero-latency scope classification, 
         and conditional compute mapping down to isolated sub-clusters.
"""

import os
import sys
import json
import re
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Core Infrastructure Performance Configurations
# Force win32 process priority class adjustment to avoid OS scheduler delays
if sys.platform == "win32":
    try:
        import win32api
        import win32process
        import win32con
        pid = win32api.GetCurrentProcessId()
        handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
        win32process.SetPriorityClass(handle, win32process.ABOVE_NORMAL_PRIORITY_CLASS)
        print("[HYVEYESH v2.0] Sovereign Router locked to ABOVE_NORMAL priority class.")
    except ImportError:
        print("[HYVEYESH v2.0] Optional win32 library missing. Proceeding with standard priority.")

class GodAgentRouter:
    def __init__(self, repo_root: str = None):
        # Resolve path abstractions
        self.repo_root = Path(repo_root) if repo_root else Path(__file__).resolve().parent.parent
        self.template_dir = self.repo_root / "sovereign_layer" / "framework_templates"
        
        # Sub-Cluster Isolated Micro-Admin Endpoints
        self.endpoints = {
            "ALPHA": "http://sub-admin-alpha:8080/v1/chat/completions", # Text / Core Brain
            "BETA":  "http://sub-admin-beta:8081/v1/audio",             # Voice / Audio Tasks
            "GAMMA": "http://sub-admin-gamma:8082/v1/vision"            # Imaging / Video Rendering
        }
        
        print(f"[HYVEYESH v2.0] Sovereign Router Initialized. Root: {self.repo_root}")

    def _load_blueprint(self, framework_name: str) -> Dict[str, Any]:
        """Loads the plug-and-play JSON agent config blueprint dynamically."""
        blueprint_path = self.template_dir / f"{framework_name}_blueprint.json"
        if not blueprint_path.exists():
            # Fallback inline generation if file layout template has not been written
            default_blueprints = {
                "hermes": {"name": "Hermes", "capability": "reasoning", "target": "ALPHA"},
                "openclaw": {"name": "OpenClaw", "capability": "automation", "target": "ALPHA"},
                "openswarm": {"name": "OpenSwarm", "capability": "multimodal_dag", "target": "ALPHA"}
            }
            return default_blueprints.get(framework_name, {"name": "Generic", "target": "ALPHA"})
        
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def classify_scope(self, prompt: str, attachments: List[str] = None) -> Tuple[str, List[str]]:
        """
        Zero-latency Scope Classification Engine.
        Evaluates input features to assign the framework blueprint and map
        conditional compute targets—safeguarding inactive clusters from idle waste.
        """
        clean_prompt = prompt.lower()
        attachments = attachments or []
        
        # Determine required physical execution pools (Alpha is always active for token reasoning)
        active_clusters = ["ALPHA"]
        
        # Conditional Audio Sub-Cluster Mapping (Beta)
        audio_signals = r'(audio|voice|speak|mp3|tts|stt|listen|podcast|speech|sound)'
        if re.search(audio_signals, clean_prompt):
            active_clusters.append("BETA")
            
        # Conditional Vision/Video Sub-Cluster Mapping (Gamma)
        vision_signals = r'(video|image|ocr|png|jpg|jpeg|mp4|draw|render|canvas|answer sheet|frames)'
        has_media_file = any(ext in ['.png', '.jpg', '.jpeg', '.mp4'] for ext in [os.path.splitext(a)[1].lower() for a in attachments])
        if re.search(vision_signals, clean_prompt) or has_media_file:
            active_clusters.append("GAMMA")

        # Framework Matrix Selection Architecture
        if len(active_clusters) > 1:
            # Complex, cross-domain request requires multi-agent workflow tree splitting
            assigned_framework = "openswarm"
        elif any(keyword in clean_prompt for keyword in ["run", "script", "file", "cmd", "powershell", "execute", "system"]):
            # System tasks requiring direct terminal automation pipelines
            assigned_framework = "openclaw"
        else:
            # Deep logical reasoning, code analytics, and algorithmic execution sequences
            assigned_framework = "hermes"

        return assigned_framework, list(set(active_clusters))

    def _query_inference_core(self, endpoint_url: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Dispatches binary token blocks down to unified sub-cluster entry points over raw TCP paths."""
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            endpoint_url, 
            data=data, 
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.URLError as e:
            print(f"[HYVEYESH CRITICAL] Sub-cluster Connection Failure on {endpoint_url}: {e}")
            return {"error": True, "message": str(e)}

    def route_transaction(self, session_id: str, prompt: str, attachments: List[str] = None) -> Dict[str, Any]:
        """
        Main execution gateway. Interlaces context through the Mother Prompt,
        orchestrates specialized agent state adjustments, and passes output back.
        """
        print(f"\n[HYVEYESH v2.0] Ingesting Request for Session: {session_id}")
        
        # 1. Interface with the Shared Memory Matrix ("The Soul")
        # In a complete installation, this imports and instantiates memory_manager.py
        # Fallback tracking implemented via mock mapping to maintain zero-idle performance during early repo phases
        shared_soul_context = f"[SESSION_ID: {session_id}] System Mode: Active Sovereign Loop."

        # 2. Scope Analytics
        framework_choice, target_clusters = self.classify_scope(prompt, attachments)
        blueprint = self._load_blueprint(framework_choice)
        
        print(f"[HYVEYESH v2.0] Routing Decision: framework={framework_choice.upper()} | Target Clusters={target_clusters}")

        # 3. Construct Unified Inference Payload bound to the Mother Prompt instructions
        mother_prompt_wrapper = (
            "System Identity: You are operating as the specialized execution lens of the Hyveyesh Swarm. "
            f"Role Directives: Ensure output aligns strictly with the {blueprint.get('name')} architectural blueprint. "
            f"Shared Soul Context State: {shared_soul_context}\n"
            f"User Objective Input: {prompt}"
        )

        # 4. Conditional Compute Execution Execution Loop
        if framework_choice == "openswarm":
            print("[HYVEYESH v2.0] OpenSwarm execution triggered. Commencing procedural DAG pipeline parsing...")
            # Deconstruct multimodal pipeline paths across isolated clusters sequentially
            text_result = self._query_inference_core(self.endpoints["ALPHA"], {
                "model": "distributed-maximal-core",
                "messages": [{"role": "user", "content": mother_prompt_wrapper}]
            })
            
            # Extract content text safely from openai completions object schema
            text_content = text_result.get("choices", [{}])[0].get("message", {}).get("content", "Error parsing swarm text layers.")
            final_output = {"text": text_content, "generated_assets": []}
            
            # Pipeline Pass: Coordinate asset compiling downstream via Sub-Cluster Gamma if isolated flag matches
            if "GAMMA" in target_clusters:
                print("[HYVEYESH v2.0] Shifting execution context payload downstream to Sub-Cluster Gamma for asset synthesis.")
                gamma_payload = {"task": "generate_renderings", "source_context": text_content, "session": session_id}
                gamma_result = self._query_inference_core(self.endpoints["GAMMA"], gamma_payload)
                if not gamma_result.get("error"):
                    final_output["generated_assets"].append(gamma_result.get("output_asset_url", "local_render_complete.png"))
            
            return final_output

        else:
            # Fast-path singular request handling via target cluster micro-admin endpoint
            target_node = blueprint.get("target", "ALPHA")
            endpoint = self.endpoints.get(target_node, self.endpoints["ALPHA"])
            
            inference_payload = {
                "model": "distributed-maximal-core",
                "messages": [{"role": "user", "content": mother_prompt_wrapper}],
                "temperature": 0.3 # Low entropy default to maximize systemic tool precision
            }
            
            raw_response = self._query_inference_core(endpoint, inference_payload)
            content = raw_response.get("choices", [{}])[0].get("message", {}).get("content", "Execution chain completed with no return token values.")
            
            return {"text": content, "generated_assets": []}

# Local Testing Execution Verification Block
if __name__ == "__main__":
    router = GodAgentRouter()
    
    # Mock Challenge 1: Pure Mathematical Linear Algebra Request
    test_prompt_1 = "Compute the singular value decomposition of a 4x4 matrix and optimize code lines."
    agent, clusters = router.classify_scope(test_prompt_1)
    assert agent == "hermes" and clusters == ["ALPHA"], "Failed Pure Logic Scope Mapping"
    
    # Mock Challenge 2: Deep Cross-Domain Multimodal Request (Matches user specification case)
    test_prompt_2 = "OCR this exam sheet image, translate the questions to English, write an answer sheet canvas graphic and render an instructional tutorial mp4 file."
    agent_2, clusters_2 = router.classify_scope(test_prompt_2, ["source_sheet.png"])
    assert agent_2 == "openswarm" and "GAMMA" in clusters_2, "Failed Multi-Modal Swarm DAG Mapping"
    
    print("\n[HYVEYESH v2.0] All integrated routing scope sanity tests passed successfully. Ready for runtime integration loop. 🚀")
