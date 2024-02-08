#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - insert a node
 * @head: pointer to list to be freed
 * @number:number to insert
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *cur = *head, *temp;

	if (*head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	while (cur != NULL)
	{

		if (number > cur->n && number < cur->next->n)
		{
			temp = cur->next;
			cur->next = new;
			new->next = temp;
		}
		cur = cur->next;
	}
	return (new);
}
