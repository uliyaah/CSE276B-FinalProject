// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pupper_interfaces:srv/TouchPupper.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__TOUCH_PUPPER__STRUCT_H_
#define PUPPER_INTERFACES__SRV__DETAIL__TOUCH_PUPPER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/TouchPupper in the package pupper_interfaces.
typedef struct pupper_interfaces__srv__TouchPupper_Request
{
  rosidl_runtime_c__String command;
  float duration;
} pupper_interfaces__srv__TouchPupper_Request;

// Struct for a sequence of pupper_interfaces__srv__TouchPupper_Request.
typedef struct pupper_interfaces__srv__TouchPupper_Request__Sequence
{
  pupper_interfaces__srv__TouchPupper_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__srv__TouchPupper_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/TouchPupper in the package pupper_interfaces.
typedef struct pupper_interfaces__srv__TouchPupper_Response
{
  bool executed;
} pupper_interfaces__srv__TouchPupper_Response;

// Struct for a sequence of pupper_interfaces__srv__TouchPupper_Response.
typedef struct pupper_interfaces__srv__TouchPupper_Response__Sequence
{
  pupper_interfaces__srv__TouchPupper_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__srv__TouchPupper_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PUPPER_INTERFACES__SRV__DETAIL__TOUCH_PUPPER__STRUCT_H_
