// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pupper_interfaces:srv/StateManagerCommand.idl
// generated code does not contain a copyright notice

#ifndef PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__STRUCT_H_
#define PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__STRUCT_H_

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
#include "pupper_interfaces/msg/detail/command__struct.h"

/// Struct defined in srv/StateManagerCommand in the package pupper_interfaces.
typedef struct pupper_interfaces__srv__StateManagerCommand_Request
{
  pupper_interfaces__msg__Command command;
} pupper_interfaces__srv__StateManagerCommand_Request;

// Struct for a sequence of pupper_interfaces__srv__StateManagerCommand_Request.
typedef struct pupper_interfaces__srv__StateManagerCommand_Request__Sequence
{
  pupper_interfaces__srv__StateManagerCommand_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__srv__StateManagerCommand_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/StateManagerCommand in the package pupper_interfaces.
typedef struct pupper_interfaces__srv__StateManagerCommand_Response
{
  bool success;
} pupper_interfaces__srv__StateManagerCommand_Response;

// Struct for a sequence of pupper_interfaces__srv__StateManagerCommand_Response.
typedef struct pupper_interfaces__srv__StateManagerCommand_Response__Sequence
{
  pupper_interfaces__srv__StateManagerCommand_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pupper_interfaces__srv__StateManagerCommand_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PUPPER_INTERFACES__SRV__DETAIL__STATE_MANAGER_COMMAND__STRUCT_H_
