# Match Condition

browser = str(input("Enter Browser name \n"))
browser = browser.lower()

match browser:
    case 'chrome':
        print("C")
    case 'firefox':
        print('f')
    case _:
        print('No browser found')
