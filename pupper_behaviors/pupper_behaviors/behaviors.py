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
            "action": "lay",
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
            "sound": "silent"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": SentryBehavior.get_movement_command(),
            "display": SentryBehavior.get_display_command(),
            "speaker": SentryBehavior.get_speaker_command()
        }

class Intervention1Behavior:
    """Behavior for INTERVENTION_1 state (responding to low distraction)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for INTERVENTION_1 state."""
        return {
            "action": "stay",
            "speed": 0
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for INTERVENTION_1 state."""
        return {
            "face": "offended"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for INTERVENTION_1 state."""
        return {
            "sound": "bark"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": Intervention1Behavior.get_movement_command(),
            "display": Intervention1Behavior.get_display_command(),
            "speaker": Intervention1Behavior.get_speaker_command()
        }



class Intervention2Behavior:
    """Behavior for INTERVENTION_2 state (responding to medium distraction)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for INTERVENTION_2 state."""
        return {
            "action": "approach",
            "speed": 0.5
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for INTERVENTION_2 state."""
        return {
            "face": "puppy_eyes_1"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for INTERVENTION_2 state."""
        return {
            "sound": "whine"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": Intervention2Behavior.get_movement_command(),
            "display": Intervention2Behavior.get_display_command(),
            "speaker": Intervention2Behavior.get_speaker_command()
        }
        

class Intervention3Behavior:
    """Behavior for INTERVENTION_3 state (responding to high distraction)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for INTERVENTION_3 state."""
        return {
            "action": "approach_and_lay",
            "speed": 0.3
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for INTERVENTION_3 state."""
        return {
            "face": "puppy_eyes_2"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for INTERVENTION_3 state."""
        return {
            "sound": "whine"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": Intervention3Behavior.get_movement_command(),
            "display": Intervention3Behavior.get_display_command(),
            "speaker": Intervention3Behavior.get_speaker_command()
        }




class PausedBehavior:
    """Behavior when robot is in PAUSED state (user paused)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for PAUSED state."""
        return {
            "action": "stay",
            "speed": 0
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for PAUSED state."""
        return {
            "face": "idle"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for PAUSED state."""
        return {
            "sound": "silent"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": PausedBehavior.get_movement_command(),
            "display": PausedBehavior.get_display_command(),
            "speaker": PausedBehavior.get_speaker_command()
        }


class CelebrateBehavior:
    """Behavior when robot is in CELEBRATE state (50-minute milestone)."""
    
    @staticmethod
    def get_movement_command():
        """Return movement command for CELEBRATE state."""
        return {
            "action": "shake",
            "speed": 0.5
        }
    
    @staticmethod
    def get_display_command():
        """Return display command for CELEBRATE state."""
        return {
            "face": "celebrate"
        }
    
    @staticmethod
    def get_speaker_command():
        """Return speaker command for CELEBRATE state."""
        return {
            "sound": "celebrate"
        }
    
    @staticmethod
    def get_all_commands():
        """Return all output commands as a dict."""
        return {
            "movement": CelebrateBehavior.get_movement_command(),
            "display": CelebrateBehavior.get_display_command(),
            "speaker": CelebrateBehavior.get_speaker_command()
        }
