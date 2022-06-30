#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
*insert_node - insert a new node at sort of a listint_t list
*@head: pointer to pointer of first node of listint_t list
*@number: integer
*Return: address of the new element or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copyhead = *head, *usr;

	if (head == NULL)
	{
		return (NULL);
	}
	usr = malloc(sizeof(listint_t));

	if (usr == NULL)
	{
		return (NULL);
	}
	usr->n = number;

	if (*head == NULL)
	{
		*head = usr;
		usr->next = NULL;
		return (usr);
	}
	for (; copyhead != NULL; copyhead = copyhead->next)
	{
		if (number <= copyhead->n)
		{
			*head = usr;
			usr->next = copyhead;
			return (usr);
		}
		if (number >= copyhead->n && copyhead->next == NULL)
		{
			usr->next = NULL;
			copyhead->next = usr;
			return (usr);
		}
		if (number >= copyhead->n && number <= copyhead->next->n)
		{
			usr->next = copyhead->next;
			copyhead->next = usr;
			return (usr);
		}
	}
	return (NULL);
}

