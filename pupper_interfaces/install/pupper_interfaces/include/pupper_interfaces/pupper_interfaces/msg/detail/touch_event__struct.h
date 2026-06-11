// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pupper_interfaces:msg/TouchEvent.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__TOUCH_EVENT__STRUCT_H_
#define PUPPER_INTERFACES__MSG__DETAIL__TOUCH_EVENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'location'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/TouchEvent in the package pupper_interfaces.
typedef struct pupper_interfaces__msg__TouchEvent
{
  rosidl_runtime_c__String location;
} pupper_interfaces__msg__TouchEvent;

// Struct for a sequence of pupper_interfaces__msg__TouchEvent.
typedef struct pupper_interfaces__msg__TouchEvent__Sequence
{
  pupper_interfaces__msg__TouchEvent * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__msg__TouchEvent__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PUPPER_INTERFACES__MSG__DETAIL__TOUCH_EVENT__STRUCT_H_
