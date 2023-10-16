from input import list_of_instructions
# import matplotlib.pyplot as plt
outfile = open('log.txt' , 'w')

class Instruction:
    head_path = []
    data_path=[]
    tail_path = []
    route = []
    #head = ""
    #data=""
    #tail = ""
    head = False
    body = False
    tail = False
    index = 0
    clock_cycle = 0
    end_time = 0
    start_time = -1
    source = ""
    destination = ""
    name=""

    head1 = ""
    data1=""
    tail1 = ""
    body1 = ""

    def __init__(self,x,routing,router_list):
        # self.index=index  ,index
        self.clock_cycle = int(x[0])
        self.source = x[1]
        self.destination = x[2]
        # self.head = self.destination + self.source + "00"
        # self.data = instruction[3] + "01"
        # self.tail = "00000000000000000000000000000010" #check krlena ek baar
        self.make_path(routing,router_list)

        self.data1 = x[3]  #To check if given flit is head,tail or body
        if (self.data1[-2:] == "01"):
            self.body1 = self.data1
            self.body = True
            self.name=" Body "
        elif (self.data1[-2:] == "00"):
            self.head1 = self.data1
            self.head = True
            self.name=" Head "
        elif (self.data1[-2:] == "10"):
            self.tail1 = self.data1
            self.tail = True
            self.name=" Tail "
    
    def make_path(self,direction,router_list):
        if direction == 1:
            self.route = self.get_path_XY(router_list)


    def get_path_XY(self,router_list):
        path=[]
        path.append(router_list[int(self.source)-1])
        row1=["1","2","3"]
        row2=["4","5","6"]
        row3=["7","8","9"]
        col1=["1","6","7"]
        col2=["2","5","8"]
        col3=["3","4","9"]
        #Write code for XY routing
        #Separate codes for head, body and tail
        if self.source==self.destination:
            return
        if self.source=="1":
            diff=(int(self.destination)-int(self.source))
            i=1
            while (i<diff+1):
                path.append(router_list[i])
                i+=1

        elif self.source=="2":
            if self.destination in row1:
                path.append(router_list[int(self.destination)-1])
            elif self.destination in row2:
                if self.destination == "4":
                    path.append(router_list[2])
                    path.append(router_list[3])
                elif self.destination == "5":
                    path.append(router_list[2])
                    path.append(router_list[3])
                    path.append(router_list[4])
                else:
                    path.append(router_list[0])
                    path.append(router_list[5])
            else:
                if self.destination == "7":
                    path.append(router_list[2])
                    path.append(router_list[3])
                    path.append(router_list[4])
                    path.append(router_list[5])
                    path.append(router_list[6])
                elif self.destination == "8":
                    path.append(router_list[2])
                    path.append(router_list[3])
                    path.append(router_list[4])
                    path.append(router_list[5])
                    path.append(router_list[6])
                    path.append(router_list[7])
                else:
                    path.append(router_list[0])
                    path.append(router_list[5])
                    path.append(router_list[4])
                    path.append(router_list[3])
                    path.append(router_list[8])

        elif self.source=="3":
            if self.destination in row1:
                path.append(router_list[1])
                if self.destination == "1":
                    path.append(router_list[0])
            else:
                path.append(router_list[1])
                path.append(router_list[0])
                if self.destination in row2:
                    path.append(router_list[5])
                    if self.destination == "5":
                        path.append(router_list[4])
                    elif self.destination == "4":
                        path.append(router_list[4])
                        path.append(router_list[3])
                else:
                    path.append(router_list[5])
                    path.append(router_list[4])
                    path.append(router_list[3])
                    path.append(router_list[8])
                    if self.destination == "8":
                        path.append(router_list[7])
                    elif self.destination == "7":
                        path.append(router_list[7])
                        path.append(router_list[6])

        elif self.source=="4":
            if self.destination in row2:
                path.append(router_list[4])
                if self.destination=="6":
                    path.append(router_list[5])
            elif self.destination in row1:
                path.append(router_list[4])
                path.append(router_list[5])
                for i in range(0,int(self.destination)):
                    path.append(router_list[i])
            elif self.destination in row3:
                path.append(router_list[4])
                path.append(router_list[5])
                for i in range(6,int(self.destination)):
                    path.append(router_list[i])

        elif self.source=="5":
            if self.destination in row2:
                path.append(router_list[int(self.destination)-1])
            elif self.destination in row1:
                if self.destination=="1":
                    path.append(router_list[5])
                    path.append(router_list[0])
                elif self.destination=="2":
                    path.append(router_list[5])
                    path.append(router_list[0])
                    path.append(router_list[1])
                else:
                    path.append(router_list[3])
                    path.append(router_list[2])
            else:
                if self.destination=="7":
                    path.append(router_list[5])
                    path.append(router_list[6])
                elif self.destination=="8":
                    path.append(router_list[5])
                    path.append(router_list[6])
                    path.append(router_list[7])
                else:
                    path.append(router_list[3])
                    path.append(router_list[8])

        elif self.source=="6":
            if self.destination in row2:
                path.append(router_list[4])
                if self.destination=="4":
                    path.append(router_list[3])
            elif self.destination in row1:
                path.append(router_list[4])
                path.append(router_list[3])
                for i in range(2,int(self.destination)-2,-1):
                    path.append(router_list[i])
            elif self.destination in row3:
                path.append(router_list[4])
                path.append(router_list[3])
                for i in range(8,int(self.destination)-2,-1):
                    path.append(router_list[i])

        elif self.source=="7":
            if self.destination in row3:
                path.append(router_list[7])
                if self.destination == "9":
                    path.append(router_list[8])
            else:
                path.append(router_list[7])
                path.append(router_list[8])
                if self.destination in row2:
                    path.append(router_list[3])
                    if self.destination == "5":
                        path.append(router_list[4])
                    elif self.destination == "6":
                        path.append(router_list[4])
                        path.append(router_list[5])
                else:
                    path.append(router_list[3])
                    path.append(router_list[4])
                    path.append(router_list[5])
                    path.append(router_list[0])
                    if self.destination == "2":
                        path.append(router_list[1])
                    elif self.destination == "3":
                        path.append(router_list[1])
                        path.append(router_list[2])

        elif self.source=="8":
            if self.destination in row3:
                path.append(router_list[int(self.destination)-1])
            elif self.destination in row2:
                if self.destination == "4":
                    path.append(router_list[8])
                    path.append(router_list[3])
                elif self.destination == "5":
                    path.append(router_list[8])
                    path.append(router_list[3])
                    path.append(router_list[4])
                else:
                    path.append(router_list[6])
                    path.append(router_list[5])
            else:
                if self.destination == "1":
                    path.append(router_list[8])
                    path.append(router_list[3])
                    path.append(router_list[4])
                    path.append(router_list[5])
                    path.append(router_list[0])
                elif self.destination == "2":
                    path.append(router_list[8])
                    path.append(router_list[3])
                    path.append(router_list[4])
                    path.append(router_list[5])
                    path.append(router_list[0])
                    path.append(router_list[1])
                else:
                    path.append(router_list[6])
                    path.append(router_list[5])
                    path.append(router_list[4])
                    path.append(router_list[3])
                    path.append(router_list[2])

        elif self.source=="9":
            i=7
            j=0
            diff=abs(int(self.destination)-int(self.source))
            while (j<diff):
                path.append(router_list[i])
                i-=1
                j+=1

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
    crossbar = []
    sw_allocator = []
    ip_buffer = []
    current_element=-1  #0 for input_buffer, 1 for SW, 2 for crossbar
    ip_port = ["North", "South", "East", "West", "Local"]
    op_port = ["North", "South", "East", "West", "Local"]

    def __init__(self, name):
        self.name = name
    # def add_source(self, source):
    #     self.source = source
    #     self.counter += 1
    # def add_destination(self, destination):
    #     self.destination = destination 
    #     self.counter += 1
    # def add_header(self):
    #     self.counter += 1
    # def add_flit(self):
    #     self.counter += 1
    # def add_tail(self):
    #     self.counter = 0
    def update(self,instruction, clock_cyle, statement, source, destination):
        
        self.current_element+=1
        type_of_element=""
        if(self.current_element==0):
            type_of_element="Input buffer"
        elif(self.current_element==1):
            type_of_element="SA"
        elif(self.current_element==2):
            type_of_element="Crossbar"
        L = ["Clock cycle: ", str(clock_cyle) + " ", "Flit: ", str(statement) + " ", "Source: ", source.name + " ", "Destination: ", destination.name+" ","Present router: ",self.name+" ","Type: "+type_of_element,"\n"]
        outfile.writelines(L)
        print("Clock cycle:", clock_cyle, "Flit:", statement, "Source:", instruction.source, "Destination:", instruction.destination,"Present router: ",self.name+" ","Type: "+type_of_element)
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
    clk1 = 50 #To find total number of clock cycles

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
            print(x)
            input = Instruction(x,routing,self.router_list)
            print(input.source)
            print(input.clock_cycle)
            self.all_instructions.append(input)
            if (input.clock_cycle >= self.clk1):
                self.clk1 = input.clock_cycle

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
    
    def play(self):
        #everything = []
        #total_tic = int(input("Enter the total number of clock cycles: "))
        total_tic = self.clk1
        queue = []
        queue_temp = []
        #routing = int(input("Enter 1 for XY routing and 2 for YX routing: "))
        routing = 1
        self.add_instruction(list_of_instructions, routing)

        for clock_cycle in range(total_tic):
            queue = queue_temp.copy()
            x = self.check(clock_cycle)
            if len(x) > 0:
                for i in x:
                    queue.append(i)
            print("clock cycle = ", clock_cycle, len(queue))
            
            for instruction in queue:
                queue_temp = queue.copy()
                if len(instruction.route) > 1 :
                    if instruction.head == True:                    
                        if instruction.start_time == -1:
                            instruction.start_time = clock_cycle
                        instruction.route[0].update(instruction, clock_cycle, instruction.name, instruction.route[0], instruction.route[1])
                        if instruction.route[0].current_element==2 :
                            instruction.route.pop(0)
                    elif instruction.body == True:                    
                        if instruction.start_time == -1:
                            instruction.start_time = clock_cycle
                        instruction.route[0].update(instruction, clock_cycle, "", instruction.route[0], instruction.route[1])
                        if instruction.route[0].current_element==2 :
                            instruction.route.pop(0)
                    elif instruction.tail == True:                    
                        if instruction.start_time == -1:
                            instruction.start_time = clock_cycle
                        instruction.route[0].update(instruction, clock_cycle, "Tail", instruction.route[0], instruction.route[1])
                        if instruction.route[0].current_element==2 :
                            instruction.route.pop(0)
                    
n = NoC()
everything = n.play()