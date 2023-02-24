use rapids;

SELECT DISTINCT  rapids_events.IsPossGoal, 
rapids_locations.PlayerX, rapids_locations.PlayerY,
rapids_locations.BallX, rapids_locations.BallY,
rapids_pass_data.teammates_within_5, rapids_pass_data.opponents_within_5, 
rapids_pass_data.teammates_within_10, rapids_pass_data.opponents_within_10, 
rapids_pass_data.teammates_within_15, rapids_pass_data.opponents_within_15, 
rapids_pass_data.teammates_ahead_of_ball, rapids_pass_data.opponents_ahead_of_ball
FROM rapids_locations
INNER JOIN rapids_events
ON rapids_locations.GameEventID = rapids_events.GameEventID
INNER JOIN rapids_pass_data
ON rapids_events.GameEventID = rapids_pass_data.GameEventID
WHERE rapids_locations.IsePlayer = 1 AND rapids_events.PassOutcome = 'Complete';


