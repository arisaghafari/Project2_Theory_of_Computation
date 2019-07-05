class PDA:
    def __init__(self):
        self.source =""
        self.destination =""
        self.alphabet =""
        self.pop_element =""
        self.push_element =""
        self.finalstates =[]
        self.states=[]
        self.firststate = ""
        self.Alphabets=[]
        self.stacksymbols=[]
        self.stackfirst=""
        self.cfg_list=[]


    def construct_PDA_from_file(self,lines):

        file1 = open("output1.txt", "w")

        lines[0]=(int(lines[0]))

        for i in range(lines[0]):
            self.states.append("q"+str(i))
        # print(self.states)

        lines[1] = lines[1].split(",")
        lines[1][len(lines[1]) - 1] = lines[1][len(lines[1]) - 1][0]
        # lines[1] = "".join(lines[1])
        # print(lines[1])
        self.Alphabets = lines[1]

        lines[2] = lines[2].split(",")
        lines[2][len(lines[2]) - 1] = lines[2][len(lines[2]) - 1][0]
        # lines[1] = "".join(lines[1])
        # print(lines[3])
        self.stacksymbols = lines[2]

        self.stackfirst=lines[3]
        lines = lines[4:]
        for i in range(0,len(lines)):
            if lines[i][0]=="-":
                lines[i]=lines[i][2:]

                self.firststate=lines[i][0:2]

            lines[i] = lines[i].split(",")

            if (lines[i][-1][-1])=="\n":
                lines[i][-1]=lines[i][-1][0:len(lines[i][-1])-1]

            for j in range(len(lines[i])):

                if lines[i][j][0] =="*":
                    # print(lines[i][-1])
                    self.finalstates.append(lines[i][j][1:])
                    # lines[i][j]=lines[i][j][1:]

        # print(lines)
        # print(self.firststate)
        # print(self.finalstates)


        for grammer in lines:
            if grammer[3]=="_":
                if grammer[4][0]=="*":
                    file1.write("(" + grammer[0] + grammer[2] + "qf" + ")->" + grammer[1]+"\n")
                else:
                    file1.write("("+grammer[0]+grammer[2]+grammer[4]+")->"+grammer[1]+"\n")
            else:
                i = 0
                for otherstates in self.states:
                    file1.write("("+grammer[0]+grammer[2]+otherstates+")->")
                    for others in self.states:
                        i+=1

                        if i%2==1:
                            file1.write(grammer[1] + "(" + grammer[4] + grammer[3][0] + others + ")" + "(" + others +grammer[3][1] + otherstates + ")|")
                        else:
                            file1.write(grammer[1] + "(" + grammer[4] + grammer[3][0] + others + ")" + "(" + others +grammer[3][1] + otherstates + ")"+"\n")
        file1.close()

