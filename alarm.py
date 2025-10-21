class Alarm:
    def __init__(self, typ, nivå):
        self.typ = typ
        self.nivå = nivå

    def __str__(self):
        return f"{self.typ}-larm: {self.nivå}%"

    def är_aktiverat(self, cpu, mem, disk):
        if self.typ == "CPU":
            return cpu > self.nivå
        elif self.typ == "Minne":
            return mem > self.nivå
        elif self.typ == "Disk":
            return disk > self.nivå
        return False
