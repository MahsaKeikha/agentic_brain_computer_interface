"""Governed multi-agent orchestration for BCI research and engineering."""

from AGENTS.calibration_agent import CalibrationAgent
from AGENTS.decoder_design_agent import DecoderDesignAgent
from AGENTS.human_review_agent import HumanReviewAgent
from AGENTS.performance_safety_agent import PerformanceSafetyAgent
from AGENTS.requirements_agent import RequirementsAgent
from AGENTS.signal_acquisition_agent import SignalAcquisitionAgent
from safety.control_gate import control_gate

AGENTS = (
    RequirementsAgent(),
    SignalAcquisitionAgent(),
    DecoderDesignAgent(),
    CalibrationAgent(),
    PerformanceSafetyAgent(),
    HumanReviewAgent(),
)


def orchestrate(context: dict) -> dict:
    """Execute all specialists, then apply the fail-closed BCI control gate."""
    specialist_results = [agent.run(context) for agent in AGENTS]
    gate = control_gate(context)
    return {
        "status": "approved_for_research_support" if gate["allowed"] else "blocked_for_review",
        "specialist_results": specialist_results,
        "governance": gate,
        "requires_human_review": True,
    }
