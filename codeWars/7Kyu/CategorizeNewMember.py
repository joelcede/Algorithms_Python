def open_or_senior(data):
    isOpenOrSenior = []
    for i in range(len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            isOpenOrSenior.append("Senior")
        else:
            isOpenOrSenior.append("Open")
    return isOpenOrSenior