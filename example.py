def change_sound(sounds, animal, new_sound):
    sounds[animal] = new_sound

sounds =
{
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

change_sound(sounds, 'cat', 'purrs')
print(sounds)