#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python string objects.
 * @p: A PyObject representing a Python string.
 *
 * Description: This function prints detailed information about a given
 * Python string object. If the object is not a valid string, it prints
 * an error message.
 */
void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");

    // Check if the PyObject is a valid string
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get the type and content of the string
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *type = "compact unicode object";
    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        type = "compact ascii";
    }

    // Print the string information
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
