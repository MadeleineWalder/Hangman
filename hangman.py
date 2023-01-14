'''
Contains the hangman diagram in each stage.
'''
__HANGMAN_STAGES__ = [  # Stage 0: head, body, arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     L L
                   |
                """,
                # Stage 1: head, body, arms, and leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |       L 
                   |
                """,
                # Stage 2: head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   |
                """,
                # Stage 3: head, body, and arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   |
                """,
                # Stage 4: head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   |
                """,
                # Stage 5: head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   |
                """,
                # Stage 6: begining
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   |
                """
    ]


def display_hangman(stage):
    '''
    Prints a stage of the hangman diagram.

    :param stage: The stage of completion that the hangman is at.
    '''
    print(__HANGMAN_STAGES__[stage])
