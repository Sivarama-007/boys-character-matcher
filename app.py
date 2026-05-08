print("Running NEW app.py")

from flask import Flask, render_template, request
from questions_data import questions
from characters import characters
from descriptions import descriptions
from character_images import character_images
from archetypes import archetypes

from scorer import (
    build_user_traits,
    calculate_score,
    get_character_traits_by_mode,
    get_top_traits,
    get_trait_percentages,
    get_top_matches
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", questions=questions)


@app.route("/result", methods=["POST"])
def result():
    mode = request.form.get("mode", "3")

    answers = []

    for i in range(len(questions)):
        ans = request.form.get(f"q{i}")

        if ans:
            answers.append(ans)
        else:
            answers.append(None)

    user_traits = build_user_traits(answers, questions, mode)

    scores = {}

    for name, data in characters.items():
        char_traits = get_character_traits_by_mode(data, mode)
        scores[name] = calculate_score(user_traits, char_traits)

    if not scores:
        return "Error: No characters found."

    best_character = max(scores, key=scores.get)

    best_traits = get_character_traits_by_mode(
        characters[best_character],
        mode
    )

    top_traits = get_top_traits(user_traits, best_traits)

    trait_percentages = get_trait_percentages(
        user_traits,
        best_traits
    )

    trait_percentages = dict(
        list(trait_percentages.items())[:5]
    )

    top_matches = get_top_matches(scores)

    confidence = top_matches[0]["confidence"]

    enriched_matches = []

    for match in top_matches:
        enriched_matches.append({
            "name": match["name"],
            "confidence": match["confidence"],
            "image": character_images.get(match["name"])
        })

    return render_template(
        "result.html",
        character=best_character,
        description=descriptions.get(
            best_character,
            "A complex force in The Boys universe."
        ),
        confidence=confidence,
        top_traits=top_traits,
        trait_percentages=trait_percentages,
        char_image=character_images.get(best_character),
        top_matches=enriched_matches,
        archetype=archetypes.get(
            best_character,
            "UNKNOWN ARCHETYPE"
        )
    )


if __name__ == "__main__":
    app.run(debug=True)