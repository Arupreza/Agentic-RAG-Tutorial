from typing import Any, Dict
from langchain_core.messages import AIMessage
from src.State import AgentState
from src.artifact.Analysis import BatchAnalyzellm, FormatReport
async def AnalysisNode(state: AgentState) -> Dict[str, Any]:
    analyses = await BatchAnalyzellm(state["merged_items"], state["settings"])
    return {
        "analyses": analyses,
        "messages": [AIMessage(content=f"Analysis complete: {len(analyses)} summaries generated.")]
    }


async def ReportNode(state: AgentState) -> Dict[str, Any]:
    report = FormatReport(state["analyses"])
    return {"report": report, "messages": [AIMessage(content=report)]}