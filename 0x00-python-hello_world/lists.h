#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#include "lists.h"

/**
 * check_cycle - checks if a list contains a cycle
 * @list: list to be checked
 *
 * Return: 1 if the list have a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
	return (0);
	while (slow && fast && fast->next)
	{
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
	return (1);
	}
	return (0);
}

#endif /* LISTS_H */
