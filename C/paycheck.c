#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//struct employee that contains employee details
struct employee
{
        char name[25];
        double wage;
        int hours;
};

//global variable to count the number of entries made
int num_employees = 0;

//function to add employee in array
void addEmployee(struct employee **Employee_arr, char e_name[],double e_wage,int e_hours)
{
        strcpy((*Employee_arr)[num_employees].name,e_name);
        
        (*Employee_arr)[num_employees].wage = e_wage;
        (*Employee_arr)[num_employees].hours = e_hours;
        
        num_employees++;
}

//function to calculate total pay of each employee and print details
//also printing the average pay
void calcPaychecks(struct employee* Employee_arr)
{
    
        double avg = 0;
        for(int i = 0;i<num_employees;i++)
        {
                double total = Employee_arr[i].wage * Employee_arr[i].hours;
                avg += total;
                printf("%s, wage %.2f, hours %d, total pay: \n",Employee_arr[i].name,Employee_arr[i].wage,Employee_arr[i].hours);
        }
        printf("Average paycheck: $%.2f\n",avg/num_employees);
}

//main() to add employees and print their details
int main()
{
        //creating array of employee instances
        struct employee* Employee_arr = (struct employee*)malloc(5*sizeof(struct employee));
        
        //adding 4 employees 
        addEmployee(&Employee_arr,"Bob Smith",21,21);
        addEmployee(&Employee_arr,"Sue Jones",22.30,12);
        addEmployee(&Employee_arr,"Carlos Suarez",21.55,15);
        addEmployee(&Employee_arr,"Jill Smith",21.34,31);
        
        //printing details
        calcPaychecks(Employee_arr);
        
        
        return 0;
}
