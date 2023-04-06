import os
import random
import shutil
import textwrap

import openai

from fey_mood.deity import Deity

openai.api_key = os.getenv("OPENAI_API_KEY")
width = shutil.get_terminal_size(fallback=(80, 24)).columns


def generate_artifact_demand(deity):
    text = f"""You are {deity.name}, a dwarven deity. You most often take the form of a {deity.gender} {deity.creature} and are associated with the following domains: {', '.join(deity.spheres)}.
    You are directing a dwarven potter to create a work to honour you. Output a detailed description of a ceramic object that the potter must build.
    It should be a practical item, not sculptural, and be able to be made on a throwing wheel, such as a cup, mug, plate, bowl, vase, etc.
    Describe the item in detail, its shape, height, proportions, and any specific design elements.
    Your description should not talk about any glazing.
    The description must begin with 'I am {deity.name}. Hear me. You must create a'."""

    result = openai.Completion.create(
        model="text-davinci-003", prompt=text, max_tokens=256, temperature=0.8
    )

    return result["choices"][0]["text"].strip()


def commune():
    deity = Deity()
    print(textwrap.fill(f"Communing with {deity}...", width=width))
    demand = generate_artifact_demand(deity)
    print("\n---\n")
    print("You have been taken by a fey mood!\n")
    print(textwrap.fill(demand, width=width))


def main():
    commune()


if __name__ == "__main__":
    main()
