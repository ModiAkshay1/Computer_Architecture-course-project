from input import list_of_instructions
from delay import delay_max
outfile = open('log.txt' , 'w')
report_file = open('report.txt','w')
delay_now =0
pelinks=[0 for i in range(9)]
links=[0 for i in range(12)]
class Instruction:
    route = []
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
    /home/akshay/Downloads/GroupNo09_ProjectNo01/Computer_Architecture-course-project-main/main copy.py

    head1 = ""
    data1=""
    tail1 = ""
    body1 = ""

    def __init__(self,x,routing,router_list):
        self.clock_cycle = int(x[0])
        self.source = x[1]
        self.destination = x[2]
        self.make_path(routing,router_list)
        # print(len(self.route))

        self.data1 = x[3]  #To find_instructions if given flit is head,tail or body
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
        path.append(Router(router_list[int(self.source)-1]))
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
            if self.destination in col1:
                if (self.destination=="6"):
                    links[7]+=1
                    path.append(Router(router_list[5]))
                elif (self.destination=="7"):
                    links[7]+=1
                    links[6]+=1
                    path.append(Router(router_list[5]))
                    path.append(Router(router_list[6]))
            elif self.destination in col2:
                links[0]+=1
                path.append(Router(router_list[1]))
                if (self.destination=="5"):
                    links[8]+=1
                    path.append(Router(router_list[4]))
                elif (self.destination=="8"):
                    links[8]+=1
                    links[10]+=1
                    path.append(Router(router_list[4]))
                    path.append(Router(router_list[7]))
            elif self.destination in col3:
                links[0]+=1
                links[1]+=1
                path.append(Router(router_list[1]))
                path.append(Router(router_list[2]))
                if (self.destination=="4"):
                    links[2]+=1
                    path.append(Router(router_list[3]))
                elif (self.destination=="9"):
                    links[2]+=1
                    links[3]+=1
                    path.append(Router(router_list[3]))
                    path.append(Router(router_list[8]))

        elif self.source=="2":
            if self.destination in col1:
                path.append(Router(router_list[0]))
                if (self.destination=="6"):
                    path.append(Router(router_list[5]))
                elif (self.destination=="7"):
                    path.append(Router(router_list[5]))
                    path.append(Router(router_list[6]))
            elif self.destination in col2:
                if (self.destination=="5"):
                    path.append(Router(router_list[4]))
                elif (self.destination=="8"):
                    path.append(Router(router_list[4]))
                    path.append(Router(router_list[7]))
            elif self.destination in col3:
                path.append(Router(router_list[2]))
                if (self.destination=="4"):
                    path.append(Router(router_list[3]))
                elif (self.destination=="9"):
                    path.append(Router(router_list[3]))
                    path.append(Router(router_list[8]))

        elif self.source=="3":
            if self.destination in col1:
                path.append(Router(router_list[1]))
                path.append(Router(router_list[0]))
                if (self.destination=="6"):
                    path.append(Router(router_list[5]))
                elif (self.destination=="7"):
                    path.append(Router(router_list[5]))
                    path.append(Router(router_list[6]))
            elif self.destination in col2:
                path.append(Router(router_list[1]))
                if (self.destination=="5"):
                    path.append(Router(router_list[4]))
                elif (self.destination=="8"):
                    path.append(Router(router_list[4]))
                    path.append(Router(router_list[7]))
            elif self.destination in col3:
                if (self.destination=="4"):
                    path.append(Router(router_list[3]))
                elif (self.destination=="9"):
                    path.append(Router(router_list[3]))
                    path.append(Router(router_list[8]))

        elif self.source=="4":
            if self.destination in col1:
                path.append(Router(router_list[4]))
                path.append(Router(router_list[5]))
                if (self.destination=="1"):
                    path.append(Router(router_list[0]))
                elif (self.destination=="7"):
                    path.append(Router(router_list[6]))
            elif self.destination in col2:
                path.append(Router(router_list[4]))
                if (self.destination=="2"):
                    path.append(Router(router_list[1]))
                elif (self.destination=="8"):
                    path.append(Router(router_list[7]))
            elif self.destination in col3:
                if (self.destination=="3"):
                    path.append(Router(router_list[2]))
                elif (self.destination=="9"):
                    path.append(Router(router_list[8]))

        elif self.source=="5":
            if self.destination in col1:
                path.append(Router(router_list[5]))
                if (self.destination=="1"):
                    path.append(Router(router_list[0]))
                elif (self.destination=="7"):
                    path.append(Router(router_list[6]))
            elif self.destination in col2:
                if (self.destination=="2"):
                    path.append(Router(router_list[1]))
                elif (self.destination=="8"):
                    path.append(Router(router_list[7]))
            elif self.destination in col3:
                path.append(Router(router_list[3]))
                if (self.destination=="3"):
                    path.append(Router(router_list[2]))
                elif (self.destination=="9"):
                    path.append(Router(router_list[8]))

        elif self.source=="6":
            if self.destination in col1:
                if (self.destination=="1"):
                    path.append(Router(router_list[0]))
                elif (self.destination=="7"):
                    path.append(Router(router_list[6]))
            elif self.destination in col2:
                path.append(Router(router_list[4]))
                if (self.destination=="2"):
                    path.append(Router(router_list[1]))
                elif (self.destination=="8"):
                    path.append(Router(router_list[7]))
            elif self.destination in col3:
                path.append(Router(router_list[4]))
                path.append(Router(router_list[3]))
                if (self.destination=="3"):
                    path.append(Router(router_list[2]))
                elif (self.destination=="9"):
                    path.append(Router(router_list[8]))

        elif self.source=="7":
            if self.destination in col1:
                if (self.destination=="1"):
                    path.append(Router(router_list[5]))
                    path.append(Router(router_list[0]))
                elif (self.destination=="6"):
                    path.append(Router(router_list[5]))
            elif self.destination in col2:
                path.append(Router(router_list[7]))
                if (self.destination=="2"):
                    path.append(Router(router_list[4]))
                    path.append(Router(router_list[1]))
                elif (self.destination=="5"):
                    path.append(Router(router_list[4]))
            elif self.destination in col3:
                path.append(Router(router_list[7]))
                path.append(Router(router_list[8]))
                if (self.destination=="3"):
                    path.append(Router(router_list[3]))
                    path.append(Router(router_list[2]))
                elif (self.destination=="4"):
                    path.append(Router(router_list[3]))

        elif self.source=="8":
            if self.destination in col1:
                path.append(Router(router_list[6]))
                if (self.destination=="1"):
                    path.append(Router(router_list[5]))
                    path.append(Router(router_list[0]))
                elif (self.destination=="6"):
                    path.append(Router(router_list[5]))
            elif self.destination in col2:
                if (self.destination=="2"):
                    path.append(Router(router_list[4]))
                    path.append(Router(router_list[1]))
                elif (self.destination=="5"):
                    path.append(Router(router_list[4]))
            elif self.destination in col3:
                path.append(Router(router_list[8]))
                if (self.destination=="3"):
                    path.append(Router(router_list[3]))
                    path.append(Router(router_list[2]))
                elif (self.destination=="4"):
                    path.append(Router(router_list[3]))

           
        elif self.source=="9":
            if self.destination in col1:
                path.append(Router(router_list[7]))
                path.append(Router(router_list[6]))
                if (self.destination=="1"):
                    path.append(Router(router_list[5]))
                    path.append(Router(router_list[0]))
                elif (self.destination=="6"):
                    path.append(Router(router_list[5]))
            elif self.destination in col2:
                path.append(Router(router_list[7]))
                if (self.destination=="2"):
                    path.append(Router(router_list[4]))
                    path.append(Router(router_list[1]))
                elif (self.destination=="5"):
                    path.append(Router(router_list[4]))
            elif self.destination in col3:
                if (self.destination=="3"):
                    path.append(Router(router_list[3]))
                    path.append(Router(router_list[2]))
                elif (self.destination=="4"):
                    path.append(Router(router_list[3]))

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
    def update(self,instruction, clock_cyle,partname, source, destination,delay_now):
        self.current_element+=1
        type_of_element=""
        if(self.current_element==0):
            type_of_element="Input buffer"
        elif(self.current_element==1):
            type_of_element="SA"
        elif(self.current_element==2):
            type_of_element="Crossbar"
        else:
            type_of_element=str(self.current_element)
        L = ["Clock cycle: ", str(clock_cyle) + " ||", " Flit: ",partname + " ||", " Source: ", instruction.source + " ||"," Destination: ",instruction.destination + " ||", " Present Router: ",self.name +" ||"," Next Router: ", destination.name+" ||"," Type: " +type_of_element," \n"]
        outfile.writelines(L)
        R = ["Clock cycle: ", str(clock_cyle) + " ||", " Flit: ",partname +" ||"," Source: ", instruction.source + " ||"," Destination: ",instruction.destination + " ||"," Present router: ",self.name+" ||"," Type: "+type_of_element +" ||"," Delay: ",str(delay_now), "\n"]
        report_file.writelines(R)
        # print("Clock cycle:", clock_cyle, "Flit: ",  partname+" ", "Source:", instruction.source, "Destination:", instruction.destination,"Present router: ",self.name+" ","Type: "+type_of_element)
        return 



