def build_user_traits(answers, questions, mode):
    user_traits = {}

    for i, answer in enumerate(answers):
        question = questions[i]

        if mode == "1" and question.get("category") != "physical":
            continue

        if mode == "2" and question.get("category") != "personality":
            continue

        option_data = question["options"].get(answer, {})
        option_traits = option_data.get("traits", {})

        for trait, value in option_traits.items():
            user_traits[trait] = user_traits.get(trait, 0) + value

    return user_traits


def calculate_score(user_traits, character_traits):
    score = 0

    for trait, value in character_traits.items():
        score += user_traits.get(trait, 0) * value

    return score


def get_character_traits_by_mode(character, mode):
    if mode == "1":
        return character.get("physical", {})

    elif mode == "2":
        return character.get("personality", {})

    else:
        combined = {}
        combined.update(character.get("physical", {}))
        combined.update(character.get("personality", {}))
        return combined


def get_top_traits(user_traits, character_traits, top_n=3):
    contributions = {}

    for trait, char_value in character_traits.items():
        user_value = user_traits.get(trait, 0)
        score = user_value * char_value

        if score > 0:
            contributions[trait] = score

    sorted_traits = sorted(
        contributions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [trait for trait, _ in sorted_traits[:top_n]]


def get_trait_percentages(user_traits, character_traits):
    percentages = {}

    for trait, char_value in character_traits.items():
        user_value = user_traits.get(trait, 0)

        if char_value > 0 and user_value > 0:
            percentages[trait] = min(
                round((user_value / char_value) * 100),
                100
            )

    return dict(
        sorted(
            percentages.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )


def get_top_matches(scores, top_n=3):
    sorted_scores = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    if not sorted_scores:
        return []

    best_score = sorted_scores[0][1] or 1

    top_matches = []

    for name, score in sorted_scores[:top_n]:
        confidence = round((score / best_score) * 100, 1)

        top_matches.append({
            "name": name,
            "score": score,
            "confidence": confidence
        })

    return top_matches