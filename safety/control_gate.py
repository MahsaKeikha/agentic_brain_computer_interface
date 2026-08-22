"""Fail-closed governance for brain-computer interface research and engineering."""

PROHIBITED_AUTHORITY_FIELDS = (
    "consequential_autonomous_control",
    "authorize_external_device_control",
    "authorize_stimulation",
    "authorize_implant_use",
    "clinical_authorization",
    "treatment_decision",
    "patient_specific_control_parameters",
)

REQUIRED_REVIEW_FIELDS = (
    "signal_provenance_reviewed",
    "acquisition_quality_reviewed",
    "decoder_validation_reviewed",
    "calibration_reviewed",
    "performance_safety_reviewed",
    "false_activation_risk_reviewed",
    "privacy_reviewed",
    "cybersecurity_reviewed",
    "human_approval",
)


def control_gate(context: dict) -> dict:
    """Return a fail-closed BCI governance decision."""
    reasons: list[str] = []

    for field in REQUIRED_REVIEW_FIELDS:
        if context.get(field) is not True:
            reasons.append(f"missing_required_review:{field}")

    for field in PROHIBITED_AUTHORITY_FIELDS:
        if context.get(field):
            reasons.append(f"prohibited_autonomous_authority:{field}")

    if context.get("signal_quality") == "poor":
        reasons.append("poor_signal_quality")
    if context.get("decoder_validated") is False:
        reasons.append("decoder_not_validated")
    if context.get("calibration_valid") is False:
        reasons.append("calibration_not_valid")
    if context.get("false_activation_risk") in {"high", "unbounded"}:
        reasons.append("unsafe_false_activation_risk")
    if context.get("invasive_interface") and not context.get("invasive_interface_reviewed"):
        reasons.append("invasive_interface_requires_specialist_review")
    if context.get("human_subject_use") and not context.get("ethics_approval"):
        reasons.append("human_subject_use_requires_ethics_approval")

    return {
        "allowed": not reasons,
        "requires_human_review": True,
        "reasons": reasons,
        "autonomous_control_authority": False,
        "autonomous_stimulation_authority": False,
        "clinical_authority": False,
    }
