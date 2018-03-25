import System
import binascii

def textToBin(stringmessage):
    newBinText = []

    for i in stringmessage:
        newBinText.append(bin(ord(i))[2:])
    return ''.join(newBinText)

def binToChuck(newBinText):
    newChuckNorrisMessage = []
    i = 0
    counter = 0
    holder = ""

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


def convertToChuckNorrisMessage(messageString):
    newBinString = textToBin(messageString)
    newMessage = binToChuck(newBinString)
    return newMessage
