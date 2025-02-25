#!/usr/bin/env python
import sys, re
data = sys.stdin.read()

def process_dennik_n(data):
    data = data.split("Tmavý režim")[1]
    data = data.split("\n")
    output = ""
    for line in data:
        if re.match('(^Zdieľať)',line) or re.match('(^\\d+:\\d+$)',line)\
            or re.match('(\\[.*\\]\\d*:\\d*)',line) or re.match('(^\\d*\\n$)',line) \
            or re.match('(^\\[.*\\].*)',line):
           continue
        elif re.match('(^\\s\\s•)',line) or re.match('(^Najnovšie z témy:)',line) or re.match('(^Prečítajte si tiež.*)',line):
            break
        else:
            if re.match('(.*Minúta po minúte\\d*.*)',line):
                line = line.replace("minúte", "minúte ")
            line = re.sub(r'(?<=[A-Za-z])(?=[A-Z][a-z])', ' ', line)
            output += line + "\n"
    sys.stdout.write(output)

def process_cnn(data):
    data = data[data.index("• About CNN")+1:]
    data = data[data.index("CNN  —")+len("CNN  —\n"):]
    data = data.split("\n")
    output = ""
    for line in data:
        line = re.sub(r'(^Link Copied!.*)',"",line)
        if re.match('(^CNN has reached.*)',line):
            continue
        if "Ad Feedback" in line:
            break
        output += line + "\n"
    sys.stdout.write(output)

def process_nytimes(data):
    data = data[data.index("SKIP ADVERTISEMENT")+len("SKIP ADVERTISEMENT\n"):]
    data = data.split("\n")
    output = ""
    for line in data:
        if "•" in line and not re.match('^.*•.*[0-9]+.*$',line):
            continue
        if re.match('(^See more on:*.)',line):
            break
        output += line + "\n"
    sys.stdout.write(output)

def process_wired(data):
    data = data[data.index("• Coupons")+len("• Coupons\n"):]
    data = data.split("\n")
    output = ""
    for line in data:
        if "•" in line and not re.match('^.*•.*[0-9]+.*$',line):
            continue
        if re.match('(^You Might Also Like*.)',line):
            break
        output += line + "\n"
    sys.stdout.write(output)

if "Denník N" in data:
    process_dennik_n(data)
elif "CNN" in data:
    process_cnn(data)
elif "Today’s Paper" in data:
    process_nytimes(data)
elif "WIRED" in data:
    process_wired(data)
else:
    sys.stdout.write(data)
