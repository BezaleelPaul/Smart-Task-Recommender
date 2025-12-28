def recommend(state):
    """
    Decision logic:
    score = (energy * 2) + mood - (stress * 1.5)
    """

    score = (state.energy * 2) + state.mood - (state.stress * 1.5)

    # Very low capacity state
    if state.energy <= 2 or state.stress >= 4:
        return {
            "task": "Light task (reading, planning, organizing)",
            "reason": (
                f"Energy is low ({state.energy}) or stress is high ({state.stress}). "
                "Light tasks help maintain momentum without burnout."
            )
        }

    # Peak performance
    if score >= 10 and state.available_time >= 45:
        return {
            "task": "Deep work session (coding, studying, problem-solving)",
            "reason": (
                f"High combined score ({score:.1f}) with sufficient time "
                f"({state.available_time} mins) indicates readiness for deep focus."
            )
        }

    # Medium productivity
    if score >= 6:
        return {
            "task": "Moderate task (revision, debugging, documentation)",
            "reason": (
                f"Balanced state detected (score {score:.1f}). "
                "Suitable for productive but less intensive work."
            )
        }

    # Default fallback
    return {
        "task": "Short break or reset activity",
        "reason": (
            f"Overall score ({score:.1f}) suggests recovery will improve future performance."
        )
    }
