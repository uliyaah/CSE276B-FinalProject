// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pupper_interfaces:msg/TouchEvent.idl
// generated code does not contain a copyright notice
#include "pupper_interfaces/msg/detail/touch_event__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `location`
#include "rosidl_runtime_c/string_functions.h"

bool
pupper_interfaces__msg__TouchEvent__init(pupper_interfaces__msg__TouchEvent * msg)
{
  if (!msg) {
    return false;
  }
  // location
  if (!rosidl_runtime_c__String__init(&msg->location)) {
    pupper_interfaces__msg__TouchEvent__fini(msg);
    return false;
  }
  return true;
}

void
pupper_interfaces__msg__TouchEvent__fini(pupper_interfaces__msg__TouchEvent * msg)
{
  if (!msg) {
    return;
  }
  // location
  rosidl_runtime_c__String__fini(&msg->location);
}

bool
pupper_interfaces__msg__TouchEvent__are_equal(const pupper_interfaces__msg__TouchEvent * lhs, const pupper_interfaces__msg__TouchEvent * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // location
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->location), &(rhs->location)))
  {
    return false;
  }
  return true;
}

bool
pupper_interfaces__msg__TouchEvent__copy(
  const pupper_interfaces__msg__TouchEvent * input,
  pupper_interfaces__msg__TouchEvent * output)
{
  if (!input || !output) {
    return false;
  }
  // location
  if (!rosidl_runtime_c__String__copy(
      &(input->location), &(output->location)))
  {
    return false;
  }
  return true;
}

pupper_interfaces__msg__TouchEvent *
pupper_interfaces__msg__TouchEvent__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__msg__TouchEvent * msg = (pupper_interfaces__msg__TouchEvent *)allocator.allocate(sizeof(pupper_interfaces__msg__TouchEvent), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pupper_interfaces__msg__TouchEvent));
  bool success = pupper_interfaces__msg__TouchEvent__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pupper_interfaces__msg__TouchEvent__destroy(pupper_interfaces__msg__TouchEvent * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pupper_interfaces__msg__TouchEvent__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pupper_interfaces__msg__TouchEvent__Sequence__init(pupper_interfaces__msg__TouchEvent__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__msg__TouchEvent * data = NULL;

  if (size) {
    data = (pupper_interfaces__msg__TouchEvent *)allocator.zero_allocate(size, sizeof(pupper_interfaces__msg__TouchEvent), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pupper_interfaces__msg__TouchEvent__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pupper_interfaces__msg__TouchEvent__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
pupper_interfaces__msg__TouchEvent__Sequence__fini(pupper_interfaces__msg__TouchEvent__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      pupper_interfaces__msg__TouchEvent__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

pupper_interfaces__msg__TouchEvent__Sequence *
pupper_interfaces__msg__TouchEvent__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__msg__TouchEvent__Sequence * array = (pupper_interfaces__msg__TouchEvent__Sequence *)allocator.allocate(sizeof(pupper_interfaces__msg__TouchEvent__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pupper_interfaces__msg__TouchEvent__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pupper_interfaces__msg__TouchEvent__Sequence__destroy(pupper_interfaces__msg__TouchEvent__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pupper_interfaces__msg__TouchEvent__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pupper_interfaces__msg__TouchEvent__Sequence__are_equal(const pupper_interfaces__msg__TouchEvent__Sequence * lhs, const pupper_interfaces__msg__TouchEvent__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pupper_interfaces__msg__TouchEvent__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pupper_interfaces__msg__TouchEvent__Sequence__copy(
  const pupper_interfaces__msg__TouchEvent__Sequence * input,
  pupper_interfaces__msg__TouchEvent__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pupper_interfaces__msg__TouchEvent);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pupper_interfaces__msg__TouchEvent * data =
      (pupper_interfaces__msg__TouchEvent *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pupper_interfaces__msg__TouchEvent__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pupper_interfaces__msg__TouchEvent__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pupper_interfaces__msg__TouchEvent__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
