import sys

def process_siri_command(command):
    """Simulates processing a Siri command for a hypothetical app."""
    print(f"Received Siri command: '{command}'")

    # In a real scenario, this would involve SiriKit or a similar framework
    # to parse the command and identify the target application and action.
    # For this demo, we'll use simple keyword matching.

    if "play" in command.lower() and "music" in command.lower():
        song_name = command.lower().split("play", 1)[1].split("music", 1)[0].strip()
        if song_name:
            print(f"-> Siri is now playing '{song_name}' in your music app.")
        else:
            print("-> Siri will now play some music.")
    elif "send" in command.lower() and "message" in command.lower():
        parts = command.lower().split("send", 1)[1].split("message", 1)
        if len(parts) > 1:
            recipient_and_message = parts[1].strip()
            # A more robust parser would extract recipient and message content
            print(f"-> Siri is sending a message: '{recipient_and_message}'")
        else:
            print("-> Siri needs more information to send a message.")
    elif "set" in command.lower() and "timer" in command.lower():
        time_str = command.lower().split("set", 1)[1].split("timer", 1)[0].strip()
        if time_str:
            print(f"-> Siri is setting a timer for {time_str}.")
        else:
            print("-> Siri needs to know for how long to set the timer.")
    else:
        print("-> Siri could not understand this command for the integrated app.")

if __name__ == "__main__":
    print("--- Siri App Integration Demo ---")
    print("This script simulates how Siri might interact with a third-party app.")
    print("In a real application, SiriKit would handle the voice input and intent parsing.")
    print("---------------------------------")

    # Example commands that a user might say to Siri to control an app
    example_commands = [
        "Hey Siri, play Bohemian Rhapsody music",
        "Hey Siri, send a message to John 'See you soon!'",
        "Hey Siri, set a timer for 5 minutes",
        "Hey Siri, open my notes app", # This would typically go to the Notes app, not our demo
        "Hey Siri, play some rock music"
    ]

    for cmd in example_commands:
        process_siri_command(cmd)
        print("---")

    print("Demo finished.")
