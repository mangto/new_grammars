class thisprogram:
    info = """
    ============================================================

        < info >

        match test program
        match is a function like switch in C language
        

        ( example )

        value = input()

        match value:
            case "somewhat":
                ...

            case default: # -> use default like else in 'if'
                ...

    ============================================================
    """

def function():
    userinput = input(" >>> ") # get an input from user

    try: userinput = eval(userinput) # change input type
    except NameError: userinput = str(userinput)

    match userinput:
        
        # string case

        case "info":
            print(thisprogram.info)
        
        case "stop":
            print("exiting program")

        case "author":
            print("@mangto on github")

        # list case

        case []:
            print("no name(s) given")
        
        case [name]:
            print(f"given name: {name}")

        case [*name]:
            print(f"given names: {name}, len: {len(name)}")
        
        #default case

        case default:
            print(f"ignored task '{userinput}'")

while __name__ == "__main__":
    function()