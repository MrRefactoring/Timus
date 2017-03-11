import sys

string = sys.stdin.read().strip().split()
trolley = 0
tram = 0
for i in string:
    if "tram," in i or "tram." in i or "tram!" in i or "tram-" in i or "tram:" in i or "tram?" in i or\
                    "tram\n" in i or i == "tram":
        tram += 1
    elif "trolleybus,"in i or "trolleybus."in i or "trolleybus!"in i or "trolleybus-"in i or\
        "trolleybus:"in i or "trolleybus?"in i or "trolleybus\n" in i or i == "trolleybus":
        trolley += 1
if tram == trolley:
    print("Bus driver")
elif tram > trolley:
    print("Tram driver")
else:
    print("Trolleybus driver")
