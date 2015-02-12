##  CHORD LOOKUP
##
## challenge #87 (intermediate)
## http://www.reddit.com/r/dailyprogrammer/comments/y0z3y/8102012_challenge_87_intermediate_chord_lookup/
##
##
## sarthak7u@gmail.com
CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F",
                   "F#", "G", "G#", "A", "A#", "B"]


def chord_lookup(chord):
    """
    Computes semitones of a chord

    Args:
        string: Nome of the chord

    Returns:
        A list of all semitones in chord
    """
    scale = CHROMATIC_SCALE

    # get the base note
    base_note = chord[0:1].upper()
    if base_note not in scale:
        return "N/A"

    # check if base note sharp
    try:
        if chord[1] == "#":
            base_note += "#"
    except:
        pass

    # compute semitones
    semitones = [base_note,
                 scale[(scale.index(base_note) + 4) % 12],
                 scale[(scale.index(base_note) + 7) % 12]]

    if len(chord) > 1:
        # check if minor chord
        if chord[1:].lower() == "m" or chord[2:].lower() == "m":
            semitones[1] = scale[(scale.index(base_note) + 3) % 12]
        # check if dom 7th chord
        elif chord[1:].lower() == "7" or chord[2:].lower() == "7":
            semitones.append(scale[(scale.index(base_note) + 10) % 12])
        # check if minor 7th chord
        elif chord[1:].lower() == "m7" or chord[2:].lower() == "m7":
            semitones[1] = scale[(scale.index(base_note) + 3) % 12]
            semitones.append(scale[(scale.index(base_note) + 10) % 12])
        # check if major 7th chord
        elif chord[1:].lower() == "maj7" or chord[2:].lower() == "maj7":
            semitones.append(scale[(scale.index(base_note) + 11) % 12])
        else:
            return "N/A"

    return semitones
