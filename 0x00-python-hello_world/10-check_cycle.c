#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
*check_cycle- checks a cycle
*@list:pointer for checker of cycle
*Return:1 if successful, 0 on failure
*/
int check_cycle(listint_t *list)
{
	listint_t *come = list;
	listint_t *go = list;

	while (come != NULL)
	{
		come = come->next;
		go = go->next;
		if ((go == NULL) || (go->next == NULL))
			break;
		go = go->next;
		if (come == go)
			return (1);
	}
	return (0);
}

