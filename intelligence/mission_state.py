MISSION_EXPLORE =0
MISSION_COMPLETE =1
RETURN_HOME=2
def update_mission_state(
    frontiers,
    current_state,
    battery,
    dist_to_home
):
    if current_state== MISSION_EXPLORE:
        if battery<15:
            return RETURN_HOME
        if len(frontiers)==0:
            return MISSION_COMPLETE
        return MISSION_EXPLORE
    if current_state== RETURN_HOME:
        if dist_to_home<5:
            return MISSION_COMPLETE
        return RETURN_HOME
        
    