from subprocess import check_call

def upp(tekst):
    # tekst = input(': ')
    tekst = tekst.upper()
    print(tekst)
    # pyperclip.copy(tekst)
    return tekst


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)

tekst = input('hej:')
tekst = upp(tekst)
copy2clip(tekst)