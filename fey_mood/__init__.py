import asyncio
import os
import random
import shutil
import sys
import textwrap

import openai
from colorama import Fore

from fey_mood.deity import Deity

openai.api_key = os.getenv("OPENAI_API_KEY")
width = shutil.get_terminal_size(fallback=(80, 24)).columns


async def generate_artifact_demand(deity):
    text = f"""You are {deity.name}, a dwarven deity. You most often take the form of a {deity.gender} {deity.creature} and are associated with the following domains: {', '.join(deity.spheres)}.
    You are directing a dwarven potter to create a work to honour you. Output a detailed description of a ceramic object that the potter must build.
    It should be a practical item, not sculptural, and be able to be made on a throwing wheel, such as a cup, mug, plate, bowl, vase, etc.
    Describe the item in detail, its shape, height, proportions, and any specific design elements.
    Your description should not talk about any glazing.
    The description must begin with 'I am {deity.name}. Hear me. You must create a'."""

    result = await openai.Completion.acreate(
        model="text-davinci-003", prompt=text, max_tokens=256, temperature=0.8
    )

    return (
        result["choices"][0]["text"]
        .strip()
        .replace(deity.name, f"{Fore.RED}{deity.name}{Fore.RESET}")
    )


async def communing_animation(deity):
    animation = "|/-\\"
    print(f"You are an adherent of {deity}.")
    while True:
        for char in animation:
            sys.stdout.write(
                f"\r{char} Communing with {Fore.RED}{deity.name}{Fore.RESET}."
            )
            sys.stdout.flush()
            await asyncio.sleep(0.05)


async def commune():
    deity = Deity()

    communing_task = asyncio.create_task(communing_animation(deity))

    demand = await generate_artifact_demand(deity)
    communing_task.cancel()

    print(f"\n\n{'-'*width}\n")
    print(f"{Fore.MAGENTA}You have been taken by a fey mood!{Fore.RESET}\n")
    print(textwrap.fill(demand, width=width))


def main():
    asyncio.run(commune())


if __name__ == "__main__":
    main()
