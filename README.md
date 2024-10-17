# Ai-DiscordBot
Ai-DiscordBot workspace

General Psuedocode

Run when discord is opened? (Run when it's meant to run)
Await call word in chat
when called, respond appropriately referencing an intro message expecting the following commands:
    Help
    Create new character
    Interact with existing character
    Tell me about existing character
Help:
    Show a list of all the commands involved in both character creation and interaction
Create New Character:
    Ask for input on the following, including an option to explain what is being asked specifically:
        Name
        Speech Quirks
        Personality Traits
            Specific traits to include - given by user with 1-10
            Openness 1-10
            Conscientiousness 1-10
            Extraversion 1-10
            Agreeablesness 1-10
            Neuroticism 1-10
                Extraversion is sociability, agreeableness is kindness, openness is creativity and intrigue, conscientiousness is thoughtfulness, and neuroticism often involves sadness or emotional instability.
        Known Information
    Confirm Given Information
Interact With Existing Character(Name):
    Show some form of proof that (Name) is listening
    Given any input, use AI to generate a respective output.
    Realistically develop based on continuing input
Tell me about existing character(Name):
    Show (Name) base information that has been revealed to client.
    Show current relationship with (Name)
    Show how relationship has changed
