#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - This function prints basic info about Python lists.
 * @ptr: PyObject list
 */
void print_python_list_info(PyObject *ptr)
{
	long int size = PyList_Size(ptr);
	int i;
	PyListObject *obj = (PyListObject *)ptr;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
