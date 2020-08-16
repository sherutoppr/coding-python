import datetime

# unique id for each note in notebook
last_id = 0


class Note:
    """Represent a note in notebook"""
    def __init__(self, memo, tags=""):
        """ initiate memo, comma-separated tags, note creation data and id """
        self.memo = memo
        self.tags = tags
        self.created_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """return true if filter is present in memo or tag , otherwise return false"""
        return filter in self.memo or filter in self.tags


class Notebook:
    """represent collection of notes that can be tagged, modified and searched"""
    def __init__(self):
        """initialize a notebook with empty list"""
        self.notes = []

    def new_note(self, memo, tags=""):
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """find the note by note_id"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
        else:
            return "Note not found"

    def modify_tags(self, note_id, tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
        else:
            return "note not found"

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]



