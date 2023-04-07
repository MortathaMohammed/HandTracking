class method:
    def thumb(list, tipIds):
        return list[tipIds[0]], list[tipIds[0]+1], list[tipIds[0]+2], list[tipIds[0]+3]

    def index(list, tipIds):
        return list[tipIds[1]], list[tipIds[1]+1], list[tipIds[1]+2], list[tipIds[1]+3]

    def middle(list, tipIds):
        return list[tipIds[2]], list[tipIds[2]+1], list[tipIds[2]+2], list[tipIds[2]+3]

    def ring(list, tipIds):
        return list[tipIds[3]], list[tipIds[3]+1], list[tipIds[3]+2], list[tipIds[3]+3]

    def little(list, tipIds):
        return list[tipIds[4]], list[tipIds[4]+1], list[tipIds[4]+2], list[tipIds[4]+3]