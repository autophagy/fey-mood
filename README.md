# Fey Mood

![](output.gif)

## What?

A tool to simulate being divinely inspired by a deity from Dwarf Fortress,
specifically to create a ceramic object. Uses OpenAI's `text-davinci-003` model.

## How?

### With Nix

```
> nix build
> export OPENAI_API_KEY="xxx"
> ./result/bin/fey_mood
```

### With Poetry

```
> poetry install
> export OPENAI_API_KEY="xxx"
> poetry run fey_mood
```

## Why?

I wanted to explore ideas around automation, labour and creative control (or
lack thereof) with regards to the generative AI models that are currently being
released. I'm an amateur ceramicist, and had an idea for a project where I
secede creative control over a pottery project to an large language model, where
I would just act as an appendage that realises the object in the real world.

Noticed that this relationship is more-or-less how the dwarves in Dwarf Fortress
must feel when they enter a strange mood. Hopefully the consequences will be
less severe if I don't fulfil the divine demands.
