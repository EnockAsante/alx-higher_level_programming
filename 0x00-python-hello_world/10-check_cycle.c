#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check if cycle single linked list or not
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (list != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			free_listint(slow);
			free_listint(fast);
			return (1);
		}
		if (fast == NULL)
		{
			free_listint(slow);
			free_listint(fast);
			return (0);
		}
		list++;
	}

	return (0);
}