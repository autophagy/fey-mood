import random
from dataclasses import dataclass, field

from colorama import Fore

from .creature import create_random_creature
from .names import create_random_name
from .spheres import bases, friends


def make_spheres():
    b = bases(random.randint(1, 2))
    f = friends(b, num_friends=random.randint(0, 3))
    return list(b.keys()) + f


def make_gender():
    return random.choice(["male", "female", "genderless"])


@dataclass
class Deity:
    name: str = field(default_factory=create_random_name)
    gender: str = field(default_factory=make_gender)
    creature: str = field(default_factory=create_random_creature)
    spheres: list[str] = field(default_factory=make_spheres)

    def __str__(self):
        spheres = self.spheres[:-1]
        last_sphere = self.spheres[-1]

        if len(self.spheres) > 1:
            spheres_string = f"{', '.join([Fore.GREEN + s.lower() + Fore.RESET for s in spheres])} and {Fore.GREEN + last_sphere.lower() + Fore.RESET}"
        else:
            spheres_string = Fore.GREEN + last_sphere.lower() + Fore.RESET

        name = Fore.RED + self.name + Fore.RESET
        species = f"{Fore.CYAN}{self.gender} {self.creature}{Fore.RESET}"

        return f"{name}. {name} most often takes the form of a {species} and is associated with {spheres_string}"
