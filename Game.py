# coding=utf8
from TimeShow import TimeShow
import Config
import enchant

class games():

    def Calculate_Score(self, value,length):
        if len(value)!=length:
            return 'Invalid input length'
        words = enchant.Dict("en_US")
        if words.check(value)==False:
            return "Invalid input words"
        list1={'a','e','i','o','u','l','n','r','s','t'}
        list2={"d","g"}
        list3={'b','c','m','p'}
        list4={'f','h','v','w','y'}
        list5={'k'}
        list6={'j','x'}
        list7={'q','z'}
        score=0
        value_list=list(value)
        for item in value_list:
            item=item.lower()
            if item in list1:
                score=score+1
            elif item in list2:
                score = score + 2
            elif item in list3:
                score = score + 3
            elif item in list4:
                score = score + 4
            elif item in list5:
                score = score + 5
            elif item in list6:
                score = score + 8
            elif item in list7:
                score = score + 10
            else:return 'Invalid input words'
        return score

    def Console(self):
        global n
        n=0
        import random
        while True:
            if Config.time == 0:
                print('Time Out')
                break
            word_length = random.randint(1, 10)
            words = input("please input " + str(word_length) + " words:")
            print(t.Calculate_Score(words,word_length))

    def Count_Down(self):
        a = TimeShow(15)
        a.start()

if __name__ == '__main__':
    import threading
    t = games()
    global n,a
    try:
        t1=threading.Thread(target=t.Console)
        t2=threading.Thread(target=t.Count_Down)
        t1.start()
        t2.start()
    except:
        print("Thread Error")




