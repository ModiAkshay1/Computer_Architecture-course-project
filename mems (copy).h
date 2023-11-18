/*
All the main functions with respect to the MeMS are inplemented here
read the function discription for more details

NOTE: DO NOT CHANGE THE NAME OR SIGNATURE OF FUNCTIONS ALREADY PROVIDED
you are only allowed to implement the functions 
you can also make additional helper functions a you wish

REFER DOCUMENTATION FOR MORE DETAILS ON FUNSTIONS AND THEIR FUNCTIONALITY
*/
// add other headers as required
#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include <inttypes.h>
#include <sys/mman.h>

/*
Use this macro where ever you need PAGE_SIZE.
As PAGESIZE can differ system to system we should have flexibility to modify this 
macro to make the output of all system same and conduct a fair evaluation. 
*/
#define PAGE_SIZE 4096

#define PROT_READ   0x1
#define PROT_WRITE  0x2
#define MAP_ANONYMOUS 0x20
#define MAP_PRIVATE   0x02
#define MAP_FAILED ((void *)-1)
uintptr_t base;
uintptr_t current=0;
struct SubChainNode {
    size_t size;
    int is_process;
    struct SubChainNode* next;
    struct SubChainNode* prev;
    struct MainChainNode* main_node;
    bool free;
    uintptr_t org_addr;
    uintptr_t vir_addr;
};

struct MainChainNode {
    size_t size;
    struct SubChainNode* sub_chain_head;
    struct MainChainNode* next;
    struct MainChainNode* prev;
    uintptr_t addr;
};


/*
Initializes all the required parameters for the MeMS system. The main parameters to be initialized are:
1. the head of the free list i.e. the pointer that points to the head of the free list
2. the starting MeMS virtual address from which the heap in our MeMS virtual address space will start.
3. any other global variable that you want for the MeMS implementation can be initialized here.
Input Parameter: Nothing
Returns: Nothing
*/

struct MainChainNode* free_list_head = NULL;  // Head of the main chain


void mems_init(){

	free_list_head = NULL;
	
}


/*
This function will be called at the end of the MeMS system and its main job is to unmap the 
allocated memory using the munmap system call.
Input Parameter: Nothing
Returns: Nothing
*/
void mems_finish(){
    struct MainChainNode* main_chain_node = main_chain_head;

    while (main_chain_node != NULL) {
        // Iterate through the sub-chain within the current main chain node
        struct SubChainNode* sub_chain_node = main_chain_node->sub_chain_head;
        struct SubChainNode* next_node;

        while (sub_chain_node != NULL) {
            next_node = sub_chain_node->next;

            // Deallocate the memory associated with PROCESS segments
            if (sub_chain_node->is_process) {
                munmap(sub_chain_node, sub_chain_node->size);
            }

            // Free the current sub-chain node
            free(sub_chain_node);

            sub_chain_node = next_node;
        }

        // Move to the next main chain node
        struct MainChainNode* next_main_chain_node = main_chain_node->next;
        free(main_chain_node);

        main_chain_node = next_main_chain_node;
    }

    // Reset global variables
    main_chain_head = NULL;
    mems_virtual_start = NULL;
}


