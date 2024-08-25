import os
import re


def split_into_paragraphs(text):
    # Remove extra whitespace and split into sentences
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    paragraphs = []
    current_paragraph = []

    for sentence in sentences:
        current_paragraph.append(sentence)

        # Check for paragraph break conditions
        if len(current_paragraph) >= 5 or (
            len(sentence) > 100 and len(current_paragraph) >= 3
        ):
            paragraphs.append(" ".join(current_paragraph))
            current_paragraph = []

    # Add any remaining sentences as the last paragraph
    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))

    return paragraphs


def find_middle_index(lst):
    length = len(lst)

    if length % 2 != 0:
        return length // 2
    else:
        return length // 2 - 1


def gen_summary(paragraphs):
    if len(paragraphs) <= 5:
        # For very short texts, return all paragraphs
        return "\n".join(paragraphs)
    elif len(paragraphs) <= 10:
        # For short texts, return first, middle, and last paragraphs
        first_section = paragraphs[0]
        middle_section = paragraphs[find_middle_index(paragraphs)]
        last_section = paragraphs[-1]
        return f"{first_section}\n{middle_section}\n{last_section}"
    elif len(paragraphs) <= 20:
        # For medium-length texts, return five sections
        first_section = paragraphs[0]
        quarter_section = paragraphs[len(paragraphs) // 4]
        middle_section = paragraphs[find_middle_index(paragraphs)]
        three_quarter_section = paragraphs[3 * len(paragraphs) // 4]
        last_section = paragraphs[-1]
        return f"{first_section}\n{quarter_section}\n{middle_section}\n{three_quarter_section}\n{last_section}"
    else:
        # For long texts, return seven sections
        first_section = paragraphs[0]
        one_sixth_section = paragraphs[len(paragraphs) // 6]
        one_third_section = paragraphs[len(paragraphs) // 3]
        middle_section = paragraphs[find_middle_index(paragraphs)]
        two_thirds_section = paragraphs[2 * len(paragraphs) // 3]
        five_sixths_section = paragraphs[5 * len(paragraphs) // 6]
        last_section = paragraphs[-1]
        return f"{first_section}\n{one_sixth_section}\n{one_third_section}\n{middle_section}\n{two_thirds_section}\n{five_sixths_section}\n{last_section}"



with open(os.path.join("No_ai_summary", "story.txt"), "r") as file:
    data = file.read()

paragraphs = split_into_paragraphs(data)

print(f"\nYour summary without using AI: \n\n{gen_summary(paragraphs)}\n")
