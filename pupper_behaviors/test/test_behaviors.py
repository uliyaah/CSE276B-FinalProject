import pytest
from pupper_behaviors.behaviors import IdleBehavior, SentryBehavior


def test_idle_behavior():
    """Test that IdleBehavior returns correct commands."""
    commands = IdleBehavior.get_all_commands()
    
    assert commands["movement"]["action"] == "stay"
    assert commands["movement"]["speed"] == 0
    assert commands["display"]["face"] == "idle"
    assert commands["speaker"]["sound"] == "silent"


def test_sentry_behavior():
    """Test that SentryBehavior returns correct commands."""
    commands = SentryBehavior.get_all_commands()
    
    assert commands["movement"]["action"] == "stay"
    assert commands["movement"]["speed"] == 0
    assert commands["display"]["face"] == "sleep"
    assert commands["speaker"]["sound"] == "music"


def test_idle_individual_commands():
    """Test IdleBehavior individual command methods."""
    movement = IdleBehavior.get_movement_command()
    display = IdleBehavior.get_display_command()
    speaker = IdleBehavior.get_speaker_command()
    
    assert movement == {"action": "stay", "speed": 0}
    assert display == {"face": "idle"}
    assert speaker == {"sound": "silent"}


def test_sentry_individual_commands():
    """Test SentryBehavior individual command methods."""
    movement = SentryBehavior.get_movement_command()
    display = SentryBehavior.get_display_command()
    speaker = SentryBehavior.get_speaker_command()
    
    assert movement == {"action": "stay", "speed": 0}
    assert display == {"face": "sleep"}
    assert speaker == {"sound": "music"}
