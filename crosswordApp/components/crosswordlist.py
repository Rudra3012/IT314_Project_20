from django_unicorn.components import UnicornView, QuerySetType

from crosswordApp.models import crossword


class CrosswordlistView(UnicornView):
    name: str = ""
    Crosswords: QuerySetType[crossword] = crossword.objects.all()

    def mount(self):
        self.Crosswords = crossword.objects.all()

    def add_crossword(self):
        crossword.objects.create(title=self.name, description="test", width=10, height=10)
        self.name = ""
        self.Crosswords = crossword.objects.all()

    def remove_crossword(self, title: str):
        print("remove crossword: " + str(title))
        crossword.objects.filter(title=title).delete()
        self.Crosswords = crossword.objects.all()


