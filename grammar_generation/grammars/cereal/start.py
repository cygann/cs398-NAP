from ideaToText import Decision

# "Start" is a special decision which is invoked by the Sampler
# to generate a single sample.
class Start(Decision):

    def registerChoices(self):

        self.addChoice('fruit', {
            'Fruit Loops':10,
            'Fruity Pebbles':5
        })

        self.addChoice('cocoa', {
            'Cocoa Puffs':10,
            'Coca Pebbles':5
        })

        self.addChoice('grain', {
            'Frosted Flakes':10,
            'Captain Crunch':5
        })


    def updateRubric(self):
        if self.getChoice('fruit') == 'Fruit Loops':
            self.turnOnRubric('Fruit Loops')
            cocoa = self.getChoice('cocoa')
            self.turnOnRubric(cocoa)
        elif self.getChoice('fruit') == 'Fruity Pebbles':
            self.turnOnRubric('Fruity Pebbles')
            grain = self.getChoice('grain')
            self.turnOnRubric(grain)

    def render(self):
        # Generate a bowl of cereal
        fruit = self.getChoice('fruit')
        if fruit == 'Fruit Loops':
            phrase = fruit + ' ' + self.getChoice('cocoa')
        elif fruit == 'Fruity Pebbles':
            phrase = fruit + ' ' + self.getChoice('grain')

        return phrase

