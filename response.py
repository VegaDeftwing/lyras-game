
def checkYN(input):
    yes_list = ["yes", "y", "true", "t", "si", "mhmm", "fuck yeah", "yeah"]
    no_list = ["no", "n", "nope", "false", "na", "noo"]
    yes_respect_male = ["yes, sir", "yes sir", "sir yes sir", "sir, yes sir"]
    yes_respect_female = ["yes, mam", "yes mam", "mam, yes mam"]
    yes_respect_andro = ["as you wish", "very well"]
    no_respcet_male = ["no, sir", "no sir", "sir no sir", "sir, no sir"]
    no_respect_female = ["no, mam", "no mam", "sir no mam", "sir, no mam"]
    disrespect = ["fuck off", "screw off", "no way", "fuck you"]

    if input.lower() in yes_list:
        return 1
    elif input.lower() in no_list:
        return 0
    elif input.lower() in yes_respect_male:
        return 2
    elif input.lower() in no_respcet_male:
        return -2
    elif input.lower() in yes_respect_female:
        return 3
    elif input.lower() in no_respect_female:
        return -3
    elif input.lower() in yes_respect_andro:
        return 4
    elif input.lower() in disrespect:
        return -5
    else:
        return "invalid"
