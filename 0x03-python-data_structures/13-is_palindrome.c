#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * struct listint_s 
 * {
 *     int n;
 *     struct listint_s *next;
 * };
 * typedef struct listint_s listint_t;
 */

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *temp;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
temp = slow->next;
slow->next = prev;
prev = slow;
slow = temp;
}
if (fast != NULL)
{
slow = slow->next;
}
while (prev != NULL && slow != NULL)
{
if (prev->n != slow->n)
{
return (0);
}
prev = prev->next;
slow = slow->next;
}
	return (1);
}
