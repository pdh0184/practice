class animal():
    name = ''
    attr = ''
    sound = ''
    body_color = ''
    def cry(self):
        return(self.name + '의 울음소리는' + self.sound + '입니다')

    def color(self):
        return (self.name + '색깔은' + self.body_color + '입니다')

    def info(self):
        return(self.name + '은' + self.attr + '!' )

maltese = animal()
maltese.name = 'dog'
maltese.attr = 'cute'
maltese.sound = '멍멍'
maltese.body_color = 'white'

print(maltese.color(), maltese.cry())
print(maltese.info())
