class Note:
    def __init__(self, name, note=[]):
        self.noteList = note  # [text, doDoneThisNote(True/False)]
        self.name = name

    def __str__(self): return self.name

    def addNote(self, text):
        self.noteList.append([text, False])
        return True

    def editNote(self, count, text=False, done=False):
        if len(self.noteList) >= count - 1 >= 0:
            if not text:
                self.noteList[count - 1][1] = done
            else:
                self.noteList[count - 1] = [text, done]
        else:
            return False  # count error
        return True

    def delNote(self, count):
        if len(self.noteList) >= count - 1 >= 0:
            del self.noteList[count - 1]
        else:
            return False
        return True

    def textNote(self):
        t = []
        for g in range(len(self.noteList)):
            i=self.noteList[g]
            t.append(
                ("✔️ " if i[1] else "❌ ")+str(i[0]) if g == len(self.noteList) else ("✔️ " if i[1] else "❌ ") + str(i[
                    0]) + ';')
        return t