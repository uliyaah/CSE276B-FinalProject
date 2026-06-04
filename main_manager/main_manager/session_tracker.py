########
# Name: session_tracker.py
#
# Purpose: Helper class for tracking distraction count across a session.
#          Logs data to a JSON file for persistence and debugging.
#
# Date: 01 June 2026
########

import json
import os
from datetime import datetime
from pathlib import Path


class SessionTracker:
    """Tracks session metrics (e.g., distraction count) and persists to a JSON file."""

    def __init__(self, session_name: str = None):
        """
        Initialize session tracker.
        
        Args:
            session_name: Optional name for the session. If None, uses timestamp.
        """
        # Create session directory
        self.session_dir = Path.home() / ".ros" / "main_manager_sessions"
        self.session_dir.mkdir(parents=True, exist_ok=True)

        # Set session name
        if session_name is None:
            session_name = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_name = session_name
        self.session_file = self.session_dir / f"{session_name}.json"

        # Initialize session data
        self.session_data = {
            "session_name": session_name,
            "start_time": datetime.now().isoformat(),
            "distraction_count": 0,
            "distraction_events": [],
            "proximity_events": [],
            "touch_events": []
        }

        # Save initial session file
        self._save()

    def log_distraction(self, duration: float, severity: str = "low"):
        """
        Log a distraction event.
        
        Args:
            duration: Duration of distraction in seconds
            severity: "low", "medium", or "high" (low: 0-5s, medium: 5-15s, high: 15s+)
        """
        self.session_data["distraction_count"] += 1
        event_entry = {
            "timestamp": datetime.now().isoformat(),
            "duration": duration,
            "severity": severity
        }
        self.session_data["distraction_events"].append(event_entry)
        self._save()

    def log_proximity(self, distance: float, user_in_range: bool):
        """
        Log a proximity event.
        
        Args:
            distance: Distance in meters
            user_in_range: True if distance < 0.5m, False otherwise
        """
        event_entry = {
            "timestamp": datetime.now().isoformat(),
            "distance": distance,
            "user_in_range": user_in_range
        }
        self.session_data["proximity_events"].append(event_entry)
        self._save()

    def log_touch(self, location: str):
        """
        Log a touch event.
        
        Args:
            location: Location of touch ("front", "left", "right", etc.)
        """
        event_entry = {
            "timestamp": datetime.now().isoformat(),
            "location": location
        }
        self.session_data["touch_events"].append(event_entry)
        self._save()

    def get_distraction_count(self) -> int:
        """Return current distraction count."""
        return self.session_data["distraction_count"]

    def get_session_data(self) -> dict:
        """Return complete session data."""
        return self.session_data

    def _save(self):
        """Save session data to JSON file."""
        try:
            with open(self.session_file, "w") as f:
                json.dump(self.session_data, f, indent=2)
        except IOError as e:
            print(f"Error saving session file: {e}")

    def reset_session(self):
        """Reset session data (for testing)."""
        self.session_data["distraction_count"] = 0
        self.session_data["distraction_events"] = []
        self.session_data["proximity_events"] = []
        self.session_data["touch_events"] = []
        self._save()


if __name__ == '__main__':
    # Simple test
    tracker = SessionTracker("test_session")
    tracker.log_distraction(12.5, "high")
    tracker.log_proximity(0.3, True)
    tracker.log_touch("front")
    print(f"Session file: {tracker.session_file}")
    print(f"Data: {tracker.get_session_data()}")
