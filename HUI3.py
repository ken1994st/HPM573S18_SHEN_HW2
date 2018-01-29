# HUI3 coefficients
Constant = 0.371
Constantb = 1.371
Coefficients = {'Vision':     [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                'Hearing':    [1, 0.95, 0.89, 0.80, 0.74, 0.61],
                'Speech':     [1, 0.94, 0.89, 0.81, 0.68],
                'Ambulation': [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                'Dexterity':  [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                'Emotion':    [1, 0.95, 0.85, 0.64, 0.46],
                'Cognition':  [1, 0.92, 0.95, 0.83, 0.60, 0.42],
                'Pain':       [1, 0.96, 0.90, 0.77, 0.55]};

def scorelevel (vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """

    :param vision: able to see
    :param hearing: able to hear
    :param speech: able to understand speech
    :param ambulation: able to walk around
    :param dexterity: use of two hands
    :param emotion: happy
    :param cognition: able to remember
    :param pain: free of pain
    :return: HUI3 score
    """

    if not(vision in [1,2,3,4,5,6]):
       raise ValueError('Vision level can take only from 1 to 6')
    if not(hearing in [1,2,3,4,5,6]):
       raise ValueError('Hearing level can take only from 1 to 6')
    if not(speech in [1,2,3,4,5]):
       raise ValueError('Speech level can take only from 1 to 5')
    if not(ambulation in [1,2,3,4,5,6]):
       raise ValueError('Ambulation level can take only from 1 to 6')
    if not(dexterity in [1,2,3,4,5,6]):
       raise ValueError('Dexterity level can take only from 1 to 6')
    if not(emotion in [1,2,3,4,5]):
       raise ValueError('Emotion level can take only from 1 to 5')
    if not(cognition in [1,2,3,4,5,6]):
       raise ValueError('Cognition level can take only from 1 to 6')
    if not(pain in [1,2,3,4,5]):
       raise ValueError('Pain level can take only from 1 to 5')




    score = [Constantb * (Coefficients['Vision'][vision -1] *
                          Coefficients['Hearing'][hearing -1] *
                          Coefficients['Speech'][speech -1] *
                          Coefficients['Ambulation'][ambulation -1] *
                          Coefficients['Dexterity'][dexterity -1] *
                          Coefficients['Emotion'][emotion -1] *
                          Coefficients['Cognition'][cognition -1] *
                          Coefficients['Pain'][pain -1])-Constant]

    return score








