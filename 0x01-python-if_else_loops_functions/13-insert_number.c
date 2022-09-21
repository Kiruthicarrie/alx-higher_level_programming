#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a node.
 * @head: head of list
 * @number: number
 * Description: insert a node in a list
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL, *prevNode = NULL, *currentNode = NULL;

	newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;
	prevNode = NULL;
	currentNode = *head;
	while (currentNode != NULL && number > currentNode->n)
	{
		prevNode = currentNode;
		currentNode = currentNode->next;
	}
	if (prevNode == NULL)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		prevNode->next = newNode;
		newNode->next = currentNode;
	}

	return (newNode);

}
