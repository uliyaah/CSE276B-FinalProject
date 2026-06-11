// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pupper_interfaces:srv/GoPupper.idl
// generated code does not contain a copyright notice
#include "pupper_interfaces/srv/detail/go_pupper__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `command`
#include "rosidl_runtime_c/string_functions.h"

bool
pupper_interfaces__srv__GoPupper_Request__init(pupper_interfaces__srv__GoPupper_Request * msg)
{
  if (!msg) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__init(&msg->command)) {
    pupper_interfaces__srv__GoPupper_Request__fini(msg);
    return false;
  }
  return true;
}

void
pupper_interfaces__srv__GoPupper_Request__fini(pupper_interfaces__srv__GoPupper_Request * msg)
{
  if (!msg) {
    return;
  }
  // command
  rosidl_runtime_c__String__fini(&msg->command);
}

bool
pupper_interfaces__srv__GoPupper_Request__are_equal(const pupper_interfaces__srv__GoPupper_Request * lhs, const pupper_interfaces__srv__GoPupper_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->command), &(rhs->command)))
  {
    return false;
  }
  return true;
}

bool
pupper_interfaces__srv__GoPupper_Request__copy(
  const pupper_interfaces__srv__GoPupper_Request * input,
  pupper_interfaces__srv__GoPupper_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // command
  if (!rosidl_runtime_c__String__copy(
      &(input->command), &(output->command)))
  {
    return false;
  }
  return true;
}

pupper_interfaces__srv__GoPupper_Request *
pupper_interfaces__srv__GoPupper_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__srv__GoPupper_Request * msg = (pupper_interfaces__srv__GoPupper_Request *)allocator.allocate(sizeof(pupper_interfaces__srv__GoPupper_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pupper_interfaces__srv__GoPupper_Request));
  bool success = pupper_interfaces__srv__GoPupper_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pupper_interfaces__srv__GoPupper_Request__destroy(pupper_interfaces__srv__GoPupper_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pupper_interfaces__srv__GoPupper_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pupper_interfaces__srv__GoPupper_Request__Sequence__init(pupper_interfaces__srv__GoPupper_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__srv__GoPupper_Request * data = NULL;

  if (size) {
    data = (pupper_interfaces__srv__GoPupper_Request *)allocator.zero_allocate(size, sizeof(pupper_interfaces__srv__GoPupper_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pupper_interfaces__srv__GoPupper_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pupper_interfaces__srv__GoPupper_Request__fini(&data[i - 1]);
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
pupper_interfaces__srv__GoPupper_Request__Sequence__fini(pupper_interfaces__srv__GoPupper_Request__Sequence * array)
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
      pupper_interfaces__srv__GoPupper_Request__fini(&array->data[i]);
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

pupper_interfaces__srv__GoPupper_Request__Sequence *
pupper_interfaces__srv__GoPupper_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__srv__GoPupper_Request__Sequence * array = (pupper_interfaces__srv__GoPupper_Request__Sequence *)allocator.allocate(sizeof(pupper_interfaces__srv__GoPupper_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pupper_interfaces__srv__GoPupper_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pupper_interfaces__srv__GoPupper_Request__Sequence__destroy(pupper_interfaces__srv__GoPupper_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pupper_interfaces__srv__GoPupper_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pupper_interfaces__srv__GoPupper_Request__Sequence__are_equal(const pupper_interfaces__srv__GoPupper_Request__Sequence * lhs, const pupper_interfaces__srv__GoPupper_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pupper_interfaces__srv__GoPupper_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pupper_interfaces__srv__GoPupper_Request__Sequence__copy(
  const pupper_interfaces__srv__GoPupper_Request__Sequence * input,
  pupper_interfaces__srv__GoPupper_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pupper_interfaces__srv__GoPupper_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pupper_interfaces__srv__GoPupper_Request * data =
      (pupper_interfaces__srv__GoPupper_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pupper_interfaces__srv__GoPupper_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pupper_interfaces__srv__GoPupper_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pupper_interfaces__srv__GoPupper_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
pupper_interfaces__srv__GoPupper_Response__init(pupper_interfaces__srv__GoPupper_Response * msg)
{
  if (!msg) {
    return false;
  }
  // executed
  return true;
}

void
pupper_interfaces__srv__GoPupper_Response__fini(pupper_interfaces__srv__GoPupper_Response * msg)
{
  if (!msg) {
    return;
  }
  // executed
}

bool
pupper_interfaces__srv__GoPupper_Response__are_equal(const pupper_interfaces__srv__GoPupper_Response * lhs, const pupper_interfaces__srv__GoPupper_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // executed
  if (lhs->executed != rhs->executed) {
    return false;
  }
  return true;
}

bool
pupper_interfaces__srv__GoPupper_Response__copy(
  const pupper_interfaces__srv__GoPupper_Response * input,
  pupper_interfaces__srv__GoPupper_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // executed
  output->executed = input->executed;
  return true;
}

pupper_interfaces__srv__GoPupper_Response *
pupper_interfaces__srv__GoPupper_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__srv__GoPupper_Response * msg = (pupper_interfaces__srv__GoPupper_Response *)allocator.allocate(sizeof(pupper_interfaces__srv__GoPupper_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pupper_interfaces__srv__GoPupper_Response));
  bool success = pupper_interfaces__srv__GoPupper_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pupper_interfaces__srv__GoPupper_Response__destroy(pupper_interfaces__srv__GoPupper_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pupper_interfaces__srv__GoPupper_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pupper_interfaces__srv__GoPupper_Response__Sequence__init(pupper_interfaces__srv__GoPupper_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__srv__GoPupper_Response * data = NULL;

  if (size) {
    data = (pupper_interfaces__srv__GoPupper_Response *)allocator.zero_allocate(size, sizeof(pupper_interfaces__srv__GoPupper_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pupper_interfaces__srv__GoPupper_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pupper_interfaces__srv__GoPupper_Response__fini(&data[i - 1]);
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
pupper_interfaces__srv__GoPupper_Response__Sequence__fini(pupper_interfaces__srv__GoPupper_Response__Sequence * array)
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
      pupper_interfaces__srv__GoPupper_Response__fini(&array->data[i]);
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

pupper_interfaces__srv__GoPupper_Response__Sequence *
pupper_interfaces__srv__GoPupper_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pupper_interfaces__srv__GoPupper_Response__Sequence * array = (pupper_interfaces__srv__GoPupper_Response__Sequence *)allocator.allocate(sizeof(pupper_interfaces__srv__GoPupper_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pupper_interfaces__srv__GoPupper_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pupper_interfaces__srv__GoPupper_Response__Sequence__destroy(pupper_interfaces__srv__GoPupper_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pupper_interfaces__srv__GoPupper_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pupper_interfaces__srv__GoPupper_Response__Sequence__are_equal(const pupper_interfaces__srv__GoPupper_Response__Sequence * lhs, const pupper_interfaces__srv__GoPupper_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pupper_interfaces__srv__GoPupper_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pupper_interfaces__srv__GoPupper_Response__Sequence__copy(
  const pupper_interfaces__srv__GoPupper_Response__Sequence * input,
  pupper_interfaces__srv__GoPupper_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pupper_interfaces__srv__GoPupper_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pupper_interfaces__srv__GoPupper_Response * data =
      (pupper_interfaces__srv__GoPupper_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pupper_interfaces__srv__GoPupper_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pupper_interfaces__srv__GoPupper_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pupper_interfaces__srv__GoPupper_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
