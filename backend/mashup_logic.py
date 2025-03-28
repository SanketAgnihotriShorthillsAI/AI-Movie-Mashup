# mashup_logic.py

def build_prompt(movie1, movie2, genre, extra_context=""):
    prompt = f"""
    You are a creative screenwriter. I want you to create a movie mashup.

    Task:
    Create a mashup of "{movie1}" and "{movie2}".
    Genre: {genre}
    Your Output MUST have the following sections:
    1. Plot Summary
    2. Sample Dialogues (at least 3 lines)
    3. Scene Script (write 1 short scene)
    4. Bonus: 3 Quiz Questions for fans to guess who said what
    
    Rules:
    - Make it fun, engaging, and unexpected.
    - Blend elements from both titles.
    - If {extra_context} is provided, use it to shape the mashup.

    Extra Context (if any): {extra_context}
    """
    return prompt

# mashup_logic.py

def build_dialogue_prompt(movie1: str, movie2: str, genre: str, scene_desc: str):
    return f"Write a short dialogue between the main characters of '{movie1}' and '{movie2}' in a '{genre}' setting. Scene context: {scene_desc}"

def build_scene_prompt(movie1: str, movie2: str, genre: str, scene_idea: str):
    return f"Write a detailed movie scene script combining '{movie1}' and '{movie2}' in the genre '{genre}'. Scene idea: {scene_idea}"

def build_quick_mashup_prompt(user_input: str):
    return f"Generate a short creative crossover scenario based on: {user_input}"