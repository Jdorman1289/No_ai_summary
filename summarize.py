def find_middle_index(lst):
    length = len(lst)

    if length % 2 != 0:
        return length // 2
    else:
        return length // 2 - 1


def split_into_paragraphs(all_text):
    sentences = all_text.split(".")

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    paragraphs = []

    # Group sentences into paragraphs (3 to 5 sentences per paragraph)
    if len(sentences) <= 30:
        for i in range(0, len(sentences), 3):
            paragraph = ". ".join(sentences[i : i + 3]) + "."
            paragraphs.append(paragraph)

        return paragraphs
    else:
        for i in range(0, len(sentences), 5):
            paragraph = ". ".join(sentences[i : i + 5]) + "."
            paragraphs.append(paragraph)

        return paragraphs


def gen_summary(paragraphs):
    if len(paragraphs) <= 10:
        first_section = paragraphs[0]
        middle_section = paragraphs[find_middle_index(paragraphs)]
        last_section = paragraphs[-1]
        return f"{first_section}\n{middle_section}\n{last_section}"

    elif len(paragraphs) <= 20:
        first_section = paragraphs[0]
        second_section = paragraphs[
            find_middle_index(paragraphs[: find_middle_index(paragraphs)])
        ]
        middle_section = paragraphs[find_middle_index(paragraphs)]
        fourth_section = paragraphs[
            find_middle_index(paragraphs[find_middle_index(paragraphs) + 1 :])
            + find_middle_index(paragraphs)
            + 1
        ]
        last_section = paragraphs[-1]
        return f"{first_section}\n{second_section}\n{middle_section}\n{fourth_section}\n{last_section}"
    else:
        first_section = paragraphs[0]
        second_section = paragraphs[
            find_middle_index(paragraphs[: find_middle_index(paragraphs)])
        ]
        third_section = paragraphs[
            find_middle_index(paragraphs[: find_middle_index(paragraphs) + 1])
            + find_middle_index(paragraphs[: find_middle_index(paragraphs)])
        ]
        middle_section = paragraphs[find_middle_index(paragraphs)]
        fifth_section = paragraphs[
            find_middle_index(paragraphs[find_middle_index(paragraphs) + 1 :])
            + find_middle_index(paragraphs)
            + 1
        ]
        sixth_section = paragraphs[
            find_middle_index(
                paragraphs[
                    find_middle_index(paragraphs[find_middle_index(paragraphs) + 1 :])
                    + find_middle_index(paragraphs)
                    + 1 :
                ]
            )
            + find_middle_index(paragraphs[find_middle_index(paragraphs) + 1 :])
            + find_middle_index(paragraphs)
            + 1
        ]
        last_section = paragraphs[-1]
        return f"{first_section}\n{second_section}\n{third_section}\n{middle_section}\n{fifth_section}\n{sixth_section}\n{last_section}"


with open("story.txt", "r") as file:
    data = file.read()

paragraphs = split_into_paragraphs(data)

print(f"Your summary without using AI: \n\n{gen_summary(paragraphs)}")
