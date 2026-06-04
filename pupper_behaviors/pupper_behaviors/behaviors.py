########
# Name: behaviors.py
#
# Purpose: Defines behavior outputs (Movement, Display, Speaker commands)
#          for each state of the State Manager FSM.
#
# Date: 03 June 2026
########


class IdleBehavior:
    """Behavior when robot is in IDLE state (waiting for activation)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for IDLE state."""
        return {
            "action": "stay",
            "speed": 0
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for IDLE state."""
        return {
            "face": "idle"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for IDLE state."""
        return {
            "sound": "silent"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": IdleBehavior.get_movement_command(),
            "display": IdleBehavior.get_display_command(),
            "speaker": IdleBehavior.get_speaker_command()
        }


class SentryBehavior:
    """Behavior when robot is in SENTRY state (active, watching for distraction)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for SENTRY state."""
        return {
            "action": "stay",
            "speed": 0
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for SENTRY state."""
        return {
            "face": "sleep"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for SENTRY state."""
        return {
            "sound": "music"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": SentryBehavior.get_movement_command(),
            "display": SentryBehavior.get_display_command(),
            "speaker": SentryBehavior.get_speaker_command()
        }
