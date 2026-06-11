// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pupper_interfaces:msg/DistractionEvent.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__STRUCT_H_
#define PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/DistractionEvent in the package pupper_interfaces.
typedef struct pupper_interfaces__msg__DistractionEvent
{
  float duration;
} pupper_interfaces__msg__DistractionEvent;

// Struct for a sequence of pupper_interfaces__msg__DistractionEvent.
typedef struct pupper_interfaces__msg__DistractionEvent__Sequence
{
  pupper_interfaces__msg__DistractionEvent * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__msg__DistractionEvent__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PUPPER_INTERFACES__MSG__DETAIL__DISTRACTION_EVENT__STRUCT_H_
