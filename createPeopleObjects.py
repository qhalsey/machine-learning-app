class People:
    def __init__(self, fn, ln, imgn):
        self.firstname = fn
        self.lastname = ln
        self.imagename = imgn

people = []

def instantiateObjectes():
    people.append(People("Quentin", "Halsey", "img/quentinhalsey.png"))
    people.append(People("Daryl", "Sansavero", "img/darylsansavero.png"))
    people.append(People("Kathy", "Emtiaz", "img/kathyemtiaz.png"))
    people.append(People("Lindy", "Tannenbaum", "img/lindytannenbaum.png"))
    people.append(People("Nathan", "Berger", "img/nathanberger.png"))
    people.append(People("Priya", "Karanam", "img/priyakaranam.jpeg"))
    people.append(People("Raj", "Nath", "img/rajnath.png"))
    people.append(People("Rigel", "Nath", "img/rigelnath.png"))
    people.append(People("Simon", "Palmer", "img/simonpalmer.png"))
    people.append(People("Soni", "Priya", "img/sonipriya.png"))
    people.append(People("Tom", "Fuchs", "img/tomfuchs.jpeg"))
    people.append(People("Tracy", "Janos", "img/tracyjanos.png"))
    return people
