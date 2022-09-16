#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//struct employee that contains monster details
struct monster
{
        char name[25];
        char location[25];
        int victims;
        int attack_ID;
};

//global variable to count the number of entries made
int num_monsters = 0;

//function to add monster in array
void addMonster(struct monster **Monster_arr, char e_name[],char e_location[],int e_victims)
{
        strcpy((*Monster_arr)[num_monsters].name,e_name);
        strcpy((*Monster_arr)[num_monsters].location,e_location);
        
        (*Monster_arr)[num_monsters].victims = e_victims;        
        num_monsters++;
        (*Monster_arr)[num_monsters].attack_ID = num_monsters;
}

void printMonsterInfo(struct monster* Monster_arr)
{
    struct monster *current_monster;
	for(int i = 0;i<num_monsters;i++)
	{
		current_monster = Monster_arr+i;
		printf("NameOfMonster: %s, Location of attack: %s, Number of victims: %d, ID of Monster: %d\n",
		current_monster->name, current_monster->location, current_monster->victims,
		current_monster->attack_ID);
	}
}

void printTotalVictims(struct monster* Monster_arr)
{
	struct monster *current_monster;
	int totalVictims = 0;
	for(int i = 0;i<num_monsters;i++)
	{
		current_monster = Monster_arr+i;
		totalVictims+=current_monster->victims;
	}
	printf("The total number of victims is %d\n",totalVictims);
}

struct monster* getUserInput()
{
	int num_of_attacks;
	char name[25];
	char location[25];
	int victims;
	printf("What is the number of attacks: ");
	scanf("%d", &num_of_attacks);
	//creating array of monster instances
	struct monster* Monster_arr = (struct monster*)malloc(num_of_attacks*sizeof(struct monster));
	for(int i = 0; i<num_of_attacks;i++)
	{
		printf("What is the name of the monster: ");
		scanf("%25s", name);
		printf("What is the location of the monster attack: ");
		scanf("%25s", location);
		printf("How many victims were there: ");
		scanf("%d", &victims);
		addMonster(&Monster_arr,name,location,victims);
	}
	return Monster_arr;
}

int main()
{
        struct monster* Monster_arr = getUserInput();
        
        printMonsterInfo(Monster_arr);
        printTotalVictims(Monster_arr);
        
        return 0;
}
