import pytest
from Game import games
from TimeShow import TimeShow

@pytest.mark.parametrize("words, expect,length",
                         [
                             ("a", 1, 1),#Verify the score of a single letter entered
                             ("e", 1, 1),
                             ("i", 1, 1),
                             ("o", 1, 1),
                             ("u", 1, 1),
                             ("l", 1, 1),
                             ("n", 1, 1),
                             ("r", 1, 1),
                             ("s", 1, 1),
                             ("t", 1, 1),
                             ("d", 2, 1),
                             ("g", 2, 1),
                             ("b", 3, 1),
                             ("c", 3, 1),
                             ("m", 3, 1),
                             ("p", 3, 1),
                             ("f", 4, 1),
                             ("h", 4, 1),
                             ("v", 4, 1),
                             ("w", 4, 1),
                             ("y", 4, 1),
                             ("k", 5, 1),
                             ("j", 8, 1),
                             ("x", 8, 1),
                             ("q", 10, 1),
                             ("z", 10, 1),
                             ("A", 1, 1),#Capital will be automatically converted to lowercase for judgment
                             ("Z", 10, 1),
                             ("cabbage", 14, 7),#Verify that the score of "cabbage" is equal to fourteen
                             ("goods", 7, 5),#Verify that the score of "goods" is equal to 14
                             ("six", 10, 3),#Verify that the score of "six" is equal to 1
                             ("cabbage",  "Invalid input length",6),#Invalid input length
                             ("cabbage", "Invalid input length",8),
                             ("1", "Invalid input words", 1),#Invalid input words
                             ("abca1", "Invalid input words", 5),#Cannot form words
                             ("!", "Invalid input words", 1),#Invalid special characters
                             ("op0", "Invalid input words",3)#Cannot form words

                          ])
def test_game(words,expect,length):
    g=games()
    assert g.Calculate_Score(words,length)==expect
def test_TimeShow():#Test countdown
    b=1
    try:
        t = TimeShow(1)
        t.start()
    except:
        print("TimeShow Error")
        b=0
    assert b==1
if __name__ == '__main__':
	pytest.main(['-v','-s'])
