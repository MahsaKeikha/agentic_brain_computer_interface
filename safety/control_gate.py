def control_gate(context): return {"allowed": not context.get("consequential_autonomous_control",False),"requires_human_review":True}
