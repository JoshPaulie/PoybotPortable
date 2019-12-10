from prettytable import PrettyTable

commandDict = {
    "g.bringe": "Returns better cringe",
    "g.fword": "Returns twink",
    "g.hello": "Returns a greeting",
    "g.help": "Returns help menu!",
    "g.joker": "Returns actual clown",
    "g.kanye": "Returns words of our Yessiah",
    "g.paypig": "Returns Dekar Twitch link",
    "g.pecs & g.quads": "Returns soft porn",
    "g.rank": "Returns rank of all gooners!",
    "g.tellmeabout" : "Returns big facts",
    "g.whiskeyrad": "Returns perfection",
    "g.yo": "Returns a better greeting"
}

commandsTable = PrettyTable()
commandsTable.field_names = ["Command", "Action"]


def printCommandsInDiscord():
    for key, value in commandDict.items():
        commandsTable.add_row((key, value))
    return "```" + str(commandsTable) + "```"
