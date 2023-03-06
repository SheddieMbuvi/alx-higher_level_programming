#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle in it or not
 * @list: head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *has_not, *has;

	has_not = list;
	has = list;

	if (!list || !list->next)
		return (0);
	for (;has && has->next;)
	{
		has = has->next->next;
		has_not = has_not->next;
		if (has == has_not)
		{
			return (1);
		}
	}
	return (0);
}
