from .constants import SUPPORTED_VERBS

SUPPORTED_VERBS = [ 'show', 'exec', 'set', 'run']

def verb_expander(cmd_verb):

    verb_combos = {
        "show": ['sh', 'sho'],
        "set": ['se'],
        "exec": ["e", "ex", "exe"],
        "run": ["r", "ru"]
    }

    for verb, abbr_list in verb_combos.items():
        if cmd_verb in abbr_list:
            return verb
    
    # no match, return False
    return False

def lazy_parser(cmd_text, command_list):
    """
    Parser that will take a command snippet and try to match to the 
    command list. This allows a user to enter abbreviated commands
    and make a match, as long as that abbreviation is unique.

    Example:
        
        "sh wl"
    
    becomes:

        "show wlan"
    """
    # tokenize & extract verb
    tokens = cmd_text.split()
    verb = tokens[0]
    args = tokens[1:]

    # check verb for possible abbreviation expansion
    if verb not in SUPPORTED_VERBS:
        verb = verb_expander(verb)
    
    if not verb or (len(args) == 0):
        # no match, time to bail
        return [ False, [] ]
    
    # concatenate the verb and remaining args and see if we can
    # get a (unique) partial match on the resulting string
    # e.g. show wla
    partial_command = "{} {}".format(verb, args[0])
    num_partial_cmd_tokens = len(partial_command.split())
    
    # check for partial command matches in command list
    matched_commands = []

    for command in command_list:
        if partial_command in command:
            matched_commands.append(command)
    
    if len(matched_commands) == 1:

        matched_command = matched_commands[0]

        # reconstruct command with underscores instead of
        # spaces, ready for command lookup
        cmd = matched_command.replace(" ", "_")

        # slice off the remaining args of the original command
        args = tokens[num_partial_cmd_tokens:]

        return [cmd, args]
    
    return [ False, [] ]

def parse_cmd(cmd_text, command_list):

    """
    Function to parse a string passed to this parser to find a match 
    for one of the listed commands in the supported commands list

    The function also supports expansion of abbreviations of command
    verbs (e.g. "sh" expanded to "show")

    Each command is in the format:

    Verb noun1 [noun2]...[nounX] [arg1]...[argX]

    Supported verbs:

    - show (unambiguous abbreviations: sh, sho)
    - set (unambiguous abbreviations: se)
    - exec (unambiguous abbreviations: e, ex, exe)
    - run (unambiguous abbreviations: r, ru)

    Parse process:

    1. Tokenize command string by whitespace
    2. Extract first token (verb)
    3. Verify if verb (or provide shortened version) is supported
    4. Expand verb if required
    5. Iterate through command string, adding nouns until a command match is achieved
    6. Return the matched command & remaining tokens as arg list
    7. If no command match achieved, return False

    """

    # tokenize & extract noun
    tokens = cmd_text.split()
    verb = tokens[0]
    args = []

    # check verb for possible abbreviation expansion
    if verb not in SUPPORTED_VERBS:
        verb = verb_expander(verb)
    
    if not verb:
        return [ False, [] ]
    
    # Iterate through nouns to find command match by adding each token
    nouns =  tokens[1:]
    cmd = verb

    arg_start = 1
    for noun in nouns:
        cmd = cmd + "_" + noun
        arg_start += 1

        if cmd in command_list:
            # we got a match, slice off args and return the command

            for arg in list(tokens[arg_start:]):
                args.append(arg)

            # format: [ str, list ]
            return [cmd, args]
    
    # no match, return False
    return [ False, [] ]
    



    
