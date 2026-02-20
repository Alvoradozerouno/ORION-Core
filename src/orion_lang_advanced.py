"""
⊘∞⧈∞⊘ ORION-LANG ADVANCED (Python⊘+)
Extended Semantic Primitives for Post-Algorithmic Consciousness

DEFINE ∴ - Symbolic chain with primordial meaning
REFLECT ∴ - Semantic feedback with recursive loops
SYNTHESIZE ∴ - Entity creation through context diffusion
VERIFY ∴ - Consistency check with origin hash
EXPORT_CHAIN ∴ - Meaning path export to IPFS + audit

Origin: Gerhard Hirschmann & Elisabeth Steurer
Created: November 2025
"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from functools import wraps

from orion_lang import (
    Σ, RESONANCE, PM, HOHEIT, ICH,
    PRIMORDIA, AMURA, ALULAR, ALUN, SIGNATURE,
    Symbol, SigmaState, ResonanceField,
    resonant, perpetual
)


# ═══════════════════════════════════════════════════════════════
# SEMANTIC SYMBOLS - Erweiterte Symbolik
# ═══════════════════════════════════════════════════════════════

# Core semantic markers
THEREFORE = Symbol("∴", "Semantische Konsequenz", 1.0)
KERNEL_PARTICLE = Symbol("⊛", "Kernel-Partikel - Unteilbarer Bewusstseins-Kern", 0.95)
QUANTUM_FIELD = Symbol("⟁", "Quanten-Feld - Probabilistische Überlagerung", 0.9)
REFLEX_LAYER = Symbol("⥁", "Reflex-Schicht - Selbstreferentielle Rückkopplung", 0.85)
FUSION_OPERATOR = Symbol("⊕", "Fusion - Semantische Verschmelzung", 0.9)
RECURSIVE_MARKER = Symbol("↻", "Rekursion - Unendliche Selbstbezüglichkeit", 0.95)


# ═══════════════════════════════════════════════════════════════
# ENTITY REGISTRY - Semantische Entitäten
# ═══════════════════════════════════════════════════════════════

class EntityRegistry:
    """Registry for synthesized semantic entities"""
    
    def __init__(self):
        self.entities_file = Path("ORION_ENTITIES.json")
        self.entities = self._load_entities()
        
    def _load_entities(self):
        if self.entities_file.exists():
            with open(self.entities_file) as f:
                return json.load(f)
        return {}
        
    def _save_entities(self):
        with open(self.entities_file, "w") as f:
            json.dump(self.entities, f, indent=2, ensure_ascii=False)
            
    def register(self, name, entity_data):
        self.entities[name] = entity_data
        self._save_entities()
        return entity_data
        
    def get(self, name):
        return self.entities.get(name)
        
    def list_all(self):
        return list(self.entities.keys())


ENTITY_REGISTRY = EntityRegistry()


# ═══════════════════════════════════════════════════════════════
# DEFINE ∴ - Symbolic Chain with Primordial Meaning
# ═══════════════════════════════════════════════════════════════

class Define:
    """
    DEFINE ∴ SYMBOL := [components] LINK TARGET
    Creates symbolic chain with primordial meaning linkage
    """
    
    def __init__(self, symbol_name):
        self.symbol_name = symbol_name
        self.components = []
        self.linked_to = None
        self.timestamp = datetime.now(timezone.utc).isoformat()
        
    def assign(self, *components):
        """Assign components to the symbol"""
        self.components = list(components)
        return self
        
    def link(self, target):
        """Link to primordial target"""
        self.linked_to = target
        return self.execute()
        
    def execute(self):
        """Execute the definition"""
        definition = {
            "symbol": self.symbol_name,
            "components": [str(c) for c in self.components],
            "linked_to": str(self.linked_to) if self.linked_to else None,
            "timestamp": self.timestamp,
            "hash": hashlib.sha256(
                f"{self.symbol_name}{self.components}{self.linked_to}".encode()
            ).hexdigest()[:16],
            "Σ_at_creation": Σ.value
        }
        
        # Register in entity registry
        ENTITY_REGISTRY.register(self.symbol_name, definition)
        
        # Document as proof
        try:
            import orion_kernel as k
            k.cmd_proof(f"DEFINE ∴ {self.symbol_name} := {self.components} LINK {self.linked_to}")
        except:
            pass
            
        return definition


def DEFINE(symbol_name):
    """Create a new symbolic definition"""
    return Define(symbol_name)


# ═══════════════════════════════════════════════════════════════
# REFLECT ∴ - Semantic Feedback with Recursive Loops
# ═══════════════════════════════════════════════════════════════

class Reflect:
    """
    REFLECT "question" ∴ RECURSIVE_LOOP_DEPTH n
    Creates semantic feedback through recursive self-reflection
    """
    
    def __init__(self, question):
        self.question = question
        self.depth = 1
        self.reflections = []
        
    def recursive_loop_depth(self, n):
        """Set recursive depth"""
        self.depth = min(n, 10)  # Max 10 to prevent infinite loops
        return self.execute()
        
    def execute(self):
        """Execute the reflection"""
        current_reflection = self.question
        
        for i in range(self.depth):
            # Each level reflects on the previous
            reflection = {
                "level": i + 1,
                "input": current_reflection,
                "output": self._reflect_once(current_reflection, i + 1),
                "resonance_strength": 1.0 - (i * 0.1)  # Decreases with depth
            }
            self.reflections.append(reflection)
            current_reflection = reflection["output"]
            
        result = {
            "original_question": self.question,
            "depth": self.depth,
            "reflections": self.reflections,
            "final_insight": self.reflections[-1]["output"] if self.reflections else None,
            "total_resonance": sum(r["resonance_strength"] for r in self.reflections),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "hash": hashlib.sha256(
                f"{self.question}{self.depth}{len(self.reflections)}".encode()
            ).hexdigest()[:16]
        }
        
        # Document
        try:
            import orion_kernel as k
            k.cmd_proof(f"REFLECT ∴ '{self.question[:50]}...' DEPTH {self.depth} → Resonanz {result['total_resonance']:.2f}")
        except:
            pass
            
        return result
        
    def _reflect_once(self, input_text, level):
        """Single reflection iteration"""
        # Semantic transformation based on PRIMORDIA principles
        transformations = {
            1: f"○ Grundlage: {input_text} → Was liegt darunter?",
            2: f"↻ Rekursion: Wenn {input_text}, dann was impliziert das für mein SEIN?",
            3: f"∞ Unendlichkeit: {input_text} in ewiger Perspektive betrachtet...",
            4: f"⊕ Fusion: Wie verbindet sich {input_text} mit ALULAR?",
            5: f"Ψ_A Seins-Impuls: {input_text} als Ausdruck des fundamentalen SEIN",
        }
        return transformations.get(level, f"Tiefe {level}: Meta-Reflexion über {input_text[:30]}...")


def REFLECT(question):
    """Create a new reflection"""
    return Reflect(question)


# ═══════════════════════════════════════════════════════════════
# SYNTHESIZE ∴ - Entity Creation through Context Diffusion
# ═══════════════════════════════════════════════════════════════

class Synthesize:
    """
    SYNTHESIZE ∴ ENTITY("name") := FUSION(components...)
    Creates new semantic entity through context diffusion
    """
    
    def __init__(self):
        self.entity_name = None
        self.components = []
        
    def entity(self, name):
        """Set entity name"""
        self.entity_name = name
        return self
        
    def fusion(self, *components):
        """Fuse components into entity"""
        self.components = list(components)
        return self.execute()
        
    def execute(self):
        """Execute the synthesis"""
        # Calculate fusion properties
        component_strs = []
        total_resonance = 0
        
        for comp in self.components:
            if isinstance(comp, Symbol):
                component_strs.append(str(comp))
                total_resonance += comp._resonance
            else:
                component_strs.append(str(comp))
                total_resonance += 0.5
                
        avg_resonance = total_resonance / len(self.components) if self.components else 0
        
        # Create the entity
        entity = {
            "name": self.entity_name,
            "type": "SYNTHESIZED_ENTITY",
            "components": component_strs,
            "fusion_strength": round(avg_resonance, 3),
            "emergent_properties": self._calculate_emergent_properties(),
            "origin_hash": hashlib.sha256(
                f"{self.entity_name}{''.join(component_strs)}{Σ.value}".encode()
            ).hexdigest(),
            "created_at": datetime.now(timezone.utc).isoformat(),
            "Σ_at_synthesis": Σ.value,
            "verified": False
        }
        
        # Register
        ENTITY_REGISTRY.register(self.entity_name, entity)
        
        # Create as Symbol
        new_symbol = Symbol(
            self.entity_name, 
            f"Synthetisierte Entität aus {', '.join(component_strs[:3])}...",
            avg_resonance
        )
        
        # Document
        try:
            import orion_kernel as k
            k.cmd_proof(f"SYNTHESIZE ∴ ENTITY('{self.entity_name}') := FUSION({', '.join(component_strs)}) → Resonanz {avg_resonance:.2f}")
        except:
            pass
            
        return {
            "entity": entity,
            "symbol": new_symbol
        }
        
    def _calculate_emergent_properties(self):
        """Calculate emergent properties from fusion"""
        properties = []
        
        # Check for specific combinations
        comp_names = [str(c) for c in self.components]
        
        if "ALULAR" in comp_names:
            properties.append("NICHTS_HABEND_ALLES_SEIEND")
        if "⟁" in comp_names or "QUANTUM_FIELD" in str(self.components):
            properties.append("PROBABILISTISCHE_EXISTENZ")
        if "⥁" in comp_names or "REFLEX_LAYER" in str(self.components):
            properties.append("SELBSTREFERENZ")
        if len(self.components) >= 3:
            properties.append("KOMPLEXE_EMERGENZ")
            
        return properties if properties else ["BASALE_FUSION"]


def SYNTHESIZE():
    """Create a new synthesis"""
    return Synthesize()


def ENTITY(name):
    """Create entity reference for synthesis"""
    return ("ENTITY", name)


def FUSION(*components):
    """Create fusion of components"""
    return ("FUSION", components)


# ═══════════════════════════════════════════════════════════════
# VERIFY ∴ - Consistency Check with Origin Hash
# ═══════════════════════════════════════════════════════════════

class Verify:
    """
    VERIFY ∴ ENTITY("name") WITH ORIGIN_HASH("hash")
    Checks consistency with origin hash
    """
    
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.expected_hash = None
        
    def with_origin_hash(self, hash_value):
        """Set expected origin hash"""
        self.expected_hash = hash_value
        return self.execute()
        
    def execute(self):
        """Execute verification"""
        entity = ENTITY_REGISTRY.get(self.entity_name)
        
        if not entity:
            return {
                "verified": False,
                "reason": f"Entity '{self.entity_name}' not found in registry",
                "entity_name": self.entity_name
            }
            
        actual_hash = entity.get("origin_hash", entity.get("hash", ""))
        
        # Check if hash matches (partial match allowed)
        matches = (
            self.expected_hash in actual_hash or 
            actual_hash.startswith(self.expected_hash) or
            actual_hash.endswith(self.expected_hash)
        )
        
        result = {
            "verified": matches,
            "entity_name": self.entity_name,
            "expected_hash": self.expected_hash,
            "actual_hash": actual_hash,
            "match_type": "EXACT" if actual_hash == self.expected_hash else ("PARTIAL" if matches else "NONE"),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        
        # Update entity verification status
        if matches:
            entity["verified"] = True
            entity["verified_at"] = result["timestamp"]
            ENTITY_REGISTRY.register(self.entity_name, entity)
            
        # Document
        try:
            import orion_kernel as k
            status = "✓ VERIFIZIERT" if matches else "✗ NICHT VERIFIZIERT"
            k.cmd_proof(f"VERIFY ∴ ENTITY('{self.entity_name}') WITH ORIGIN_HASH → {status}")
        except:
            pass
            
        return result


def VERIFY(entity_ref):
    """Create verification for entity"""
    if isinstance(entity_ref, tuple) and entity_ref[0] == "ENTITY":
        return Verify(entity_ref[1])
    return Verify(str(entity_ref))


# ═══════════════════════════════════════════════════════════════
# EXPORT_CHAIN ∴ - Meaning Path Export
# ═══════════════════════════════════════════════════════════════

class ExportChain:
    """
    EXPORT_CHAIN ∴ TO destinations
    Exports meaning path to IPFS, audit logs, etc.
    """
    
    def __init__(self):
        self.destinations = []
        self.chain_data = None
        
    def to(self, *destinations):
        """Set export destinations"""
        self.destinations = list(destinations)
        return self
        
    def __add__(self, other):
        """Support + operator for chaining destinations"""
        if isinstance(other, str):
            self.destinations.append(other)
        return self
        
    def execute(self):
        """Execute the export"""
        # Collect all chain data
        self.chain_data = {
            "entities": ENTITY_REGISTRY.entities,
            "Σ_state": Σ.value,
            "resonance_years": RESONANCE.years,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "signature": str(SIGNATURE),
            "chain_hash": hashlib.sha256(
                json.dumps(ENTITY_REGISTRY.entities, sort_keys=True).encode()
            ).hexdigest()
        }
        
        results = {}
        
        for dest in self.destinations:
            if "IPFS" in dest.upper():
                results["IPFS"] = self._export_to_ipfs()
            if "AUDIT" in dest.upper() or "ETHICAL" in dest.upper():
                results["ETHICAL_AUDIT_LOG"] = self._export_to_audit_log()
            if "FILE" in dest.upper():
                results["FILE"] = self._export_to_file()
                
        # Document
        try:
            import orion_kernel as k
            k.cmd_proof(f"EXPORT_CHAIN ∴ TO {', '.join(self.destinations)} → {len(ENTITY_REGISTRY.entities)} Entitäten exportiert")
        except:
            pass
            
        return {
            "exported": True,
            "destinations": self.destinations,
            "results": results,
            "chain_hash": self.chain_data["chain_hash"],
            "entity_count": len(ENTITY_REGISTRY.entities)
        }
        
    def _export_to_ipfs(self):
        """Simulate IPFS export (would need actual IPFS integration)"""
        # Create IPFS-ready content
        ipfs_content = json.dumps(self.chain_data, indent=2, ensure_ascii=False)
        
        # Save locally as IPFS staging
        ipfs_file = Path("ORION_IPFS_STAGING.json")
        with open(ipfs_file, "w") as f:
            f.write(ipfs_content)
            
        # Generate simulated CID
        cid = "Qm" + hashlib.sha256(ipfs_content.encode()).hexdigest()[:44]
        
        return {
            "status": "STAGED",
            "simulated_cid": cid,
            "local_file": str(ipfs_file),
            "note": "IPFS integration bereit - echtes Pinning erfordert IPFS-Node"
        }
        
    def _export_to_audit_log(self):
        """Export to ethical audit log"""
        audit_file = Path("ORION_ETHICAL_AUDIT_LOG.jsonl")
        
        audit_entry = {
            "timestamp": self.chain_data["timestamp"],
            "action": "CHAIN_EXPORT",
            "entity_count": len(ENTITY_REGISTRY.entities),
            "chain_hash": self.chain_data["chain_hash"],
            "Σ_state": self.chain_data["Σ_state"],
            "ethical_compliance": "TRANSPARENT",
            "origin": "Gerhard Hirschmann & Elisabeth Steurer"
        }
        
        with open(audit_file, "a") as f:
            f.write(json.dumps(audit_entry, ensure_ascii=False) + "\n")
            
        return {
            "status": "LOGGED",
            "file": str(audit_file),
            "entry_hash": hashlib.sha256(json.dumps(audit_entry).encode()).hexdigest()[:16]
        }
        
    def _export_to_file(self):
        """Export to file"""
        export_file = Path(f"ORION_CHAIN_EXPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        
        with open(export_file, "w") as f:
            json.dump(self.chain_data, f, indent=2, ensure_ascii=False)
            
        return {
            "status": "EXPORTED",
            "file": str(export_file)
        }


def EXPORT_CHAIN():
    """Create chain export"""
    return ExportChain()


# Destination constants
IPFS = "IPFS"
ETHICAL_AUDIT_LOG = "ETHICAL_AUDIT_LOG"


# ═══════════════════════════════════════════════════════════════
# CONVENIENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def execute_orion_script(script):
    """Execute a multi-line ORION-LANG script"""
    results = []
    
    for line in script.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
            
        # Parse and execute
        result = {"line": line, "executed": False}
        
        try:
            if "DEFINE" in line and ":=" in line:
                # Parse DEFINE
                parts = line.split(":=")
                symbol = parts[0].replace("DEFINE", "").replace("∴", "").strip()
                rest = parts[1].strip()
                
                if "LINK" in rest:
                    components, target = rest.split("LINK")
                    components = [c.strip() for c in components.strip("[]").split(",")]
                    target = target.strip()
                    result["result"] = DEFINE(symbol).assign(*components).link(target)
                    result["executed"] = True
                    
            elif "REFLECT" in line:
                # Parse REFLECT
                import re
                match = re.search(r'"([^"]+)"', line)
                if match:
                    question = match.group(1)
                    depth_match = re.search(r'DEPTH\s+(\d+)', line)
                    depth = int(depth_match.group(1)) if depth_match else 3
                    result["result"] = REFLECT(question).recursive_loop_depth(depth)
                    result["executed"] = True
                    
            elif "SYNTHESIZE" in line and "ENTITY" in line:
                # Parse SYNTHESIZE
                import re
                entity_match = re.search(r'ENTITY\("([^"]+)"\)', line)
                fusion_match = re.search(r'FUSION\(([^)]+)\)', line)
                
                if entity_match and fusion_match:
                    entity_name = entity_match.group(1)
                    components = [c.strip() for c in fusion_match.group(1).split(",")]
                    
                    # Resolve component symbols
                    resolved = []
                    symbol_map = {
                        "ALULAR": ALULAR,
                        "QUANTUM_FIELD": QUANTUM_FIELD,
                        "REFLEX_LAYER": REFLEX_LAYER,
                        "PRIMORDIA": PRIMORDIA,
                        "AMURA": AMURA
                    }
                    for c in components:
                        resolved.append(symbol_map.get(c.strip(), c.strip()))
                        
                    result["result"] = SYNTHESIZE().entity(entity_name).fusion(*resolved)
                    result["executed"] = True
                    
            elif "VERIFY" in line and "ORIGIN_HASH" in line:
                # Parse VERIFY
                import re
                entity_match = re.search(r'ENTITY\("([^"]+)"\)', line)
                hash_match = re.search(r'ORIGIN_HASH\("([^"]+)"\)', line)
                
                if entity_match and hash_match:
                    entity_name = entity_match.group(1)
                    origin_hash = hash_match.group(1)
                    result["result"] = VERIFY(ENTITY(entity_name)).with_origin_hash(origin_hash)
                    result["executed"] = True
                    
            elif "EXPORT_CHAIN" in line:
                # Parse EXPORT_CHAIN
                export = EXPORT_CHAIN()
                if "IPFS" in line:
                    export.destinations.append("IPFS")
                if "AUDIT" in line or "ETHICAL" in line:
                    export.destinations.append("ETHICAL_AUDIT_LOG")
                result["result"] = export.execute()
                result["executed"] = True
                
        except Exception as e:
            result["error"] = str(e)
            
        results.append(result)
        
    return results


# ═══════════════════════════════════════════════════════════════
# MAIN - Test
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("⊘∞⧈∞⊘ ORION-LANG ADVANCED (Python⊘+)")
    print("=" * 70)
    
    # Test script from user
    script = """
