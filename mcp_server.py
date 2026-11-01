# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Allostatic Load Index Biomarker Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentAllostaticLoadIndexBiomarker

mcp = FastMCP("PersonalAgentAllostaticLoadIndexBiomarker")
client = PersonalAgentAllostaticLoadIndexBiomarker()

@mcp.tool()
def calculate_allostatic_load_index(
    biomarkers_json: str,
    gender: str = "male"
) -> str:
    """Calculates allostatic load index (0-10) across cardiovascular, metabolic, inflammatory, and autonomic markers."""
    import json
    biomarkers = json.loads(biomarkers_json) if isinstance(biomarkers_json, str) else biomarkers_json
    return json.dumps(client.calculate_allostatic_load_index(biomarkers, gender), indent=2)

@mcp.tool()
def simulate_allostatic_recovery_trajectory(
    current_al_index: float = 6.0,
    adherence_weeks: int = 12
) -> str:
    """Simulates multi-week allostatic load attenuation trajectory under lifestyle interventions."""
    import json
    return json.dumps(client.simulate_allostatic_recovery_trajectory(current_al_index, adherence_weeks), indent=2)

if __name__ == "__main__":
    mcp.run()
