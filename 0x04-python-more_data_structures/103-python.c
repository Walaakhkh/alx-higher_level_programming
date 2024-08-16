#include <Python.h>

/* Function prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t i;
    Py_ssize_t size;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python List info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %ld\n", PyList_GET_SIZE(p));

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);
        print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    const char *bytes;

    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes);
    printf("  first %zd bytes: ", (size < 10 ? size : 10));

    for (i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x ", (unsigned char)bytes[i]);
    }
    printf("\n");
}
