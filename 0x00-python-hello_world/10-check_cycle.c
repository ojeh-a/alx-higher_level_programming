#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a alinked list.
 * @list: pointer to list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (!list || !list->next)
		return (0);
	current = list;
	check = current->next;

	while (current && check->next && check->next->next)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
