class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def turnOn(self):
        if self._tv:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv:
            self._tv.turnOff()

    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()

    def setCanal(self, canal):
        if self._tv:
            self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        if self._tv:
            self._tv.setVolumen(volumen)

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv