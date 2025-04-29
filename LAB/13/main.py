from FileReader import *

class ShowLiner(FileReaderObserver):

    def onReceive(self, line):
        line = line.rstrip()
        print(line)

class WordsCounter(FileReaderObserver):

    def __init__(self):
        self.word_counter = 0

    def onReceive(self, line):
        words = line.split()
        self.word_counter += len(words)

class CheckWord(FileReaderObserver):

    def __init__(self, word):
        self.word = word

    def onReceive(self, line):
        words = line.split()
        for w in words:
            if w == self.word:
                return True
        return False

class UniqueWordsCounter(FileReaderObserver):
    def __init__(self):
        self.word_counter = 0

    def onReceive(self, line):
        words = line.lower().split()
        self.word_counter += len(set(words))

class TheLongestWord(FileReaderObserver):
    def __init__(self):
        self.word_counter = 0

    def onReceive(self, line):
        words = line.lower().split()
        for w in words:
            if len(w) > self.word_counter:
                self.word_counter = len(w)


if __name__ == '__main__':
    filereader = FileReader('input01.txt')

    # showliner = ShowLiner()
    # filereader.subscribe(showliner)

    # wordcounter = WordsCounter()
    # filereader.subscribe(wordcounter)

    # word = "suka"
    # checkword = CheckWord(word)
    # print(checkword.onReceive("suka"))

    # uniquewordcounter = UniqueWordsCounter()
    # filereader.subscribe(uniquewordcounter)

    thelongestword = TheLongestWord()
    filereader.subscribe(thelongestword)

    filereader.read()

    #print(wordcounter.word_counter)
    # print(uniquewordcounter.word_counter)
    print(thelongestword.word_counter)