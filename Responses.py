from datetime import *

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","helo","hi","broooo","hai",):
        return "Hi Mawa!! Ela unnav"

    if user_message in ("who are you","who r u","eh evaru nuvvu","eh evaru nuvvu ila unnav enti","koun hey re thuu",):
        return "My name is Bot.... Sir!!"

    if user_message in ("who can you do","what can u do","em cheyagallav","edhina chey",):
        return "Time entho telusaa..."

    if user_message in ("hotstar","hotstar cookies","hotstarcookies","hsc",):
        return "Under Processing"

    if user_message in ("fuck","foff","f*ck","suck",):
        return "No Bad Words please...."

    if user_message in ("agent anand santosh episode 1","agent anand santosh ep1","aas episode 1","aas ep1","aas ep 1","aas1","aasep1",):
        return "https://www.youtube.com/watch?v=BL5RW8PM4F0"
    if user_message in ("agent anand santosh episode 2","agent anand santosh ep2","aas episode 2","aas ep2","aas ep 2","aasep2","aas2",):
        return "https://drive.google.com/u/2/uc?id=1-0JavQzvUYoKORtN6TISoLm7Aq81uSDE"
    if user_message in ("agent anand santosh episode 3","agent anand santosh ep3","aas episode 3","aas ep3","aas ep 3","aasep3","aas3",):
        return "https://drive.google.com/u/2/uc?id=1gEMztYgXW-7VlJfwZ3LE6j4RqcThMntc&export=download"

    if user_message in ("bro time entha","time","time?","time entha","time cheppu ra pumka","cheppu","chepu",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%M:%S")

        return str(date_time)
    return "Ardhamkaledhu!!"
    