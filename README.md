    CA-Project Cycle Accurate Simulator for a NoC Router and Mesh 

Group members
Akshay Modi | 2021166
Shivanshu Aggarwal | 2021203
Mohit | 2021167
Viyaash | 2021216
Ashhar | 2021137

    Structure of the Simulator

We have made a simple NOC router and followed a 3x3 mesh architecture.
The mesh has 9 blocks, and connections like:

    A -- B -- C
    |    |    |
    F -- E -- D
    |    |    |
    G -- H -- I 

We have provided 2 types of Routing Algorithms

1. XY Routing prioritizes horizontal movement over vertical movement.
2. YX Routing prioritizes vertical movement over horizontal movement.

Packet is the basic unit of transfer in NOC which is broken down into 3 parts:

1. Head Flit: contains the control information, the source and the destination.
2. Body Flit: contains main data that is to be transferred.
3. Tail Flit: indicates the end of the packet.

Working of Simulator
   
Our simulator takes an input traffic file that describes which packets are inserted in the NOC at various clock cycles. The structure of the input file is:

Cycle Number (1 bit)
Source Processor (1 bit)
Destination Processor (1 bit)
Payload: Data (32 bits)

With this input file, we also take the user input to choose the type of routing algorithm XY or YX.

The simulator outputs a log file which indicates:

The Cycle Number
Type of Flit
Source of the Flit
Destination of the Flit
Present Router
Next Router
Router element

The simulator outputs a log file which indicates:

The Cycle Number
Type of Flit
Source of the Flit
Destination of the Flit
Present Router
Next Router
Router element
Delay

    The Usage of Graph Plotter
Through the log file we plot two graphs:

1. A bar graph which plots the number of flits sent over a connection.
2. A bar graph showing the packet transfer latency for each packet.

The first graph keeps a check of the number of flits that pass through a given connection and plots them.

The second graph depicts the number of clock cycles a given packet takes to go from the source to destination.

    The Building and Usage Instructions
We run the file by the following command in terminal:

    python <insert name of main file>.py
After this it would take input from the input.txt file that we had provided and two user inputs:

    What routing algo to implement? Type 1 for XY and 2 for YX "
After taking the inputs, the file runs and generates the log file and report file. Through the log file, we make the two graphs.