class NoC:
    traffic = [[] for i in range(9)]
    all_instructions=[]
    clk1 = 50 #To find total number of clock cycles

    router_list = ["Router 1","Router 2","Router 3","Router 4","Router 5","Router 6","Router 7","Router 8","Router 9"]

    def add_instruction(self,instructions,routing):
        index=1
        for x in instructions:
            x1 = x.split()
            x = list(map(str,x1))
            print(x)
            input = Instruction(x,routing,self.router_list)
            # print(input.source)
            # print(input.clock_cycle)
            self.all_instructions.append(input)
            if (input.clock_cycle >= self.clk1):
                self.clk1 = input.clock_cycle

            if(input.source=="1"):
                self.traffic[0].append(input)
                self.traffic[0].sort(key = lambda x:x.clock_cycle)
            if(input.source=="2"):
                self.traffic[1].append(input)
                self.traffic[1].sort(key = lambda x:x.clock_cycle)
            if(input.source=="3"):
                self.traffic[2].append(input)
                self.traffic[2].sort(key = lambda x:x.clock_cycle)
            if(input.source=="4"):
                self.traffic[3].append(input)
                self.traffic[3].sort(key = lambda x:x.clock_cycle)    
            if(input.source=="5"):
                self.traffic[4].append(input)
                self.traffic[4].sort(key = lambda x:x.clock_cycle)
            if(input.source=="6"):
                self.traffic[5].append(input)
                self.traffic[5].sort(key = lambda x:x.clock_cycle)
            if(input.source=="7"):
                self.traffic[6].append(input)
                self.traffic[6].sort(key = lambda x:x.clock_cycle)
            if(input.source=="8"):
                self.traffic[7].append(input)
                self.traffic[7].sort(key = lambda x:x.clock_cycle)
            if(input.source=="9"):
                self.traffic[8].append(input)
                self.traffic[8].sort(key = lambda x:x.clock_cycle)
            index+=1

    def find_instructions(self, clock_cycle):
        list = []
        if len(self.traffic[0])>0 and int(self.traffic[0][0].clock_cycle) == clock_cycle:
            list.append(self.traffic[0][0])
            self.traffic[0].pop(0)
        if len(self.traffic[1])>0 and int(self.traffic[1][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[1][0])
            self.traffic[1].pop(0)
        if len(self.traffic[2])>0 and int(self.traffic[2][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[2][0])
            self.traffic[2].pop(0)
        if len(self.traffic[3])>0 and int(self.traffic[3][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[3][0])
            self.traffic[3].pop(0)
        if len(self.traffic[4])>0 and int(self.traffic[4][0].clock_cycle) == clock_cycle:
            list.append(self.traffic[4][0])
            self.traffic[4].pop(0)
        if len(self.traffic[5])>0 and int(self.traffic[5][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[5][0])
            self.traffic[5].pop(0)
        if len(self.traffic[6])>0 and int(self.traffic[6][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[6][0])
            self.traffic[6].pop(0)
        if len(self.traffic[7])>0 and int(self.traffic[7][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[7][0])
            self.traffic[7].pop(0)
        if len(self.traffic[8])>0 and int(self.traffic[8][0].clock_cycle)  == clock_cycle:
            list.append(self.traffic[8][0])
            self.traffic[8].pop(0)
        return list
    
    def stage(self):
        clk_total = self.clk1
        queue = []
        dup_queue = []
        routing = 1
        self.add_instruction(list_of_instructions, routing)

        for clock_cycle in range(clk_total):
            global delay_now            
            delay_now += delay_max
            queue = dup_queue.copy()
            x = self.find_instructions(clock_cycle)
            if len(x) > 0:
                for i in x:
                    queue.append(i)
            # print("clock cycle = ", clock_cycle, len(queue))
            
            for instruction in queue:
                # for i in queue:
                #     for j in range(len(i.route)):
                #         print(j,i.route[j].name,i.route[j].current_element)
                #     print("")
                dup_queue = queue.copy()
                if len(instruction.route) > 1 :
                    if(instruction.start_time==-1):
                        instruction.start_time=delay_now
                    instruction.route[0].update(instruction, clock_cycle,instruction.name, instruction.route[0], instruction.route[1],delay_now-instruction.start_time+delay_max)
                    if instruction.route[0].current_element==2 :
                        instruction.route.pop(0)
                    
n = NoC()
p = n.stage()