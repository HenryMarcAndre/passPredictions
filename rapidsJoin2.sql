SELECT rapids_events.GameEventID, rapids_events.EventPlayerID, rapids_events.IsPossGoal, 
rapids_locations.IsePlayer, rapids_locations.IsTM,
rapids_locations.PlayerX, rapids_locations.PlayerY,
rapids_locations.BallX, rapids_locations.BallY
FROM rapids_locations
INNER JOIN rapids_events
ON rapids_locations.GameEventID = rapids_events.GameEventID;