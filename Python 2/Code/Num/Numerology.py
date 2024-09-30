class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName.upper()  # Convert name to uppercase for consistency
        self.dob = sDOB

        # Private variables to store computed values
        self.__iPersonalityNumber = self._calculatePersonalityNumber()
        self.__iSoulNumber = self._calculateSoulNumber()
        self.__iLifePathNumber = self._calculateLifePathNumber()
        self.__iAttitudeNumber = self._calculateAttitudeNumber()
        self.__iBirthdayNumber = self._calculateBirthdayNumber()
        self.__iPowerName = self.__iSoulNumber + self.__iPersonalityNumber

    # Getters
    def getBirthdate(self):
        return self.dob

    def getName(self):
        return self.name

    def getPersonality(self):
        return self.__iPersonalityNumber

    def getSoulNumber(self):
        return self.__iSoulNumber

    def getLifePath(self):
        return self.__iLifePathNumber

    def getAttitude(self):
        return self.__iAttitudeNumber

    def getBirthDay(self):
        return self.__iBirthdayNumber

    def getPowerName(self):
        return self.__iPowerName

    # Private methods for calculations
    def _calculatePersonalityNumber(self):
        consonants = ''.join(char for char in self.name if char not in 'AEIOU' and char.isalpha())
        return self.__reduceNumber(sum(self.convertCharToInteger(c) for c in consonants))

    def _calculateSoulNumber(self):
        vowels = ''.join(char for char in self.name if char in 'AEIOU')
        return self.__reduceNumber(sum(self.convertCharToInteger(c) for c in vowels))

    def _calculateLifePathNumber(self):
        numbers = [int(char) for char in self.dob if char.isdigit()]
        return self.__reduceNumber(sum(numbers))

    def _calculateAttitudeNumber(self):
        month, day, _ = self.dob.split('-')
        return self.__reduceNumber(int(month) + int(day))

    def _calculateBirthdayNumber(self):
        _, day, _ = self.dob.split('-')
        return self.__reduceNumber(int(day))

    # Utility functions as provided
    def convertCharToInteger(self, sCharacter):
        iCharacterToNumberValue = 0
        if sCharacter.isalpha():
            iCharacterToNumberValue = ((ord(sCharacter.upper()) - 65) % 9 + 1)
        return iCharacterToNumberValue

    def __reduceNumber(self, iNumber):
        while len(str(iNumber)) > 1:
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber
