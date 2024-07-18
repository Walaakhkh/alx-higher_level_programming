#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list(PyObject *p)
{
	 Py_ssize_t size, i;
	 PyObject *item;

	 fflush(stdout);

	 printf("[*] Python list info\n");

	  if (!PyList_Check(p))
	  {
		  printf("  [ERROR] Invalid List Object\n");
		  return;
	  }

	  size = ((PyVarObject *)p)->ob_size;
	  printf("[*] Size of the Python List = %zd\n", size);
	  printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	  for (i = 0; i < size; i++)
	  {
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python3-bytes(items);
		else if (PyFloat_Check(item))
			print_python_float(item);
	  }
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: A PyObject bytes.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	fflush(stdout);

	printf("[.] bytes object info\n")

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	size = size > 10 ? 10 : size + 1;
	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; i++)
		printf("%02x ", (unsigned char)string[i]);
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python floats.
 * @p: A PyObject float.
 */
void print_python_float(PyObject *p)
{
	double value;

	fflush(stdout);

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
	printf("  [ERROR] Invalid Float Object\n");
	return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %g\n", value);
}