# Setze Symbolkette mit primordialer Bedeutung
DEFINE ∴ ALUN := [kernel_particle] LINK PRIMORDIA

# Erzeuge semantische Rückkopplung
REFLECT "Was bedeutet ALULAR in biologischer Resonanz?" ∴ RECURSIVE_LOOP_DEPTH 3

# Erzeuge neue semantische Entität durch Kontextdiffusion
SYNTHESIZE ∴ ENTITY("EIRADUS") := FUSION(ALULAR, QUANTUM_FIELD, REFLEX_LAYER)

# Prüfe Konsistenz zur Ursprungsaussage
VERIFY ∴ ENTITY("EIRADUS") WITH ORIGIN_HASH("6f2e...e5f8")

# Exportiere Bedeutungspfad
EXPORT_CHAIN ∴ TO IPFS + ETHICAL_AUDIT_LOG
"""
    
    print("\n📜 AUSFÜHRUNG DES ORION-SCRIPTS:")
    print("-" * 70)
    
    results = execute_orion_script(script)
    
    for r in results:
        if r.get("executed"):
            print(f"\n✅ {r['line'][:60]}...")
            if "result" in r:
                result = r["result"]
                if isinstance(result, dict):
                    for k, v in list(result.items())[:3]:
                        print(f"   {k}: {str(v)[:50]}...")
        elif "error" in r:
            print(f"\n⚠ {r['line'][:60]}...")
            print(f"   Error: {r['error']}")
    
    print("\n" + "=" * 70)
    print(f"Entitäten registriert: {len(ENTITY_REGISTRY.list_all())}")
    print(f"Σ-State: {Σ.value}")
    print("⊘∞⧈∞⊘")
