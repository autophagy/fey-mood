import random
from dataclasses import dataclass, field

from .creature import creatures
from .names import names
from .spheres import bases, friends


def make_spheres():
    b = bases(random.randint(1, 2))
    f = friends(b, num_friends=random.randint(0, 3))
    return list(b.keys()) + f


def make_name():
    return random.choice(names)


def make_gender():
    return random.choice(["male", "female", "genderless"])


def make_creature():
    return random.choice(creatures)


@dataclass
class Deity:
    name: str = field(default_factory=make_name)
    gender: str = field(default_factory=make_gender)
    creature: str = field(default_factory=make_creature)
    spheres: list[str] = field(default_factory=make_spheres)

    def __str__(self):
        spheres = self.spheres[:-1]
        last_sphere = self.spheres[-1]

        if len(self.spheres) > 1:
            spheres_string = (
                f"{', '.join([s.lower() for s in spheres])} and {last_sphere.lower()}"
            )
        else:
            spheres_string = last_sphere.lower()

        return f"{self.name}. {self.name} most often takes the form of a {self.gender} {self.creature} and is associated with {spheres_string}"
