import glob


folder  = glob.glob("C:\Files\p4ne_training\config_files\*.txt")
netlist = []

for i in folder:
    with open(i) as f:
        for l in f:
            if (l.find("ip address") >= 1) & (l.find(".") >= 3):
                l = l.strip()
                l = l.replace("ip address", "")
                netlist.append(l)


netlist = list(set(netlist))

for i in netlist:
    print(i)
