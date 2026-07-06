1. a = ['a', 'e', 'i', 'o', 'u']
A Python list is a PyListObject (approximately):
ctypedef struct {
    PyObject_HEAD          // refcount + type pointer
    Py_ssize_t ob_size;    // number of items currently in use
    PyObject **ob_item;    // pointer to a C array of *pointers*
    Py_ssize_t allocated;  // size of the allocated array (can be > ob_size)
} PyListObject;
Key point: the list does not store the strings inline. ob_item is a contiguous array of pointers (PyObject*), each pointing to a separately-allocated string object elsewhere on the heap.
a (PyListObject)
┌─────────────┬──────┬───────────┬────────────┐
│ refcnt/type │ size=5│ ob_item ──┼──► [ptr0][ptr1][ptr2][ptr3][ptr4]
└─────────────┴──────┴───────────┴────────────┘
                                        │      │      │      │      │
                                        ▼      ▼      ▼      ▼      ▼
                                       'a'    'e'    'i'    'o'    'u'
                                   (separate heap objects, PyUnicodeObject)
For single-character ASCII strings like 'a', CPython doesn't even allocate new memory — it reuses cached singleton objects from a global table (unicode_latin1[256] in the interpreter). So 'a' here is likely the same object as any other 'a' string literal anywhere in your program. That's why 'a' is 'a' is True for these.
Since this list is built from a literal (a "list display"), CPython knows the size up front (5), so ob_item is allocated exactly for 5 pointers — no over-allocation slack in this case (over-allocation only kicks in on append()/growth operations).
2. iter_a = iter(a)
iter() calls a.__iter__(), which creates a new, separate object: a PyListIterObject.
ctypedef struct {
    PyObject_HEAD
    Py_ssize_t it_index;   // current position, starts at 0
    PyListObject *it_seq;  // strong reference (refcount incremented) to `a`
} PyListIterObject;
This is a small, distinct heap allocation. It does not copy any elements — it just holds:

an integer cursor (it_index = 0)
a pointer back to the original list a (with its refcount bumped by 1, which is why a can't be garbage collected while the iterator is alive)

iter_a (PyListIterObject)
┌─────────────┬───────────┬────────────┐
│ refcnt/type │ it_index=0│ it_seq ────┼──► a (the same list object above)
└─────────────┴───────────┴────────────┘
3. Each next(iter_a) call
next() invokes the iterator's tp_iternext slot, implemented (roughly) as:
cstatic PyObject *listiter_next(PyListIterObject *it) {
    PyListObject *seq = it->it_seq;
    if (it->it_index >= Py_SIZE(seq))
        return NULL;  // triggers StopIteration
    PyObject *item = PyList_GET_ITEM(seq, it->it_index);
    it->it_index++;
    Py_INCREF(item);   // caller now owns a reference
    return item;
}
So each call:

Reads ob_item[it_index] directly — an O(1) pointer dereference, no searching.
Increments the refcount of that string object (since print() will hold a temporary reference to it).
Increments it_index by 1.

No new memory is allocated per next() call except the temporary reference bookkeeping — you're just walking a pointer array and copying out pointers.
Trace through your 5 calls
Callit_index beforeReturnsit_index after1st next0'a'12nd next1'e'23rd next2'i'34th next3'o'45th next4'u'5
Since you only call next() exactly 5 times (matching the list length), all 5 succeed and print. A 6th call would find it_index (5) >= ob_size (5) and raise StopIteration.