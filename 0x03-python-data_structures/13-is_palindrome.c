#include "lists.h"

/**
  * reverse_listint - everses a listint_t linked list
  * @head: pointer to head
  * Return: address to modified list
  */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *nxt = NULL;

	while (*head != NULL)
	{
		nxt = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = nxt;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to list to insert
 * Return: 1 else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur = *head ,*rev = reverse_listint(head);

	while(cur)
	{
		if(rev->n != (cur)->n)
			return (0);
		cur = cur->next, rev = rev->next;
	}
	return (1);
}