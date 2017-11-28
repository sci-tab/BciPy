# -*- coding: utf-8 -*-
from helpers.load import load_txt_data


def _write_triggers_from_sequence_calibration(array, file):
    """
    Write triggers from calibration.

    Helper Function to write trigger data to provided file. It assigns
        target letter based on the first presented letter in sequence, then
        assigns target/nontarget label to following letters.

    It writes in the following order:
        (I) presented letter, (II) targetness, (III) timestamp
    """

    x = 0
    for i in array:

        # extract the letter and timing from the array
        (letter, time) = i

        # determine what the trigger are
        if x == 0:
            targetness = 'first_pres_target'
            target_letter = letter
        elif x == 1:
            targetness = 'fixation'
        elif x > 1 and target_letter == letter:
            targetness = 'target'
        else:
            targetness = 'nontarget'

        # write to the file
        file.write('%s %s %s' % (letter, targetness, time) + "\n")

        x += 1

    return file


def _write_triggers_from_sequence_copy_phrase(array, file,
                                              copy_text, typed_text):
    """
    Write triggers from copy phrase.

    Helper Function to write trigger data to provided file. It assigns
        target letter based on matching the next needed letter in typed text
        then assigns target/nontarget label to following letters.

    It writes in the following order:
        (I) presented letter, (II) targetness, (III) timestamp
    """

    # get relevant spelling info to determine what was and should be typed
    spelling_length = len(typed_text)
    last_typed = typed_text[-1]
    correct_letter = copy_text[spelling_length - 1]

    # because there is the possiblility of incorrect letter and correction,
    # we check here what is appropriate as a correct response
    if last_typed == correct_letter:
        correct_letter = copy_text[spelling_length]
    else:
        correct_letter = '<'

    x = 0

    for i in array:

        # extract the letter and timing from the array
        (letter, time) = i

        # determine what the triggers are:
        #       assumes there is no target letter presentation.
        if x == 0:
            targetness = 'fixation'
        elif x > 1 and correct_letter == letter:
            targetness = 'correct'
        else:
            targetness = 'incorrect'

        # write to the file
        file.write('%s %s %s' % (letter, targetness, time) + "\n")

        x += 1

    return file


def _write_triggers_from_sequence_free_spell(array, file):
    """
    Write triggers from free spell.

    Helper Function to write trigger data to provided file.

    It writes in the following order:
        (I) presented letter, (II) timestamp
    """

    x = 0

    for i in array:

        # extract the letter and timing from the array
        (letter, time) = i

        # write to file
        file.write('%s %s' % (letter, time) + "\n")

        x += 1

    return file


def trigger_decoder(trigger_loc):

    # Load triggers.txt
    if not trigger_loc:
        trigger_loc = load_txt_data()

    with open(trigger_loc, 'r') as text_file:
        # Get every line of trigger.txt if that line does not contain 'fixation' and 'first_pres_target'
        # [['words', 'in', 'line'], ['second', 'line']...]

       # trigger file has three columns: SYMBOL, TARGETNESS_INFO, TIMING

        trigger_txt = [line.split() for line in text_file
                       if 'fixation' not in line and 'first_pres_target' not in line]

    return trigger_txt