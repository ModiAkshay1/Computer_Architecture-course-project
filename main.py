from input import list_of_instructions
# import matplotlib.pyplot as plt
outfile = open('log.txt' , 'w')

class Instruction:
    head_path = []
    data_path=[]
    tail_path = []
    route = []
    head = ""
    data=""
    tail = ""
    index = 0
    clock_cycle = 0
    end_time = 0
    start_time = -1
    source = ""
    destination = ""

    def __init__(self,instruction,routing,router_list,index):
        self.index=index
        self.clock_cycle = int(instruction[0])
        self.source = instruction[1]
        self.destination = instruction[2]
        self.head = self.destination + self.source + "00"
        self.data = instruction[3] + "01"
        self.tail = "00000000000000000000000000000010" #check krlena ek baar
        self.make_path(routing,router_list)
    
    def make_path(self,direction,router_list):
        self.route = self.get_path_XY(router_list)


    def get_path_XY(router_list):
        path=[]
        #Write code for XY routing
        return path

    def print_route(self):
        for i in self.route:
            print(i, end=" ")
        print()



class Router:
    name = ""
    counter = 0
    busy = False
    source = ""
    destination = ""
    def __init__(self, name):
        self.name = name
    def add_source(self, source):
        self.source = source
        self.counter += 1
    def add_destination(self, destination):
        self.destination = destination 
        self.counter += 1
    def add_header(self):
        self.counter += 1
    def add_flit(self):
        self.counter += 1
    def add_tail(self):
        self.counter = 0
    def update(self,instruction, clock_cyle, statement, source, destination):
        L = ["Clock cycle: ", str(clock_cyle) + " ", "Flit: ", str(statement) + " ", "Source: ", source.name + " ", "Destination: ", destination.name, "\n"]
        outfile.writelines(L)
        print("Clock cycle:", clock_cyle, "Flit:", statement, "Source:", instruction.source, "Destination:", instruction.destination)
        return 



class NoC:
    traffic1 = []
    traffic2 = []
    traffic3 = []
    traffic4 = []
    traffic5 = []
    traffic6 = []
    traffic7 = []
    traffic8 = []
    traffic9 = []
    all_instructions=[]

    r1 = Router("Router 1")
    r2 = Router("Router 2")
    r3 = Router("Router 3")
    r4 = Router("Router 4")
    r5 = Router("Router 5")
    r6 = Router("Router 6")
    r7 = Router("Router 7")
    r8 = Router("Router 8")
    r9 = Router("Router 9")
    router_list = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

    def add_instruction(self,instructions,routing):
        index=1
        for x in instructions:
            x = list(map(str,x.split()))
            input = Instruction(self,instructions,routing)
            self.all_instructions.append(input)
            
            if(input.source=="1"):
                self.traffic1.append(input)
                self.traffic1.sort(key = lambda x:x.clock_cycle)
            if(input.source=="2"):
                self.traffic2.append(input)
                self.traffic2.sort(key = lambda x:x.clock_cycle)
            if(input.source=="3"):
                self.traffic3.append(input)
                self.traffic3.sort(key = lambda x:x.clock_cycle)
            if(input.source=="4"):
                self.traffic4.append(input)
                self.traffic4.sort(key = lambda x:x.clock_cycle)    
            if(input.source=="5"):
                self.traffic5.append(input)
                self.traffic5.sort(key = lambda x:x.clock_cycle)
            if(input.source=="6"):
                self.traffic6.append(input)
                self.traffic6.sort(key = lambda x:x.clock_cycle)
            if(input.source=="7"):
                self.traffic7.append(input)
                self.traffic7.sort(key = lambda x:x.clock_cycle)
            if(input.source=="8"):
                self.traffic8.append(input)
                self.traffic8.sort(key = lambda x:x.clock_cycle)
            if(input.source=="9"):
                self.traffic9.append(input)
                self.traffic9.sort(key = lambda x:x.clock_cycle)
            index+=1

    def check(self, clock_cycle):
        list = []
        if len(self.traffic1)>0 and int(self.traffic1[0].clock_cycle) == clock_cycle:
            list.append(self.traffic1[0])
            self.traffic1.pop(0)
        if len(self.traffic2)>0 and int(self.traffic2[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic2[0])
            self.traffic2.pop(0)
        if len(self.traffic3)>0 and int(self.traffic3[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic3[0])
            self.traffic3.pop(0)
        if len(self.traffic4)>0 and int(self.traffic4[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic4[0])
            self.traffic4.pop(0)
        if len(self.traffic5)>0 and int(self.traffic5[0].clock_cycle) == clock_cycle:
            list.append(self.traffic5[0])
            self.traffic5.pop(0)
        if len(self.traffic6)>0 and int(self.traffic6[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic6[0])
            self.traffic6.pop(0)
        if len(self.traffic7)>0 and int(self.traffic7[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic7[0])
            self.traffic7.pop(0)
        if len(self.traffic8)>0 and int(self.traffic8[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic8[0])
            self.traffic8.pop(0)
        if len(self.traffic9)>0 and int(self.traffic9[0].clock_cycle)  == clock_cycle:
            list.append(self.traffic9[0])
            self.traffic9.pop(0)
        return list
    