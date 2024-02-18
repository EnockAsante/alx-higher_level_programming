#include "lists.h"
#include "stdlib.h"
/**
 * insertAtBegining - insert item at beginning of list
 * @head: pointer to list to insert
 * @data: data to insert
 * Return: void
 */
listint_t *insertAtBegining(listint_t **head, int data)
{
	listint_t *new;

	new = (listint_t *)malloc(sizeof(listint_t));
	if (new != NULL)
	{
		new->n = data;
		new->next = *head;
		*head = new;
	}
	return (new);
}
/**
 * cpy - copy item into list
 * @head: pointer to list to insert
 * Return: list
 */
listint_t *cpy(listint_t **head)
{
	listint_t *rev = NULL, *cur = *head;

	while (cur != NULL)
	{
		insertAtBegining(&rev, (cur)->n);
		cur = cur->next;
	}
	return (rev);
}
/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to list to insert
 * Return: 1 else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *dup = cpy(head), *cur = *head;

	while(cur != NULL)
	{
		if(dup->n != (cur)->n)
			return (0);
		cur = cur->next, dup = dup->next;
	}
	free_listint(dup);
	return (1);
}