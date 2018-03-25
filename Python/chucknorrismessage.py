import System
import binascii

# Creates a binary string out of a ASCII string
def textToBin(stringmessage):
    newBinText = []

    for i in stringmessage:
        if len(bin(ord(i))[2:]) == 7:
            newBinText.append(bin(ord(i))[2:])
        else:
            newBinText.append('0' + bin(ord(i))[2:])

    return ''.join(newBinText)

# Converts the binary string to unary string
def binToChuck(newBinText):
    newChuckNorrisMessage = []
    i = 0
    counter = 0

    while i < len(newBinText):
        if (i+1) < len(newBinText):
            if newBinText[i] == "1":
                counter += 1
                if newBinText[i+1] == "0":
                    newChuckNorrisMessage.append("0" + " " + ("0" * counter) + " ")
                    counter = 0
                    i += 1
                else:
                    i += 1
            else:
                counter += 1
                if newBinText[i+1] == "1":
                    newChuckNorrisMessage.append("00" + " " + ("0" * counter) + " ")
                    counter = 0
                    i += 1

                else:
                    i += 1
        else:
            if newBinText[i] == "1":
                
                if counter == 0:
                    newChuckNorrisMessage.append("0 0")
                    return ''.join(newChuckNorrisMessage)
                else:
                    counter += 1
                    newChuckNorrisMessage.append("0" + " " + ("0" * counter))
                    return ''.join(newChuckNorrisMessage)
            else:
                if counter == 0:
                    newChuckNorrisMessage.append("00 0")
                    return ''.join(newChuckNorrisMessage)
                else:
                    counter += 1
                    newChuckNorrisMessage.append("00" + " " + ("0" * counter))
                    return ''.join(newChuckNorrisMessage)

# Calls for all other functions with input
def convertToChuckNorrisMessage(messageString):
    newBinString = textToBin(messageString)
    newMessage = binToChuck(newBinString)
    return newMessage