/*
Allocates memory of the specified size by reusing a segment from the free list if 
a sufficiently large segment is available. 

Else, uses the mmap system call to allocate more memory on the heap and updates 
the free list accordingly.

Note that while mapping using mmap do not forget to reuse the unused space from mapping
by adding it to the free list.
Parameter: The size of the memory the user program wants
Returns: MeMS Virtual address (that is created by MeMS)
*/ 
void* mems_malloc(size_t size){
	// size_t num_pages = (size + PAGE_SIZE - 1) / PAGE_SIZE;
    if(free_list_head==NULL){
        size_t num_pages;
        if(size%PAGE_SIZE==0){
            num_pages=size/PAGE_SIZE;
        }else{
            num_pages=size/PAGE_SIZE;
            num_pages++;
        }
        struct MainChainNode* new_main_chain_node = (struct MainChainNode*)malloc(sizeof(struct MainChainNode));
        new_main_chain_node->size=PAGE_SIZE*num_pages;
        new_main_chain_node->next=NULL;
        new_main_chain_node->prev=NULL;
        free_list_head=new_main_chain_node;
        free_list_head->sub_chain_head=(struct SubChainNode*)malloc(sizeof(struct SubChainNode));
        free_list_head->sub_chain_head->main_node=free_list_head;
        free_list_head->sub_chain_head->next=NULL;
        free_list_head->sub_chain_head->prev=NULL;
        free_list_head->sub_chain_head->size=size;
        free_list_head->sub_chain_head->free=false;
        void* addr = mmap(NULL,PAGE_SIZE*num_pages, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
        base=(uintptr_t)addr;
        free_list_head->addr=base;
        free_list_head->sub_chain_head->org_addr=base;
        free_list_head->sub_chain_head->vir_addr=current;
        current+=size;
        if(PAGE_SIZE*num_pages>size){
            struct SubChainNode* temp = (struct SubChainNode*)malloc(sizeof(struct SubChainNode));
            temp->free=true;
            temp->size=PAGE_SIZE*num_pages-size;
            temp->next=NULL;
            temp->prev=free_list_head->sub_chain_head;
            temp->main_node=free_list_head;
            temp->org_addr=base+size;
            free_list_head->sub_chain_head->next=temp;
        }
        return &(free_list_head->sub_chain_head->vir_addr);
    }

    

    // Find a suitable segment in the free list
    struct MainChainNode* main_chain_node =free_list_head;
    struct SubChainNode* sub_chain_node = NULL;
    struct MainChainNode* last=NULL;
    bool found=false;
    while (main_chain_node != NULL) {
        // Search for a suitable segment in the sub-chain
        sub_chain_node = main_chain_node->sub_chain_head;

        while (sub_chain_node != NULL) {
            if (!sub_chain_node->free==true && sub_chain_node->size >= size) {
                // Allocate from this segment
                if(sub_chain_node->size>size){
                    // Split the segment into two: one for PROCESS and one for HOLE
                    struct SubChainNode* new_hole = (struct SubChainNode*)malloc(sizeof(struct SubChainNode));
                    new_hole->size = sub_chain_node->size-size;
                    new_hole->next = sub_chain_node->next;
                    new_hole->prev = sub_chain_node;
                    new_hole->free=true;
                    new_hole->main_node=main_chain_node;
                    new_hole->org_addr=sub_chain_node->org_addr+size;
                    if (sub_chain_node->next != NULL) {
                        sub_chain_node->next->prev = new_hole;
                    }
                    sub_chain_node->size=size;
                    sub_chain_node->free=false;
                    sub_chain_node->next = new_hole;
                    if(sub_chain_node->vir_addr!=NULL){
                        return &sub_chain_node->vir_addr;
                    }
                    sub_chain_node->vir_addr=current;
                    current+=size;
                    return &sub_chain_node->vir_addr;
                    //add addresses carefully      ************
                }else{
                    sub_chain_node->free=false;
                    if(sub_chain_node->vir_addr!=NULL){
                        return &sub_chain_node->vir_addr;
                    }
                    sub_chain_node->vir_addr=current;
                    current+=size;
                    return &sub_chain_node->vir_addr;
                    //add addresses carefully      ************
                }

                found=true;
                break;
            }
            sub_chain_node = sub_chain_node->next;
        }

        if (found) {
            break;
        }
        last=main_chain_node;
        main_chain_node = main_chain_node->next;
    }

    if (!found) {
        // If a suitable segment wasn't found, request a new block from the OS using mmap
        size_t num_pages;
        if(size%PAGE_SIZE==0){
            num_pages=size/PAGE_SIZE;
        }else{
            num_pages=size/PAGE_SIZE;
            num_pages++;
        }
        void* new_block = mmap(NULL, num_pages * PAGE_SIZE, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
        uintptr_t addrr=(uintptr_t)new_block;
        struct MainChainNode* new_main_chain_node = (struct MainChainNode*)malloc(sizeof(struct MainChainNode));
        new_main_chain_node->size=num_pages * PAGE_SIZE;
        new_main_chain_node->next=NULL;
        new_main_chain_node->prev=last;
        new_main_chain_node->sub_chain_head = (struct SubChainNode*)malloc(sizeof(struct SubChainNode));
        new_main_chain_node->sub_chain_head->main_node=new_main_chain_node;
        new_main_chain_node->sub_chain_head->size=size;
        new_main_chain_node->sub_chain_head->free=false;
        new_main_chain_node->sub_chain_head->next = NULL;
        new_main_chain_node->sub_chain_head->prev = NULL;
        new_main_chain_node->sub_chain_head->org_addr=addrr;
        new_main_chain_node->sub_chain_head->vir_addr=current;
        current+=size;
        if(PAGE_SIZE*num_pages>size){
            struct SubChainNode* temp = (struct SubChainNode*)malloc(sizeof(struct SubChainNode));
            temp->free=true;
            temp->size=PAGE_SIZE*num_pages-size;
            temp->next=NULL;
            temp->prev=new_main_chain_node->sub_chain_head;
            temp->main_node=new_main_chain_node;
            temp->org_addr=addrr+size;
            new_main_chain_node->sub_chain_head->next=temp;
        }

        last->next=new_main_chain_node;
        

        
    }

    return &(last->next->sub_chain_head->vir_addr);
}


/*
this function print the stats of the MeMS system like
1. How many pages are utilised by using the mems_malloc
2. how much memory is unused i.e. the memory that is in freelist and is not used.
3. It also prints details about each node in the main chain and each segment (PROCESS or HOLE) in the sub-chain.
Parameter: Nothing
Returns: Nothing but should print the necessary information on STDOUT
*/
void mems_print_stats(){
	size_t used_pages = 0;
    size_t unused_memory = 0;

    printf("MeMS Statistics:\n");

    // Traverse the main chain and sub-chains
    struct MainChainNode* main_chain_node = main_chain_head;
    int main_chain_index = 1;

    while (main_chain_node != NULL) {
        printf("Main Chain Node %d:\n", main_chain_index);

        // Iterate through the sub-chain within the current main chain node
        struct SubChainNode* sub_chain_node = main_chain_node->sub_chain_head;
        int sub_chain_index = 1;

        while (sub_chain_node != NULL) {
            printf("  Sub-Chain Node %d:\n", sub_chain_index);
            printf("    Size: %zu bytes\n", sub_chain_node->size);
            printf("    Type: %s\n", sub_chain_node->is_process ? "PROCESS" : "HOLE");

            if (sub_chain_node->is_process) {
                used_pages += sub_chain_node->size / PAGE_SIZE;
            } else {
                unused_memory += sub_chain_node->size;
            }

            sub_chain_node = sub_chain_node->next;
            sub_chain_index++;
        }

        main_chain_node = main_chain_node->next;
        main_chain_index++;
    }

    printf("Total Used Pages: %zu pages\n", used_pages);
    printf("Total Unused Memory: %zu bytes\n", unused_memory);
}


/*
Returns the MeMS physical address mapped to ptr ( ptr is MeMS virtual address).
Parameter: MeMS Virtual address (that is created by MeMS)
Returns: MeMS physical address mapped to the passed ptr (MeMS virtual address).
*/
void *mems_get(void*v_ptr){
	return v_ptr;  
}


/*
this function free up the memory pointed by our virtual_address and add it to the free list
Parameter: MeMS Virtual address (that is created by MeMS) 
Returns: nothing
*/
void mems_free(void *v_ptr){
	struct MainChainNode* main_chain_node = main_chain_head;

    while (main_chain_node != NULL) {
        struct SubChainNode* sub_chain_node = main_chain_node->sub_chain_head;

        while (sub_chain_node != NULL) {
            if (v_ptr >= mems_virtual_start && v_ptr < mems_virtual_start + sub_chain_node->size) {
                // Mark the segment as a HOLE
                sub_chain_node->is_process = 0;

                // Coalesce adjacent HOLE nodes if necessary
                if (sub_chain_node->prev != NULL && sub_chain_node->prev->is_process == 0) {
                    // Merge with the previous HOLE node
                    sub_chain_node->prev->size += sub_chain_node->size;
                    sub_chain_node->prev->next = sub_chain_node->next;

                    if (sub_chain_node->next != NULL) {
                        sub_chain_node->next->prev = sub_chain_node->prev;
                    }

                    free(sub_chain_node);
                    sub_chain_node = sub_chain_node->prev;
                }

                if (sub_chain_node->next != NULL && sub_chain_node->next->is_process == 0) {
                    // Merge with the next HOLE node
                    sub_chain_node->size += sub_chain_node->next->size;
                    sub_chain_node->next = sub_chain_node->next->next;

                    if (sub_chain_node->next != NULL) {
                        sub_chain_node->next->prev = sub_chain_node;
                    }

                    free(sub_chain_node->next);
                }

                return;
            }

            sub_chain_node = sub_chain_node->next;
        }

        main_chain_node = main_chain_node->next;
    } 	   
}
